"""
Mission Day 36
Topic: Pandas GroupBy and Aggregation

Concepts Learned:
- groupby()
- mean()
- max()
- min()
- count()
- agg()
- Grouping by multiple columns
- Group + filter
- Group + sort
"""

import pandas as pd

students = pd.DataFrame({
    "Name": [
        "Sarath", "Ravi", "Abhi", "Kiran",
        "Priya", "Rahul", "Anu", "Vikram",
        "Neha", "Arjun", "Meena", "Rohan"
    ],
    "Department": [
        "CSE", "ECE", "CSE", "EEE",
        "CSE", "ECE", "CSE", "EEE",
        "ECE", "CSE", "EEE", "ECE"
    ],
    "Year": [
        2, 2, 2, 2, 3, 3, 2, 3, 3, 2, 3, 2
    ],
    "Python": [
        85, 72, 91, 65, 88, 55, 96, 74, 81, 93, 69, 77
    ],
    "Math": [
        78, 88, 95, 70, 90, 62, 92, 81, 85, 89, 73, 80
    ],
    "Physics": [
        90, 76, 89, 68, 94, 58, 98, 79, 87, 91, 71, 83
    ]
})

print(students)
# ----------- Exercise 1 -----------
print(students.groupby("Department")["Python"].mean())
print(students.groupby("Department")["Math"].mean())
print(students.groupby("Department")["Physics"].mean())

# ----------- Exercise 2 -----------
print(students.groupby("Department")["Python"].agg(["mean", "max", "min"
                                                    , "count"]))

# ----------- Exercise 3 -----------
print(students.groupby("Department")[["Python", "Math", "Physics"]]
      .agg(["mean", "max", "min"]))


# ----------- Exercise 4 ----------
print(students.groupby("Department").agg({
    "Python" : "mean",
    "Math" : "max",
    "Physics" : "min"
}))

# ---------- Exercise 5 ----------
print(students.groupby("Department")["Name"].count())
print(students["Department"].value_counts())

# ------------ Exercise 6 --------
print(students.groupby(["Department", "Year"])["Python"].mean())

# ----------- Exercise 7 ----------
print(students.groupby(["Department", "Year"])[
    ["Python", "Math", "Physics"]].mean())

# ----------- Exercise 8 ----------
dept_avg = students.groupby("Department")[
    ["Python", "Math", "Physics"]
].mean()
print(dept_avg)
print(dept_avg.sort_values(["Python"],ascending=False))

# ---------- Exercise 9 ---------
students["Average"] = students[
    ["Python", "Math", "Physics"]
].mean(axis=1)
print(students.groupby("Department")["Average"].mean())

# ---------- Exercise 10 ----------
students_above_80 = (students["Python"] >= 80)
print(students[students_above_80].groupby("Department").count())

# ---------- Exercise 11 ---------
cleaned = students.groupby("Department").agg({
    "Python" : "mean",
    "Math" : "mean",
    "Physics" : "mean"
})
print(cleaned)

print("\nMission Day 36 Completed Successfully!")