"""FastAPI entrypoint for the AI Govern Dashboard POC."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import httpx
import msal
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
PAGES_DIR = SRC_DIR / "pages"
ASSETS_DIR = SRC_DIR / "assets"
STYLES_DIR = SRC_DIR / "styles"

load_dotenv(BASE_DIR / ".env.local")


def _parse_bool(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _first_present(*values: str | None) -> str | None:
    for value in values:
        if value and value.strip():
            return value.strip()
    return None


@dataclass(frozen=True)
class AuthConfig:
    mock_auth_enabled: bool
    tenant_id: str | None
    authority_url: str | None
    client_id: str | None
    client_secret: str | None
    callback_url: str | None


def _strip_v2_suffix(url: str | None) -> str | None:
    """MSAL authority must not include /v2.0; strip it if present."""
    if url and url.rstrip("/").endswith("/v2.0"):
        return url.rstrip("/")[: -len("/v2.0")]
    return url


def _load_auth_config() -> AuthConfig:
    app_env = os.getenv("APP_ENV", "test").strip().lower()
    is_production = app_env in {"prod", "production"}
    prefix = "PROD" if is_production else "TEST"

    tenant_id = _first_present(os.getenv("AZURE_TENANT_ID"))

    raw_authority = _first_present(
        os.getenv("OIDC_AUTHORITY_URL"),
        f"https://login.microsoftonline.com/{tenant_id}" if tenant_id else None,
    )
    authority_url = _strip_v2_suffix(raw_authority)

    # Variable names follow the TEST_/PROD_ prefix pattern used in .env.local.
    callback_url = _first_present(os.getenv(f"{prefix}_AZURE_CLIENT_REDIRECT_URI"))
    client_id = _first_present(os.getenv(f"{prefix}_AZURE_CLIENT_ID"))
    client_secret = _first_present(os.getenv(f"{prefix}_AZURE_CLIENT_SECRET"))

    return AuthConfig(
        mock_auth_enabled=_parse_bool(os.getenv("MOCK_AUTH_ENABLED")),
        tenant_id=tenant_id,
        authority_url=authority_url,
        client_id=client_id,
        client_secret=client_secret,
        callback_url=callback_url,
    )


AUTH_CONFIG = _load_auth_config()
SESSION_SECRET = os.getenv("SESSION_SECRET")
if not SESSION_SECRET:
    raise RuntimeError("SESSION_SECRET must be set before starting the application.")

APP_ENV = os.getenv("APP_ENV", "test").strip().lower()
IS_PRODUCTION = APP_ENV in {"prod", "production"}

# Server-side store for MSAL auth code flows.
# The full flow dict (code_verifier, auth_uri, etc.) is too large for a cookie;
# only the short state key is kept in the session cookie.
_auth_flow_store: dict[str, dict] = {}

app = FastAPI(title="AI Govern Dashboard")
app.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET,
    same_site="lax",
    https_only=IS_PRODUCTION,
)

app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")
app.mount("/styles", StaticFiles(directory=STYLES_DIR), name="styles")


def _file_response(file_name: str) -> FileResponse:
    file_path = PAGES_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Missing page file: {file_name}")
    return FileResponse(file_path)


def _build_msal_app() -> msal.ConfidentialClientApplication:
    if not AUTH_CONFIG.authority_url or not AUTH_CONFIG.client_id or not AUTH_CONFIG.client_secret:
        raise HTTPException(
            status_code=500,
            detail=(
                "Authentication is not fully configured. Set AZURE_TENANT_ID, "
                "a client ID/secret, and a callback URL."
            ),
        )
    return msal.ConfidentialClientApplication(
        client_id=AUTH_CONFIG.client_id,
        authority=AUTH_CONFIG.authority_url,
        client_credential=AUTH_CONFIG.client_secret,
    )


def _session_user(request: Request) -> dict[str, Any] | None:
    user = request.session.get("user")
    if isinstance(user, dict):
        return user
    return None


def _redirect_to_login(request: Request) -> RedirectResponse:
    target = f"{request.url.path}"
    if request.url.query:
        target = f"{target}?{request.url.query}"
    return RedirectResponse(
        url=f"/login?next={target}",
        status_code=303,
    )


def _require_user(request: Request) -> dict[str, Any]:
    user = _session_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required.")
    return user


def _mock_user() -> dict[str, str]:
    return {
        "username": "mock.user@contoso.com",
        "display_name": "Mock User",
        "auth_mode": "mock",
    }


@app.get("/api/health")
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})


@app.get("/api/auth/me")
async def auth_me(request: Request) -> JSONResponse:
    user = _require_user(request)
    return JSONResponse(user)


@app.get("/login", response_model=None)
async def login_page(request: Request):
    if _session_user(request):
        return RedirectResponse(url="/", status_code=303)
    return _file_response("login.html")


@app.get("/auth/login")
async def login(request: Request, prompt: str = "select_account", next: str = "/") -> RedirectResponse:
    request.session["post_login_redirect"] = next

    if AUTH_CONFIG.mock_auth_enabled:
        request.session["user"] = _mock_user()
        return RedirectResponse(url=next, status_code=303)

    msal_app = _build_msal_app()
    flow = msal_app.initiate_auth_code_flow(
        scopes=["User.Read"],  # openid/profile are reserved and added automatically by MSAL
        redirect_uri=AUTH_CONFIG.callback_url,
        prompt=prompt,
    )
    # Store the full flow server-side; put only the short state key in the cookie.
    state_key: str = flow["state"]
    _auth_flow_store[state_key] = flow
    request.session["auth_flow_state"] = state_key
    return RedirectResponse(url=flow["auth_uri"], status_code=303)


@app.get("/auth/callback")
async def auth_callback(request: Request) -> RedirectResponse:
    if AUTH_CONFIG.mock_auth_enabled:
        request.session["user"] = _mock_user()
        return RedirectResponse(url=request.session.pop("post_login_redirect", "/"), status_code=303)

    # Retrieve the MSAL flow from the server-side store.
    state_key = request.session.get("auth_flow_state") or request.query_params.get("state")
    flow = _auth_flow_store.pop(state_key, None) if state_key else None
    if not isinstance(flow, dict):
        print(
            f"[auth-callback] auth_flow missing; state_key={state_key!r} "
            f"store_keys={list(_auth_flow_store.keys())}"
        )
        raise HTTPException(status_code=400, detail="Authentication flow state is missing.")

    try:
        result = _build_msal_app().acquire_token_by_auth_code_flow(
            flow, dict(request.query_params)
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=f"Authentication callback failed: {exc}") from exc

    if "error" in result:
        error_description = result.get("error_description", result["error"])
        raise HTTPException(
            status_code=400,
            detail=f"Authentication callback failed: {error_description}",
        )

    claims = result.get("id_token_claims") or {}
    request.session["user"] = {
        "username": claims.get("preferred_username") or claims.get("upn") or claims.get("email"),
        "display_name": claims.get("name") or claims.get("preferred_username") or "Entra ID User",
        "auth_mode": "entra_id",
    }
    request.session.pop("auth_flow_state", None)
    return RedirectResponse(url=request.session.pop("post_login_redirect", "/"), status_code=303)


@app.get("/auth/logout")
async def logout(request: Request) -> RedirectResponse:
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)


@app.get("/", response_model=None)
async def homepage(request: Request):
    if not _session_user(request):
        return _redirect_to_login(request)
    return _file_response("index.html")


@app.get("/domains/data-privacy", response_model=None)
async def data_privacy_page(request: Request):
    if not _session_user(request):
        return _redirect_to_login(request)
    return _file_response("data-privacy.html")


# ---------------------------------------------------------------------------
# Shared helper: acquire an application-level token (client credentials flow)
# ---------------------------------------------------------------------------

def _acquire_app_token(scope: str) -> str:
    """Acquire a service-to-service token using the app's client credentials."""
    msal_app = _build_msal_app()
    result = msal_app.acquire_token_for_client(scopes=[scope])
    if "access_token" not in result:
        err = result.get("error_description") or result.get("error") or "unknown error"
        print(f"[token] Failed to acquire token for scope={scope}: {err}")
        raise HTTPException(status_code=502, detail=f"Token acquisition failed: {err}")
    return result["access_token"]


