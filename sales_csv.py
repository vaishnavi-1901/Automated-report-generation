import pandas as pd

# Create data
data = {
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [120, 200, 150, 180, 170, 220],
    "Profit": [30, 50, 45, 40, 55, 60]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sales.csv", index=False)

print("✅ sales.csv file created successfully!")