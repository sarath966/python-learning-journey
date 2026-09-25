import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    amount REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method TEXT,
    payment_status TEXT
)
""")
"""
customers = [
    (1, "Alice", "Hyderabad"),
    (2, "Bob", "Chennai"),
    (3, "Charlie", "Bangalore"),
    (4, "Diana", "Mumbai"),
    (5, "Ethan", "Delhi"),
    (6, "Farah", "Pune")
]

cursor.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)

orders = [
    (101, 1, "Laptop", 75000),
    (102, 2, "Phone", 30000),
    (103, 1, "Mouse", 1500),
    (104, 3, "Keyboard", 3000),
    (105, 4, "Monitor", 18000),
    (106, 2, "Headphones", 5000),
    (107, 5, "Tablet", 25000),
    (108, 3, "Webcam", 4000)
]

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    orders
)

payments = [
    (1, 101, "UPI", "Completed"),
    (2, 102, "Card", "Completed"),
    (3, 103, "UPI", "Completed"),
    (4, 104, "Card", "Pending"),
    (5, 105, "UPI", "Completed"),
    (6, 106, "Cash", "Completed"),
    (7, 107, "Card", "Completed"),
    (8, 108, "UPI", "Failed")
]

cursor.executemany(
    "INSERT INTO payments VALUES (?, ?, ?, ?)",
    payments
)

conn.commit()
"""
# ----------- Exercise 1 ----------
query = """
SELECT *
FROM customers
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM orders
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM payments
"""
print(pd.read_sql_query(query, conn))

# ---------- Exercise 2 ---------
query = """
SELECT
    customers.customer_name,
    orders.product,
    orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT
    customers.customer_name,
    customers.city,
    orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
ORDER BY amount DESC;
"""

print(pd.read_sql_query(query, conn))

# ------------ Exercise 3 ------------
query = """
SELECT
    customers.customer_name,
    customers.city,
    orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
WHERE city = "Chennai" and amount > 10000
"""
print(pd.read_sql_query(query, conn))

# ------------ Exercise 4 -----------
query = """
SELECT
    customers.city,
    SUM(orders.amount) AS total_sales
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.city
ORDER BY total_sales DESC;
"""

print(pd.read_sql_query(query, conn))
