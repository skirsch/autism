# Work log

## 2026-08-08 — USA SORA risk-ratio analysis

- **What we did:** Read `SORA incidence-Grid view.csv` from Downloads; retained USA rows where total children equaled the sum of fully vaccinated, partially vaccinated, and fully unvaccinated children. Blank count cells were treated as zero.
- **Command / executable:** PowerShell `Import-Csv` with numeric consistency filtering and aggregate risk-ratio calculations; 95% confidence intervals used the log (Katz) approximation.
- **Outputs:** No derived data file; results reported in the Codex task.
- **Results:** The total-consistency rule initially retained 1,178 records. Six records were then excluded because at least one category-specific SORA count exceeded the corresponding vaccination-category child count, leaving 1,172 records. Corrected aggregates: fully vaccinated 116/1,545; partially vaccinated 35/1,069; unvaccinated 4/1,360. RR fully vaccinated vs unvaccinated = 25.53 (95% CI 9.45–68.98); RR partially vaccinated vs unvaccinated = 11.13 (95% CI 3.97–31.22).
- **Next steps:** Consider household clustering and survey-selection effects for formal inference.

## 2026-08-08 — Mixed-family healthier-cohort analysis

- **What we did:** Among the 1,172 cleaned USA records, selected families containing at least one fully vaccinated and at least one fully unvaccinated child. Evaluated only the independent `Healthier cohort` response; SORA counts were not used.
- **Command / executable:** PowerShell filtering and grouping; exact two-sided binomial test and Clopper–Pearson interval calculated with Python/SciPy.
- **Outputs:** No derived data file; results reported in the Codex task.
- **Results:** 125 mixed families; 103 left the healthier-cohort field blank. Among 22 responses: 10 significantly and 5 somewhat favored unvaccinated children, 5 reported about the same, and 1 significantly plus 1 somewhat favored vaccinated children. Overall directional ratio = 15:2 = 7.5:1; exact two-sided sign-test p = 0.00235; exact-derived 95% interval for the directional ratio = 1.74–67.59.
- **Next steps:** Treat the result as respondent-reported and highly vulnerable to nonresponse and survey-selection bias.

## 2026-08-08 — Article infographic

- **What we did:** Generated a landscape editorial infographic summarizing the cleaned USA survey analysis and mixed-family healthier-cohort responses.
- **Command / executable:** Built-in image generation, followed by a project-local copy.
- **Outputs:** `docs/assets/sora-parent-survey-summary.png`.
- **Results:** Graphic uses the corrected post-exclusion estimates: fully vaccinated RR 25.5, partially vaccinated RR 11.1, unvaccinated reference risk 0.294%, significant-health response 10:1, and all directional health responses 7.5:1. It labels the analysis as observational and self-selected.
- **Next steps:** Insert the PNG into the article and keep the article prose consistent with the corrected figures.
