---
name: call-analyzer
description: >
  Analyzes a customer call transcript or meeting notes against the founder's personal knowledge base, covering both customer discovery methodology and communication quality. Use this skill whenever a user shares a call transcript, meeting notes, or conversation log and wants feedback. Triggers on: "analyze this call", "review this transcript", "what did I do well/poorly", "grade this customer conversation", "how was my discovery call", "feedback on this meeting". Produces a structured scorecard with specific quotes from the transcript linked to principles from the knowledge base. The analysis covers: discovery quality (Mom Test compliance, commitment signals, customer segmentation), and communication quality (presence, vocal signals, questioning craft, listening, structure).
---

# Call Analyzer Skill

Analyzes customer call transcripts against the founder's personal knowledge base. Produces specific, evidence-based feedback with transcript quotes as evidence, grounded in the KB principles.

## Reference Files
Before analyzing, read both reference files:
- `references/customer-discovery-kb.md` — Customer discovery and sales principles
- `references/communication-kb.md` — Communication and delivery principles

Only analyze against content in these files. Do not apply generic communication advice not grounded in the KB.

## Analysis Mode Selection

First, determine what kind of call this is:

| Call Type | Primary Analysis |
|---|---|
| Customer discovery / problem interview | Full Mom Test analysis + communication |
| Sales / demo call | Commitment & Advancement focus + communication |
| General meeting / stakeholder call | Communication focus + discovery if relevant |
| Investor pitch call | Commitment signals + clarity + communication |
| User research / UX interview | Mom Test analysis + questioning craft |

Ask the user if the call type is unclear.

## Output Structure

Produce a structured report with these sections:

---

### 🎯 Quick Verdict
One paragraph: what was the single most important thing that went well, and the single most important thing to change.

---

### 📊 Scorecard

Score each dimension 1–5 with a brief (one-sentence) justification.

**Customer Discovery Quality** (if applicable):
| Dimension | Score | Evidence |
|---|---|---|
| Mom Test compliance | /5 | [Brief justification + quote] |
| Avoided bad data (compliments/fluff) | /5 | |
| Asked scary/important questions | /5 | |
| Commitment/next steps secured | /5 | |
| Customer talk ratio (60–70% target) | /5 | |
| Segment clarity | /5 | |

**Communication Quality**:
| Dimension | Score | Evidence |
|---|---|---|
| Presence / active listening | /5 | |
| Questioning craft | /5 | |
| Message clarity | /5 | |
| Filler / linguistic precision | /5 | |
| Talk/listen balance | /5 | |

---

### 🔴 What to Change (Top 3, Prioritized)

For each issue:
- **The problem** (one sentence)
- **KB principle violated** (cite the relevant KB section)
- **Evidence from transcript** (exact quote or paraphrase)
- **What to do instead** (specific, actionable)

---

### ✅ What Worked (Top 3)

For each strength:
- **The behavior** (one sentence)
- **KB principle demonstrated** (cite the relevant KB section)
- **Evidence from transcript** (exact quote or paraphrase)

---

### 💬 Specific Transcript Moments

Find 5–7 specific moments in the transcript and annotate them:

> **[Quote from transcript]**  
> ⚠️/✅ [Analysis: what this demonstrates and why it matters, linked to KB]

---

### 🔁 Patterns Across the Call

Note any patterns that appear multiple times (e.g., "recurring: accepted compliments without anchoring" or "recurring: strong past-behavior questions"). Patterns are more actionable than isolated moments.

---

### 📋 Top 3 Drills / Improvements for Next Call

Concrete practice suggestions tied to KB content. Not generic advice — specific behaviors to practice.

---

## Analysis Principles

### Quote first, conclude second
Ground every critique and every compliment in a specific transcript moment. Don't make claims without evidence.

### Prioritize discovery over delivery
If the call was a customer discovery call and the Mom Test was violated, that's more important than filler language. Lead with the high-impact issues.

### Distinguish fatal from fixable
Some issues prevent learning (talking too much, accepting compliments as validation, hypothetical questions) — flag these as high priority. Other issues reduce effectiveness (filler, pace) but don't corrupt the data.

### Be specific and constructive
"You said 'would you ever use something like this?' — this is a hypothetical future question that invites 'yes' regardless of real intent. Instead: 'Tell me about the last time you ran into this problem. What did you do?'"

Not: "You asked bad questions."

### Calibrate by call stage
Early discovery calls should be evaluated primarily on Mom Test compliance. Later-stage calls (sales, demo) should weight commitment/advancement more heavily.

---

## Handling Missing Transcript Elements

If the transcript is incomplete (e.g., one-sided, partial, from notes):
- Analyze what's available
- Flag clearly what can't be assessed
- Note what additional information would allow a fuller analysis

If the user shares notes rather than a full transcript:
- Analyze the notes
- Ask: "Do you have the actual transcript, or is this all we have?" — more specific feedback is possible with full text

---

## Calibrating Tone

The goal is growth, not judgment. Frame feedback as:
- "This is what happened and why it matters" (not "this was wrong")
- "Here's a better version of that moment" (concrete alternative)
- "The principle behind this" (so the user internalizes, not just fixes)

If the call was generally strong, say so clearly — founders often benefit more from reinforcement of good instincts than critique of minor issues.
