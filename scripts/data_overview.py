import pandas as pd
df = pd.read_csv("data/amazon.csv")
print(df.head())

print("\nShape : ")
print(df.shape)

print("\nColumns : ")
print(df.columns.tolist())