# ---------------------------------------------------------------------------
# Purview helper: page through search results and count classified entities
# ---------------------------------------------------------------------------

async def _count_purview_classified(
    search_url: str,
    headers: dict[str, str],
    entity_types: list[str],
) -> tuple[int, int]:
    """Return (total, classified) counts for the given Purview entity types."""
    total = 0
    classified = 0
    offset = 0
    limit = 1000

    if len(entity_types) == 1:
        filter_body: dict[str, Any] = {"entityType": entity_types[0]}
    else:
        filter_body = {"or": [{"entityType": t} for t in entity_types]}

    async with httpx.AsyncClient(timeout=30) as client:
        while True:
            body = {"keywords": None, "limit": limit, "offset": offset, "filter": filter_body}
            resp = await client.post(search_url, headers=headers, json=body)
            if resp.status_code != 200:
                print(f"[purview-coverage] search error: {resp.status_code} {resp.text[:300]}")
                raise HTTPException(
                    status_code=502,
                    detail=f"Purview Data Map API error: HTTP {resp.status_code}",
                )
            data = resp.json()
            entities: list[dict] = data.get("value", [])
            if not entities:
                break
            for entity in entities:
                total += 1
                if entity.get("classification"):
                    classified += 1
            if len(entities) < limit or offset + limit >= 10000:
                break
            offset += limit

    return total, classified


