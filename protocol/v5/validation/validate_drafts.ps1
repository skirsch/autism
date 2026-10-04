<#!
Local document/reference checks only. No participant data, network calls, writes,
production export transformation, deployment or IRB submission.
Run: pwsh -NoProfile -File protocol/v5/validation/validate_drafts.ps1
#>
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$draftRoot = Split-Path $PSScriptRoot -Parent
$script:checkCount = 0
$script:failures = [System.Collections.Generic.List[string]]::new()

function Assert-Equal($Name, $Actual, $Expected) {
    $script:checkCount++
    $actualJson = ConvertTo-Json -InputObject $Actual -Depth 8 -Compress
    $expectedJson = ConvertTo-Json -InputObject $Expected -Depth 8 -Compress
    if ($actualJson -cne $expectedJson) {
        $script:failures.Add("$Name expected $expectedJson; got $actualJson")
    }
}

function Get-DateValue([string]$Value) {
    [datetime]::ParseExact($Value, 'yyyy-MM-dd', [Globalization.CultureInfo]::InvariantCulture)
}

function Get-Lag([string]$Onset, [string]$Anchor) {
    [int]((Get-DateValue $Onset) - (Get-DateValue $Anchor)).TotalDays
}

function Test-VisitEligible([string]$Onset, [string]$Anchor) {
    $lag = Get-Lag $Onset $Anchor
    $lag -ge 0 -and $lag -le 90
}

function Get-CompletedMonths([string]$Birth, [string]$Onset) {
    $birthDate = Get-DateValue $Birth
    $onsetDate = Get-DateValue $Onset
    if ($onsetDate -lt $birthDate) { throw 'ONSET precedes birthdate' }
    $months = ($onsetDate.Year-$birthDate.Year)*12 + $onsetDate.Month-$birthDate.Month
    if ($birthDate.AddMonths($months) -gt $onsetDate) { $months-- }
    $months
}

function Get-Quarter([string]$Onset) {
    $date = Get-DateValue $Onset
    $quarterMonth = [int]([math]::Floor(($date.Month-1)/3)*3+1)
    [datetime]::new($date.Year, $quarterMonth, 1).ToString('yyyy-MM-dd')
}

function Get-NominalAnchor([string]$Birth, [string]$Onset) {
    $birthDate = Get-DateValue $Birth
    $onsetDate = Get-DateValue $Onset
    $eligible = @(2,4,6,12,15,18 | ForEach-Object {
        $candidate = $birthDate.AddMonths($_)
        $lag = [int]($onsetDate-$candidate).TotalDays
        if ($lag -ge 0 -and $lag -le 90) { $candidate }
    })
    if ($eligible.Count -eq 0) { return $null }
    ($eligible | Sort-Object -Descending | Select-Object -First 1).ToString('yyyy-MM-dd')
}

function Get-ExactMajority($Votes) {
    # Include precision/status in each vote. This tests exact tuple agreement,
    # not corroboration or the consistency of a whole accepted record.
    $groups = @($Votes | ForEach-Object {
        ConvertTo-Json -InputObject $_ -Compress -Depth 8
    } | Group-Object -CaseSensitive | Where-Object Count -ge 2)
    if ($groups.Count -ne 1) { return $null }
    $groups[0].Name | ConvertFrom-Json
}

Assert-Equal 'F01 lag zero' (Get-Lag '2024-07-01' '2024-07-01') 0
Assert-Equal 'F02 day 90' (Test-VisitEligible '2024-07-01' '2024-04-02') $true
Assert-Equal 'F03 day 91' (Test-VisitEligible '2024-07-01' '2024-04-01') $false
Assert-Equal 'F04 future' (Test-VisitEligible '2024-07-01' '2024-07-02') $false
Assert-Equal 'F05 quarter date' (Get-Quarter '2024-03-31') '2024-01-01'
Assert-Equal 'F05 quarter lag' (Get-Lag '2024-03-31' (Get-Quarter '2024-03-31')) 90
Assert-Equal 'F06 quarter 91 allowed' (Get-Lag '2024-09-30' (Get-Quarter '2024-09-30')) 91
Assert-Equal 'F07 original birthday arithmetic' ((Get-DateValue '2023-01-31').AddMonths(2).ToString('yyyy-MM-dd')) '2023-03-31'
Assert-Equal 'F08 February clamp' ((Get-DateValue '2024-08-31').AddMonths(6).ToString('yyyy-MM-dd')) '2025-02-28'
Assert-Equal 'F09 leap birthday' ((Get-DateValue '2024-02-29').AddMonths(12).ToString('yyyy-MM-dd')) '2025-02-28'
Assert-Equal 'F10 below age floor' (Get-CompletedMonths '2023-01-01' '2023-06-30') 5
Assert-Equal 'F10 age floor' (Get-CompletedMonths '2023-01-01' '2023-07-01') 6
Assert-Equal 'F11 upper included month' (Get-CompletedMonths '2023-01-01' '2025-01-31') 24
Assert-Equal 'F11 upper excluded month' (Get-CompletedMonths '2023-01-01' '2025-02-01') 25
Assert-Equal 'F12 no extra nominal point' (Get-NominalAnchor '2023-01-01' '2024-12-31') $null
Assert-Equal 'nominal coincident' (Get-NominalAnchor '2023-01-01' '2024-07-01') '2024-07-01'
Assert-Equal 'F14 count reconciliation' (5+10+5) 20
Assert-Equal 'F14 lower and upper' @(5, (5+5)) @(5,10)
Assert-Equal 'F15 partial return not a complete day' @(0,(0+2)) @(0,2)
Assert-Equal 'F16 preserve out of range flag' (12 -gt 10) $true
$matching = @([ordered]@{status='exact';value='2024-06-01'}, [ordered]@{status='exact';value='2024-06-01'}, [ordered]@{status='exact';value='2024-06-03'})
Assert-Equal 'F20 date majority' ((Get-ExactMajority $matching).value) '2024-06-01'
$different = @([ordered]@{status='exact';value=5}, [ordered]@{status='lower_bound';value=5}, [ordered]@{status='unknown';value=$null})
Assert-Equal 'F21 status not collapsed' (Get-ExactMajority $different) $null
Assert-Equal 'F22 inverted bounds flagged' ((Get-DateValue '2024-06-04') -gt (Get-DateValue '2024-06-02')) $true
Assert-Equal 'batch example' ([int][math]::Ceiling(1.20*(100-20)/(20/100))) 480
Assert-Equal 'top up example' (50-25) 25

