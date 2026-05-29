# Workflow: Call Analysis (auto, self-improving)

Trigger: a new YAML file lands in the calls inbox. The agent runs the `call-analyzer`
skill on it, sends the tips to you/your team, files the result, and gets better at
coaching over time.

Runs end-to-end on its own — per `POLICY.md`, analyzing and notifying *internally* is
low-risk, so no approval needed.

---

## 1. Sensor (trigger + input)
- **Trigger:** a `.yaml`/`.yml` file appears in the calls inbox that isn't in the processed
  ledger (`.processed`).
- **Input — map the YAML to the skill like this:**
  - Transcript → join the `transcript[]` list into text, prefixing each line with
    `speaker_name`. This is what the skill analyzes.
  - External tool feedback → `coaching_feedback[]` (each has `section_label`,
    `short_feedback`, `long_feedback`). Pass this to the skill as the tool's prior feedback
    so it can corroborate or push back, not just repeat it.
  - Metadata → `recording.title`, `recording.date`, `recording.duration_seconds`, `speakers`.
- Also load: `playbook.md` and the last 3 files in `analyzed/` to detect recurrence.

## 2. Policy
- Analyze → auto. Send tips to internal Slack/email → auto (stays in the company).
- Editing `playbook.md` → auto. A change to the skill itself follows the self-improvement
  rule in `POLICY.md`.

## 3. Tools & skill
- `call-analyzer` skill → `SKILLS/call-analyzer/SKILL.md` (reads its own `references/` KBs).
- `notify` (`TOOLS/notify.md`) to send the tips.
- `gdrive`/filesystem to read the YAML and write the analysis + playbook.

## 4. Quality gate
Before sending, self-check:
- [ ] Output follows the skill's own structure (Quick Verdict → Scorecard → What to Change
      → What Worked → Moments → Patterns → Drills for next call).
- [ ] Every critique/compliment is tied to a transcript quote AND a KB principle.
- [ ] Recurrence vs. the last 3 calls is noted.
- [ ] The "Top 3 Drills for Next Call" are specific behaviors, not generic advice.

## 5. Learning step (this is what closes the loop)
1. Append the analysis to `analyzed/<date>-<recording.title>.md`.
2. Update `playbook.md`:
   - Add/increment any recurring issue (with a count).
   - Move resolved issues to an "Improved" section with the date.
3. If an issue recurs **3+ times**, propose sharpening the skill — usually by adding a line
   to a `references/` KB so the analyzer catches it earlier (this keeps your KB, the
   portable asset, improving). Skill change = follows `POLICY.md`.
4. Add the file to `.processed` and move it to `analyzed/`.

**The signal that the loop works:** recurring-issue counts in `playbook.md` trend down.

---

## How the trigger fires
- **Level 0 (no code):** drop the YAML in the inbox, then run the skill on it in a chat. Do
  steps 1–5 by hand once to see the shape.
- **Level 2 (automatic):** `scripts/watch_calls.py` (cron or file-watcher) finds new files
  and hands each to Claude Code to run this workflow, then moves and ledgers them.

## Destination
Set where tips go and where the inbox lives in `CONTEXT/company.md`.
