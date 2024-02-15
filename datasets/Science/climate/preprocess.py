import pandas as pd

# Read the CSV file
df = pd.read_csv('datasets/Science/climate/climate_fever.csv')

# Perform preprocessing steps here
# drop claim_id,evidences
df = df.drop(columns=['claim_id', 'evidences'])

# rename claim and claim_label to text and label
df = df.rename(columns={"claim": "text"})
df = df.rename(columns={"claim_label": "label"})


# Save the preprocessed data to a new CSV file
df.to_csv('datasets/Science/climate/preprocessed_climate_fever.csv', index=False)