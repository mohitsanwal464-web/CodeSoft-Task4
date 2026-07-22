import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("custon er_data.xlsx.xlsx")

# Display Data
print(df.head())

# Top Customers
top_customers = df.sort_values(by="Purchase_Amount", ascending=False)
print("\nTop Customers:")
print(top_customers)

# Location Wise Purchase
location_sales = df.groupby("Location")["Purchase_Amount"].sum()
print("\nLocation Wise Purchase:")
print(location_sales)

# Product Wise Purchase
product_sales = df.groupby("Product")["Purchase_Amount"].sum()
print("\nProduct Wise Purchase:")
print(product_sales)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(location_sales.index, location_sales.values)
plt.title("Location Wise Purchase")
plt.xlabel("Location")
plt.ylabel("Purchase Amount")
plt.show()

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(product_sales.index, product_sales.values, marker="o")
plt.title("Product Wise Purchase")
plt.xlabel("Product")
plt.ylabel("Purchase Amount")
plt.xticks(rotation=45)
plt.show()