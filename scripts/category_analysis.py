import pandas as pd
df = pd.read_csv('data/amazon_clean.csv')


# average rating by category
avg_rating = (df.groupby("category")['rating'].mean().sort_values(ascending=False)
              )
print("\n===== TOP RATED CATEGORIES =====")
print(avg_rating.head(5))


# Average Discount by category
avg_discount = (df.groupby("category")['discount_percentage'].mean().sort_values(ascending=False))
print("\n===== HIGHEST DISCOUNT CATEGORIES =====")
print(avg_discount.head(5))


# review volume by Category
review_volume = (
    df.groupby('category')['rating_count'].sum().sort_values(ascending=False)
)
print("\n===== MOST REVIEWED CATEGORIES =====")
print(review_volume.head(5))