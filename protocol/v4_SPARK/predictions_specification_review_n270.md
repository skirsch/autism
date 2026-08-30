# Specification review after the n=270 export

**Review date:** 2026-08-30  
**Data snapshot:** `C:\Users\stk\Downloads\SOA2-Grid view.csv` (270 rows; SHA-256 `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`)  
**Prediction document reviewed:** `prespecified_predictions.md` (SOA Survey v2.3)

## Bottom line

The present prediction table is useful as a list of patterns to examine, but it is too strict to serve as a valid three-way causal decision rule. In particular:

1. **H-vax already says “in some children.”** It does not predict that all sudden-onset cases follow vaccination, and the existence of non-vaccine cases does not refute a vaccine-associated subgroup.
2. **The three columns are not mutually exclusive.** Visit anchoring, recruitment selection, vaccine-associated events, infections, and other acute events can coexist in one sample. A mixture can produce a result that no single column predicts.
3. **Rejecting the stated H-null is not evidence that vaccination caused the clustering.** That null assumes random timing and perfect recall. Failure can reflect visit-age structure, interval rounding, recall, selection, other acute triggers, or vaccination.
4. **The primary control is not yet measured.** The authoritative “None — certain” vaccine-type field has only one populated response in this export. Absence of `Vaccination(s)` from the earlier visit checklist is not evidence that no vaccination occurred.
5. **The current sample is outcome-selected and largely vaccine-aware.** It can describe the submitted sudden-onset cases, but it cannot estimate population causal fractions or the population share of vaccine-, infection-, or other-triggered cases.

The original file should remain frozen. Any changes below should be labeled a **post-n=270 amendment** and applied prospectively to later responses or a held-out neutral-channel sample.

## What the n=270 export can and cannot say

The form changed during collection. The last-visit checklist is populated for 79 rows, vaccine schedule for 61, autism diagnosis for 22, and authoritative vaccine type for only 1. Consequently, most discriminating predictions do not yet have the required fields.

| Prediction | Current observation | Specification assessment |
|---|---|---|
| P1 onset year | Exact onset date is present for 170 rows, but only 3 rows answer NEVER and only about 2 of those have usable dates. | VAX-versus-NEVER pandemic comparison is not testable. Calendar-era recruitment and recall also require adjustment. |
| P2 day of week | Only 38 give a named day; 162 say “Don't remember” and 69 give only weekday/weekend. Among the 61 schedule-era rows, only 6 VAX and 1 NEVER respondents give a named day. | The exposure contrast is not testable. The named-day subset is strongly selected by recall ability. |
| P3 early lag | Reported categories contain 19 same-day-after, 51 next-day, 26 day-2, 13 day-3, 2 day-4, and 14 day-5 responses. | This is strong reported early clustering, but it rejects only the flat/perfect-recall model. It does not distinguish vaccine effects, infection/other triggers, anchoring, and selection. The stated 6–60 reference is also not exactly recoverable because the form combines day 60 with days 61–89. Use days 6–59 prospectively or change the form. |
| P4 SHOT versus NOSHOT | Checklist-era rows include 62 that mention vaccination and 17 that do not, but checklist omission is not “certain no vaccine.” The authoritative vaccine-type field has n=1. | The primary analysis is not merely underpowered; its valid NOSHOT exposure cell has not yet accumulated. Do not calculate a causal SHOT/NOSHOT cliff from checklist omission. |
| P5 before versus after | The export contains 19 exact same-day-after labels. A near-matching same-day-before label also appears because Airtable labels changed. | Harmonize labels before counting. Deferral and time-of-day structure prevent a simple 2–3× causal baseline. The SHOT/NOSHOT comparison is unavailable. |
| P6 MMR timing | Vaccine type has n=1. The form's 8–13-day bin also cannot isolate the prespecified day 5–12 window. | Not testable. Align response bins to the biological window before using this as a confirmatory test. |
| P7 onset age | Modal reported ages are 18, 15, 12, and 24 months. | Compatible with scheduled-visit ages, developmental recognition ages, digit heaping, or more than one mechanism. Without an appropriate denominator/control, it does not identify cause. |
| P8 attribution | Cause is open text; no frozen, blinded attribution codebook is specified. | Define coding rules, multiple-rater adjudication, and treatment of ambiguous narratives before further scoring. Attribution can affect recall without fully explaining an underlying event. |
| P9 verification | The survey asks whether documentation might be available, not what the verified interval is. | Requires a separate validation protocol and verified fields. It is not testable from this export. |
| P10 digit pattern | Exact labels show day 4/5/6/7 counts of 2/14/1/10. | This supports heaping or reconstruction in reported intervals. It does **not** prove that all early clustering is artifact, nor can one assert that no biological process could contribute without an external model. Also, the document says this pattern was “already observed at n=230,” so it is not genuinely prespecified for the same accumulating dataset. Treat replication only in a held-out tranche. |
| P11 NEVER fraction | NEVER is 3/61 among rows receiving the schedule question. | The denominator needed by the prediction—the never-vaccinated share of the invited/respondent source population—is unknown. This survey alone cannot estimate a population etiologic fraction. |
| P12 discordance | Authoritative vaccine type has n=1. | Not testable yet. Freeze the precedence rule and report missingness before evaluating discordance. |

