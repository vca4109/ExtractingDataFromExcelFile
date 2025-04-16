📊 Excel Column Extractor Script (Python)-
This Python script is designed to automate the extraction of specific columns from an Excel sheet and save the results into a new file. It’s ideal for handling large deliverables or data logs where only selected data fields are needed.

🔧 Features
📁 Reads data from a specified sheet in an Excel workbook (ABC.xlsx)

🔍 Extracts specific columns by index for a cleaner, focused output

📤 Exports to a new Excel file (ABC_Extracted_Data_26-03-2024.xlsx)

⚠️ Handles missing file errors and alerts for failed operations

🛑 Suppresses unnecessary warnings for cleaner terminal output

🧠 How It Works
Input File:

Excel workbook: ABC.xlsx

Target sheet: Deliverables

Columns Extracted:

Columns are selected by zero-based index (e.g., column 1 = 2nd column in Excel).

Duplicates and placeholder indices (100) are included for flexibility and future-proofing.

Output:

A new Excel file named ABC_Extracted_Data_26-03-2024.xlsx containing only the selected columns.

Error Handling:

Alerts if the input file is missing.

Confirms whether the export was successful.

📌 Sample Use Case
This script is useful for:

Document Controllers extracting specific fields from a large log

Engineers or analysts preparing a filtered report

Anyone handling structured Excel data needing quick cleanup

💡 Customization Tips
Update the uploaded_file_name and sheet_name for different data sources.

Modify the columns_to_extract list to suit your column structure.

You can rename the output file by changing the output_file_path variable.

