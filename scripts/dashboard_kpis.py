import pandas as pd
df = pd.read_csv('data/amazon_final.csv')

print("\n EXECUTIVE KPIs")
total_products = len(df)
average_rating = round(df['rating'].mean(), 2)
average_discount = round(df['discount_percentage'].mean(), 2)
total_reviews = (df['rating_count'].sum())

print(
    f"Total Product : {total_products}"
    )
print(
    f"Average Rating: {average_rating}"
)

print(
    f"Average Discount: {average_discount}%"
)

print(
    f"Total Reviews: {total_reviews:,}"
)