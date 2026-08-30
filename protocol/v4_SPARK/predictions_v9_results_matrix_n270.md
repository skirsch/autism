# V9 results — n=270 assumed-verification exercise

**Data:** `C:\Users\stk\Downloads\SOA2-Grid view.csv`, 270 rows, SHA-256 `42F732E2D6DB49BA1DBC393AE20EE2FFEBA2E8A187FDE80311696824D5CBD681`.  
**Exercise assumption:** Treat retained survey values as verified and correct.  
**Rules:** `prespecified_predictions_v9.md`. P1–P6 use all eligible records; none requires a VAX-versus-NEVER comparison. P7 uses confirmed vaccination visits.

| Test | Result | Observed statistic and reason |
|---|:---:|---|
| **P1. 2020 dip** | **Vaccine** | Counts were 2019=5, 2020=1, and 2021=10. Thus $Q_{2020}=1/7.5=0.133$, below 0.50; the one-sided exact test of 1 event in 2020 among the 16 events in 2019–2021 against probability $1/3$ gives $p=0.0137$. |
| **P2. Weekday concentration** | **Vaccine** | There were 92 weekday and 15 weekend reports among 107 classifiable records: 86.0% weekday versus the null 71.4%. The one-sided exact test gives $p=0.000305$, and the point estimate exceeds 80%. |
| **P3. Named-day distribution** | **Indeterminate** | Named-day counts were Monday=7, Tuesday=4, Wednesday=8, Thursday=5, Friday=7, Saturday=5, and Sunday=2 ($n=38$). Total-variation distance from uniformity was 0.1504, but the chi-square test gave $p=0.578$. The data therefore do not satisfy the Vaccine region, while the point estimate itself prevents ruling out departures greater than 0.15 for the Null region. |
| **P4. Modal onset age** | **Indeterminate** | The unique observed mode was 18 months (43 reports), which is in the Vaccine point-estimate region. V9 nevertheless requires the mode to be stable under a frozen bootstrap procedure, which has not yet been specified; the formal result is therefore Indeterminate. |
| **P5. Peak width** | **Indeterminate** | The counts at 17, 18, and 19 months were 5, 43, and 6, giving $B=\min(5/43,6/43)=0.116$. This is far inside the Vaccine point-estimate region, but v9 requires a confidence interval from the still-unfrozen bootstrap procedure. |
| **P6. Peak asymmetry** | **Indeterminate** | The observed six-month asymmetry was $A=57/127=0.449$, above 0.20. V9 additionally requires its lower confidence limit to exceed 0.20 and the excess to follow a direction frozen before analysis; neither procedure is yet frozen. |
| **P7. Verified 0–5-day lag excess** | **Vaccine** | Among confirmed vaccination visits, $E=36$ and $R=8$. The early fraction was 81.8%, $RR=(36/6)/(8/54)=40.5$, exact 95% RR interval 18.5–100.9, and one-sided exact $p=7.82\times10^{-29}$. This satisfies every Vaccine-region criterion. |

## Summary

| Result | Tests | Count |
|---|---|---:|
| **Vaccine** | P1, P2, P7 | 3 |
| **Null** | None | 0 |
| **Indeterminate** | P3, P4, P5, P6 | 4 |

Under v9's overall rule, the exercise result is **Vaccine favored** because the primary test, P7, is Vaccine. P1 and P2 independently enter their supporting Vaccine regions. P4–P6 have Vaccine-region point estimates but remain formally Indeterminate because their required procedures were not frozen.

This classification means that the observations match v9's prespecified Vaccine regions under the assumed-verification exercise. It does not by itself prove that vaccination caused the reported autism onsets. The pooled all-visit counts ($E=125$, $R=62$) must not be interpreted as a no-vaccine control: most corresponding `What happened?` values are blank or unknown. Among detailed non-vaccination visits, only three records have usable lags in the P7 window; all three are in days 6–59 and none is in days 0–5. This tiny negative-control cell is directionally consistent with the prediction but formally indeterminate.
