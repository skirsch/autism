import fs from "node:fs/promises";
import path from "node:path";
import { Workbook } from "@oai/artifact-tool";

const inputPath = "C:/Users/stk/Downloads/SORA incidence-Grid viewBW.csv";
const outputPath = "C:/Users/stk/Downloads/SORA incidence-Grid viewBW_cleaned.csv";
const previewPath = "C:/Users/stk/Documents/GitHub/autism/.codex-tmp/clean-sora/preview.png";

const sourceText = await fs.readFile(inputPath, "utf8");
const sourceBook = await Workbook.fromCSV(sourceText, { sheetName: "SORA incidence" });
const sourceSheet = sourceBook.worksheets.getItem("SORA incidence");
const sourceValues = sourceSheet.getUsedRange(true).values;
const headers = sourceValues[0].map((value) => String(value ?? ""));
const index = Object.fromEntries(headers.map((header, column) => [header, column]));

const required = [
  "Number of kids under age 20",
  "# kids full",
  "# kids partially vaxxed",
  "# kids fully unvaccinated",
  "# SORA vaxxed",
  "# SORA partial",
  "# SORA unvax",
];
for (const header of required) {
  if (!(header in index)) throw new Error(`Missing required column: ${header}`);
}

function countValue(value) {
  if (value === null || value === undefined || String(value).trim() === "") return 0;
  const parsed = Number(String(value).trim());
  return Number.isFinite(parsed) ? parsed : null;
}

const reasonCounts = new Map();
const kept = [sourceValues[0]];
const removed = [];
for (const row of sourceValues.slice(1)) {
  const total = countValue(row[index["Number of kids under age 20"]]);
  const full = countValue(row[index["# kids full"]]);
  const partial = countValue(row[index["# kids partially vaxxed"]]);
  const unvax = countValue(row[index["# kids fully unvaccinated"]]);
  const soraFull = countValue(row[index["# SORA vaxxed"]]);
  const soraPartial = countValue(row[index["# SORA partial"]]);
  const soraUnvax = countValue(row[index["# SORA unvax"]]);
  const values = [total, full, partial, unvax, soraFull, soraPartial, soraUnvax];
  const reasons = [];
  if (values.some((value) => value === null)) {
    reasons.push("nonnumeric_count");
  } else {
    if (total !== full + partial + unvax) reasons.push("total_mismatch");
    if (soraFull > full) reasons.push("sora_vaxxed_exceeds_category");
    if (soraPartial > partial) reasons.push("sora_partial_exceeds_category");
    if (soraUnvax > unvax) reasons.push("sora_unvax_exceeds_category");
  }
  if (reasons.length === 0) {
    kept.push(row);
  } else {
    removed.push({ number: row[index.number], reasons });
    for (const reason of reasons) reasonCounts.set(reason, (reasonCounts.get(reason) ?? 0) + 1);
  }
}

function csvCell(value) {
  const text = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}
const cleanedText = kept.map((row) => row.map(csvCell).join(",")).join("\r\n") + "\r\n";
await fs.writeFile(outputPath, cleanedText, "utf8");

const verificationText = await fs.readFile(outputPath, "utf8");
const verificationBook = await Workbook.fromCSV(verificationText, { sheetName: "Cleaned" });
const verifiedSheet = verificationBook.worksheets.getItem("Cleaned");
const verifiedValues = verifiedSheet.getUsedRange(true).values;
if (verifiedValues.length !== kept.length) throw new Error("Output row count failed verification");
const preview = await verificationBook.render({ sheetName: "Cleaned", range: "A1:O12", scale: 1, format: "png" });
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));

console.log(JSON.stringify({
  inputPath,
  outputPath,
  sourceRows: sourceValues.length - 1,
  keptRows: kept.length - 1,
  removedRows: removed.length,
  reasonCounts: Object.fromEntries(reasonCounts),
  removedSample: removed.slice(0, 10),
  verifiedRows: verifiedValues.length - 1,
}, null, 2));
