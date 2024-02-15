import pandas as pd

# Read the CSV files
fake_news = pd.read_csv("datasets/Health/COVID19-FNIR/fakeNews.csv")
true_news = pd.read_csv("datasets/Health/COVID19-FNIR/trueNews.csv")

# Match both of the file columns to the format: text, label
# fakenews: Date Posted,Link,Text,Region,Country,Explanation,Origin,Origin_URL,Fact_checked_by,Poynter_Label,Binary Label
# truenes: Date Posted,Link,Text,Region,Username,Publisher,Label
fake_news = fake_news.rename(columns={"Explanation": "Label"})
fake_news = fake_news.rename(columns={"Text": "text"})
fake_news = fake_news.rename(columns={"Binary Label": "label"})
fake_news = fake_news[["text", "label"]]
true_news = true_news.rename(columns={"Label": "label"})
true_news = true_news.rename(columns={"Text": "text"})
true_news = true_news[["text", "label"]]

# Combine both of the files
news = pd.concat([fake_news, true_news])

# Save the combined file
news.to_csv("datasets/Health/COVID19-FNIR/combined.csv", index=False)