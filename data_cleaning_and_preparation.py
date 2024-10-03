import pandas as pd
import numpy as np

# Simulate a dataset
np.random.seed(42)

# Generate a dataset with columns for Date, Region, Product, Quantity, Unit Price, and Customer Age
data_size = 1000
dates = pd.date_range(start="2023-01-01", periods=data_size, freq='D').strftime('%Y-%m-%d')
regions = np.random.choice(['North', 'South', 'East', 'West'], data_size)
products = np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], data_size)
quantities = np.random.randint(1, 10, size=data_size)
unit_prices = np.random.uniform(10, 100, size=data_size).round(2)
customer_ages = np.random.randint(18, 70, size=data_size)

# Combine into a DataFrame
sales_data = pd.DataFrame({
    'Date': dates,
    'Region': regions,
    'Product': products,
    'Quantity': quantities,
    'Unit_Price': unit_prices,
    'Customer_Age': customer_ages
})

# Introduce some missing values randomly
sales_data.loc[sales_data.sample(frac=0.05).index, 'Quantity'] = np.nan
sales_data.loc[sales_data.sample(frac=0.03).index, 'Region'] = np.nan

# Show the first few rows of the simulated dataset
sales_data.head()

# Export the cleaned data to a CSV file
cleaned_file_path = 'data/cleaned_sales_data.csv'
sales_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to: {cleaned_file_path}")
