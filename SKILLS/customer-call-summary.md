# Skill: customer-call-summary

Turn a customer call transcript into a durable artifact: notes, CRM updates, feature requests.

## Inputs
- A transcript (recorded call). If none exists, that's the legibility gap to close — record next time.
- The customer's prior notes from `CONTEXT/customers/` if any.

## Procedure
1. Summarize: who, what they want, blockers, sentiment, next step + owner + date.
2. Extract feature requests verbatim-in-meaning; tag each as on-roadmap / maybe / decline.
3. Propose CRM/Trello updates (per `POLICY.md`: filing internal = auto; emailing them = approve).
4. Surface the 1 thing from this call that should change a product or sales decision.

## Output
A note filed to `CONTEXT/customers/<name>.md` + a list of proposed updates for approval.
