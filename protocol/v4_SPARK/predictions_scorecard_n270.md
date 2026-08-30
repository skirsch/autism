# Predictions Scorecard — n=270 export (2026-08-30)

Applying `prespecified_predictions.md` to SOA2 Grid view, 270 rows. All rows are from vaccine-aware channels (top sources: Autism Action Network 76, Facebook 48, direct invite 33, Substack 27, Lara Logan 21, Attkisson 16), so per decision rule 5 every result below carries the channel caveat. The new instrument questions went live mid-collection: visit checklist populated on 79 rows, schedule question on 61, diagnosis on 22, vaccine-type on 1.

| # | Result at n=270 | Verdict |
|---|-----------------|---------|
| P1 | Onset years 1978–2026; 2020=1, 2021=10 (dip + rebound present). NEVER arm has 2 dated rows. | Dip exists but both H-vax and H-artifact predict it in pooled data (2020 killed well-visits too). The discriminating VAX-vs-NEVER comparison is **untestable** (NEVER n≈2). |
| P2 | Weekday fraction 0.86 vs 0.714 uniform-null. Named days flat (χ² p=0.58, n=38; Sunday now 2, not 0). VAX arm 21:1 weekday; NEVER arm n=1. | Weekday shift confirmed — but predicted by **both** H-vax and H-artifact. Exposure split untestable. No discrimination. |
| P3 | Days 0–5 = 126 vs days 6–60 = 62; ratio 2.03 vs null's 0.11 (p ≈ 10⁻⁸⁰). Per-day: wk1 = 17.1 → 3.0 → 0.94 → 0.60 → 0.40 → 0.26. | **H-null is excluded** on timing. Both surviving hypotheses predicted this, so it doesn't separate them. |
| P4 (primary) | SHOT-visits: 29/50 with intervals in days 0–2, cliff ≈ 66× the day 6–60 per-day rate. NOSHOT-visits: **7 rows total, 4 with usable intervals, 0 early** (Fisher p=0.017). But 4 of the 7 NOSHOT rows name vaccines in their Cause text (#242 "multiple vaccines in one appt," #275, #291 "Varivax… 7 days after," #308 "MMR") — the control cell is both tiny and contaminated. | **No verdict, per the pre-registered rule** (requires ≥100 NOSHOT cases; we have 4 clean-ish). Direction (0 early at no-shot visits) points H-vax, but 4 discordant rows cannot carry it. |
| P5 | Same-day AFTER=19, BEFORE=1 — and the lone BEFORE row (#316) writes "Got vaccinated (0) → was never the same again," Cause "VACCINATION": a response error, not a genuine before-shot onset. Effectively 19:0, exceeding the 2–3:1 waking-hours null (p=0.02). NOSHOT-visit before/after cell: 0:0. | Exceeds null, but decision rule 4 already concedes deferral produces AFTER-excess under all hypotheses. The discriminating NOSHOT ratio is empty. No discrimination. |
| P6 | Vaccine-type question populated on 1 row. | **Untestable** — question added 2026-08-29. |
| P7 | Ages 12–23 mo = 154/268; modal ages 18, 15, 12, 24 — the vaccinating-visit ages. NEVER arm too small for the contrast. | Sharpening at visit ages confirmed — predicted by both H-vax and H-artifact. |
| P8 | Day 0–2 fraction: vaccine-attributing 84/187 (45%) vs non-attributing 9/31 (29%). Fisher p=0.12. | Point estimate orders in the **artifact** direction (concentration among attributors) but not significant. Note: the non-attributing 29% is itself ~6× flat-null — visit-anchoring without attribution, or a real effect, both explain that; pure believer-selection doesn't. Mixed. |
| P9 | Requires record follow-up. | Untestable from survey alone. |
| P10 | Days 4/5/6/7 = **2 / 14 / 1 / 10**. Heaping on 5 and 7, troughs at 4 and 6, exactly as pre-specified (and now at larger n than when first observed). | **Matches H-artifact's specific prediction.** No biological risk curve produces 2/14/1/10; at minimum it proves reported day-values are memory-reconstructed, not diary-accurate. |
| P11 | NEVER = 3/61 (4.9%) of rows answering the schedule question; exact CI ~1–14%. All three carry non-vaccine narratives (APGAR-0 birth injury; PEG-3350; viral infection 30–59 d before). | H-vax (as amended 2026-08-30: ≥80% of cases vaccine-caused) predicts NEVER ≈ 20% of the never-vax population share; H-null/H-artifact predict the full share. Untestable here: the never-vax share of the *invited* population is unknown, and vaccine-aware channels over-sample never-vaccinating families by an unknown factor. Consistent with the amended H-vax that all 3 narratives name non-vaccine triggers. Descriptive only. |
| P12 | 1 row with the type question; but the P4 cell already previews the problem: 4/7 checklist-no-vaccination rows mention vaccines in Cause. | Untestable formally; discordance is clearly nonzero. "None — I'm certain" on the type question becomes the control definition once it fills in. |

## Bottom line

H-null is dead on this sample's timing (P3, p ≈ 10⁻⁸⁰) — which no party disputed. Between the two live hypotheses, this dataset moves the needle only slightly:

- **For H-artifact:** P10 confirmed at larger n (the single most internally-probative result — the day-4/6 troughs cannot come from biology); P8 point estimate orders the artifact way (ns).
- **For H-vax:** P4's direction (0/4 early at no-shot visits vs 29/50 at shot visits, Fisher p=0.017) — but at 4% of the pre-registered sample size, in a contaminated cell.
- **Shared cells (no weight):** P1 dip, P2 weekday shift, P3 clustering, P5 after-excess, P7 visit-age peaks.

The committed verdict machinery cannot fire yet because every discriminating cell is empty or nearly so: the diagnosis, vaccine-type, and schedule questions cover only the newest ~60–80 rows, the NOSHOT control has 4 usable rows against a required 100, and the NEVER arm has 3. At the observed rate (~9% of checklist rows are no-shot visits) reaching NOSHOT ≥ 100 needs roughly 1,100 more checklist-era responses in these channels — or a neutral channel where no-shot last visits aren't rare, which is the same conclusion the channel-gradient design already reached.

*Scored 2026-08-30 against prespecified_predictions.md; no predictions were added or reinterpreted after seeing this data.*
