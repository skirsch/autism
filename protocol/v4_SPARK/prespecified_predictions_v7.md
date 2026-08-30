# Mutually Exclusive Prespecified Predictions — Verified SOA Survey Data (version 7 draft)

**Drafted:** 2026-08-30, after inspection of the first 270 raw responses.  
**Status:** Superseded by v8. V7 incorrectly reintroduced VAX-versus-NEVER comparisons into P1–P6 despite the inadequate NEVER sample.  
**Primary data:** Respondent-verified survey responses; document-verified records are the higher-evidence replication.  
**Outcome:** The survey-defined PARENT-observed sudden and lasting autism-consistent change.

## 1. Hypotheses

- **H-null:** vaccination does not produce a material short-window increase in the defined sudden-onset phenotype.
- **H-vax:** vaccination triggers the defined sudden-onset phenotype in a subgroup, producing material vaccination-linked timing, calendar, or age-pattern differences.

H-vax does not assert that every sudden-onset case is vaccine-caused.

## 2. Mandatory paired scoring rule

Each P1–P7 row is one hypothesis-discrimination test, not two unrelated evidence assessments. Exactly three paired outcomes are allowed:

| Result region | H-null | H-vax |
|---|:---:|:---:|
| Prespecified null region | **Yes** | **No** |
| Prespecified vaccine region | **No** | **Yes** |
| Uncertainty region, inadequate data, or unpredicted direction | **Indeterminate** | **Indeterminate** |

Yes/Yes is prohibited because the prediction regions overlap. No/No is prohibited because the observed result was left outside the scoring system. Mixed determinate/indeterminate pairs are also prohibited because a row is scored as one paired discrimination result: if the statistic does not enter either hypothesis's prespecified region, the row is Indeterminate/Indeterminate.

## 3. Exposure groups

- **VAX:** verified receipt of one or more vaccines before onset.
- **NEVER:** verified “No vaccines were ever given.”
- **SHOT-VISIT:** verified `What happened?` includes `Vaccination(s)` at the last regular wellness visit before onset.
- **E:** onset same-day AFTER through day 5 after SHOT-VISIT.
- **R:** onset days 6–59 after SHOT-VISIT.

Unknown or missing exposure is never converted to NEVER or no-shot.

## 4. Authoritative paired P1–P7 table

The null and vaccine regions are separated. Anything between them, inadequately measured, or in an unpredicted direction is Indeterminate/Indeterminate.

| Test | Yes / No: H-null region | No / Yes: H-vax region | Indeterminate / Indeterminate |
|---|---|---|---|
| **P1. VAX-specific 2020 dip** | 95% CI for $C_1$ lies within ±0.10. | Upper CI for $C_1$<−0.10, showing a material VAX-specific deficit. | NEVER inadequate; CI crosses a boundary; shared dip; or opposite direction. |
| **P2. Weekday/weekend difference** | 95% CI for $C_2$ lies within ±0.10. | Lower CI for $C_2$>0.10 in the frozen vaccination-calendar direction. | NEVER inadequate; CI crosses a boundary; shared departure; or opposite direction. |
| **P3. Named-day distribution difference** | Upper CI for total-variation distance $C_3$≤0.15. | Lower CI for $C_3$>0.15 and VAX fits the frozen vaccine-calendar model better. | Named-day data inadequate; calendar model unfrozen; CI crosses margin; or difference is unpredicted. |
| **P4. Modal onset-age alignment** | Stable VAX and NEVER modes agree within ±1 month. | Stable VAX mode lies within ±1 month of 12, 15, or 18 and differs from NEVER by ≥3 months. | Unstable mode, <20 per group, two-month difference, both align, or another pattern. |
| **P5. Peak-width difference** | Both peaks are broad (adjacent ratios ≥0.80) and $\lvert B_{VAX}-B_{NEVER}\rvert≤0.20$. | $B_{VAX}<0.80$ and $B_{NEVER}-B_{VAX}>0.20$. | Unstable modes; sparse group; intervals cross thresholds; both equally sharp; or NEVER sharper. |
| **P6. Peak-asymmetry difference** | Both $A_g≤0.20$ and $\lvert A_{VAX}-A_{NEVER}\rvert≤0.10$. | $A_{VAX}>0.20$, $A_{VAX}-A_{NEVER}>0.10$, and excess features align with vaccination ages. | Unstable modes; sparse group; intervals cross thresholds; shared asymmetry; or opposite direction. |
| **P7. Verified 0–5-day lag excess** | Upper 95% RR limit <2.0. | Point RR≥2.0, one-sided exact p<0.05, and lower 95% RR limit >1. | CI spans both regions; reference count inadequate; verification tiers conflict; or opposite direction. |

