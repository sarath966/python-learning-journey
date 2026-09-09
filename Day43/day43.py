"""
Mission Day 43
Topic: Pandas Consolidation - Sales Analysis

Concepts:
- read_csv()
- DataFrame inspection
- Creating columns
- Filtering
- groupby()
- sum()
- mean()
- idxmax()
- loc
- sort_values()
- to_csv()
"""
import pandas as pd

sales = pd.read_csv(r"sales.csv")
print(sales)

# ---------- Exercise 1 --------
print(sales.head())
print(sales.shape)
sales.info()
print(sales.describe())

# ---------- Exercise 2 ---------
sales["Revenue"] = sales["Price"] * sales["Quantity"]
print(sales[["Product", "Price", "Quantity", "Revenue"]])

# ---------- Exercise 3  --------
print(sales[sales["Revenue"] >= 20000])
print(sales[(sales["Rating"] >= 4.3) &
             (sales["Quantity"] >= 2)])

# ---------- Exercise 4 ---------
print(sales.groupby("Category")["Revenue"].sum())
print(sales.groupby("Category")["Rating"].mean())
print(sales.groupby("Category")["Quantity"].sum())

# ---------- Exercise 5 --------
print(sales.loc[sales["Revenue"].idxmax()])
print(sales.loc[sales["Rating"].idxmax()])
print(sales.iloc[sales["Quantity"].idxmax()])

# ---------- Exercise 6 --------
sales = sales.sort_values("Revenue",ascending=False)
print(sales[["Product", "Category", "Revenue", "Rating"]])


print("\nMission Day 43 Completed Successfully!")