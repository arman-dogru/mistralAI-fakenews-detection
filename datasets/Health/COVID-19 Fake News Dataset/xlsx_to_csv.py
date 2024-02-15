import pandas as pd

# Read the Excel file
df = pd.read_excel('datasets/Health/COVID-19 Fake News Dataset/fake_new_dataset.xlsx')

# drop the 'Unnamed: 0' column, title and subcategory
df = df.drop(columns=['Unnamed: 0', 'title', 'subcategory'])

# Convert to CSV
df.to_csv('datasets/Health/COVID-19 Fake News Dataset/fake_new_dataset.csv', index=False)