# Tool: kpi-sheet

## Capability
Read values from the company's KPI sheet. Schema defined in TEMPLATES/kpi-schema.md.

## Contract
- `read-current` → latest value per metric. (read, auto)
- `read-period start:<date> end:<date>` → values over a range, for deltas/trends. (read, auto)

## Notes
Read-only by design — the agent reports on KPIs, humans set targets. At Level 0, paste the rows.
