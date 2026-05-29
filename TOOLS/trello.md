# Tool: trello

## Capability
Read cards, move cards between lists, create cards.

## Contract (intent → action)
- `list-done since:<date>` → cards moved to Done since date. (read, auto)
- `create-card list:<list> title:<t> due:<date>` → new card. (auto for internal trackers)
- `move-card id:<id> to:<list>` → reflect reality. (auto)

## Notes
At Level 0, "done" = paste your Done column. At Level 2, wire Trello's API behind this contract.
Nothing here sends anything externally, so all actions are low-risk/auto per POLICY.md.
