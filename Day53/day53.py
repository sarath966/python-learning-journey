import sqlite3
import pandas as pd

df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.db")

df.to_sql("passengers", conn, if_exists="replace", index=False)

print("Database created successfully")

# ---------- Exercise 1 ----------
query = """
SELECT *
FROM passengers
LIMIT 5;
"""

print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
LIMIT 10;
"""

print(pd.read_sql_query(query, conn))

query = """
SELECT Name, SEX, AGE
FROM passengers;
"""

print(pd.read_sql_query(query, conn))

query = """
SELECT PASSENGERID, SURVIVED, PCLASS
FROM passengers;
"""

print(pd.read_sql_query(query, conn))

# ------------ Exercise 2 -------------
query = """
SELECT *
FROM passengers
WHERE SURVIVED = 1;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE SURVIVED = 0;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE Pclass = 1;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE Age > 50;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE Fare > 100;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE sex = "female";
"""
print(pd.read_sql_query(query, conn))

# ------------ Exercise 3 ------------
query = """
SELECT *
FROM passengers
WHERE Sex = "female"
and Survived = 1;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT *
FROM passengers
WHERE Pclass = 1
or Pclass = 2;
"""
print(pd.read_sql_query(query, conn))

# ------------ Exercise 4 ------------
query = """
SELECT Name, Age
FROM passengers
ORDER BY Age DESC
LIMIT 10;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT Name, Age
FROM passengers
WHERE Age IS NOT NULL
ORDER BY Age ASC
LIMIT 10;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT Name, Fare
FROM passengers
ORDER BY Fare DESC
LIMIT 10;
"""
print(pd.read_sql_query(query, conn))

# ------------ Exercise 5 -----------
query = """
SELECT COUNT(Name)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT AVG(Age)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT MIN(Age)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT Max(Age)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT AVG(Fare)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT SUM(Fare)
FROM passengers;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT COUNT(Survived)
FROM passengers
WHERE Survived = 1;
"""
print(pd.read_sql_query(query,conn))

# ------------ Exercise 6 -----------
query = """
SELECT Sex, COUNT(NAME) AS passenger_count
FROM passengers
GROUP BY Sex;
"""
print(pd.read_sql_query(query, conn))

query = """
SELECT Survived, COUNT(Survived) AS count
FROM passengers
GROUP BY Survived;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT Pclass, AVG(Age) AS Average_age
FROM passengers
GROUP BY Pclass; 
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT Sex,AVG(Fare) AS Average_Fare
FROM passengers
GROUP BY Sex;
"""
print(pd.read_sql_query(query,conn))

# ------------ Exercise 7 -----------
query = """
SELECT Sex, COUNT(*) AS survived_count
FROM passengers
WHERE Survived = 1
GROUP BY Sex;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT Pclass, COUNT(Name) AS passengers_count
FROM passengers
WHERE Sex = "female"
GROUP BY Pclass;
"""
print(pd.read_sql_query(query,conn))

# ------------ Exercise 8 ----------
query = """
SELECT Pclass, COUNT(*) AS passenger_count
FROM passengers
GROUP BY Pclass
HAVING COUNT(*) > 100;
"""
print(pd.read_sql_query(query,conn))

query = """
SELECT Pclass, AVG(Fare) AS Average_fare
FROM passengers
GROUP BY Pclass
HAVING AVG(Fare) > 50;
"""
print(pd.read_sql_query(query,conn))

# ------------ Exercise 9 ---------
query = """
SELECT
    CASE
        WHEN Age < 13 THEN 'Child'
        WHEN Age < 18 THEN 'Teenager'
        ELSE 'Adult'
    END AS Age_Group,
    COUNT(Name) AS passenger_count
FROM passengers
GROUP BY Age_Group;
"""
print(pd.read_sql_query(query,conn))

# ----------- Exercise 10 ---------
# Which passenger class had highest number of survivors
query = """
SELECT Pclass, COUNT(*) AS Survivors
FROM passengers
WHERE Survived = 1
GROUP BY Pclass
ORDER BY Survivors DESC;
"""
print(pd.read_sql_query(query, conn))

"""
Class 3 has highest survivors.
Class 1 has lowest survivors.
"""