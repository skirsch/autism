# Clean invalid vaccination CSV

> look at the most recent file in Download (the .csv file).
>
> load the .csv and remove invalid entries.... invalid means total != sum of the 3 vax categories.  Or that the sora count for any column is > than number of kids in the vax category.

<details><summary>9 previous messages</summary>

> I’ll inspect the required workspace instructions, identify the newest CSV in Downloads, then validate its columns and write a cleaned copy while preserving the original. I’m using the spreadsheet skill because this is a CSV cleaning task.
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content -Raw 'C:\Users\stk\Documents\GitHub\ai\.memory.md'; Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\SKILL.md'`
>
> </details>
>
> The shared instructions also require the repo-specific memory, if present. I’m checking that plus the CSV’s headers and a few rows first, because the exact vaccine and SORA column names determine the validation mapping.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `$repoMemory='C:\Users\stk\Documents\GitHub\autism\.memory.md'; if (Test-Path -LiteralPath $repoMemory) { Get-Content -Raw -LiteralPath $repoMemory }; Get-ChildItem -LiteralPath 'C:\Users\stk\Downloads' -File -Filter '*.csv' | Sort-Object LastWriteTime -Descending | Select-Object -First 5 FullName,Length,LastWriteTime | Format-List`
> - Ran `Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\style_guidelines.md'; Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\artifact_tool_docs\API_QUICK_START.md'`
> - Ran `$f='C:\Users\stk\Downloads\SORA incidence-Grid viewBW.csv'; $rows=Import-Csv -LiteralPath $f; 'ROW_COUNT=' + $rows.Count; 'HEADERS:'; $rows[0].PSObject.Properties.Name; 'FIRST_ROWS:'; $rows | Select-Object -First 3 | ConvertTo-Json -Depth 3`
> - Ran `$f='C:\Users\stk\Downloads\SORA incidence-Grid viewBW.csv'; $rows=Import-Csv -LiteralPath $f; $cols=@('Number of kids under age 20','# kids full','# kids partially vaxxed','# kids fully unvaccinated','# SORA vaxxed','# SORA partial','# SORA unvax'); foreach($c in $cols){ $bad=$rows | Where-Object { $v=0; -not [decimal]::TryParse(($_.$c).Trim(),[Globalization.NumberStyles]::Number,[Globalization.CultureInfo]::InvariantCulture,[ref]$v) }; "$c nonnumeric=$($bad.Count) blanks=$(($rows | Where-Object {[string]::IsNullOrWhiteSpace($_.$c)}).Count)" }; $invalid=@(); foreach($row in $rows){ $vals=@{}; $parse=$true; foreach($c in $cols){$v=0; if(-not [decimal]::TryParse(($row.$c).Trim(),[Globalization.NumberStyles]::Number,[Globalization.CultureInfo]::InvariantCulture,[ref]$v)){$parse=$false};$vals[$c]=$v}; $sum=$vals['# kids full']+$vals['# kids partially vaxxed']+$vals['# kids fully unvaccinated']; $reasons=@(); if(-not $parse){$reasons+='nonnumeric'}; if($vals['Number of kids under age 20'] -ne $sum){$reasons+='total_mismatch'}; if($vals['# SORA vaxxed'] -gt $vals['# kids full']){$reasons+='sora_vaxxed_exceeds'}; if($vals['# SORA partial'] -gt $vals['# kids partially vaxxed']){$reasons+='sora_partial_exceeds'}; if($vals['# SORA unvax'] -gt $vals['# kids fully unvaccinated']){$reasons+='sora_unvax_exceeds'}; if($reasons.Count){$invalid += [pscustomobject]@{number=$row.number;reasons=($reasons -join '|')}} }; "INVALID=$($invalid.Count) VALID=$($rows.Count-$invalid.Count)"; $invalid | Group-Object reasons | Sort-Object Count -Descending | Select-Object Count,Name | Format-Table -AutoSize; 'SAMPLE_INVALID'; $invalid | Select-Object -First 10 | Format-Table -AutoSize`
>
> </details>
>
> The count fields contain some blanks, which in this survey appear to represent zero rather than malformed data. I’ll therefore normalize blank count cells to 0 for validation, remove only rows that fail the two stated consistency rules, and report the exact removal counts.
>
> <details><summary>Created a file, ran 3 commands</summary>
>
> - Ran `$f='C:\Users\stk\Downloads\SORA incidence-Grid viewBW.csv'; $rows=Import-Csv -LiteralPath $f; function N($x){if([string]::IsNullOrWhiteSpace($x)){return [decimal]0}; $v=0; if([decimal]::TryParse($x.Trim(),[Globalization.NumberStyles]::Number,[Globalization.CultureInfo]::InvariantCulture,[ref]$v)){return $v}; return $null}; $invalid=@(); foreach($row in $rows){$t=N $row.'Number of kids under age 20';$f1=N $row.'# kids full';$p=N $row.'# kids partially vaxxed';$u=N $row.'# kids fully unvaccinated';$sv=N $row.'# SORA vaxxed';$sp=N $row.'# SORA partial';$su=N $row.'# SORA unvax';$reasons=@();if($null -in @($t,$f1,$p,$u,$sv,$sp,$su)){$reasons+='nonnumeric'}else{if($t -ne ($f1+$p+$u)){$reasons+='total_mismatch'};if($sv -gt $f1){$reasons+='sora_vaxxed_exceeds'};if($sp -gt $p){$reasons+='sora_partial_exceeds'};if($su -gt $u){$reasons+='sora_unvax_exceeds'}};if($reasons.Count){$invalid+=[pscustomobject]@{number=$row.number;reasons=$reasons -join '|'}}}; "INVALID=$($invalid.Count) VALID=$($rows.Count-$invalid.Count)"; $invalid|Group-Object reasons|Sort-Object Count -Descending|Select-Object Count,Name|Format-Table -AutoSize`
> - Ran `$mods='C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules'; @('csv-parse','csv-stringify','@oai/artifact-tool') | ForEach-Object { "$_=" + (Test-Path -LiteralPath (Join-Path $mods $_)) }; New-Item -ItemType Directory -Force -Path 'C:\Users\stk\Documents\GitHub\autism\.codex-tmp\clean-sora' | Out-Null; if(Test-Path 'C:\Users\stk\Documents\GitHub\autism\process\work_log.md'){'WORKLOG_EXISTS'}`
> - Wrote `./.codex-tmp/clean-sora/clean.mjs` (+88 -0)
> - Ran `$tmp='C:\Users\stk\Documents\GitHub\autism\.codex-tmp\clean-sora'; $mods='C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules'; if(-not (Test-Path -LiteralPath (Join-Path $tmp 'node_modules'))){New-Item -ItemType Junction -Path (Join-Path $tmp 'node_modules') -Target $mods | Out-Null}; Test-Path -LiteralPath (Join-Path $tmp 'clean.mjs'); & 'C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' (Join-Path $tmp 'clean.mjs')`
>
> </details>
>
> The filtering logic is now running against all 1,496 records and then re-importing the cleaned file for a row-count and visual verification pass.
>
> Viewed an image
>
> <details><summary>Edited a file, ran 3 commands</summary>
>
> - Ran `$f='C:\Users\stk\Downloads\SORA incidence-Grid viewBW_cleaned.csv'; $rows=Import-Csv -LiteralPath $f; function N($x){if([string]::IsNullOrWhiteSpace($x)){return [decimal]0}; return [decimal]::Parse($x,[Globalization.CultureInfo]::InvariantCulture)}; $bad=$rows|Where-Object{(N $_.'Number of kids under age 20') -ne ((N $_.'# kids full')+(N $_.'# kids partially vaxxed')+(N $_.'# kids fully unvaccinated')) -or (N $_.'# SORA vaxxed') -gt (N $_.'# kids full') -or (N $_.'# SORA partial') -gt (N $_.'# kids partially vaxxed') -or (N $_.'# SORA unvax') -gt (N $_.'# kids fully unvaccinated')}; Get-Item -LiteralPath $f | Select-Object FullName,Length,LastWriteTime; "ROWS=$($rows.Count) INVALID_REMAINING=$($bad.Count)"; (Get-FileHash -Algorithm SHA256 -LiteralPath $f).Hash`
> - Ran `Get-Content -Tail 30 'C:\Users\stk\Documents\GitHub\autism\process\work_log.md'`
> - Wrote `./process/work_log.md` (+8 -0)
> - Ran `Get-Content -Tail 12 'C:\Users\stk\Documents\GitHub\autism\process\work_log.md'`
>
> </details>
</details>

