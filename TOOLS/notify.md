# Tool: notify

## Capability
Send a message internally — Slack channel/DM or email — to you or your team.

## Contract
- `slack channel:<#name> text:<...>` → post to a channel. (internal → auto)
- `email to:<internal@...> subject:<...> body:<...>` → send. (internal → auto)
- Sending to anyone **outside the company** → not this tool; that path is approve-gated.

## Notes
Destination defaults live in `CONTEXT/company.md` (e.g. call-coaching channel).
Level 0: "send" = the agent just shows you the message in chat. Level 2: wire Slack/email APIs.
