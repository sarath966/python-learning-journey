"""
Mission Day 41
Topic: Pandas File Handling

Concepts:
- read_csv()
- head()
- tail()
- shape
- columns
- info()
- describe()
- Filtering CSV data
- to_csv()
- read_excel()
- to_excel()
"""

import pandas as pd

# ----------- Exercise 1 ---------
students = pd.read_csv("students.csv")

print(students)

# ----------- Exercise 2 ----------
print(students.head())
print(students.tail())
print(students.shape)
print(students.columns)
students.info()
print(students.describe())

# ----------- Exercise 3 -----------
print(students[students["Python"] >= 80][["Name", "Department", "Python"]])
print(students[students["Department"] == "CSE"])
print(students[(students["Python"] >= 80) &
                (students["Attendance"] >= 90)][
                    ["Name", "Department", "Python", "Attendance"]])

# ----------- Exercise 4 ----------
students["Average"] = students[
    ["Python", "Math", "Physics"]
].mean(axis=1)
print(students.iloc[students["Average"].idxmax()])
print(students["Average"].mean())
print(students.groupby("Department")["Python"].mean())
print(students.groupby("Department")["Average"].mean())
print(students["Department"].value_counts())

print("\nMission Day 41 Completed Successfully!")