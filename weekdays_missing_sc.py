import os
from datetime import datetime, timedelta
import csv

# Get file path from user
input_file = input("Enter your file path: ").strip('"')

# Check if the file exists
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    exit()

# Read and convert date strings, removing duplicates
with open(input_file, "r") as file:
    file_dates = {line.strip() for line in file}

# Convert to datetime objects
file_dates = {datetime.strptime(date, "%Y-%m-%d") for date in file_dates}

# Get start and end dates
start_date = min(file_dates)
end_date = max(file_dates)

print(f"\nStart Date: {start_date.strftime('%Y-%m-%d')}")
print(f"End Date:   {end_date.strftime('%Y-%m-%d')}\n")

# Generate all dates in range
all_dates = []
current_date = start_date
while current_date <= end_date:
    all_dates.append(current_date)
    current_date += timedelta(days=1)

# Find missing weekdays
missing_weekdays = [
    date.strftime("%Y-%m-%d")
    for date in all_dates
    if date.weekday() < 5 and date not in file_dates
]

# Find weekend dates present in file
weekend_dates = [
    date.strftime("%Y-%m-%d")
    for date in file_dates
    if date.weekday() >= 5
]

# Print output
print("Missing Weekdays:")
for date in missing_weekdays:
    print(date)

print("\nWeekend Dates Present in File:")
for date in weekend_dates:
    print(date)

# Extract year from start date
summary_year = start_date.year

# Write (append) summary to CSV
file_exists = os.path.isfile("date_summary.csv")

with open("date_summary.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write header only if file doesn't exist
    if not file_exists:
        writer.writerow([
            "Year",
            "Start",
            "End",
            "Missed Weekdays Count",
            "Missed Weekdays",
            "Weekend Present Count",
            "Weekend Dates"
        ])

    writer.writerow([
        summary_year,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
        len(missing_weekdays),
        ", ".join(missing_weekdays),
        len(weekend_dates),
        ", ".join(weekend_dates)-*
    ])

print("\n✅ Summary appended to 'date_summary.csv'")
