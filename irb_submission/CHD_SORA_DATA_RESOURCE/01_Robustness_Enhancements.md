# SORA Study — Robustness Enhancements Summary

**Purpose:** Consolidated list of the design additions discussed to make the SORA
result more reliable and harder to dismiss. Organized by the bias each addition
targets, with what it fixes and the residual it does *not* fix, so the packet can
pre-empt reviewers rather than react to them.

**Organizing principle — two independent axes.** Every control lands in one of two
columns and does little for the other. Keep them separate:

- **Selection** — *who ends up in the sample.* Fixed by response rate, varied-sponsor
  replication, population-based recruitment, and characterizing non-responders.
  *Not* fixed by validation.
- **Measurement / recall** — *is the onset date actually correct.* Fixed by records,
  date-stamped media, and blinded adjudication. *Not* fixed by replication.

---

## A. Selection-bias controls (who ends up in the sample)

**A1. Whole-population, clinic-branded neutral invitation.**
Invitation goes to the clinic's complete contactable parent population, not a
diagnosis- or vaccine-selected subset; sent under clinic branding.
*Controls:* recipient-side selection at the invitation stage.
*Residual:* who *responds* among those invited is still self-selected (see A4).

**A2. Opt-out reason capture.**
Parents who decline are asked to write, in open text, why.
*Controls:* converts silent decliners into partially characterized ones; feeds a
sensitivity narrative.
*Residual:* reasons tell you *why* they declined, not their child's onset timing;
most decliners write nothing, so reason-givers are themselves a selected slice.

**A3. Non-responder characterization + two-phase nonresponse double-sample. (NEW — strongest selection control)**

*A3a — reason callback (weak form).* Clinic places structured calls to a sample of
non-responders and records **why** they didn't respond and **where in the funnel**
they dropped (never-opened vs. opened-then-declined). Never-openers had no exposure
to the survey's content, so their non-response is plausibly *non-differential* with
respect to vaccine/onset timing. *Limit:* this captures reasons, not the outcome —
it supports a non-differential argument but cannot prove it.

*A3b — nonresponse double-sample (strong form; Hansen–Hurwitz two-phase sampling).*
This is the control that actually measures the selection differential instead of
arguing about it.

- **Phase 1** is the main survey at whatever response rate it achieves (low is OK).
- **Phase 2:** draw a **random probability subsample** of the non-responders (a few
  hundred), documented and non-convenience.
- **Convert that subsample with intensive effort** — mode switch (phone/in-person),
  a shortened instrument limited to the outcome-critical items (onset timing
  relative to any shot, developmental pattern, SORA screen), incentive, repeated
  contact — targeting **high conversion (≥~70%) within the subsample.**
- Because the subsample is a random draw of non-responders that is nearly completed,
  it is an approximately unbiased snapshot of the outcome **among non-responders** —
  the exact quantity the main survey cannot observe.

*Controls:* directly estimates and removes selection bias. Compare the
"within-window" fraction among responders vs. the non-responder subsample: matching
fractions are positive evidence the differential is small and the headline cluster
is credible; a much lower subsample fraction quantifies the artifact. Combine into
an unbiased whole-population estimate via the Hansen–Hurwitz two-phase estimator
(responders + subsample reweighted by the subsampling fraction). Converts "you
can't know your non-responders" from an unanswerable objection into a measured
number.

*Residual / requirements (state in the packet, do not oversell):*
- Phase-2 conversion must genuinely be high; if the intensive follow-up also lands
  low, the bias recurses (non-response on the non-responders). High conversion is
  the load-bearing assumption — budget and design for it.
- Requires a random, documented probability subsample and enough n for usable
  precision on the non-responder fraction.
- Fixes **selection only** — recall still needs the validation core (B4–B6).
- Corrects selection *within the clinic panel*, not which clinics/patients are in
  the panel (that coarser frame → population-based replication, D1).
- Rides on the recontact capability accepted in B2; clinic holds contacts, CHD
  receives only de-identified results (consistent with the no-list architecture).

**A4. Response-rate maximization.**
Clinic actively encourages participation on a vaccine-orthogonal rationale
("categorize regression types in the practice"); reminders on the fixed schedule.
*Controls:* raises response rate — the single lever that makes selection
sensitivity bounds *informative* rather than vacuous (see C2).
*Residual:* encouragement lifts the whole response curve but rarely equalizes it
across belief subgroups; the regression-typing framing can enrich for the
regressive phenotype.

**A5. Varied-arm independent replication (see D1).**
A neutral-sponsor and/or population-based recruitment arm tests whether the sponsor
identity or the volunteer frame is driving the sample.

---

## B. Measurement / recall controls (is the onset date correct)

**B1. Up-front event narrative + anchor probe.**
Before any structured questions, the parent describes the sequence of events leading
to diagnosis, names a specific onset date, and states **how they anchored** that
date.
*Controls:* reduces priming from later structured items; the anchor variable
("I remember because it was right after his shots") lets you stratify out anchored
memories.
*Residual:* the CHD/vaccine frame may itself install the vaccine as the anchor; you
observe how the memory is narrated *now*, not how it was originally encoded.

