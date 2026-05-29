# Skill: weekly-update

Turn raw inputs into a structured weekly update. Composable — the workflow calls this; you
can also call it standalone in a chat.

## Inputs

- KPI table: metric, current value, prior value (from `kpi-digest` or pasted).
- Shipped: list of things completed this week (from Trello Done or pasted).
- Customer signal: 2–5 notable things customers said/did this week.
- Prior update (optional): to reference open asks and deltas.

## Procedure

1. Run the numbers through the framing in `SKILLS/kpi-digest.md` (value + delta + why).
2. Write "Shipped" as outcomes, not activity ("X now live for all users", not "worked on X").
3. Distill customer signal into the 1–3 things that should change a decision.
4. End with one ask, or state there's none.
5. Format per `TEMPLATES/weekly-update.md`.

## Rules

- Plain voice, no hype (see `instructions.md`).
- Lead with the headline metric and any bad news. Don't bury misses.
- Never assert a number or a "shipped" item without a source.

## Output

A filled `TEMPLATES/weekly-update.md`, ready for the workflow's quality gate.
