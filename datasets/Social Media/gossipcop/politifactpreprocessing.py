import pandas as pd

# Read the CSV file
df_real = pd.read_csv('datasets/Social Media/gossipcop/politifact_real.csv')
df_fake = pd.read_csv('datasets/Social Media/gossipcop/politifact_fake.csv')

# Perform preprocessing steps here
# drop id,news_url,tweet_ids
df_real = df_real.drop(columns=['id', 'news_url', 'tweet_ids'])
df_fake = df_fake.drop(columns=['id', 'news_url', 'tweet_ids'])

#add label column with value 1
df_real['label'] = 1
df_fake['label'] = 0

# merge the dataframes and save to a new CSV file
df = pd.concat([df_real, df_fake])
df.to_csv('datasets/Social Media/gossipcop/preprocessed_politifact.csv', index=False)