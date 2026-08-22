# SORA Study — Revised Design (v3 working draft)

## What changed from v2

| | v2 | v3 |
|---|---|---|
| Recruitment | Clinic emails entire patient roster | Consecutive capture at diagnostic intake |
| Consent | Individual consent, full survey | IRB waiver of consent + HIPAA waiver of authorization |
| Denominator | None (responder-only) | Consecutive series; all onset patterns captured |
| Vaccination dates | Parent recall; 20–30% record-verified subset | Documented immunization records as primary |
| Onset dating | Parent recall only | Parent recall + evidence tiering + chart-abstracted prior account |
| Recall gap | ~8+ years (treatment rosters) | ~2–3 years (at diagnosis) |
| External check | Mixed-view study team | Blinded analyst + independent data custody |

The central move: **consent bias was the largest remaining threat, and a waiver removes it by construction.** Parents who attribute regression to vaccination are far more likely to consent to a CHD-funded study than parents who don't; consenting-sample enrichment for attributors would bias the primary endpoint in the exact direction of the hypothesis. Consecutive capture under waiver eliminates that mechanism entirely.

---

## Three arms

### Arm A — Intake capture (primary)

Structured developmental-history module added to diagnostic clinic intake. Every family presenting for ASD evaluation completes it. No vaccine content in the module. Immunization records obtained through the clinic's **existing** pediatric records release (already standard in ASD workup — marginal ask is adding immunization history to a request the clinic already makes).

- Consecutive → real denominator, SORA proportion becomes estimable
- Short recall gap (median age at ASD diagnosis ~4–5 years)
- Documented exposure dates, not recalled
- Clinic computes day intervals; only relative timing transmitted

### Arm B — Record abstraction / SCCS (anchor)

Retrospective chart abstraction under waiver. No parent involvement at all.

- Onset from ADI-R items #11 (loss of ≥5 words) and #20 (loss of other skills) — coded at evaluation by a clinician with no stake in the question
- Documented immunization dates
- Month-level resolution → 30-day SCCS, not Day 0–2
- **Zero recall bias, zero consent bias, zero selection on causal belief**

This arm is the anchor. If A and B agree, the parent-recall objection is largely answered. If A shows sharp Day 0–2 clustering and B is flat at 30 days, the most parsimonious reading is recall anchoring — and that interpretation must be committed to in advance.

### Arm C — Recent-parent survey (pilot + calibration)

Survey to families diagnosed within the last 18 months. Self-selected; explicitly labeled as such.

