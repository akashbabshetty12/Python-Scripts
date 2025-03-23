# Python Scripts for Date Processing and Log Analysis

## Overview
This repository contains two Python scripts:

1. **`weekdays_missing_sc.py`** - Identifies missing weekdays from a date list.
2. **`pan_in_test.py`** - Reads log files from a directory and saves them into a CSV.

---

## 1️⃣ Script: `weekdays_missing_sc.py`
### 📌 **Purpose**
This script reads a file containing dates and identifies:
- **Missing weekdays (Monday-Friday)**
- **Weekend dates present in the file**

### 🛠 **How to Use**
1. Ensure you have a text file with dates in `YYYY-MM-DD` format.
2. Run the script:
   ```bash
   python weekdays_missing_sc.py
   ```
3. Enter the path to the file when prompted.

### 📤 **Expected Output**
- List of missing weekdays.
- List of weekends present in the file.

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

