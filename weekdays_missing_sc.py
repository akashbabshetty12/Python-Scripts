import os
from datetime import datetime, timedelta

# Correct file path
input_file = input("enter your path: ").strip('"')

# Check if the file exists before proceeding
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    exit()

# Read dates from file and store in a set
with open(input_file, "r") as file:
    file_dates = {line.strip() for line in file}

# Convert strings to datetime objects
file_dates = {datetime.strptime(date, "%Y-%m-%d") for date in file_dates}

# Get start and end date from the file
start_date = min(file_dates)
end_date = max(file_dates)

# Generate all dates between start and end date
current_date = start_date
all_dates = []
while current_date <= end_date:
    all_dates.append(current_date)
    current_date += timedelta(days=1)

# Find missing weekdays (Monday-Friday)
missing_weekdays = [
    date.strftime("%Y-%m-%d")
    for date in all_dates
    if date.weekday() < 5 and date not in file_dates
]

# Find weekend dates present in the file
weekend_dates = [
    date.strftime("%Y-%m-%d")
    for date in file_dates
    if date.weekday() >= 5
]

# Print missing weekdays
print("Missing weekdays:")
for date in missing_weekdays:
    print(date)

# Print weekend dates found in the file
print("\nWeekend dates present in the file:")
for date in weekend_dates:
    print(date)
