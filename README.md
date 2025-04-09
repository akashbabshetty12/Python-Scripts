# Python Scripts for Date Processing and Log Analysis

## Overview
This repository contains two Python scripts:

1. **`weekdays_missing_sc.py`** - Identifies missing weekdays from a date list and saves them into a CSV.
2. **`pan_in_test.py`** - Reads log files from a directory and saves them into a CSV.

---

## 1️⃣ Script: `weekdays_missing_sc.py`
📅 Date Range Checker and Summary Generator
This Python script reads a list of dates from a text file, analyzes them, and generates a summary report with the following:

• The start and end dates in the list
• Weekdays that are missing between the start and end dates
• Weekend dates that are present in the input
• A CSV summary file with all the details

✅ Features
• Supports date input in YYYY-MM-DD format
• Detects missing weekdays (Monday–Friday)
• Lists weekend dates (Saturday and Sunday) that are present in the input
• Saves the report to date_summary.csv

📝 Input File Format
• One date per line
• Date format: YYYY-MM-DD

Example (dates.txt):
2025-04-01
2025-04-02

🗂️ Output CSV Format
Year	Start Date	End Date	Weekdays Missing (Count)	Weekdays Missing (List)	Weekend Dates Present (Count)	Weekend Dates Present (List)
Example row:
2025,2025-04-01,2025-04-08,2,2025-04-03, 2025-04-07,2,2025-04-05, 2025-04-06
▶️ How to Use
Save your dates in a file like dates.txt

Run the script:
python your_script_name.py
Enter the full path to your date file when prompted

💻 Requirements
This script only uses Python's built-in modules:
• os
• datetime
• csv

No extra installations needed.

🧠 Notes
• Make sure dates are correctly formatted and no duplicates are included
• The script automatically removes duplicates and processes unique dates only

📂 Example Output (Console)

Start Date: 2025-04-01
End Date:   2025-04-08

Missing Weekdays:
2025-04-03

Weekend Dates Present in File:
2025-04-05

Full summary saved to 'date_summary.csv'

---

## 2️⃣ Script: `pan_in_test.py`
### 📌 **Purpose**
This script scans a directory for `.log` and `.txt` files, extracts their contents, and saves them into a structured CSV file.

### 🛠 **How to Use**
1. Place the script inside a folder containing log files.
2. Run the script:
   ```bash
   python pan_in_test.py
   ```
3. Enter the directory path containing the log files.
4. The script will generate an `output.csv` file.

### 📤 **Expected Output**
A CSV file with the following columns:
- `Folder Name` - Path of the folder.
- `File Name` - Name of the log file.
- `Log Data` - Content of each line.

---

## 📌 **Requirements**
Ensure you have Python installed. To install dependencies:
```bash
pip install pandas
```

---

## 📌 **Contributing**
Feel free to submit issues or pull requests for improvements. 😊

