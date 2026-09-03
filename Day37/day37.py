"""
Mission Day 37
Topic: Combining Pandas DataFrames

Concepts Learned:
- concat()
- merge()
- join()
- inner merge
- left merge
- right merge
- outer merge
- axis
- Combining multiple datasets
"""

import pandas as pd

# --------- Exercise 1 ----------
df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Marks": [75, 85]
})

combined = pd.concat([df1, df2])
print(combined)

combined = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(combined)

# ---------- Exercise 2 --------

names = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi"]
})

marks = pd.DataFrame({
    "Python": [85, 72, 91]
})

result = pd.concat(
    [names, marks],
    axis=1
)

print(result)

# ---------- Exercise 3 ---------
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE"]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Python": [85, 72, 91, 65, 88],
    "Math": [78, 88, 95, 70, 90]
})

attendance = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Attendance": [92, 85, 96, 78]
})


result = pd.merge(
    students,
    marks,
    on="Student_ID"
)

print(result)

# ---------- Exercise 4 ----------
result = pd.merge(
    students,
    attendance,
    on="Student_ID",
    how="inner"
)

print(result)

# --------- Exercise 5 ----------
result = pd.merge(
    students,
    attendance,
    on="Student_ID",
    how="left"
)

print(result)

# ----------- Exercise 6 ----------
result = pd.merge(
    students,
    attendance,
    on="Student_ID",
    how="right"
)

print(result)

print("\nMission Day 37 Completed Successfully!")