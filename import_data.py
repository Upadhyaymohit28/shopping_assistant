# import_data.py

import sqlite3
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:\Users\Mohit\shopping_assistant\superstore_products.csv')

# Data Cleaning (Optional)
# For example, fill NaN values, rename columns, etc.
# df = df.fillna('')

# Connect to the SQLite database
conn = sqlite3.connect('superstore.db')

# Write the data to the 'products' table
df.to_sql('products', conn, if_exists='append', index=False)

# Close the connection
conn.close()

print("Data imported successfully into the 'products' table.")
# import_data.py

import sqlite3
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:\Users\Mohit\shopping_assistant\superstore_products.csv')

# Data Cleaning (Optional)
# For example, fill NaN values, rename columns, etc.
# df = df.fillna('')

# Connect to the SQLite database
conn = sqlite3.connect('product_reviews.db')

# Write the data to the 'product_reviews' table
df.to_sql('product_reviews', conn, if_exists='append', index=False)

# Close the connection
conn.close()

print("Data imported successfully into the 'product_reviews' table.")