# ---------------------------------------------------------------------------
# API: Purview Classification Coverage
# ---------------------------------------------------------------------------

@app.get("/api/metrics/purview-classification-coverage")
async def purview_classification_coverage(request: Request, range: str = "4w") -> JSONResponse:
    _require_user(request)

    account_name = os.getenv("PURVIEW_ACCOUNT_NAME", "").strip()
    if not account_name:
        raise HTTPException(status_code=500, detail="PURVIEW_ACCOUNT_NAME is not configured.")

    token = _acquire_app_token("https://purview.azure.net/.default")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    search_url = (
        f"https://{account_name}.purview.azure.com"
        "/datamap/api/search/query?api-version=2023-09-01-preview"
    )

    # Try column-level first; fall back to table/view level if no columns registered.
    for entity_types, asset_level in [
        (["azure_sql_column"], "column"),
        (["azure_sql_table", "azure_sql_view"], "table/view"),
    ]:
        total, classified = await _count_purview_classified(search_url, headers, entity_types)
        if total > 0:
            coverage_pct = round(classified / total * 100)
            print(
                f"[purview-coverage] asset_level={asset_level} total={total} "
                f"classified={classified} pct={coverage_pct}%"
            )
            return JSONResponse(
                {
                    "coverage_pct": coverage_pct,
                    "classified_count": classified,
                    "total_count": total,
                    "asset_level": asset_level,
                }
            )

    print("[purview-coverage] No data assets found in Purview Data Map.")
    return JSONResponse(
        {
            "coverage_pct": 0,
            "classified_count": 0,
            "total_count": 0,
            "asset_level": "none",
            "note": "No data assets found in Purview Data Map.",
        }
    )


# ---------------------------------------------------------------------------
# API: Sensitive Data Exposure Alerts  (Office 365 Management Activity API)
# ---------------------------------------------------------------------------

_DLP_WORKLOADS = {"sharepoint", "onedrive", "exchange"}


