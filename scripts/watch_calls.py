#!/usr/bin/env python3
"""
watch_calls.py — Level 2 trigger for WORKFLOWS/call-analysis.md

Polls CONTEXT/calls/inbox/ for new YAML files and runs the call-analysis workflow on each,
then ledgers and moves them so nothing is processed twice.

Run on a schedule (every few minutes):
    */5 * * * * cd /path/to/company-os && python3 scripts/watch_calls.py

Or as a real file-watcher (fswatch on macOS, inotifywait on Linux) calling this script.

How it hands work to your agent:
  This script is harness-agnostic. Set RUN_AGENT below to the command that runs your agent
  on one file. With Claude Code, that's typically a non-interactive invocation that points
  the agent at WORKFLOWS/call-analysis.md and the file path. Until you wire that, the script
  runs in DRY mode and just prints which files it WOULD process — safe to test immediately.
"""

import os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "CONTEXT" / "calls" / "inbox"
ANALYZED = ROOT / "CONTEXT" / "calls" / "analyzed"
LEDGER = ROOT / "CONTEXT" / "calls" / ".processed"

# Set to a list like: ["claude", "-p", "Run WORKFLOWS/call-analysis.md on {file}"]
# Use {file} as the placeholder for the absolute path. Leave as None for DRY mode.
RUN_AGENT = None

YAML_EXT = {".yaml", ".yml"}


def processed_set():
    if not LEDGER.exists():
        return set()
    return set(LEDGER.read_text().splitlines())


def mark_processed(name):
    with LEDGER.open("a") as f:
        f.write(name + "\n")


def main():
    ANALYZED.mkdir(parents=True, exist_ok=True)
    done = processed_set()
    new = [p for p in sorted(INBOX.glob("*")) if p.suffix.lower() in YAML_EXT and p.name not in done]

    if not new:
        print("No new call files.")
        return

    for path in new:
        print(f"New call file: {path.name}")
        if RUN_AGENT is None:
            print("  DRY mode — set RUN_AGENT to actually analyze. Skipping.")
            continue
        cmd = [arg.replace("{file}", str(path)) for arg in RUN_AGENT]
        try:
            subprocess.run(cmd, check=True, cwd=ROOT)
        except subprocess.CalledProcessError as e:
            print(f"  Agent run failed for {path.name}: {e}", file=sys.stderr)
            continue  # leave in inbox, retry next poll
        mark_processed(path.name)
        shutil.move(str(path), str(ANALYZED / path.name))
        print(f"  Analyzed and moved to analyzed/.")


if __name__ == "__main__":
    main()
