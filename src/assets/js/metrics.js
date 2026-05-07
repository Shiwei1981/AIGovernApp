/* Async metric loader for the AI Govern Dashboard homepage.
 *
 * Fetches live data for each metric tile after page load.
 * Each metric is a separate API call (rule #5d).
 * Errors are printed to console AND surfaced in the UI (rule #14).
 */

(function () {
  "use strict";

  function getRange() {
    return new URLSearchParams(window.location.search).get("range") === "12w" ? "12w" : "4w";
  }

  function setLoading(id) {
    const el = document.getElementById(id);
    if (el) el.textContent = "…";
  }

  function showTileError(tileId, message) {
    const tile = document.getElementById(tileId);
    if (!tile) return;
    // Remove any existing error note before adding a new one.
    const existing = tile.querySelector(".metric-api-error");
    if (existing) existing.remove();
    const div = document.createElement("div");
    div.className = "data-note text-danger mt-1 metric-api-error";
    div.textContent = message;
    tile.appendChild(div);
  }

  // -------------------------------------------------------------------------
  // Purview Classification Coverage
  // -------------------------------------------------------------------------

  async function loadCoverageMetric(range) {
    try {
      const res = await fetch(
        `/api/metrics/purview-classification-coverage?range=${range}`,
        { credentials: "same-origin" }
      );
      if (!res.ok) {
        const body = await res.text().catch(() => "");
        throw new Error(`HTTP ${res.status}: ${body.slice(0, 120)}`);
      }
      const data = await res.json();
      const pct = data.coverage_pct;

      const pctEl = document.getElementById("coverage-pct");
      if (pctEl) pctEl.textContent = `${pct}%`;

      const holeEl = document.getElementById("coverage-hole");
      if (holeEl) holeEl.textContent = `${pct}%`;

      const donutEl = document.getElementById("coverage-donut");
      if (donutEl) donutEl.style.setProperty("--value", pct);

      const captionEl = document.getElementById("coverage-caption");
      if (captionEl) {
        const levelLabel = data.asset_level === "column" ? "columns" : "assets";
        captionEl.textContent =
          data.total_count > 0
            ? `${data.classified_count} of ${data.total_count} ${levelLabel} classified`
            : "No data assets found in Purview";
      }
    } catch (err) {
      console.error("[coverage-metric]", err);
      const pctEl = document.getElementById("coverage-pct");
      if (pctEl) pctEl.textContent = "—";
      const holeEl = document.getElementById("coverage-hole");
      if (holeEl) holeEl.textContent = "—";
      showTileError("coverage-tile", `Coverage unavailable: ${err.message}`);
    }
  }

  // -------------------------------------------------------------------------
  // Sensitive Data Exposure Alerts
  // -------------------------------------------------------------------------

  async function loadAlertsMetric(range) {
    try {
      const res = await fetch(
        `/api/metrics/sensitive-data-exposure-alerts?range=${range}`,
        { credentials: "same-origin" }
      );
      if (!res.ok) {
        const body = await res.text().catch(() => "");
        throw new Error(`HTTP ${res.status}: ${body.slice(0, 120)}`);
      }
      const data = await res.json();

      const totalEl = document.getElementById("alerts-total");
      if (totalEl) totalEl.textContent = data.total;

      const legendEl = document.getElementById("alerts-legend-value");
      if (legendEl) legendEl.textContent = data.total;

      const captionEl = document.getElementById("alerts-caption");
      if (captionEl) {
        const weeks = range === "12w" ? "12" : "4";
        captionEl.textContent = `unique alert cases in last ${weeks} weeks`;
      }

      // Rebuild weekly bar chart from API data.
      const barsEl = document.getElementById("alerts-bars");
      if (barsEl && Array.isArray(data.weeks) && data.weeks.length > 0) {
        const maxCount = Math.max(...data.weeks.map((w) => w.count), 1);
        const maxBarPx = 56;
        barsEl.innerHTML = data.weeks
          .map((w) => {
            const height = w.count > 0
              ? Math.max(Math.round((w.count / maxCount) * maxBarPx), 4)
              : 0;
            return (
              `<div class="week-col">` +
              `<div class="week-stack">` +
              `<div class="week-seg fill-blue" style="height:${height}px"></div>` +
              `</div>` +
              `<div class="week-label">${w.label}</div>` +
              `</div>`
            );
          })
          .join("");
      }
    } catch (err) {
      console.error("[alerts-metric]", err);
      const totalEl = document.getElementById("alerts-total");
      if (totalEl) totalEl.textContent = "—";
      showTileError("alerts-tile", `Alerts unavailable: ${err.message}`);
    }
  }

  // -------------------------------------------------------------------------
  // Bootstrap: fetch both metrics in parallel after DOM is ready.
  // -------------------------------------------------------------------------

  document.addEventListener("DOMContentLoaded", function () {
    const range = getRange();
    setLoading("coverage-pct");
    setLoading("coverage-hole");
    setLoading("alerts-total");
    setLoading("alerts-legend-value");

    // Independent calls — do not await sequentially (rule #5d).
    loadCoverageMetric(range);
    loadAlertsMetric(range);
  });
})();
