import pandas as pd
df = pd.read_csv('data/amazon_final.csv')

# products per category
products_by_category = (df['main_category'].value_counts())

print("\nPRODUCTS BY CATEGORY")
print(products_by_category)

# average rating by category
rating_by_category = (
    df.groupby('main_category')['rating'].mean().sort_values(ascending=False)
)

print("\n===== RATING BY CATEGORY =====")
print(rating_by_category)

# average Discount by category
discount_by_category = (
    df.groupby("main_category")["discount_percentage"].mean().sort_values(ascending=False)
                        )
print("\n===== DISCOUNT BY CATEGORY =====")
print(discount_by_category)