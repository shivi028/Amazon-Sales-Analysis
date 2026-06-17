import pandas as pd
df = pd.read_csv("data/amazon_clean.csv")

# extract main category

df["main_category"] = (
    df['category'].str.split('|').str[0]
)

print(df['main_category'].value_counts())

df.to_csv('data/amazon_final.csv', index=False)

print('\nSaved as amazon_final.csv')