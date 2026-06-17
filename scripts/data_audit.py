import pandas as pd
df = pd.read_csv("data/amazon.csv")

print("\n INFO")
print(df.info())

print("\n MISSING VALUES")
print(df.isnull().sum())

print("\n DUPLICATEs")
print(df.duplicated().sum())

print("\n TYEPS")
print(df.dtypes)




