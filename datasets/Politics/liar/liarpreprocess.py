import pandas as pd

# Read the CSV file
df = pd.read_csv('datasets/Politics/liar/liar_train.csv')

# Perform preprocessing steps on the dataset
# change the labels 1,2,3,4 to 1 and 5 to 0
df['label'] = df['label'].replace([1, 2, 3, 4], 1)
df['label'] = df['label'].replace(5, 0)

# Save the preprocessed dataset
df.to_csv('datasets/Politics/liar/liar_train_preprocessed.csv', index=False)

# Print the preprocessed dataset
print(df.head())