**B2. Email collection → recontact/validation.**
Survey collects email so responses can be validated against records.
*Controls:* enables the record-validation substudy inline.
*Residual (regulatory):* identifiable data about a minor — likely exits the
anonymous exempt [45 CFR 46.104(d)(2)] framing into expedited/full review with
HIPAA authorization and a breach surface. **Design the packet for this pathway from
the start.**

**B3. Vaccine-date validation against records.**
Reported vaccine dates checked against immunization registry / card / portal.
*Controls:* the record-verifiable endpoint of the Dpre/Dpost interval.
*Residual:* records rarely contain a day-level *onset* date — the reconstructed
endpoint — so this validates the easy half of the interval (see B4).

**B4. Blinded professional adjudication of onset (+ unblinded comparison).**
Trained adjudicators read the narrative and evidence and assign an onset date,
**blinded** to vaccine timing (with an explicit redaction protocol for exposure
cues). Run **both** blinded and unblinded.
*Controls:* attacks onset-recall bias — the endpoint records can't fix. The
blinded read is the *primary* estimate; the blinded-vs-unblinded difference
*measures* adjudicator anchoring directly.
*Residual:* redaction leaks through context; for evidence-poor cases the adjudicator
grades memory quality, not truth.

**B5. Evidence-tier variable.**
Every case tagged by strength of onset evidence:
date-stamped media > contemporaneous clinical note > detailed dated memory > vague
memory.
*Controls:* lets analysis weight or restrict by evidence quality instead of treating
all onset dates as equal.

**B6. Validated-core primary analysis.**
Primary/confirmatory analysis restricted to fully-validated cases (records confirm
vaccine date + date-stamped media brackets onset + blinded adjudication).
*Controls:* creates a recall-bias-immune core; "everyone else's recall is wrong"
stops applying to this subset.
*Residual:* the validated core is a **selected** subset (media/consent availability
correlates with engagement and salience) — internally valid on timing, not
generalizable to a rate; still needs a base-rate comparison to become causal (C1).

---

## C. Internal analytic checks

**C1. Dpre/Dpost self-control.**
Compare the distribution of the interval to the nearest vaccine looking *backward*
(Dpre) vs *forward* (Dpost) within the same children.
*Controls:* supplies an internal base-rate / within-person counterfactual — the step
that turns "verified proximity" into "more than expected."
*Residual:* recall bias can produce a tight-Dpre/diffuse-Dpost asymmetry too; most
powerful when applied inside the validated core (B6).

**C2. Sensitivity analyses.**
- Worst-case dropout bound (all mid-survey dropouts → null bucket).
- Non-responder tipping-point / Manski bound — **informative only at high response
  rate**; at single-digit response the worst case always contains "no effect," so
  the bound is vacuous. Report the response rate at which it bites.
- Non-differential-nonresponse argument supported by A3a callback reasons.
- **Hansen–Hurwitz two-phase estimator (A3b):** primary selection correction —
  reweight responders + the intensively-converted random non-responder subsample
  into an unbiased whole-population estimate; report responder vs. non-responder
  cluster fractions side by side.
- Validated-subset-only analysis (B6) as the recall-robust sensitivity arm.

**C3. Prespecified interval-censored timing methods.**
Exact and ranged intervals kept distinct; a prespecified nonparametric
interval-censored estimator; **no midpoint imputation**; code and synthetic cases
frozen before outcome access. *(Already in protocol Sections 12–13.)*

---

## D. External validity / replication

**D1. Independent university replication (e.g., a Hopkins-type sponsor).**
Freeze the **core instrument** for comparability; **add a deliberately-varied
bias-probe arm** (neutral/pro-safety-perceived sponsor, or population-based rather
than clinic-volunteer recruitment).
*Controls:* a faithful clone rules out operator/CHD-specific artifacts; the varied
arm tests whether the signal survives a different selection mechanism.
*Residual:* a faithful clone alone reproduces any bias inherent to the shared
design — reproducibility is not validity. The varied arm is what earns the credit.

---

## E. Positioning (what makes it un-ignorable)

**E1. Frame the survey as the front end for a record-based, within-person study.**
The convergence of every addition above (records, emails, validation, comparison
arms, replication) points to a self-controlled case series or case-crossover on real
immunization + developmental records — a design at the *top* of the evidence
hierarchy, where volunteer-selection and reconstructed-onset are structurally
absent. The survey recruits and defines the phenotype; the record study is what a
critic cannot wave off as recall or selection bias.

---

## Residuals no addition on this list removes

1. **Selection among validated cases.** Even a perfect validated core is a
   self-selected subset; it supports "timing is real in these cases," not a
   population rate.
2. **Association ≠ causation without a base rate.** Verified temporal proximity
   still requires the within-person expected-rate comparison (C1) to exceed chance;
   proximity alone, however well-dated, is not a causal effect.

These two are the structural ceiling of a survey design and the reason E1 exists.
