"""
Mission Day 33
Topic: Pandas Missing Data

Concepts Learned:
- NaN
- isna()
- isnull()
- notna()
- dropna()
- fillna()
- Mean imputation
- Median imputation
- Missing-value analysis
"""
import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya", "Rahul", "Anu", "Vikram"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE", "CSE", "EEE"],
    "Python": [85, 72, np.nan, 65, 88, 55, 96, np.nan],
    "Math": [78, np.nan, 95, 70, 90, 62, np.nan, 81],
    "Physics": [90, 76, 89, np.nan, 94, 58, 98, 79]
})

print(students)

# ---------- Exercise 1 ---------
print(students.isna())
print(students.isna().sum())
print(students.isnull())

# -------- Exercise 2 ---------
print(students[students.isna().any(axis=1)])
print(students[students.notna().all(axis=1)])

# -------- Exercise 3 --------
print(students["Python"].isna().sum())
print(students["Math"].isna().sum())
print(students["Physics"].isna().sum())
print((students[["Python", "Math", "Physics"]].isna().sum()).sum())

# -------- Exercise 4 --------
clean_students = students.dropna()
print(clean_students)
print(students.dropna(subset=["Python"]))

# --------- Exercise 5 ---------
print(students["Python"].fillna(0))
print(students["Math"].fillna(0))
print(students["Physics"].fillna(0))
print(students.fillna(0))

# -------- Exercise 6 ----------
avg_python = students["Python"].mean()
avg_math = students["Math"].mean()
avg_phy = students["Physics"].mean()
print(students["Python"].fillna(avg_python))
print(students["Math"].fillna(avg_math))
print(students["Physics"].fillna(avg_phy))

# --------- Exercise 7 ----------
print(students["Python"].fillna(students["Python"].median()))
print(students["Math"].fillna(students["Math"].median()))
print(students["Physics"].fillna(students["Physics"].median()))

# ---------- Exercise 8 --------
print(students[students["Python"].notna()])
print(students[students["Math"].notna()])
print(students[students["Physics"].notna()])
print(students[(students["Python"].notna()) & 
               (students["Math"].notna())])

# -------- Exercise 9 ---------
print(students[["Python", "Math", "Physics"]].isna().sum())
print(students[["Python", "Math", "Physics"]].isna().mean() * 100)

# -------- Exercise 10 ---------
cleaned = students.copy()
cleaned["Python"] = cleaned["Python"].fillna(cleaned["Python"].mean())
cleaned["Math"] = cleaned["Math"].fillna(cleaned["Math"].mean())
cleaned["Physics"] = cleaned["Physics"].fillna(cleaned["Physics"].mean())
print(cleaned.isna().sum())

print("\nMission Day 33 Completed Successfully!")