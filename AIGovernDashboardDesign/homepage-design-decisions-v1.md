# AI Govern Dashboard - Homepage Design Decisions V1

This document records the current homepage design decisions, metric selection logic, and decisions confirmed during iteration. It is intended to guide later design and development work.

## 0. Review Status

| Domain | Status |
|---|---|
| 1. AI Asset Inventory | Confirmed |
| 2. Third-Party and Supply Chain | Confirmed |
| 3. Data and Privacy | Confirmed |
| 4. AI Security Protection | Confirmed |
| 5. Output Trustworthiness and Content Provenance | Confirmed |
| 6. Validation, Audit, and Compliance Assurance | Confirmed |
| 7. Operational Incidents, Response, and Remediation | Pending review |
| 8. Governance Oversight and Control Execution | Pending review |

## 1. Homepage Positioning

The homepage is a **control tower overview and navigation page**, not:

- a documentation hub
- a report library
- a dense chart wall

Its primary job is to help a management user:

1. identify which governance domain needs attention
2. compare domains quickly
3. click into the right domain page for detail

## 2. Confirmed Homepage Structure

Current confirmed structure:

1. **Top status bar**
   - time range
   - last updated

2. **8 domain cards only**
   - no global summary block
   - no action list block

3. **Homepage-to-domain relationship**
   - each homepage card maps to exactly one domain page
   - each homepage card shows only 2 key metrics
   - those 2 homepage metrics must be a subset of the full metric set on the corresponding domain page
   - domain pages do **not** need to repeat those 2 metrics as standalone top tiles
   - domain pages may represent them with more detailed or split metrics if the same meaning is preserved

## 3. Card Design Principles

The homepage card design has been refined to the following rules:

1. **No domain numbering**
   - domain names should stand out on their own

2. **Domain title should be visually prominent**
   - larger
   - heavier weight
   - darker color

3. **Each card contains 1-2 metrics**
   - displayed left/right, not stacked vertically

4. **Top-right badge should express domain risk / attention level**
   - current badge set:
     - **High Risk**
     - **Attention**
     - **Low Risk**
   - use badge color to match the domain status color
   - if a card uses sample data, show that as a separate neutral note instead of mixing it into the badge

5. **Metric blocks must include explanation**
   - not just a title and a number
   - each metric should tell the user what it represents
   - use short noun phrases instead of long explanatory sentences

6. **Narrative issue text should not be relied on**
   - avoid free-form statements that are difficult to auto-generate reliably

7. **Avoid long helper narratives in cards**
   - remove "Why it matters" helper text from homepage cards
   - keep the cards lighter and faster to scan

8. **Choose graphics based on meaning**
   - ratio / coverage -> donut
   - composition -> donut + legend
   - trend / backlog -> sparkline
   - target comparison -> bullet bar
   - plain total population -> number-first display

9. **Homepage donut metrics should use a vertical stack**
   - put the **number / caption text on top**
   - put the **donut below**
   - do not use left-right donut layout in homepage cards
   - reason: homepage cards are too narrow for stable side-by-side donut layout, and horizontal layout can squeeze text or shift the chart visually

## 4. Spacing Decisions

The homepage has been iteratively adjusted for visual breathing room:

- keep **4 cards per row**
- increase left/right page margins
- increase card-to-card spacing
- increase card internal padding

This was preferred over switching permanently to a 3-card row layout.

## 5. Domain 1 Metric Decision

### Domain
**AI Asset Inventory**

### Earlier candidates considered

- Inventory Coverage
- Owner Coverage
- High-Risk Assets
- Asset Total
- Lifecycle Status

### Why the earlier coverage-style metrics were rejected

#### Inventory Coverage
Potential problem:
- if discovery and registration are effectively the same source, the metric risks becoming self-referential or near-100%

#### Owner Coverage
Potential problem:
- if owner is simply read from Graph / Entra / technical ownership metadata, it may not represent true governance accountability

These concerns made both metrics too easy to become **pseudo-metrics**.

### Confirmed replacement

#### Metric 1: Discovered Assets
Reason:
- shows the size of the governance population directly
- easy for management to understand
- does not depend on self-validating logic

Representation:
- **plain large number**

#### Metric 2: Asset Type Mix
Reason:
- complements total size with structure
- tells the user what types of AI assets dominate the environment
- more meaningful than another generic coverage metric

Representation:
- **stacked composition bar + type legend**

Layout:
- keep the two metric tiles in this card at **equal width**

### Current accepted logic for Domain 1

| Metric | Why it stays |
|---|---|
| Discovered Assets | Best expression of total governed population |
| Asset Type Mix | Best quick expression of inventory composition |

## 6. Domain 2 Metric Decision

### Domain
**Third-Party and Supply Chain**

### Rejected option

- External Dependency Ratio  
Reason rejected:
  - not sufficiently meaningful to the user for homepage use

### Confirmed direction

