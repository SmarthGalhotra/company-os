#!/usr/bin/env python3
"""
verify_company_os.py — checks your company-os repo against the intended design.

Run from the repo root:  python verify_company_os.py
No dependencies. Prints a PASS/FAIL report. Exit code 0 = all good.
"""

import os, sys

# (path, must-be-dir?)  — relative to repo root
CORE = [
    "README.md", "SETUP.md", "POLICY.md", "instructions.md", "AGENTS.md", ".gitignore",
    "CONTEXT/README.md", "CONTEXT/company.example.md",
    "CONTEXT/customers/.gitkeep", "CONTEXT/updates/.gitkeep",
    "SKILLS/weekly-update.md", "SKILLS/kpi-digest.md", "SKILLS/customer-call-summary.md",
    "SKILLS/1on1-prep.md", "SKILLS/deck-builder.md", "SKILLS/two-sentence-pitch.md",
    "WORKFLOWS/weekly-update.md",
    "TOOLS/README.md", "TOOLS/trello.md", "TOOLS/gdrive.md", "TOOLS/kpi-sheet.md",
    "TEMPLATES/weekly-update.md", "TEMPLATES/kpi-schema.md",
    "TEMPLATES/meeting-notes.md", "TEMPLATES/deck-outline.md",
]

CALL_ADDON = [
    "SKILLS/call-analyzer/SKILL.md",
    "SKILLS/call-analyzer/references/communication-kb.md",
    "SKILLS/call-analyzer/references/customer-discovery-kb.md",
    "WORKFLOWS/call-analysis.md",
    "TOOLS/notify.md",
    "CONTEXT/calls/README.md", "CONTEXT/calls/playbook.md", "CONTEXT/calls/.processed",
    "CONTEXT/calls/inbox/.gitkeep", "CONTEXT/calls/analyzed/.gitkeep",
    "scripts/watch_calls.py",
]

# substrings that should appear in AGENTS.md (the three resolver rows)
AGENTS_ROWS = [
    "WORKFLOWS/call-analysis.md",
    "SKILLS/call-analyzer/SKILL.md",
    "TOOLS/notify.md",
]

# substrings the corrected workflow should contain (proves the YAML-schema fix landed)
WORKFLOW_CONTENT = ["coaching_feedback", "transcript", "recording"]

SHOULD_NOT_EXIST = ["SKILLS/call-analyzer.md"]  # the old single-file placeholder

GREEN, RED, YEL, OFF = "\033[92m", "\033[91m", "\033[93m", "\033[0m"
ok = lambda: f"{GREEN}OK{OFF}"
miss = lambda: f"{RED}MISSING{OFF}"
warn = lambda: f"{YEL}WARN{OFF}"

def check_files(label, files):
    print(f"\n=== {label} ===")
    bad = 0
    for f in files:
        present = os.path.exists(f)
        print(f"  [{ok() if present else miss()}] {f}")
        bad += 0 if present else 1
    return bad

def main():
    if not os.path.exists("AGENTS.md"):
        print(f"{RED}AGENTS.md not found — run this from the company-os repo root.{OFF}")
        sys.exit(2)

    fails = 0
    fails += check_files("Core OS files", CORE)
    fails += check_files("Call-analysis add-on files", CALL_ADDON)

    print("\n=== AGENTS.md resolver rows ===")
    agents = open("AGENTS.md", encoding="utf-8").read()
    for row in AGENTS_ROWS:
        hit = row in agents
        print(f"  [{ok() if hit else miss()}] links to {row}")
        fails += 0 if hit else 1

    print("\n=== Workflow schema fix ===")
    if os.path.exists("WORKFLOWS/call-analysis.md"):
        wf = open("WORKFLOWS/call-analysis.md", encoding="utf-8").read()
        for s in WORKFLOW_CONTENT:
            hit = s in wf
            print(f"  [{ok() if hit else miss()}] mentions '{s}'")
            fails += 0 if hit else 1
    else:
        print(f"  [{miss()}] WORKFLOWS/call-analysis.md not present")
        fails += 1

    print("\n=== Should NOT exist (old placeholders) ===")
    for f in SHOULD_NOT_EXIST:
        gone = not os.path.exists(f)
        print(f"  [{ok() if gone else warn()}] {f} {'(absent, good)' if gone else '(delete this — replaced by the folder)'}")

    print("\n" + ("="*40))
    if fails == 0:
        print(f"{GREEN}ALL CHECKS PASSED — your repo matches the intended design.{OFF}")
        sys.exit(0)
    else:
        print(f"{RED}{fails} item(s) missing or wrong — see the lines marked above.{OFF}")
        sys.exit(1)

if __name__ == "__main__":
    main()
