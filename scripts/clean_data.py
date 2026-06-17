import pandas as pd
df = pd.read_csv("data/amazon.csv")

# clean discounted price
df["discounted_price"] = (df["discounted_price"]
                          .str.replace('₹', '', regex=False)
                          .str.replace(',', '', regex=False)
                          .astype(float))

# clean actual price
df["actual_price"] = (df["actual_price"]
                      .str.replace("₹", '', regex=False)
                      .str.replace(',', '', regex=False)
                      .astype(float))

# clean discount percentage
df["discount_percentage"] = (df["discount_percentage"]
                             .str.replace("%", '', regex=False)
                             .astype(float))

# clean rating
df['rating'] = pd.to_numeric(df["rating"], errors='coerce')

# clean rating_count
df["rating_count"] = (df["rating_count"]
                      .fillna("0")
                      .str.replace(',', '', regex=False))

df["rating_count"] = pd.to_numeric(df["rating_count"], errors='coerce')

# saved clean data
df.to_csv("data/amazon_clean.csv", index=False)

print("Data cleaning completed. Cleaned data saved to 'data/amazon_clean.csv'.")

print("\n New Data Types: ")
print(
    df[
        ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
    ].dtypes
)

