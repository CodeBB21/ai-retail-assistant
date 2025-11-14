import pandas as pd
import numpy as np
import os

# Fix random seed (reproductibilité)
np.random.seed(42)

# Create data directory if not exists
os.makedirs("data", exist_ok=True)

# Number of customers
n = 1500  

# Generate dataset
df = pd.DataFrame({
    "customer_id": np.arange(1, n+1),
    "age": np.random.randint(18, 70, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "income": np.random.randint(18000, 120000, n),
    "city": np.random.choice(["Paris", "Lyon", "Marseille", "Toulouse", "Nice"], n),
    "category": np.random.choice(["Electronics", "Fashion", "Sports", "Home", "Beauty"], n),
    "amount": np.round(np.random.uniform(10, 2000, n), 2),
    "frequency": np.random.randint(1, 15, n),
    "last_purchase_days_ago": np.random.randint(1, 365, n),
})

# Add churn target
df["churn"] = np.where(
    (df["frequency"] < 3) & 
    (df["last_purchase_days_ago"] > 150), 
    1, 
    0
)

# Save CSV
output_path = "data/customers.csv"
df.to_csv(output_path, index=False)

print(f"Dataset generated and saved to: {output_path}")
print(df.head())
