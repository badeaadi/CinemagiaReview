import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv('reviews.csv')
train_df, test_df = train_test_split(df, test_size=0.25)

train_df.to_csv('cinemagia-train-dataset.csv', sep=',', encoding='utf-8', index=False)
test_df.to_csv('cinemagia-test-dataset.csv', sep=',', encoding='utf-8', index=False)

print(len(df))
print(df.columns)