Definitions and draft margins: $C_1=D_{VAX}-D_{NEVER}$, where $D_g=p_{g,2020}-(p_{g,2019}+p_{g,2021})/2$; $C_2=p_{weekday,VAX}-p_{weekday,NEVER}$; $C_3=\tfrac12\sum_{d=1}^{7}\lvert p_{VAX,d}-p_{NEVER,d}\rvert$; $B_g=\min(n_{g,m_g-1}/n_{g,m_g},n_{g,m_g+1}/n_{g,m_g})$; and $A_g=\sum_{k=1}^{6}\lvert n_{g,m_g-k}-n_{g,m_g+k}\rvert/\sum_{k=1}^{6}(n_{g,m_g-k}+n_{g,m_g+k})$. For P7, $E/R$ null=6/54=1/9, $P_0(E)=0.10$, and $RR=(E/6)/(R/54)$. P1–P6 margins remain draft; P7 RR=2 is fixed.

## 5. Why P4 had to change

“There is one modal onset month” cannot be a discriminating test because both H-null and H-vax can produce one mode. V7 therefore tests whether the VAX and NEVER modal ages agree versus whether a stable VAX mode aligns with a prespecified vaccination age and differs materially from NEVER. If the NEVER sample is too small, P4 is Indeterminate/Indeterminate—not Yes/Yes.

## 6. Overall decision

P7 is the primary statistical decision test. P1–P6 are core supporting tests and must all be reported.

- **Overall H-vax favored:** P7 is No/Yes and respondent-verified/document-verified results agree in direction. Supporting No/Yes rows strengthen the conclusion.
- **Overall H-null favored against a material short-window effect:** P7 is Yes/No and no prespecified multiplicity-controlled product/window analysis produces a material association.
- **Overall indeterminate:** P7 is Indeterminate/Indeterminate or the verification tiers materially conflict.

P1–P6 cannot override a precise P7 result, but discordant or indeterminate supporting rows must be visible.

## 7. Verification

Respondents receive a readback and confirm or correct phenotype eligibility, PARENT onset timing, last wellness visit, `What happened?` vaccination status, same-day BEFORE/AFTER or lag, onset age/year/day, and VAX/NEVER status. Corrections are logged without overwriting originals.

- Respondent-verified records are primary.
- Document-verified records are the higher-evidence replication.

## 8. P7 exact and Monte Carlo procedures

The exact one-sided binomial test of $P(E)>0.10$ is authoritative. Report two-sided p, exact CI, E, R, and RR. Monte Carlo is only a code check: seed `20260830`, 100,000 replicates, independently draw lags uniformly from integers 0–59, and confirm the simulated tail probability agrees with the exact p-value.

## 9. Required output

Publish a seven-row-by-two-column paired matrix:

| Test | H-null | H-vax |
|---|:---:|:---:|
| P1 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P2 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P3 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P4 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P5 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P6 | Yes / No / Indeterminate | No / Yes / Indeterminate |
| P7 | Yes / No / Indeterminate | No / Yes / Indeterminate |

Validate in code that every row is exactly `(Yes, No)`, `(No, Yes)`, or `(Indeterminate, Indeterminate)`.

## 10. Freeze checklist

Before v7 is final:

1. approve or replace the draft P1–P6 margins;
2. freeze the vaccination-calendar model for P2/P3;
3. simulate Type I error, power, sparse NEVER groups, mode instability, rounding, and selection;
4. implement the mutually exclusive state validator;
5. freeze verification and bootstrap procedures; and
6. publish code, simulation results, timestamp, version, and cryptographic hash before confirmatory analysis.

## 11. Version history

- **v1–v5:** progressively developed hypotheses, verification, lag windows, RR=2, and Monte Carlo checking.
- **v6:** first explicit H-null/H-vax prediction beside every P1–P7 test, but some rows could still score Yes/Yes or No/No.
- **v7 draft:** gives every test non-overlapping paired null, vaccine, and indeterminate regions; P4 is redesigned as an exposure-group modal-age comparison.

### V7 clarification log

- **2026-08-30:** After considering independent cell scoring, restored the paired three-outcome rule: Yes/No, No/Yes, or Indeterminate/Indeterminate. This matches the purpose of each row as a single discriminator between two mutually exclusive prediction regions.
