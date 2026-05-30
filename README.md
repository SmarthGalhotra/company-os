# [Company OS]([url](https://smarthgalhotra.github.io/company-os/))

A portable, data-free operating layer for running a company through AI. Clone it,
point it at a new company's data, and the workflows come with you.

This repo is **the OS**: skills, workflow specs, templates, policies, and the agent's
editable memory. It contains **no company data**. Data lives in Google Drive, Trello,
your KPI sheet, and call transcripts — none of which is committed here (see `.gitignore`).

That separation is the whole point. The valuable, portable thing is the *encoded
know-how* — how the company runs. The dashboards and scripts on top are disposable and
regenerable. Take the know-how with you; leave the data behind.

## The three principles this is built on

1. **Legibility** — every meaningful action produces a durable artifact in one place
   the agent can read. If it wasn't recorded, it didn't happen to the AI.
2. **Closed loops** — each process has a sensor (input), a policy (what's allowed), a
   tool layer (deterministic actions), a quality gate (eval + your review), and a
   learning step (it improves its own skill from what you corrected). The learning step
   is what makes it get better while you sleep.
3. **Durable vs. disposable** — context and skills are durable and portable; software
   on top is ephemeral. Regenerate the software per company; keep the skills forever.

## Progressive automation — you don't need code to start

| Level | What you do | What it needs |
|-------|-------------|---------------|
| 0 — Manual | Paste a `SKILLS/*.md` file + your data into a chat | Nothing |
| 1 — Assisted | Same, but the agent pulls data from Drive/Trello you connect | A chat app with connectors |
| 2 — Looped | Claude Code runs a `WORKFLOWS/*.md` on a schedule, drafts, waits for your approval | Claude Code + `TOOLS/` wired up |
| 3 — Self-improving | The workflow's learning step edits `instructions.md` and the skill after you correct it | Level 2 + a nightly run |

Start at Level 0 today. The first loop built out end-to-end is the **weekly update**
(`WORKFLOWS/weekly-update.md`) — use it as the template for every other function.

## Map

```
company-os/
  README.md          ← you are here
  SETUP.md           ← how to stand it up at a new company
  POLICY.md          ← what agents do alone vs. what needs your approval
  instructions.md    ← the agent's editable memory (behavioral). Edit like feedback to a hire.
  AGENTS.md          ← the resolver: index of every skill/workflow/tool. Keep it DRY + MECE.
  CONTEXT/           ← company data + brain (GITIGNORED). Example structure only is committed.
  SKILLS/            ← portable, composable units of know-how
  WORKFLOWS/         ← closed loops that chain skills + tools on a schedule
  TOOLS/             ← contracts for integrations (Trello, Drive, KPI sheet, email)
  TEMPLATES/         ← the shape of outputs (weekly update, KPI schema, notes, deck)
```

## Three kinds of memory (so you know where things go)

- **Factual** — what's true about the company. Lives in `CONTEXT/` and your real data.
- **Behavioral** — how you want the agent to act. Lives in `instructions.md`. You edit it.
- **Procedural** — repeatable tasks. Lives in `SKILLS/` and `TOOLS/`. The agent extends it.