#### Metric 1: 3rd-Party Dependencies
Reason:
- better expresses total dependency footprint
- easier to understand than a ratio
- allows composition to be shown in the same metric area

Representation:
- **plain large number + major dependency categories**

#### Metric 2: Critical Open-Source Findings
Reason:
- shows current supply-chain risk load
- more actionable than pure enumeration of suppliers

Representation:
- **trend-oriented sparkline + count**

## 7. Domain 3 Metric Decision

### Domain
**Data and Privacy**

### Confirmed direction

#### Metric 1: Purview Classification Coverage
Reason:
- more directly reflects privacy and data-identification readiness
- shows how much of the AI-connected data estate has been classified in Microsoft Purview
- easier to anchor than a vague "total data items" denominator

Representation:
- **coverage donut + percentage**

Layout:
- keep the coverage number and donut **top-aligned** within the homepage tile

#### Metric 2: Sensitive Data Exposure Alerts
Reason:
- more decision-useful than a static count of sensitive-data AI systems
- better expresses active leakage or exposure risk
- current confirmed implementation should prioritize default **M365 / Purview** detections instead of relying on extra Azure application log correlation

Representation:
- **plain large number + 4-week bars**

Metric definition note:
- count **deduplicated alerts by week** using the M365 / Purview alert case population
- homepage copy should prefer **unique alert cases** instead of the more technical word **deduplicated**
- on the domain page, this metric is currently carried by:
  - **M365 / Purview Exposure Alerts**
- the earlier **Azure AI App Exposure Alerts** branch is no longer part of the current confirmed scope

## 8. Domain 4 Metric Decision

### Domain
**AI Security Protection**

### Confirmed direction

#### Metric 1: AI Resources in Unhealthy State
Reason:
- uses Microsoft Defender for Cloud / AI security posture's native assessment status
- avoids inventing a custom AI security baseline standard
- shows how much of the AI-scoped resource population is currently in unhealthy posture

Representation:
- **coverage donut + percentage**

#### Metric 2: Open High/Critical Defender Recommendations
Reason:
- uses Defender's native recommendation severity model
- expresses the current backlog of unresolved high-priority security weaknesses
- more decision-useful than raw attack-attempt or block-count metrics

Representation:
- **plain large number + short trend line**

Data basis:
- **Microsoft Defender for Cloud / AI security posture**
- filter to **AI-scoped resources**
- use **assessment state** and **open High/Critical recommendations**

## 9. Domain 5 Metric Decision

### Domain
**Output Trustworthiness and Content Provenance**

### Confirmed direction

#### Metric 1: Grounded Response Rate
Reason:
- best expresses whether outputs are supported by approved sources or validated evidence
- more suitable for homepage use than a generic hallucination metric
- better aligned to trustworthiness than a pure testing-process indicator

Representation:
- **coverage donut + percentage**

Automation note:
- feasible when outputs include citations, source references, retrieval traces, or evaluator results
- can be supported by Azure AI Foundry evaluations, Azure AI Search retrieval logs, and application output logs

#### Metric 2: Synthetic Content Labeling Gaps
Reason:
- directly expresses content disclosure / transparency gaps
- easier to automate than full provenance coverage in the current phase
- strongly aligned with NIST AI 600-1 attention to content provenance and disclosure

Representation:
- **plain large number + short trend line**

Automation note:
- feasible when generated content records include label / disclosure / watermark fields
- can be supported by content metadata, application logs, and workflow records

## 10. Domain 6 Metric Decision

### Domain
**Validation, Audit, and Compliance Assurance**

### Confirmed direction

#### Metric 1: Required Validation Coverage
Reason:
- best expresses whether the required assurance baseline has actually been completed across the in-scope AI population
- clearer for homepage use than an abstract score-style metric
- keeps the domain focused on assurance execution rather than runtime posture

Representation:
- **coverage donut + percentage**

Data basis:
- Azure AI Foundry evaluations
- Azure DevOps test plans / work items
- Microsoft Purview Compliance Manager
- Defender for Cloud regulatory compliance

#### Metric 2: Open High-Risk Findings
Reason:
- expresses the backlog of unresolved high-priority findings produced by validation, audit, or compliance work
- complements coverage by showing whether assurance issues are actually being closed
- preserves a clean boundary from security posture recommendations and incident counts

Representation:
- **plain large number + short trend line**

Scope note:
- count only findings from formal assurance activities
- do not mix in runtime security alerts, Defender posture recommendations, or operational incidents

## 11. Current Homepage Prototype File

Current visual prototype:

- `./AIGovernDashboardDesign/homepage-overview-mockup-v1.html`

This file should be kept aligned with decisions recorded in this document.

For implementation-level logic of the confirmed homepage KPIs, use:

- `./AIGovernDashboardDesign/dashboard-columns-v1.md`
- section: **一级页面已确认 KPI 实施口径（开发参考）**
