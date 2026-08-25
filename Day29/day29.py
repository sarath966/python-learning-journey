"""
Mission Day 29
Topic: Introduction to Pandas

Concepts Learned:
- Pandas Series
- Pandas DataFrame
- DataFrame shape
- Columns and data types
- describe()
- loc
- iloc
- Column selection
- Boolean filtering
- Adding new columns
- Basic DataFrame analysis
"""
import pandas as pd
import numpy as np
# ------- Exercise 1 -------
marks = pd.Series([85, 92, 88],
                  index = ["Python", "Math", "Physics"])
print(marks)
print(marks["Python"])
print(marks["Physics"])
print("Average: ",np.mean(marks))

# ------- Exercise 2 -------
students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Python": [85, 72, 91, 65, 88],
    "Math": [78, 88, 95, 70, 90],
    "Physics": [90, 76, 89, 68, 94]
})

print(students)
print(students.shape)
print(students.columns)
print(students.dtypes)
print(students.describe())

# ------- Exercise 3 -------
print(students["Name"])
print(students["Physics"])
print(students[["Name", "Math"]])
print(students[["Python", "Math", "Physics"]])

# -------- Exercise 4 --------
print(students.iloc[0])
print(students.iloc[2])
print(students.iloc[:3])
print(students.loc[0,"Python"])
print(students.loc[2,"Math"])

# ------- MAIN CHALLENGE -----
students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya", "Rahul"],
    "Python": [85, 72, 91, 65, 55, 88],
    "Math": [78, 88, 95, 70, 62, 90],
    "Physics": [90, 76, 89, 68, 58, 94]
})
print(students.shape)
print(students.columns)
print(students.dtypes)

print(students[["Python", "Math", "Physics"]].mean())

top_mark_python = students["Python"].idxmax()
print(top_mark_python)
print(students["Name"][top_mark_python])

top_mark_math = students["Math"].idxmax()
print(top_mark_math)
print(students["Name"][top_mark_math])

top_marks_python = students[students["Python"] >= 80]
print(top_marks_python)

top_python_math = (students["Python"] >= 80) & (students["Math"] >= 80)
print(students[top_python_math])

average = students[["Python", "Math", "Physics"]].mean(axis=1)
print(average)

high_avg = average.idxmax()
print("index of Highest Average: ",high_avg)
print("Student with Highest average: ",students["Name"][high_avg])

performance = np.where(average >= 80, "Excellent",
                        np.where(average >= 70, "Good", "Need Improvement"))
print(performance)

students_final = pd.DataFrame({
    "Name" : students["Name"],
    "Python" : students["Python"],
    "Math" : students["Math"],
    "Physics" : students["Physics"],
    "Average" : average ,
    "performance" : performance
})
print(students_final)

print("\nMission Day 29 Completed Successfully!")