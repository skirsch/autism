from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SOURCE = Path(r"C:\Users\stk\Downloads\SOA2-Public view.csv")
OUTPUT = Path(r"C:\Users\stk\Documents\GitHub\autism\outputs\parent_onset_age_confidence_comparison_4_to_60.png")
PRECISE = {
    "Absolutely certain",
    "Within 0 to 2 days",
    "Within 2 days to a week",
    "Could be off by a week to up to a month",
}


def is_sudden(row: dict[str, str]) -> bool:
    pattern = (row.get("Developmental pattern") or "").strip()
    speed = (row.get("Regression speed") or "").strip().lower()
    return not pattern or speed.startswith("there was a rapid change")


def age_month(row: dict[str, str]) -> int | None:
    try:
        value = float((row.get("Age at onset (in months)") or "").strip())
    except ValueError:
        return None
    return int(value) if math.isfinite(value) and value >= 0 and value.is_integer() else None


with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))

cohort = [row for row in rows if is_sudden(row)]
restricted = [
    row for row in cohort
    if (row.get("Confidence in onset date") or "").strip() in PRECISE
]
months = np.arange(4, 61)


def distribution(records: list[dict[str, str]]) -> tuple[Counter[int], int]:
    counts = Counter(
        age for row in records
        if (age := age_month(row)) is not None and 4 <= age <= 60
    )
    return counts, sum(counts.values())


all_counts, all_n = distribution(cohort)
restricted_counts, restricted_n = distribution(restricted)
all_pct = np.array([100 * all_counts[m] / all_n for m in months])
restricted_pct = np.array([100 * restricted_counts[m] / restricted_n for m in months])
correlation = float(np.corrcoef(all_pct, restricted_pct)[0, 1])

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(16, 7.5))
width = 0.40
ax.bar(months - width / 2, all_pct, width=width, color="#A8C9D6", label=f"All sudden-onset respondents (n={all_n})")
ax.bar(months + width / 2, restricted_pct, width=width, color="#176B87", label=f"Onset date certain within ≤1 month (n={restricted_n})")
ax.set_title("Age at Parent-Noticed Onset: Date-Confidence Sensitivity", fontsize=19, weight="bold", pad=18)
ax.text(
    0.5, 1.012,
    f"One-month bins, ages 4–60 • normalized within each group • monthly-profile correlation r={correlation:.3f}",
    transform=ax.transAxes, ha="center", va="bottom", fontsize=10.5, color="#44515C",
)
ax.set_xlabel("Child age when parent noticed onset (months)", fontsize=12, labelpad=12)
ax.set_ylabel("Percent of respondents in group", fontsize=12, labelpad=10)
ax.set_xticks(months)
ax.set_xticklabels(months, fontsize=8, rotation=90)
ax.set_xlim(3.35, 60.65)
ax.set_ylim(bottom=0)
ax.grid(axis="x", visible=False)
ax.grid(axis="y", color="#D9E0E5", linewidth=0.8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, loc="upper right", fontsize=10)
fig.tight_layout()
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"all_n_4_60={all_n}")
print(f"restricted_n_4_60={restricted_n}")
print(f"monthly_profile_correlation={correlation:.6f}")
print("month,all_count,all_percent,restricted_count,restricted_percent")
for i, month in enumerate(months):
    print(f"{month},{all_counts[month]},{all_pct[i]:.3f},{restricted_counts[month]},{restricted_pct[i]:.3f}")
print(f"output={OUTPUT}")
