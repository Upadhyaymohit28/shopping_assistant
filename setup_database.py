import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('product_reviews.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Drop the existing 'product_reviews' table if it exists
cursor.execute('DROP TABLE IF EXISTS product_reviews')

# Create the 'product_reviews' table based on the updated columns shown
cursor.execute('''
CREATE TABLE IF NOT EXISTS product_reviews (
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    discounted_price TEXT,
    actual_price TEXT,
    discount_percentage TEXT,
    rating REAL,
    rating_count TEXT,
    about_product TEXT,
    user_id TEXT,
    user_name TEXT,
    review_id TEXT,
    review_title TEXT,
    review_content TEXT,
    img_link TEXT,
    product_link TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and 'product_reviews' table created successfully.")
