import fs from "node:fs/promises";
import { Workbook } from "@oai/artifact-tool";

const inputPath = "C:/Users/stk/Downloads/SORA incidence-Grid viewBW_cleaned.csv";
const text = await fs.readFile(inputPath, "utf8");
const workbook = await Workbook.fromCSV(text, { sheetName: "Cleaned" });
const sheet = workbook.worksheets.getItem("Cleaned");
const matrix = sheet.getUsedRange(true).values;
const headers = matrix[0].map((v) => String(v ?? ""));
const col = Object.fromEntries(headers.map((h, i) => [h, i]));
const n = (row, header) => {
  const value = row[col[header]];
  return value === null || value === undefined || String(value).trim() === "" ? 0 : Number(value);
};
const rows = matrix.slice(1);

const totals = {
  fullKids: 0, partialKids: 0, unvaxKids: 0,
  soraFull: 0, soraPartial: 0, soraUnvax: 0,
};
for (const row of rows) {
  totals.fullKids += n(row, "# kids full");
  totals.partialKids += n(row, "# kids partially vaxxed");
  totals.unvaxKids += n(row, "# kids fully unvaccinated");
  totals.soraFull += n(row, "# SORA vaxxed");
  totals.soraPartial += n(row, "# SORA partial");
  totals.soraUnvax += n(row, "# SORA unvax");
}

function healthCounts(selected) {
  const counts = { blank: 0, unvaxSignificant: 0, unvaxSomewhat: 0, same: 0, vaxSomewhat: 0, vaxSignificant: 0, other: 0 };
  for (const row of selected) {
    const value = String(row[col["Healthier cohort"]] ?? "").trim();
    if (!value) counts.blank++;
    else if (value === "Unvaccinated children are significantly healthier") counts.unvaxSignificant++;
    else if (value === "Unvaccinated children are somewhat healthier") counts.unvaxSomewhat++;
    else if (value === "About the same") counts.same++;
    else if (value === "Vaccinated children are somewhat healthier") counts.vaxSomewhat++;
    else if (value === "Vaccinated children are significantly healthier") counts.vaxSignificant++;
    else counts.other++;
  }
  return counts;
}

const mixedFullUnvax = rows.filter((row) => n(row, "# kids full") > 0 && n(row, "# kids fully unvaccinated") > 0);
const mixedAnyVaxUnvax = rows.filter((row) => n(row, "# kids full") + n(row, "# kids partially vaxxed") > 0 && n(row, "# kids fully unvaccinated") > 0);
const rates = {
  full: totals.soraFull / totals.fullKids,
  partial: totals.soraPartial / totals.partialKids,
  unvax: totals.soraUnvax / totals.unvaxKids,
};
console.log(JSON.stringify({
  records: rows.length,
  totals,
  rates,
  rrFullVsUnvax: rates.full / rates.unvax,
  rrPartialVsUnvax: rates.partial / rates.unvax,
  healthAll: healthCounts(rows),
  mixedFullUnvaxFamilies: mixedFullUnvax.length,
  healthMixedFullUnvax: healthCounts(mixedFullUnvax),
  mixedAnyVaxUnvaxFamilies: mixedAnyVaxUnvax.length,
  healthMixedAnyVaxUnvax: healthCounts(mixedAnyVaxUnvax),
}, null, 2));