## Recommended post-n=270 hypothesis structure

Replace the mutually exclusive three-column contest with mechanisms that may coexist:

- **M0: no measured acute trigger / background onset and recognition.** This is not required to have a uniform lag or perfect recall.
- **MV: vaccine-associated subgroup.** Its estimand is the excess early-onset rate after a vaccination visit relative to comparable no-vaccine visits, not the fraction of all sudden-onset cases.
- **MI: infection-associated or other non-vaccine biological subgroup.** This covers a prespecified set of objectively defined acute exposures. The suggested “around 10%” should be recorded as a working prediction, not a fact established by this dataset.
- **MA: reporting, visit anchoring, digit heaping, and recruitment selection.** These processes may modify any of the above groups rather than acting as a mutually exclusive cause.

The main causal quantity should be an **incremental contrast**: how much larger is the early-lag signal after SHOT visits than after comparable NOSHOT visits, with source channel, onset era, age, recall confidence, and documentation status specified in advance. A nonzero NOSHOT cliff does not by itself make the SHOT excess artifactual; conversely, a SHOT cliff does not establish causation if exposure classification and selection remain differential.

## Prospective amendments needed

1. Define SHOT and NOSHOT only from the authoritative vaccine-type question; keep unknown and discordant records separate.
2. Use a reference window the form can identify exactly (days 6–59), or change the bins to isolate day 60 and the MMR day 5–12 window.
3. Add structured, time-resolved fields for prespecified non-vaccine acute exposures if infection-associated hypotheses are to be tested. Define whether evidence must be laboratory-confirmed, clinician-diagnosed, contemporaneously documented, or parent-reported.
4. State the infection/other-trigger prediction as a range and denominator, for example: “Among eligible sudden-onset cases, X–Y% meet the prespecified documented-infection definition within window W.” Do not pool fever, nonspecific illness, strep, and *C. difficile* without a frozen rule.
5. Freeze a blinded codebook for open-text Cause and sequence responses before coding the next tranche.
6. Split discovery from confirmation. Treat rows through n=270 as exploratory; test amended predictions on later rows and report recruitment channel separately.
7. Replace “H-null is excluded” with the narrower statement “the flat reported-lag model is incompatible with this selected sample,” followed by the alternative explanations that remain.
8. Do not turn the ≥100 NOSHOT threshold into a binary truth switch. Report the effect estimate and uncertainty continuously, while retaining a minimum-information rule for strong conclusions.

## Interpretation at this checkpoint

The export shows substantial reported clustering in the first few days after the last pediatrician visit and conspicuous heaping on days 5 and 7. Those observations make recall/rounding important and justify the SHOT-versus-NOSHOT design. They do not yet decide whether an incremental vaccine-associated component exists, because the valid NOSHOT and vaccine-type fields are essentially empty. Non-vaccine sudden-onset cases are compatible with the stated “some children” vaccine hypothesis and should be modeled explicitly rather than used as automatic evidence against it.
