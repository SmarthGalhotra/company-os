# Tool: gdrive

## Capability
Read and write documents in the company Google Drive (the factual-memory store).

## Contract
- `read path:<folder/doc>` → text of a doc/transcript. (read, auto)
- `write path:<folder/doc> content:<...>` → create/update an internal doc. (auto for drafts/notes)
- Sharing a doc externally → approve (leaves the company).

## Notes
Drive is where transcripts, notes, and filed updates live. The repo never copies this data in.
At Level 0, "read" = you paste the doc. At Level 2, connect Drive via a connector or API.
