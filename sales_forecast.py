# Importing necessary libraries namely Numpy
import numpy as np
import matplotlib.pyplot as plt

# Creating Sample sales Data and products

products = np.array(["Laptop", "Phones", "Headphones", "Tvs", "Keyboards"])
sales = np.array([500, 350, 280, 346, 480])

# Creating a random generation function for Market Variation
np.random.seed(42) # for reproducibility
variation = np.random.randint(-50, 60, size = 5)
adjusted_sales = sales + variation

# Forecasted Sales 
growth_rate = 0.12
forecasted_sales = adjusted_sales * (1 + growth_rate)

# Statistical analysis

total_sales = np.sum(adjusted_sales)
avg_sales = np.mean(adjusted_sales)
std_dev = np.std(adjusted_sales)
best_product = products[np.argmax(adjusted_sales)]
worst_product = products[np.argmin(adjusted_sales)]

# Final Display

print("=== Monthly Sales Summary===")

for product, current, forecast in zip(products, adjusted_sales, forecasted_sales):
    print(f" {product}: Current Sale = {current}, Forecast = {forecast:.2f}")

print(f"Total Sales on products: {total_sales}")
print(f" Average Sales on Products: {avg_sales:.2f}")
print(f" Standard Deviation: {std_dev:.2f}")
print(f" Best Performer: {best_product}")
print(f" Worst Performer: {worst_product}")


x = np.arange(len(products))
width = 0.35

plt.bar(x - width/2, adjusted_sales, width, label="Current Sales")
plt.bar(x + width/2, forecasted_sales, width, label="Forecasted Sales")

plt.xlabel("Products")
plt.ylabel("Sales (Units or $)")
plt.title("Sales Forecast Comparison")
plt.xticks(x, products)
plt.legend()
plt.show()