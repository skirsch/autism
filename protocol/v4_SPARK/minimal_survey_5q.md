# Minimal Onset Survey (5 questions)

Airtable-ready. No vaccine or immunization word appears anywhere; the only cause question is last and open-ended. Everything about what happened before onset is unaided free text, coded blind after collection.

---

## Form title
**When did you first notice the change?**

## Intro (shown above the questions)
This is a short survey for parents of a child with autism who remember a **sudden, dramatic change** in their child — a day when the child lost words, eye contact, or skills, or when new behaviors appeared, after developing normally before that. We call that day the **onset date**. If your child's autism appeared gradually with no such day, this survey is not for you — thank you anyway.

Five questions, about one minute.

## Consent (required checkbox)
I am 18 or older and the child's parent or legal guardian. I understand that my answers to the first three questions will be published as-is, and that my written answers will be published only after names, places, dates, and other identifying details have been removed.

---

### Q1 — How long ago (required, single select)
**How long ago was the onset date?**
- Within the last 3 months
- 3 to 6 months ago
- 6 months to 1 year ago
- 1 to 2 years ago
- 2 to 5 years ago
- More than 5 years ago

### Q2 — Day of week (required, single select)
**Do you remember what day of the week the onset date was?**
- Monday · Tuesday · Wednesday · Thursday · Friday · Saturday · Sunday
- It was a weekday, but I don't remember which
- It was a weekend, but I don't remember which
- Don't remember

### Q3 — Age (required, integer)
**How old was your child on the onset date, in months?** (e.g., 18)

### Q4 — The two days before (required, long text)
**Tell us anything you remember about the two days before the onset date.**
Anything at all — where you were, what the child did, how they were feeling, who you saw. If you don't remember anything, write "nothing."

*(No example text. No prompts.)*

### Q5 — Your view (required, long text)
**What do you think caused the change, and why do you think so?** Tell us what you saw or learned that led you to that view. It's fine to say you have no idea, or that you think it was random — if so, say why.

*(Last on the form so it cannot influence Q4. Required — "no idea, because…" is an answer. The "why" often surfaces events outside the two-day window of Q4 — a shot four days earlier, an illness the week before — so Q5 is also coded for events and their timing.)*

---

## Blind coding scheme for Q4 and Q5

Two coders, neither sees Q1–Q3. Q4 is coded before Q5 is revealed to the coder. Codebook fixed before collection. Each narrative gets one value per column.

| Column | Values |
|---|---|
| `shot` | mentioned / not mentioned |
| `shot_day` | if mentioned: same day (0) / day before (1) / two days before (2) / unclear |
| `visit_no_shot` | doctor or clinic visit mentioned with no shot mentioned: yes / no |
| `illness` | fever, infection, or illness mentioned: yes / no |
| `medication` | any medicine mentioned (incl. acetaminophen, antibiotic): yes / no |
| `other_event` | birthday, travel, daycare start, move, new sibling, etc.: yes / no |
| `nothing` | "nothing" or no event content: yes / no |
| `pii_flag` | contains names, places, dates, or other identifiers: yes / no (drives redaction) |

Q5 coded separately, after Q4 coding is locked:

| Column | Values |
|---|---|
| `attrib` | vaccine / illness or infection / other specific cause / random or no idea / other |
| `attrib_reason` | temporal ("it happened right after…") / clinical (doctor, test, diagnosis) / family history / read or heard it / none given |
| `q5_event` | any dated event mentioned that is NOT in Q4: shot / visit / illness / medication / other / none |
| `q5_event_days_before` | if given: number of days before onset, or "unclear" |
| `attrib_pii_flag` | yes / no |

Cohen's κ reported per column; disagreements resolved by a third blind coder.

## What the five answers give you

- **Spontaneous shot-mention rate** in the two days before onset. Reference point: at 12–24 months, roughly 3 vaccinating visits in ~365 days, so a random 2-day window lands within 0–2 days after a shot about 2–3% of the time. A rate several times that is the signal.
- **Shot mention vs. visit-without-shot mention.** Same two-day window, same unaided prompt — the visit-anchoring control, from the parent's own words.
- **Day-of-week distribution** (Q2), overall and split by whether Q4 mentions a shot. Under no effect the named days are flat; under a 0–2 day lag they are weekday-heavy with a Sunday hole, and the no-shot narratives should look flat.
- **Age distribution** (Q3) of the onset peak, and shot-mention rate by age band (the 12–18-month band is where the schedule is densest, so the mention rate should be highest there under either account; the ratio to the 2–3% baseline is what matters).
- **Recency** (Q1) as a recall-quality stratifier: mention rate and day-of-week sharpness in ≤2 years vs >5 years.
- **Attribution split** (Q5): every statistic above reported for `attrib` = vaccine and `attrib` ≠ vaccine separately. `attrib_reason` separates parents whose belief rests on what they saw (temporal) from those whose belief came from elsewhere. `q5_event` recovers exposures outside the Q4 window, giving a partial lag histogram for shots mentioned only in Q5 (e.g., 4–14 days before). The non-attributing parents who nonetheless mention a shot in Q4, and their day-of-week distribution, are the decisive subgroup: a spike and Sunday hole among parents who do not blame vaccines cannot be explained by belief-driven recall.

## What it does not give you (by design)
No interval beyond two days, so no lag histogram, no 84–97-day mirror, no dose–response, no confidence rating, no shot count. Those are for the longer instruments. This one is built so there is nothing on the page to argue with.

## Publication
Q1–Q3 and all coded columns released row-level. Q4 and Q5 text released only after redaction per the PII flags; unredacted text retained privately.
