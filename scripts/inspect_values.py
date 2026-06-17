import pandas as pd
df = pd.read_csv("data/amazon.csv")

print("DISCOUNTED PRICE")
print(df["discounted_price"].head())

print("\nACTUAL PRICE")
print(df["actual_price"].head())

print("\nDISCOUNT")
print(df["discount_percentage"].head())

print("\nRATING")
print(df["rating"].head())

print("\nRATING COUNT")
print(df["rating_count"].head())
