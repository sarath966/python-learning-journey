"""
Mission Day 32
Topic: Pandas GroupBy and Aggregation

Concepts Learned:
- groupby()
- mean()
- sum()
- max()
- min()
- count()
- agg()
- value_counts()
- Grouping and aggregation
- Grouping + filtering
- Grouping + sorting
"""
import pandas as pd
# ------ DATA -------
import pandas as pd

students = pd.DataFrame({
    "Name": [
        "Sarath", "Ravi", "Abhi", "Kiran",
        "Priya", "Rahul", "Anu", "Vikram",
        "Neha", "Arjun"
    ],
    "Department": [
        "CSE", "ECE", "CSE", "EEE",
        "CSE", "ECE", "CSE", "EEE",
        "ECE", "CSE"
    ],
    "Year": [
        2, 2, 2, 2,
        2, 2, 2, 2,
        2, 2
    ],
    "Python": [85, 72, 91, 65, 88, 55, 96, 74, 81, 93],
    "Math": [78, 88, 95, 70, 90, 62, 92, 81, 85, 89],
    "Physics": [90, 76, 89, 68, 94, 58, 98, 79, 87, 91]
})

print(students)

# --------- Exercise 1 ----------
print(students.groupby("Department")["Python"].mean())
print(students.groupby("Department")["Math"].mean())
print(students.groupby("Department")["Physics"].mean())
print(students.groupby("Department")["Python"].max())
print(students.groupby("Department")["Math"].min())

# --------- Exercise 2 ---------
print(students.groupby("Department")["Python"].agg(["mean", "max", "min", "count"]))
print(students.groupby("Department")["Math"].agg(["mean", "max", "min", "count"]))

# --------- Exercise 3 ----------
average = pd.DataFrame(
    students.groupby("Department")[["Python", "Math", "Physics"]].mean()
)
print(average)

max_marks = pd.DataFrame(
    students.groupby("Department")[["Python", "Math", "Physics"]].max()
)
print(max_marks)

# -------- Exercise 4 ---------
print(students["Department"].value_counts())
print(students["Department"][students["Python"] < 80].value_counts())

# -------- Exercise 5 --------
print(students.groupby("Department")[["Python", "Math", "Physics"]].mean())
print(students.groupby("Department").agg({
    "Python" : max,
    "Math" : min,
    "Physics" : max
}))

# --------- Exercise 6 -------
dept_avg = pd.DataFrame(
    students.groupby("Department")[
    ["Python", "Math", "Physics"]
].mean()
)
print(dept_avg.sort_values("Python", ascending=False))
print(dept_avg.sort_values("Math", ascending=False))
print(dept_avg.sort_values("Physics", ascending=False))

print("\nMission Day 32 Completed Successfully!")