$requiredDrafts = @('study_overview.md','survey1.md','survey2.md','data_specification.md','data_dictionary.md','eligibility_and_construction.md','survey_screen_map.md','recruitment_and_compensation.md','consent_and_disclosure.md','records_review_manual.md','privacy_security_and_release.md','governance_and_confirmations.md','irb_application.md','irb_feedback_responses.md','submission_checklist.md','prelaunch_validation.md','document_guide.md','task_list.md')
foreach ($name in $requiredDrafts) {
    Assert-Equal "required document $name" (Test-Path -LiteralPath (Join-Path $draftRoot $name) -PathType Leaf) $true
}

$partnerScreen = Get-Content -LiteralPath (Join-Path $draftRoot 'survey1.md') -Raw
$followupSurvey = Get-Content -LiteralPath (Join-Path $draftRoot 'survey2.md') -Raw
$recruitmentProcedure = Get-Content -LiteralPath (Join-Path $draftRoot 'recruitment_and_compensation.md') -Raw
$logicalDictionary = Get-Content -LiteralPath (Join-Path $draftRoot 'data_dictionary.md') -Raw
# Text-contract checks only: these do not implement referral permission or
# prove deployed routing, custody, eligibility or queue isolation.
Assert-Equal 'partner screen exactly two question headings' ([regex]::Matches($partnerScreen, '(?m)^### Question [12]').Count) 2
Assert-Equal 'partner individual answers not transferred' ($partnerScreen.Contains('not the partner''s individual screening answers')) $true
Assert-Equal 'all-referral follow-up access' ($followupSurvey.Contains('every authorized possible-case email referral')) $true
Assert-Equal 'follow-up date confidence collected' ($followupSurvey.Contains('Separate date-confidence screen after A2')) $true
Assert-Equal 'records confidence follows narrative' ($followupSurvey.IndexOf('### Question A4') -gt $followupSurvey.IndexOf('### Question A1')) $true
Assert-Equal 'records confidence precedes disclosure' ($followupSurvey.IndexOf('### Question A4') -lt $followupSurvey.IndexOf('## Part B:')) $true
Assert-Equal 'deferred material requests' ($followupSurvey.Contains('A Yes answer does not itself send a request or enable an upload')) $true
Assert-Equal 'request-selection minimized queue' ($recruitmentProcedure.Contains('not exposure fields, causal beliefs or reviewer judgments')) $true
Assert-Equal 'records confidence schema moved to study' ($logicalDictionary.Contains('`records_confidence_s2`')) $true
Assert-Equal 'retired partner records-confidence schema' ($logicalDictionary.Contains('`records_confidence_s1`')) $false

$linkCount = 0
foreach ($file in Get-ChildItem -LiteralPath $draftRoot -Filter '*.md' -File) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    if ($file.Name -notin @('document_guide.md','task_list.md')) {
        Assert-Equal "version $($file.Name)" ([bool]($content -match '\*\*Version:\*\*\s+\d+\.\d+ draft')) $true
    }
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\(([^)]+)\)')) {
        $target = $match.Groups[1].Value.Trim('<','>')
        if ($target -match '^[a-zA-Z]+:' -or $target.StartsWith('#')) { continue }
        $relative = [uri]::UnescapeDataString(($target -split '#')[0])
        $linkCount++
        Assert-Equal "link $($file.Name) -> $relative" (Test-Path -LiteralPath (Join-Path $file.DirectoryName $relative)) $true
    }
}

[pscustomobject]@{
    scope='local document/reference checks; not live platform or production processing'
    checks=$script:checkCount
    local_links=$linkCount
    failures=$script:failures.Count
    details=@($script:failures.ToArray())
} | ConvertTo-Json -Depth 8
if ($script:failures.Count -gt 0) { exit 1 }
