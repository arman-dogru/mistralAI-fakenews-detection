import json
import csv

# Path to the JSON file
json_file = 'datasets/Politics/Politifact/politifact_factcheck_data.json'

# Path to the CSV file
csv_file = 'datasets/Politics/Politifact/politifact.csv'

# Read the JSON file
data = []
with open(json_file, "r") as file:
    for line in file:
        data.append(json.loads(line))

# Extract the "verdict" and "statement" values from the JSON data
rows = [(item['verdict'], item['statement']) for item in data]

# Write the data to a CSV file
with open(csv_file, 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['verdict', 'statement'])  # Write the header
    writer.writerows(rows)  # Write the rows

#print unique values in the verdict column
import pandas as pd
df = pd.read_csv(csv_file)
print(df['verdict'].unique())

# change the values true, mostly true, half-true to 1, and false, pants-fire to 0
df['verdict'] = df['verdict'].replace(['true', 'mostly-true', 'half-true'], 1)
df['verdict'] = df['verdict'].replace(['false', 'pants-fire', "mostly-false"], 0)

# Save the preprocessed dataset
df.to_csv('datasets/Politics/Politifact/politifact_preprocessed.csv', index=False)