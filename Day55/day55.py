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

# ---------- Exercise 1 ---------
quary = """
SELECT 
    order_id,
    product,
    amount
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
)
"""
print(pd.read_sql_query(quary, conn))

# ---------- Exercise 2 ---------
quary = """
SELECT 
    customers.customer_name,
    orders.product,
    orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
)
"""
print(pd.read_sql_query(quary, conn))

# ---------- Exercise 3 ---------
# ---------- Exercise 3 ---------
quary = """
SELECT
    customer_name,
    total_spent
FROM (
    SELECT
        customers.customer_name,
        SUM(orders.amount) AS total_spent
    FROM customers
    INNER JOIN orders
        ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_name
)
WHERE total_spent > (
    SELECT AVG(total_spent)
    FROM (
        SELECT
            SUM(amount) AS total_spent
        FROM orders
        GROUP BY customer_id
    )
);
"""

print(pd.read_sql_query(quary, conn))

# ----------- Exercise 4 ---------
quary = """
SELECT
    orders.order_id,
    customers.customer_name,
    orders.product,
    orders.amount
    FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id
WHERE amount = (
    SELECT MAX(amount)
    FROM orders    
)
"""
print(pd.read_sql_query(quary,conn))

# ----------- Exercise 5 ---------
# ----------- Exercise 5 ---------
quary = """
SELECT
    orders.order_id,
    customers.customer_name,
    orders.product,
    orders.amount
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id
WHERE orders.amount > (
    SELECT AVG(o2.amount)
    FROM orders AS o2
    WHERE o2.customer_id = orders.customer_id
);
"""

print(pd.read_sql_query(quary, conn))

# ----------- Exercise 6 ----------
quary = """
SELECT
    customers.customer_name,
    orders.order_id,
    orders.product,
    payments.payment_status
    FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN payments
    ON orders.order_id = payments.order_id
WHERE payment_status IS NOT "Completed"
"""
print(pd.read_sql_query(quary,conn))

# --------- Exercise 7 -----------
query = """
SELECT
    customers.customer_name,
    SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name
ORDER BY total_spent DESC;
"""

df = pd.read_sql_query(query, conn)

print(df)
print(df.head())
print(df.describe())
print(df["total_spent"].mean())
print(df["total_spent"].max())
print(df[df["total_spent"] > df["total_spent"].mean()])

# ---------- Exercise 8 -----------
quary = """
SELECT
    customers.customer_name,
    SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name
HAVING total_spent > (
    SELECT AVG(total_spent)
    FROM (
        SELECT
            SUM(amount) AS total_spent
        FROM orders
        GROUP BY customer_id
    )
);
"""

print(pd.read_sql_query(quary, conn))