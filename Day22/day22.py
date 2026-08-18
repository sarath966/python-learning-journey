"""
Mission Day 22
Topic: NumPy 2D Arrays and Axis

Concepts Learned:
- 2D arrays
- Row and column indexing
- Slicing
- axis=0
- axis=1
- Row-wise calculations
- Column-wise calculations
"""
import numpy as np
# -------- Exercise 1 -------
marks = np.array([
    [80, 75, 90],
    [85, 92, 78],
    [70, 88, 95]
])
print(marks[0])
print(marks[1])
print(marks[:, 0])
print(marks[:, 2])
print(marks[1][1])
print(marks[2][2])

# -------- Exercise 2 -------
print(marks[:2,:])
print(marks[:,:2])
print(marks[0:2,1:])

# -------- Exercise 3 -------
print(np.mean(marks, axis=0))
print(np.mean(marks, axis=1))

# -------- Exercise 4 -------
print(np.sum(marks, axis=1))
print(np.sum(marks, axis=0))

# -------- Exercise 5 -------
print(np.max(marks, axis=0))
print(np.max(marks, axis=1))

# ------- DATA SCIENCE CHALLENGE --------
marks = np.array([
    [85, 72, 91],
    [65, 88, 79],
    [92, 95, 89],
    [70, 68, 75],
    [88, 90, 94]
])
print("Average marks for every student: ",np.mean(marks,axis=1))
print("Average marks for every subject: ",np.mean(marks,axis=0))
print("Total marks for every student: ",np.sum(marks,axis=1))
print("Total marks for every subject: ",np.sum(marks,axis=0))
print("Highest mark in each subject: ",np.max(marks,axis=0))
students_80 = (np.mean(marks,axis=1)) >= 80
print("Student(s) whose average is at least 80: ",np.sum(students_80))

print("\nMission Day 22 Completed Successfully!")