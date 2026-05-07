"""FastAPI entrypoint for the AI Govern Dashboard POC."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

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
    request.session["auth_flow"] = flow
    return RedirectResponse(url=flow["auth_uri"], status_code=303)


@app.get("/auth/callback")
async def auth_callback(request: Request) -> RedirectResponse:
    if AUTH_CONFIG.mock_auth_enabled:
        request.session["user"] = _mock_user()
        return RedirectResponse(url=request.session.pop("post_login_redirect", "/"), status_code=303)

    flow = request.session.get("auth_flow")
    if not isinstance(flow, dict):
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
    request.session.pop("auth_flow", None)
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
