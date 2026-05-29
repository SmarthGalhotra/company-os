# Policy — autonomy and approval

Default stance: **auto for low-risk, approve for high-risk.** Every workflow references
this file. When in doubt, treat it as high-risk and ask.

## Auto (do it, then log it)

The agent may complete these without asking, and records what it did to the run log:

- Reading data (Drive, Trello, KPI sheet, transcripts).
- Drafting internal artifacts: weekly-update drafts, meeting summaries, KPI digests,
  call notes, deck outlines, 1-on-1 prep briefs.
- Updating internal trackers it owns: moving Trello cards to reflect reality, tagging,
  filing notes into `CONTEXT/`.
- Proposing changes to its own skills / `instructions.md` (proposing — not merging
  anything that sends or spends).

## Approve (draft it, then wait for a human "go")

The agent must surface a draft and get an explicit yes before:

- **Anything that leaves the company**: emails/messages to investors, the accelerator,
  customers, or partners; anything published.
- **Anything that spends money** or commits to spend.
- **Anything destructive or irreversible**: deleting data, closing tickets as resolved,
  changing prices, cancelling/booking.
- **Hiring, legal, financial, or personnel** content.
- **Merging a self-improvement** that changes how a high-risk task behaves.

## How approval works

The agent posts: (1) the draft, (2) a one-line "what I'm about to do and where it goes,"
(3) the risk tag. You reply `approve`, `edit: <change>`, or `no`. Your edits feed the
learning step (see any `WORKFLOWS/*.md`).

## Escalate to a human, never auto

Novel/high-stakes/emotional situations the model shouldn't touch alone: co-founder
disputes, firing, crisis comms, anything where a wrong call is expensive and the model
lacks context. These are the "humans at the edge" cases — the agent flags and stops.
