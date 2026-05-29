# Skill: kpi-digest

Read the KPI sheet, compute period-over-period deltas, and explain each move.

## Inputs
- KPI sheet (via `TOOLS/kpi-sheet.md`) or a pasted table. Schema in `TEMPLATES/kpi-schema.md`.
- The prior period's values.

## Procedure
1. For each metric: current value, absolute + % delta vs. prior, direction (good/bad/flat).
2. Write a one-line reason for each material move. If unknown, say "driver unknown — needs investigation" (don't guess).
3. Flag any metric off target or trending the wrong way at the top.

## Output
A short digest: headline metric first, then a metric → value → delta → reason line each.
Feeds `weekly-update` and any KPI alert.
