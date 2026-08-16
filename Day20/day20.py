"""
Mission Day 20
Topic: Introduction to NumPy

Concepts Learned:
- NumPy arrays
- Array creation
- Array operations
- Indexing
- Slicing
- ndim
- shape
- dtype
- 2D arrays
"""
import numpy as np
# --------- Exercise 1 ---------
arr_1 = np.array([10, 20, 30, 40, 50])
arr_2 = np.array([1, 2, 3, 4, 5])
print(arr_1)
print(arr_2)

# --------- Exercise 2 ---------
a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])
print("a + b = ",a + b)
print("a - b = ",a - b)
print("a * b = ",a * b)
print("a / b = ",a / b)

# --------- Exercise 3 ---------
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])
print(numbers[-1])
print(numbers[1])
print(numbers[:3])
print(numbers[-2:])

# --------- Exercise 4 ---------
print(numbers.ndim)
print(numbers.shape)
print(numbers.dtype)

# --------- Exercise 5 ---------
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix[0,1])
print(matrix[1,1])
print(matrix[0])
print(matrix[1])
print(matrix[0:,0])

# ----------- MINI CHALLENGE -------
temperatures = np.array([32, 35, 31, 36, 38, 34, 30])
avg_temp = np.mean(temperatures)
print("Average Temperature: ",avg_temp)
print("Maximum Temp: ",np.max(temperatures))
print("Minimum Temp: ",np.min(temperatures))
print("Days above 34: ",np.sum(temperatures > 34))

print("\nMission Day 20 Completed Successfully!")