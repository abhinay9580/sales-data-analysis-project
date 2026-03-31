import pandas as pd

df = pd.read_csv("sales_dataset.csv")

print(df.head())
print(df.info())


# Total sales

total_sales = df["SALES"].sum()

# Average sales

avg = df["SALES"].mean()

# Top 5 product

top_products = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False).head(5)

# Top 5 city.

top_city = df.groupby("CITY")["SALES"].sum().sort_values(ascending=False).head(5)

# OUTPUT

print("\n Total Sales:", total_sales)

print("\n Average Sales:", avg)

print("\n Top Products:\n", top_products)
print("\n Top City:\n", top_city)
