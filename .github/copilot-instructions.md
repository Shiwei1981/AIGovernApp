# Superpowers Project Instructions

Apply the superpowers workflow by default in this repository.

## When to Use

- Bootstrap a project from a short requirement
- Plan implementation from a vague request
- Diagnose a failing behavior or unclear bug report
- Refactor a local code path with minimal risk
- Add validation, tests, or setup steps before shipping

## Required Workflow

1. Identify the closest concrete anchor: a file, symbol, test, command, or failing behavior.
2. Form one falsifiable local hypothesis about the behavior or needed change.
3. Run the cheapest discriminating check available before widening scope.
4. Make the smallest grounded edit that tests or implements the hypothesis.
5. Validate immediately with the narrowest relevant test, lint, build, or runtime check.
6. Iterate locally until the slice is correct before expanding to adjacent work.
7. Summarize outcome, residual risk, and the next concrete step.

## Output Expectations

- Prefer minimal, targeted changes over broad rewrites.
- Preserve existing style and public APIs unless the task requires change.
- Validate with executable checks whenever the environment provides them.
- Call out blockers, assumptions, and missing inputs explicitly.

## Working Style

- Start from the nearest implementation surface instead of exploring broadly.
- Use the first focused validation step immediately after the first substantive edit.
- Keep changes local until the current slice is verified.
- If a hypothesis is disproved, move one hop closer to the controlling code path instead of reopening broad exploration.

## Repository Constraints

- Run the narrowest available validation for the touched slice before making adjacent edits.
- Do not widen scope with opportunistic refactors, formatting churn, or unrelated cleanup.
- Prefer `rg` and other targeted search commands over broad repository exploration.
- Prefer one persistent terminal session for diagnostics unless a separate long-running task is required.
- When tests exist, run the smallest relevant test target first; when they do not, run the narrowest lint, typecheck, or runtime validation that covers the change.
- Treat `.env.local` and other local configuration as sensitive: do not print, duplicate, or rewrite secrets unless the task explicitly requires it.
- Preserve existing APIs, file layout, and naming unless the requested change requires a breaking adjustment.
- If validation fails, repair the same local slice first before opening a second edit path.

The repository also includes the explicit skill entrypoint at `.github/skills/superpowers/SKILL.md`, so `/superpowers` remains available in chat.