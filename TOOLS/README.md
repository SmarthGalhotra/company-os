# Tools

A tool is a **contract**: a named, deterministic capability the agent can call. Each file
states what the tool does, its inputs/outputs, and which actions are auto vs. approve.

At Level 0–1 a "tool" is just you (or a chat connector) doing the read/write by hand.
At Level 2+ it's a real CLI/script Claude Code runs. The contract stays the same either way,
which is why the skills don't change when you automate. Keep tools **CLI-style** — agents
work well with simple command-line contracts.

Register every tool in `AGENTS.md`. Don't add a second tool that does what an existing one
does (DRY); extend the existing one with a parameter instead.
