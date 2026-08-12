import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = "outputs/sora_irb";
await fs.mkdir(outputDir, { recursive: true });

const wb = Workbook.create();
const data = wb.worksheets.add("Data Entry");
data.showGridLines = false;
data.getRange("A1:F1").values = [[
  "site_code", "clinic_row_id", "sex", "age_at_onset_months", "dpre_days", "dpost_days"
]];
data.getRange("A2:F401").values = Array.from({ length: 400 }, () => [null, null, null, null, null, null]);
data.getRange("A1:F1").format = {
  fill: "#17365D",
  font: { bold: true, color: "#FFFFFF" },
  wrapText: true,
  rowHeight: 32,
  borders: { preset: "outside", style: "thin", color: "#17365D" },
};
data.getRange("A2:F401").format = {
  fill: "#FFFBE6",
  borders: { preset: "inside", style: "thin", color: "#D9E2F3" },
};
data.getRange("A:B").format.columnWidth = 18;
data.getRange("C:C").format.columnWidth = 12;
data.getRange("D:D").format.columnWidth = 23;
data.getRange("E:F").format.columnWidth = 16;
data.getRange("A2:B401").format.numberFormat = "@";
data.getRange("D2:F401").format.numberFormat = "0";
data.getRange("C2:C401").dataValidation = { rule: { type: "list", values: ["Female", "Male", "Intersex", "Unknown/not recorded"] } };
data.getRange("D2:D401").dataValidation = { rule: { type: "whole", operator: "between", formula1: 0, formula2: 60 } };
data.getRange("E2:F401").dataValidation = { rule: { type: "whole", operator: "between", formula1: 0, formula2: 3650 } };
data.freezePanes.freezeRows(1);
data.tables.add("A1:F401", true, "SoraDataTable");

const instructions = wb.worksheets.add("Instructions");
instructions.showGridLines = false;
instructions.getRange("A1:D1").merge();
instructions.getRange("A1").values = [["SORA Electronic Data Submission Template"]];
instructions.getRange("A1:D1").format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30 };
instructions.getRange("A3:B12").values = [
  ["Submission", "Complete the Data Entry sheet electronically and upload the workbook through the approved secure portal. Do not print, handwrite, scan, photograph, fax, or paste data into an email."],
  ["One row", "Enter one eligible patient per row. Do not add columns."],
  ["site_code", "Use the nonidentifying site code assigned for this study (for example, SITE01). Do not enter the clinic name."],
  ["clinic_row_id", "Clinic-assigned arbitrary row code. It must not be derived from a name, MRN, date, or other identifier. The clinic retains the mapping."],
  ["sex", "Select the clinic-recorded category from the dropdown."],
  ["age_at_onset_months", "Age in completed months on the locally determined onset date."],
  ["dpre_days", "Calendar days from the most recent administered vaccination before/on onset to onset. Same day = 0."],
  ["dpost_days", "Calendar days from onset to the first administered vaccination after onset."],
  ["Prohibited", "No calendar dates, phenotype information, narrative/free text, patient names, MRNs, contact data, geography, clinic name, or patient mapping key."],
  ["Certification", "The uploading clinic certifies that eligibility was verified locally and the electronic file contains only the six approved data fields."],
];
instructions.getRange("A3:A12").format = { fill: "#D9EAF7", font: { bold: true, color: "#17365D" }, wrapText: true };
instructions.getRange("B3:B12").format = { wrapText: true, fill: "#FFFFFF" };
instructions.getRange("A3:B12").format.borders = { preset: "all", style: "thin", color: "#CBD5E1" };
instructions.getRange("A:A").format.columnWidth = 22;
instructions.getRange("B:B").format.columnWidth = 85;
instructions.getRange("A3:B12").format.autofitRows();

const check = await wb.inspect({ kind: "table", sheetId: "Data Entry", range: "A1:F6", include: "values,formulas", tableMaxRows: 6, tableMaxCols: 6 });
console.log(check.ndjson);
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 50 }, summary: "formula error scan" });
console.log(errors.ndjson);

for (const [sheetName, filename] of [["Data Entry", "data-entry-preview.png"], ["Instructions", "instructions-preview.png"]]) {
  const img = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outputDir}/${filename}`, new Uint8Array(await img.arrayBuffer()));
}
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(`${outputDir}/SORA_Electronic_Data_Submission_Template_v1.0.xlsx`);