**Primary purpose is not sample — it is parameter estimation:**
- What fraction of parents can supply a day-level onset date? *(This determines whether the Day 0–2 framework is buildable at all. Currently unknown. Every downstream decision depends on it.)*
- Realistic response rate (v2's 50% assumption is not survivable; 5–15% is typical)
- Worst-case selection calibration against Arms A and B

Cost: ~$8–10k, ~2 months. **Run before committing the full budget.**

---

## The intake module

Design constraints:
- Clinically justified on its own merits (DSM-5 has an onset criterion; "around 18 months" is poor documentation)
- Applies to **all** patients, not a research-eligible subset
- Data appears in and is used from the clinical record
- **No vaccine questions anywhere in this module** — both to avoid priming attribution and because a vaccine item is an instant clinic refusal
- Under 3 minutes of staff/parent time

### Question sequence

**1. Developmental pattern** *(single select)*
- Never met milestones
- Met milestones, then rapid change
- Met milestones, then slow decline
- Met milestones, then plateaued
- Unsure

**2. What changed** *(multi-select; only if pattern 2–4)*
- Lost words or language
- Lost eye contact or social responsiveness
- Lost motor or self-care skills
- New repetitive or self-injurious behaviors
- New sensory sensitivities (light, sound, touch, food, pain)

**3. How quickly** *(single select)*
- Within a few days
- 1–2 weeks
- 2–4 weeks
- 1–3 months
- Gradual / can't separate

**4. Age when the change began** — years / months

### The objective-evidence block

This is the heart of the redesign. **Ask what anchors the date before asking for the date.** A parent who has told this story many times will produce a confident date on demand; asking for the evidence first separates dating that rests on something external from dating that rests on narrative.

**5. How do you know when the change began?** *(multi-select)*

*Tier 1 — documentary*
- Dated photos or videos showing my child before and after
- A medical or therapy record noting the change
- Early intervention referral or evaluation date
- Daycare, preschool, or caregiver report
- A dated message, email, or post where I described the change at the time

*Tier 2 — anchored to a fixed dated event*
- It was around a holiday, birthday, trip, move, or other event I can date

*Tier 3 — recalled interval*
- I remember roughly how long after something else it happened

*Tier 4*
- I remember the month or season only

*Tier 5*
- I couldn't put a date on it

**6. Photos or video** *(yes / no / unsure)*
Do you have dated photos or video of your child from the weeks before and the weeks after the change?

> Phone media carries exact timestamps and is the single most objective onset evidence available to a parent. Blind-coded home video is the gold standard in this literature (cf. Goldberg's own video work). Worth building a substudy around: parents supply timestamped media, coders rate developmental status blind to hypothesis and to date.

**7. Best date estimate** — date, plus the narrowest range the parent would stand behind

**8. Maximum error** — "What's the most days you think you could be off?"

**9. In your own words** — free text: what happened, before and after

Vaccination timing, schedule status, and causal-belief questions live in a **separate, later module** — after the clinical intake is complete, and after any consented research follow-up begins.

### Evidence tiering in analysis

Primary analysis restricted to a prespecified high-evidence tier (locked before unblinding). Tier is a **prespecified stratum**, not a post-hoc filter. Report the Day 0–2 statistic across ordered evidence tiers: if concentration *increases* as evidence quality improves, that argues against anchoring; if it *decreases*, that argues for it. Either way it is informative, which is why the tiering has to be locked in advance.

---

## Recall-drift substudy

For children whose parents complete a survey, abstract the **original** onset account recorded at their first evaluation — documented years earlier by a clinician with no stake in the question.

Compare then vs. now. If current recall systematically differs from the contemporaneous account — and especially if it drifts *toward* vaccination dates — recall anchoring has been measured rather than argued about.

Nobody has done this. It is cheap, requires no intake modification, and is publishable independently.

---

## Governance

Since a co-PI is not available, substitute checks that require no one to stake a career:

- **Blinded analyst** — paid statistician runs the locked plan on relabeled data, not told which variable is the exposure. Acknowledged as "independent analysis"; no public defense required.
- **Methods reviewer under NDA** — reads protocol pre-submission; does not endorse conclusions.
- **Independent data custody** — CRO holds the raw file and can attest nothing was dropped. Vendor relationship, not reputational commitment.

If a paid, blinded, non-attributed analyst role gets no takers, that is itself information — at that point no one is risking anything.

**Sponsor structure:** independent research institute or CRO as sponsor of record; independent IRB (WCG or Advarra); CHD disclosed as one funder among several if possible. This addresses clinic reluctance and IRB scrutiny with the same move.

---

## Blinding during the pilot

**Critical failure mode:** running 40 cases, looking at the lag distribution, then locking the analysis plan. That voids the pre-registration entirely, and it happens by accident — usually as "just checking whether it's working."

During pilot, inspect **process metrics only**. Someone outside the analysis team holds the intervals sealed. Lock the SAP, then unblind — which preserves the pilot cases for the primary analysis instead of discarding them.

**Safe to inspect (properties of the instrument, not the outcome):**

| Metric | Threshold |
|---|---|
| Intake completion | >85% |
| Added staff time | <3 min |
| Day-level onset dates supplied | >30% |
| Records requests fulfilled ≤60 days | >60% |
| Follow-up consent rate | track |

If day-level fraction comes back at ~8%, the Day 0–2 framework is unbuildable — redesign around 30-day windows. **That is what the pilot is for.**

---

## Power

n does not appear to be the constraint. Rough null: three vaccine visits (12/15/18 months) × 3-day windows ≈ 9 of ~180 days ≈ 5% baseline. At n=100, 30% observed vs 5% expected gives >99% power; even 15% vs 5% is adequately powered.

**Implication:** effort spent on sample size is misallocated. The attack surface is provenance — one site, selected parents, recalled dates — and 100 cases from a single sympathetic clinic makes that objection *easier*, not harder. Three sites of deliberately different types matters more than three times the n.

Accrual: ~300 diagnoses/year/clinic × ~25–30% regression × ~50% day-level dating ≈ 40 usable cases/clinic/year. One clinic → 2.5 years to 100. Three clinics → ~10 months.

---

## Sequence

1. **Pre-submission consult** with independent IRB on the waiver — determines whether the design is buildable. Cheap, one call. *Do this first, before any clinic conversation.*
2. **Arm C pilot** — recall parameter + response rate
3. **Lock SAP**, timestamped, pilot outcome data sealed until locked
4. **Engage blinded analyst** and data custodian
5. **Arm A pilot at one clinic** — workflow, with process metrics only
6. **Clinic 2 = conventional practice** — the real portability and bias test
7. Scale to 3+ sites, stratified by clinic type

File the IRB for the full multisite protocol now; add sites by amendment. Amending is far faster than refiling.

---

## Open items

- **Expert determination for de-identification.** Dates finer than year are among the 18 Safe Harbor identifiers, so Safe Harbor is unavailable. Requires a certifying statistician and a clinic-side workflow that converts calendar dates to relative intervals *before* transmission. Budget line.
- **Waiver scope.** Waivers for prospective collection are a higher bar than for existing records. A hybrid outcome is likely and acceptable: waiver for record components (immunization dates, ADI-R onset codes), consent for the narrative follow-up. Primary endpoint then runs on waived, unbiased data; consented layer is labeled secondary and self-selected.
- **Debriefing condition.** IRBs sometimes attach one to waivers. Need an answer for what a parent is told if they later ask.
- **Clinic budget.** $2,000/clinic understates staff time, IRB liaison, and workflow disruption.
- **Named vs. anonymous sites** in publication — decide before a clinic asks.

---

## What this still does not fix

The waiver eliminates **consent** bias. It does not touch:

- **Recall.** Parents at intake still date onset from memory. Anchoring operates on consecutively-sampled parents exactly as it does on self-selected ones. Largest remaining exposure; addressed only partially by evidence tiering, the recall-drift substudy, and Arm B.
- **Clinic selection.** Sympathetic sites draw parents selected on the belief under test. Only fixed by including conventional practices.
- **Case selection.** Sampling children who reached diagnosis; families who never sought evaluation are absent.

Three distinct mechanisms. Worth tracking separately so it stays clear which objections have actually been pre-empted.

---

## Cut from v2

**"Why this study is hard to dismiss."** Public data and pre-registration answer procedural objections. The objections that will actually be raised are structural — funding, selection, recall anchoring. A section listing only the solved ones signals the others weren't engaged.

---

## The decision worth making now

Write down, before any data exists, what happens if the result is null.

Given how thin the current evidence for a day-scale effect is, no concentration beyond schedule structure is a plausible single outcome. Publishing that prominently would be a real contribution — and it is what would make a positive finding credible, from this team, later.

Decide it while it is abstract.
