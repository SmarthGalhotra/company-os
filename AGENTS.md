# AGENTS.md — the resolver

The index the agent reads first. Every skill, workflow, and tool is listed here exactly
once with a one-line description and a link. Keep it **DRY** (no duplicate capability) and
**MECE** (each entry distinct, together they cover the job). If two entries overlap, merge
them. This table is the optimal "what can I do" lookup.

## Workflows (closed loops — chain skills + tools on a cadence)

| Workflow | Trigger | What it does | Spec |
|----------|---------|--------------|------|
| Weekly update | Weekly / manual | Compose KPI + shipped + customer signal into the update; draft, gate, learn | [WORKFLOWS/weekly-update.md](WORKFLOWS/weekly-update.md) |

## Skills (composable units of know-how)

| Skill | Use it to | File |
|-------|-----------|------|
| weekly-update | Turn inputs into a structured weekly update | [SKILLS/weekly-update.md](SKILLS/weekly-update.md) |
| kpi-digest | Read the KPI sheet, compute deltas, explain moves | [SKILLS/kpi-digest.md](SKILLS/kpi-digest.md) |
| customer-call-summary | Turn a call transcript into notes + CRM updates + feature requests | [SKILLS/customer-call-summary.md](SKILLS/customer-call-summary.md) |
| 1on1-prep | Build a brief before an accelerator/team 1-on-1; capture follow-ups after | [SKILLS/1on1-prep.md](SKILLS/1on1-prep.md) |
| deck-builder | Draft a deck outline from company context | [SKILLS/deck-builder.md](SKILLS/deck-builder.md) |
| two-sentence-pitch | Write/sharpen the "what is it + why interesting" description | [SKILLS/two-sentence-pitch.md](SKILLS/two-sentence-pitch.md) |

## Tools (deterministic actions — contracts the agent calls)

| Tool | Capability | Contract |
|------|-----------|----------|
| trello | Read/move/create cards | [TOOLS/trello.md](TOOLS/trello.md) |
| gdrive | Read/write docs in the company Drive | [TOOLS/gdrive.md](TOOLS/gdrive.md) |
| kpi-sheet | Read rows/columns from the KPI sheet | [TOOLS/kpi-sheet.md](TOOLS/kpi-sheet.md) |

## How to extend (the self-extending pattern)

When a repeated task can't be done with what's above: build the skill or tool, add one
row here, then run a "check-resolvable" pass — is it DRY (does it duplicate something?)
and MECE (is its scope distinct?). If it overlaps, merge instead of adding.
