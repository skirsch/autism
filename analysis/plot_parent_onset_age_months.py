from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


SOURCE = Path(r"C:\Users\stk\Downloads\SOA2-Public view.csv")
OUTPUT = Path(r"C:\Users\stk\Documents\GitHub\autism\outputs\parent_onset_age_4_to_60_months.png")


def is_sudden_onset(row: dict[str, str]) -> bool:
    """Match the sudden-onset cohort used in the current seven-test analysis."""
    developmental_pattern = (row.get("Developmental pattern") or "").strip()
    regression_speed = (row.get("Regression speed") or "").strip().lower()
    return not developmental_pattern or regression_speed.startswith("there was a rapid change")


def whole_month(value: str) -> int | None:
    try:
        number = float(value.strip())
    except (AttributeError, ValueError):
        return None
    if not math.isfinite(number) or number < 0 or not number.is_integer():
        return None
    return int(number)


with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))

eligible = [row for row in rows if is_sudden_onset(row)]
ages = [whole_month(row.get("Age at onset (in months)", "")) for row in eligible]
valid_ages = [age for age in ages if age is not None]

counts = Counter(age for age in valid_ages if 4 <= age <= 60)
months = list(range(4, 61))
values = [counts[month] for month in months]

below = sum(age < 4 for age in valid_ages)
above = sum(age > 60 for age in valid_ages)
missing_invalid = len(ages) - len(valid_ages)
included = sum(values)

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(16, 7.5))
ax.bar(months, values, width=0.82, color="#176B87", edgecolor="#0E4F63", linewidth=0.45)
ax.set_title("Parent-Reported Age at Noticed Onset", fontsize=20, weight="bold", pad=20)
ax.text(
    0.5,
    1.015,
    f"Sudden-onset cohort • one-month bins • ages 4–60 months • n={included:,}",
    transform=ax.transAxes,
    ha="center",
    va="bottom",
    fontsize=11,
    color="#44515C",
)
ax.set_xlabel("Child age when parent noticed onset (months)", fontsize=12, labelpad=12)
ax.set_ylabel("Number of respondents", fontsize=12, labelpad=10)
ax.set_xticks(months)
ax.set_xticklabels(months, fontsize=8, rotation=90)
ax.set_xlim(3.35, 60.65)
ax.set_ylim(bottom=0)
ax.grid(axis="x", visible=False)
ax.grid(axis="y", color="#D9E0E5", linewidth=0.8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

peak = max(values) if values else 0
for month, value in zip(months, values):
    if value == peak and peak > 0:
        ax.text(month, value + max(0.5, peak * 0.015), str(value), ha="center", va="bottom", fontsize=9, weight="bold")

fig.text(
    0.01,
    0.012,
    f"Outside plotted range: {below} below 4 months; {above} above 60 months. "
    f"Missing/non-whole-month age: {missing_invalid}.",
    fontsize=9,
    color="#56636E",
)
fig.tight_layout(rect=(0, 0.045, 1, 1))
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT, dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"source_rows={len(rows)}")
print(f"sudden_onset_eligible={len(eligible)}")
print(f"valid_whole_month_ages={len(valid_ages)}")
print(f"included_4_to_60={included}")
print(f"below_4={below}")
print(f"above_60={above}")
print(f"missing_or_invalid={missing_invalid}")
print("month,count")
for month in months:
    print(f"{month},{counts[month]}")
print(f"output={OUTPUT}")
