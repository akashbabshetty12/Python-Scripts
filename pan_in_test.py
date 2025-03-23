import os
import pandas as pd

# Define the folder containing log files
folder_name = input("Enter your path: ").strip('"')
log_dir = os.path.join(os.getcwd(), folder_name)

# Initialize an empty list to store log data
log_data = []

# Iterate through each log file in the folder
for filename in os.listdir(log_dir):
    if filename.endswith('.log') or filename.endswith('.txt'):

        file_path = os.path.join(log_dir, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Process each line and store it along with the folder name and file name
            for line in lines:
                log_data.append([folder_name, filename, line.strip()])

# Convert the collected data into a Pandas DataFrame
df = pd.DataFrame(log_data, columns=['Folder', 'File Name', 'Log Data'])

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

print("CSV file created successfully: output.csv")
