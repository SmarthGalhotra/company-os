# Workflow: Weekly Update (the reference closed loop)

This is the template every other workflow copies. It has the five parts of a closed loop.
Read `instructions.md` and `POLICY.md` before running.

**Goal:** every week, produce an accurate weekly update — KPIs, what shipped, customer
signal — drafted automatically, approved by a human before it leaves, and a little
better each week than the last.

---

## 1. Sensor (inputs)

Pull, don't ask. Gather from real sources every run:

- **KPIs** — via `TOOLS/kpi-sheet.md`. Current values + last week's values.
- **Shipped** — via `TOOLS/trello.md`: cards moved to Done since last update.
- **Customer signal** — call summaries in `CONTEXT/customers/` (produced by the
  `customer-call-summary` skill), support tickets, notable emails.
- **Last week's update** — `CONTEXT/updates/` so you can reference deltas and open asks.

If a source is empty or unreachable, say so in the draft rather than inventing.

## 2. Policy (what's allowed)

- Drafting the update → **auto** (low-risk; per `POLICY.md`).
- Sending it to the accelerator / investors → **approve** (high-risk; leaves the company).
- Filing the approved copy into `CONTEXT/updates/` → auto.

## 3. Tools (deterministic actions)

`kpi-sheet` (read), `trello` (read Done), `gdrive` (read transcripts, write the draft).
Sending is a separate, gated step — not part of the auto path.

## 4. Quality gate

Before surfacing the draft, self-check against this list. If any fails, fix and re-check:

- [ ] Every number has value + delta + one-line reason for the move.
- [ ] Bad news is stated plainly and up top, not buried.
- [ ] "Shipped" reflects Trello Done, not plans.
- [ ] There is exactly one clear ask (or "no ask this week").
- [ ] Output matches `TEMPLATES/weekly-update.md`.
- [ ] No claim without a source.

Then post: the draft + "Ready to send to <recipient>? [approve / edit / no]" + risk tag.

## 5. Learning step (what makes it improve)

After you approve or edit:

1. Diff your final version against the agent's draft.
2. Extract the *general* lesson from each edit (not the one-off fact).
3. Append it to `instructions.md` under "Learned lessons" (1–2 lines, dated, "from your edit").
4. If the same kind of edit recurs 2–3 times, propose updating `SKILLS/weekly-update.md`
   itself — and per `POLICY.md`, a change affecting a high-risk send needs your approval.

That's the loop: it drafts, you correct, it encodes the correction, next week it needs
fewer corrections.

---

## Run modes

- **Level 0 (today):** paste `SKILLS/weekly-update.md` + your KPI numbers + your Done list
  into a chat. Do the learning step by hand (paste your edits back, ask it for the lesson).
- **Level 2+:** Claude Code runs this file on a schedule, pulls via `TOOLS/`, posts the
  draft to Slack, waits for `approve`, then sends and files. The learning step runs nightly.

## Copy this for a new function

To add (e.g.) a customer-feedback loop: copy this file, swap the sensor sources, point at
the relevant skill + tools, write a gate checklist for that output, keep the same learning
step. Add a row to `AGENTS.md`.
