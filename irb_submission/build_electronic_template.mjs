import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = "outputs/sora_irb";
await fs.mkdir(outputDir, { recursive: true });

const wb = Workbook.create();
const data = wb.worksheets.add("Data Entry");
data.showGridLines = false;
data.getRange("A1:E1").values = [[
  "clinic_row_id", "sex", "age_at_onset_months", "dpre_days", "dpost_days"
]];
data.getRange("A2:E201").values = Array.from({ length: 200 }, () => [null, null, null, null, null]);
data.getRange("A1:E1").format = {
  fill: "#17365D",
  font: { bold: true, color: "#FFFFFF" },
  wrapText: true,
  rowHeight: 32,
  borders: { preset: "outside", style: "thin", color: "#17365D" },
};
data.getRange("A2:E201").format = {
  fill: "#FFFBE6",
  borders: { preset: "inside", style: "thin", color: "#D9E2F3" },
};
data.getRange("A:A").format.columnWidth = 18;
data.getRange("B:B").format.columnWidth = 12;
data.getRange("C:C").format.columnWidth = 23;
data.getRange("D:E").format.columnWidth = 16;
data.getRange("A2:A201").format.numberFormat = "@";
data.getRange("C2:E201").format.numberFormat = "0";
data.getRange("B2:B201").dataValidation = { rule: { type: "list", values: ["Female", "Male", "Intersex", "Unknown/not recorded"] } };
data.getRange("C2:C201").dataValidation = { rule: { type: "whole", operator: "between", formula1: 0, formula2: 60 } };
data.getRange("D2:E201").dataValidation = { rule: { type: "whole", operator: "between", formula1: 0, formula2: 3650 } };
data.freezePanes.freezeRows(1);
data.tables.add("A1:E201", true, "SoraDataTable");

const instructions = wb.worksheets.add("Instructions");
instructions.showGridLines = false;
instructions.getRange("A1:D1").merge();
instructions.getRange("A1").values = [["SORA Electronic Data Submission Template"]];
instructions.getRange("A1:D1").format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30 };
instructions.getRange("A3:B11").values = [
  ["Submission", "Complete the Data Entry sheet electronically and upload the workbook through the approved secure portal. Do not print, handwrite, scan, photograph, fax, or paste data into an email."],
  ["One row", "Enter one eligible patient per row. Do not add columns."],
  ["clinic_row_id", "Clinic-assigned arbitrary row code. It must not be derived from a name, MRN, date, or other identifier. The clinic retains the mapping."],
  ["sex", "Select the clinic-recorded category from the dropdown."],
  ["age_at_onset_months", "Age in completed months on the locally determined onset date."],
  ["dpre_days", "Calendar days from the most recent administered vaccination before/on onset to onset. Same day = 0."],
  ["dpost_days", "Calendar days from onset to the first administered vaccination after onset."],
  ["Prohibited", "No calendar dates, phenotype information, narrative/free text, names, MRNs, contact data, geography, clinic identity, or mapping key."],
  ["Certification", "The uploading clinic certifies that eligibility was verified locally and the electronic file contains only the five approved data fields."],
];
instructions.getRange("A3:A11").format = { fill: "#D9EAF7", font: { bold: true, color: "#17365D" }, wrapText: true };
instructions.getRange("B3:B11").format = { wrapText: true, fill: "#FFFFFF" };
instructions.getRange("A3:B11").format.borders = { preset: "all", style: "thin", color: "#CBD5E1" };
instructions.getRange("A:A").format.columnWidth = 22;
instructions.getRange("B:B").format.columnWidth = 85;
instructions.getRange("A3:B11").format.autofitRows();

const check = await wb.inspect({ kind: "table", sheetId: "Data Entry", range: "A1:E6", include: "values,formulas", tableMaxRows: 6, tableMaxCols: 5 });
console.log(check.ndjson);
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 50 }, summary: "formula error scan" });
console.log(errors.ndjson);

for (const [sheetName, filename] of [["Data Entry", "data-entry-preview.png"], ["Instructions", "instructions-preview.png"]]) {
  const img = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outputDir}/${filename}`, new Uint8Array(await img.arrayBuffer()));
}
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(`${outputDir}/SORA_Electronic_Data_Submission_Template_v1.0.xlsx`);
