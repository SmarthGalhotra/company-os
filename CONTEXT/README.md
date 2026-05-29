# CONTEXT — the company brain (data layer)

**This folder is git-ignored. It never goes to GitHub.** It holds company-specific data:
the factual memory the agent reads. Only this README and `company.example.md` are committed,
so a new company knows the shape to fill in.

Suggested layout:

```
CONTEXT/
  company.md          ← who we are, model, stage, the two-sentence pitch, current priorities
  customers/          ← one file per customer (filed by customer-call-summary)
  updates/            ← past weekly updates (filed after approval)
  people.md           ← team, DRIs per area, accelerator contacts
  funding.md          ← raise status, investor pipeline, asks
```

Rule from the source material: **never throw data away, treat software as disposable.**
Keep transcripts and notes here (or pointers to Drive); regenerate dashboards/scripts freely.
