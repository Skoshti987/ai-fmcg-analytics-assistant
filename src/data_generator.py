import pandas as pd
import random
from datetime import datetime, timedelta

# Reproducible results
random.seed(42)

# Dataset configuration
regions = ["North", "South", "East", "West"]
categories = ["Beverages", "Snacks", "Dairy"]
products = {
    "Beverages": ["Cola", "Juice", "Energy Drink"],
    "Snacks": ["Chips", "Biscuits", "Namkeen"],
    "Dairy": ["Milk", "Yogurt", "Cheese"]
}

start_date = datetime(2026, 1, 1)
number_of_days = 180

data = []

for i in range(number_of_days):
    current_date = start_date + timedelta(days=i)

    for region in regions:
        for category in categories:

            product = random.choice(products[category])

            # Randomly decide if a promotion is running
            promotion = random.choice(["Yes", "No"])

            # Base sales
            base_sales = random.randint(50000, 150000)

            # Promotions increase sales
            if promotion == "Yes":
                sales = base_sales * random.uniform(1.10, 1.40)
            else:
                sales = base_sales

            units_sold = int(sales / random.uniform(20, 50))

            inventory = random.randint(500, 5000)

            data.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "region": region,
                "category": category,
                "product": product,
                "promotion": promotion,
                "sales": round(sales, 2),
                "units_sold": units_sold,
                "inventory": inventory
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/fmcg_promotions.csv", index=False)

print("Dataset created successfully!")
print(f"Total rows: {len(df)}")
print(df.head())