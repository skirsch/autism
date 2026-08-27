# Airtable SOA form — v2 changes (drop-in wording)

### 0. Onset definition  *(edit the intro; replace the "Why do some children…" bullet list)*

> The **onset date** is the first day you noticed a clear, unmistakable change in your child — a skill that was lost (words, eye contact, pointing, play) or a new behavior that appeared (screaming, repetitive movements, withdrawal, new sensitivities) — **that did not go away**. Use the day the change first appeared, not the day you first worried something might be wrong, and not the day of diagnosis. If the change unfolded over several days, use the first day. A bad night that was back to normal within a few days does not count.

Why: "sudden" must not depend on the parent having a dated event to hang the memory on, and ordinary post-shot reactions that resolve (the 1–6-month-old cases in the current data) must not count as onset.

Replace the single question **"Was your child vaccinated within 120 days PRIOR to onset?"** with the two-plus-one items below. Keep "Confidence in vaccination interval" but attach it to the visit interval. Everything else on the form is unchanged except item 4 (and item 5 if you choose to include it).

---

### 1. Most recent doctor visit before onset  *(required, single select)*

**Label:** How many days BEFORE onset was your child's most recent doctor visit (well-child or sick visit)?

**Help text:** Choose the closest answer, even if you are unsure of the exact interval.

Options (same as the current vaccination list, with the last two bins split):

- Don't remember
- No doctor visit within 120 days before onset
- Less than 1 day (onset happened < 24 hrs after the visit)
- 2 days (onset was 24–48 hours after the visit)
- 3 days (onset was 49 to 72 hours after the visit)
- 4 days after the visit
- 5 days after the visit
- 6 days after the visit
- 7 days after the visit
- 8 to 13
- 14 to 29
- 30 to 59
- 60 to 83
- 84 to 97
- 98 to 120

### 2. Confidence in that interval  *(required, single select — existing item, relabeled)*

**Label:** How certain are you in your previous answer?
Options unchanged: Absolutely certain / Within 1 day / Within 2 days / Within 3 days / Within 4 days to a week / Could be off by a week or more

### 3. Shots at that visit  *(required, single select)*

**Label:** How many vaccine injections were given at that visit?

**Help text:** Count injections, not diseases covered (an MMR is one injection). Nasal flu counts as one.

- 0 — no shots at that visit
- 1
- 2
- 3
- 4
- 5 or more
- Don't remember

### 3a. Earlier visit with shots  *(conditional: show only if item 3 = "0")*

**Label:** Was there an earlier visit WITH shots within 120 days before onset? If so, how many days before onset?

- Don't remember
- No visit with shots within 120 days before onset
- Less than 1 day … 98 to 120  *(same 13 interval bins as item 1)*

> Airtable forms support "show field only if" conditions on single-select fields; set item 3a's condition to *Shots at that visit = 0*.

---

### 4. Sequence-of-events example  *(edit help text)*

Current example is *birthday party (0) → illness (1) → fever (2) → tylenol (2) → high-pitched screaming (2) → lost eye contact (4)*, which is the vaccine-injury narrative template with the word removed and tells respondents what shape a "good" answer has. Replace with two short examples of different shape, or none:

> For example: *moved house (0) → started daycare (3) → stopped responding to name (10)*, or *ear infection (0) → antibiotic (1) → lost words (5)*.

### 5. Hypothesis exposure  *(OPTIONAL — recommended to omit: it is the only item that would explicitly pair "vaccines" and "autism" on the form. The Cause? free text already supplies the attribution split; the visit/shots items carry the structural controls.)*

**Label:** When did you first hear the idea that vaccines might be connected to autism?

- Before my child was born
- Before I noticed the change
- Around the time I noticed it
- After the diagnosis
- Never heard it
- Not sure

This is the cleanest measure of whether the belief predates the observation, and it is the subgroup that matters most for the attribution analysis.

---

## What the new items give you that the old one didn't

| Quantity | Old form | New form |
|---|---|---|
| Vaccination-to-onset interval | yes | yes (item 1 if shots ≥ 1, else item 3a) |
| No-shot-visit-to-onset interval (the visit-anchoring control) | no | yes (item 1 where item 3 = 0) |
| Dose–response: Day 0–2 fraction by number of injections | no | yes |
| ~90-day mirror hump | hidden in "60 to 90" | visible (84–97 bin) |
| Questions per respondent | 2 | 3 (4 only if the nearest visit had no shots) |

## Column mapping for pooling with the SPARK export

| Airtable field | SPARK field |
|---|---|
| Most recent doctor visit before onset | `visit_interval` |
| Confidence in that interval | `visit_confidence` |
| Shots at that visit | `visit_shots` |
| Earlier visit with shots | `vax_prior_interval` |
| When did you first hear… | `hypothesis_exposure` |

Rows collected under the old form keep their `# days ago vaccinated` value; the analysis script treats it as `vax_interval` with `visit_shots` unknown, so they contribute to the lag histogram but not to the dose–response or control rows.
