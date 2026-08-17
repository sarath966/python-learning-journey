"""
Mission Day 21
Topic: NumPy Statistics and Boolean Indexing

Concepts Learned:
- NumPy statistical functions
- Boolean arrays
- Boolean indexing
- Vectorization
- reshape()
- Numerical data filtering
"""
import numpy as np
# ---------- Exercise 1 ---------
marks = np.array([72, 85, 91, 68, 79, 95, 88])
print("Total = ",np.sum(marks))
print("Average = ",np.mean(marks))
print("Median = ",np.median(marks))
print("Highest = ",np.max(marks))
print("Lowest = ",np.min(marks))
print("Standard deviation = ",np.std(marks))

# ---------- Exercise 2 ---------
marks = np.array([45, 67, 82, 91, 38, 76, 55, 29])
Passing_marks = marks[marks >= 50]
high_marks = marks[marks >= 80]
marks_below_50 = marks[marks < 50]
print(Passing_marks)
print(high_marks)
print(marks_below_50)

# ---------- Exercise 3 ---------
print("Number of students passed: ",np.sum(marks >= 50))
print("Number of students scored 80+ : ",np.sum(marks >= 80))

# ---------- Exercise 4 ---------
prices = np.array([100, 200, 300, 400, 500])
print("prices after adding 50: ",prices + 50)
print("prices after 10% increase: ",prices + (prices*0.1))
print("prices after Rs20 discount: ",prices - 20)
print("Double price:",prices*2)

# ---------- Exercise 5 ---------
numbers = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])
print(numbers)
numbers = numbers.reshape(3, 4)
print(numbers)

print("\nMission Day 21 Completed Successfully!")