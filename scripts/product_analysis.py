import pandas as pd
df = pd.read_csv('data/amazon_clean.csv')

print("\nData Overview:")
# print("products : ", len(df))
# print("Categories : ", df["category"].nunique())
print("Average Rating : ", round(df["rating"].mean(),2))
print("Average Discount : ", round(df["discount_percentage"].mean(),2))

# top rated products
top_rated = (
    df[["product_name", "rating"]].sort_values(by="rating", ascending=False).head(5)
)

print("\n===== TOP RATED PRODUCTS =====")
print(top_rated)

# most reviewd porducts
most_reviewed = (df[['product_name', 'rating_count']].sort_values(by="rating_count", ascending=False).head(5))

print("\n===== MOST REVIEWED PRODUCTS =====")
print(most_reviewed)

# biggest discount
largest_discount = (df[["product_name", "discount_percentage"]].sort_values(by="discount_percentage", ascending=False).head(5))

print("\n===== BIGGEST DISCOUNTS =====")
print(largest_discount)