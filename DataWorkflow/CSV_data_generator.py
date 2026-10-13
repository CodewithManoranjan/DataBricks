import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Number of rows - around 10 MB CSV
num_rows = 100000

np.random.seed(42)
random.seed(42)

transaction_types = ["DEBIT", "CREDIT", "TRANSFER", "PAYMENT", "WITHDRAWAL"]
merchant_categories = [
    "Grocery", "Fuel", "Restaurant", "Travel", "Electronics",
    "Healthcare", "Insurance", "Utilities", "Entertainment", "Retail"
]
currencies = ["USD", "EUR", "GBP", "INR", "JPY"]
countries = ["US", "UK", "India", "Germany", "Japan", "Canada", "France"]

start_date = datetime(2023, 1, 1)

data = {
    "transaction_id": [f"TXN{i:08d}" for i in range(1, num_rows + 1)],
    "customer_id": np.random.randint(10000, 99999, num_rows),
    "account_id": np.random.randint(1000000, 9999999, num_rows),
    "transaction_date": [
        start_date + timedelta(minutes=int(x))
        for x in np.random.randint(0, 525600, num_rows)
    ],
    "transaction_type": np.random.choice(transaction_types, num_rows),
    "merchant_category": np.random.choice(merchant_categories, num_rows),
    "amount": np.round(np.random.exponential(scale=250, size=num_rows), 2),
    "currency": np.random.choice(currencies, num_rows),
    "country": np.random.choice(countries, num_rows),
    "account_balance": np.round(np.random.normal(loc=5000, scale=2500, size=num_rows), 2),
    "credit_score": np.random.randint(300, 850, num_rows),
    "is_fraud": np.random.choice([0, 1], size=num_rows, p=[0.97, 0.03])
}

df = pd.DataFrame(data)

# Use Unity Catalog Volume POSIX path
volume_csv_path = "/Volumes/workspace/default/finance_volume/finance_transactions_10mb.csv"

# Save directly to Volume
df.to_csv(volume_csv_path, index=False)

print("CSV file created successfully!")
print("File saved at:", volume_csv_path)
