# KPI sheet schema

One row per metric per period. Keep it boring and consistent — the agent reads this shape.

| Column | Meaning |
|--------|---------|
| metric | Name (e.g. ARR, active users, runway months) |
| period | Week/month identifier (e.g. 2026-W22) |
| value | The number |
| target | The goal for this period (optional) |
| owner | Who is the DRI for this metric |
| note | Optional driver/context |

Conventions: one canonical sheet, never delete history (append new periods), one DRI per metric.