Cleaned the newest Downloads CSV.

- Original: 1,496 entries
- Removed: 176 invalid entries
- Remaining: 1,320 entries
- Verified: 0 invalid entries remain
- Blank count cells were treated as zero.
- Original file was preserved.

Cleaned file: :codex-file-citation{path="C:\Users\stk\Downloads\SORA incidence-Grid viewBW_cleaned.csv" purpose="output"}

> then do the RR computations for v/u and partial/u.
>
> then do the odds of uvaxxed:vaxxed on which group is healthier.

<details><summary>4 previous messages</summary>

> I’ll use the cleaned CSV to calculate category-level SORA risks and risk ratios for fully vaccinated vs. unvaccinated and partially vaccinated vs. unvaccinated. I’ll also tabulate the “Healthier cohort” responses and compute unvaccinated:vaccinated odds from directional responses, stating exactly how blanks and “about the same” responses are handled. I’m using the spreadsheet skill for the CSV analysis.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\SKILL.md'; $f='C:\Users\stk\Downloads\SORA incidence-Grid viewBW_cleaned.csv'; $rows=Import-Csv -LiteralPath $f; 'HEALTHIER VALUES'; $rows | Group-Object 'Healthier cohort' | Sort-Object Count -Descending | Select-Object Count,Name | Format-Table -AutoSize; 'COUNTRY'; $rows | Group-Object Country | Sort-Object Count -Descending | Select-Object -First 10 Count,Name | Format-Table -AutoSize`
> - Ran `Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\style_guidelines.md'; Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\artifact_tool_docs\API_QUICK_START.md'; Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\domain_guidance\healthcare.md'; Get-Content -Raw 'C:\Users\stk\.codex\plugins\cache\openai-primary-runtime\spreadsheets\26.805.11740\skills\spreadsheets\domain_guidance\scientific_research.md'`
>
> </details>
>
> The cleaned file has 54 nonblank healthier-cohort responses, but not every respondent necessarily has both vaccinated and unvaccinated children. I’m calculating the headline comparison on mixed families (at least one fully vaccinated and one fully unvaccinated child), then I’ll show the all-response figure separately so the denominator is transparent.
>
> <details><summary>Created a file, edited a file, ran 4 commands</summary>
>
> - Wrote `./.codex-tmp/clean-sora/analyze.mjs` (+63 -0)
> - Ran `& 'C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' 'C:\Users\stk\Documents\GitHub\autism\.codex-tmp\clean-sora\analyze.mjs'`
> - Ran `@'
> import math
> from scipy.stats import beta, binomtest
> comparisons = [('full',100,1306,0,742),('partial',48,1152,0,742)]
> for name,a,n1,c,n0 in comparisons:
>     # Haldane-Anscombe: add 0.5 to every 2x2 cell
>     b=n1-a; d=n0-c
>     ac=a+0.5; bc=b+0.5; cc=c+0.5; dc=d+0.5
>     rr=(ac/(ac+bc))/(cc/(cc+dc))
>     se=math.sqrt(1/ac-1/(ac+bc)+1/cc-1/(cc+dc))
>     lo=math.exp(math.log(rr)-1.96*se); hi=math.exp(math.log(rr)+1.96*se)
>     print(name, rr, lo, hi)
> x=35;n=37
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('health',x,n-x,x/(n-x),res.pvalue,plo,phi,plo/(1-plo),phi/(1-phi))
> x=20;n=21
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('significant',x,n-x,x/(n-x),res.pvalue,plo/(1-plo),phi/(1-phi))
> '@ | & 'C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -`
> - Ran `$env:PYTHONPATH='C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\python'; @'
> import math
> from scipy.stats import beta, binomtest
> comparisons = [('full',100,1306,0,742),('partial',48,1152,0,742)]
> for name,a,n1,c,n0 in comparisons:
>     b=n1-a; d=n0-c
>     ac=a+0.5; bc=b+0.5; cc=c+0.5; dc=d+0.5
>     rr=(ac/(ac+bc))/(cc/(cc+dc))
>     se=math.sqrt(1/ac-1/(ac+bc)+1/cc-1/(cc+dc))
>     lo=math.exp(math.log(rr)-1.96*se); hi=math.exp(math.log(rr)+1.96*se)
>     print(name, rr, lo, hi)
> x=35;n=37
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('health',x,n-x,x/(n-x),res.pvalue,plo,phi,plo/(1-plo),phi/(1-phi))
> x=20;n=21
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('significant',x,n-x,x/(n-x),res.pvalue,plo/(1-plo),phi/(1-phi))
> '@ | & 'C:\Users\stk\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -`
> - Ran `@'
> import math
> from scipy.stats import beta, binomtest
> comparisons = [('full',100,1306,0,742),('partial',48,1152,0,742)]
> for name,a,n1,c,n0 in comparisons:
>     b=n1-a; d=n0-c
>     ac=a+0.5; bc=b+0.5; cc=c+0.5; dc=d+0.5
>     rr=(ac/(ac+bc))/(cc/(cc+dc))
>     se=math.sqrt(1/ac-1/(ac+bc)+1/cc-1/(cc+dc))
>     lo=math.exp(math.log(rr)-1.96*se); hi=math.exp(math.log(rr)+1.96*se)
>     print(name, rr, lo, hi)
> x=35;n=37
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('health',x,n-x,x/(n-x),res.pvalue,plo/(1-plo),phi/(1-phi))
> x=20;n=21
> res=binomtest(x,n,0.5,alternative='two-sided')
> plo=beta.ppf(.025,x,n-x+1); phi=beta.ppf(.975,x+1,n-x)
> print('significant',x,n-x,x/(n-x),res.pvalue,plo/(1-plo),phi/(1-phi))
> '@ | python -`
> - Wrote `./process/work_log.md` (+8 -0)
>
> </details>
</details>