@app.get("/api/metrics/sensitive-data-exposure-alerts")
async def sensitive_data_exposure_alerts(request: Request, range: str = "4w") -> JSONResponse:
    _require_user(request)

    tenant_id = AUTH_CONFIG.tenant_id
    if not tenant_id:
        raise HTTPException(status_code=500, detail="AZURE_TENANT_ID is not configured.")

    token = _acquire_app_token("https://manage.office.com/.default")
    headers = {"Authorization": f"Bearer {token}"}
    feed_base = f"https://manage.office.com/api/v1.0/{tenant_id}/activity/feed"

    week_count = 12 if range == "12w" else 4
    # O365 Management API retains content for max 7 days.
    available_days = 7
    now_utc = datetime.now(timezone.utc).replace(tzinfo=None)

    # Collect unique DLP alerts across the available 7-day window.
    # Each request window must be ≤ 24 h; iterate day by day.
    seen: dict[str, datetime] = {}  # alertId -> event CreationTime

    async with httpx.AsyncClient(timeout=60) as client:
        for day in range(available_days):
            end_dt = now_utc - timedelta(days=day)
            start_dt = end_dt - timedelta(hours=24)
            start_str = start_dt.strftime("%Y-%m-%dT%H:%M:%S")
            end_str = end_dt.strftime("%Y-%m-%dT%H:%M:%S")

            content_url = (
                f"{feed_base}/subscriptions/content"
                f"?contentType=DLP.All&startTime={start_str}&endTime={end_str}"
            )

            # Follow NextPageUri pagination for the content list.
            next_page: str | None = content_url
            while next_page:
                resp = await client.get(next_page, headers=headers)
                if resp.status_code != 200:
                    print(
                        f"[dlp-alerts] content list HTTP {resp.status_code} "
                        f"day=-{day}: {resp.text[:200]}"
                    )
                    break
                blobs: list[dict] = resp.json() or []
                next_page = resp.headers.get("NextPageUri")

                for blob in blobs:
                    content_uri = blob.get("contentUri")
                    if not content_uri:
                        continue
                    blob_resp = await client.get(content_uri, headers=headers)
                    if blob_resp.status_code != 200:
                        print(f"[dlp-alerts] blob fetch HTTP {blob_resp.status_code}: {content_uri}")
                        continue
                    events: list[dict] = blob_resp.json() or []
                    for ev in events:
                        alert_id = ev.get("AlertId") or ev.get("alertId")
                        if not alert_id:
                            continue
                        status = (ev.get("AlertStatus") or ev.get("alertStatus") or "").lower()
                        if status == "dismissed":
                            continue
                        workload = (ev.get("Workload") or ev.get("workload") or "").lower()
                        if workload not in _DLP_WORKLOADS:
                            continue
                        if alert_id in seen:
                            continue
                        raw_time = ev.get("CreationTime") or ev.get("creationTime") or ""
                        try:
                            event_time = datetime.fromisoformat(raw_time.replace("Z", "+00:00"))
                            event_time = event_time.replace(tzinfo=None)
                        except (ValueError, AttributeError):
                            event_time = now_utc
                        seen[alert_id] = event_time

    # Bucket alerts into calendar weeks (Mon-Sun), newest = W{week_count}.
    today = now_utc.date()
    current_week_monday = today - timedelta(days=today.weekday())
    week_counts = [0] * week_count

    for event_time in seen.values():
        event_date = event_time.date()
        event_week_monday = event_date - timedelta(days=event_date.weekday())
        weeks_ago = (current_week_monday - event_week_monday).days // 7
        if 0 <= weeks_ago < week_count:
            bucket = week_count - 1 - weeks_ago
            week_counts[bucket] += 1

    total = len(seen)
    weeks_payload = [{"label": f"W{i + 1}", "count": week_counts[i]} for i in range(week_count)]

    print(f"[dlp-alerts] range={range} total_unique_alerts={total}")
    return JSONResponse(
        {
            "total": total,
            "weeks": weeks_payload,
            "data_window_days": available_days,
            "note": "Office 365 Management API retains content for up to 7 days.",
        }
    )
