"""
Mission Day 23
Topic: NumPy Conditional Operations and Data Cleaning

Concepts Learned:
- np.where()
- np.unique()
- Boolean masking
- Conditional replacement
- Basic data cleaning
"""
import numpy as np
# --------- Exercise 1 --------
marks = np.array([45, 72, 91, 38, 85, 67, 29])
result = np.where(marks >= 50,"Pass","Fail")
print(result)

# --------- Exercise 2 --------
marks = np.array([45, 72, 91, 38, 85, 67, 29])
performance = np.where(marks >= 80,"Excellent","Needs Improvement")
print(performance)

# --------- Exercise 3 --------
cities = np.array([
    "Vijayawada",
    "Guntur",
    "Vijayawada",
    "Hyderabad",
    "Guntur",
    "Chennai"
])
uni_cities = np.unique(cities)
print(uni_cities)
print(len(uni_cities))

# --------- Exercise 4 --------
prices = np.array([100, 250, 80, 400, 150, 120])
print(np.where(prices < 150,prices * 1.10,prices))

# --------- MINI DATA SCIENCE CHALLENGE --------
prices = np.array([500, 1200, -1, 800, 1500, -1, 700])
valid_prices = prices[prices >= 0]
mean_valid = np.mean(valid_prices)
prices = np.where(prices <= 0,mean_valid,prices)
print(prices)
print(np.mean(prices))

print("\nMission Day 23 Completed Successfully!")