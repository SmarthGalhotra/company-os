# Setup — standing this up at a new company

This is the plug-and-play path. The repo is the OS; you supply the data.

1. **Clone the repo.** `CONTEXT/` is empty except the example — that's intentional.
2. **Fill `CONTEXT/company.md`** from `company.example.md`. This is the agent's factual base.
3. **Adjust `POLICY.md`** if this company's risk lines differ.
4. **Start at Level 0 (no code):** open `WORKFLOWS/weekly-update.md`, paste the skill +
   your KPI numbers + your Trello Done list into a chat, get a draft, approve, file it to
   `CONTEXT/updates/`. Do the learning step by hand.
5. **Move to Level 2 when ready:** wire `TOOLS/` (Trello, Drive, KPI sheet) to real APIs and
   let Claude Code run the workflow on a schedule with human approval on the send.
6. **Grow the OS:** each new function = copy `WORKFLOWS/weekly-update.md`, swap the sensors,
   add a row to `AGENTS.md`, run the DRY/MECE check.

What you carry to the next company: everything here **except** `CONTEXT/`. The know-how is portable.