Using the 1,320 valid records in the cleaned CSV: :codex-file-citation{path="C:\Users\stk\Downloads\SORA incidence-Grid viewBW_cleaned.csv" purpose="source"}

| Cohort | SORA / children | Risk | RR vs. unvaccinated |
|---|---:|---:|---:|
| Fully vaccinated | 100 / 1,306 | 7.657% | Infinite/undefined |
| Partially vaccinated | 48 / 1,152 | 4.167% | Infinite/undefined |
| Fully unvaccinated | 0 / 742 | 0.000% | Reference |

The raw RRs are not finite because the unvaccinated reference group had zero SORA cases. Using a Haldane–Anscombe 0.5-cell correction:

- Vaccinated/unvaccinated RR: **114.26** (95% CI **7.11–1,836.83**)
- Partial/unvaccinated RR: **62.51** (95% CI **3.86–1,012.19**)

For the 54 families containing both fully vaccinated and fully unvaccinated children:

- Unvaccinated healthier: **35**
- About the same: **17**
- Vaccinated healthier: **2**

Excluding “about the same,” the directional odds are **35:2**, or **17.5:1 favoring unvaccinated children**.

- Exact 95% CI for the odds: **4.50–150.18**
- Two-sided exact sign-test: **p = 1.02 × 10⁻⁸**

For “significantly healthier” responses alone, the split was **20:1 favoring unvaccinated children**. These are descriptive results from a self-selected survey, not causal estimates.
