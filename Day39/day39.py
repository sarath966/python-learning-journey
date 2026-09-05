"""
Mission Day 39
Topic: Pandas Revision and Data Analysis

Concepts:
- DataFrame
- mean()
- axis
- Boolean filtering
- groupby()
- sort_values()
- idxmax()
- value_counts()
- apply()
"""
import pandas as pd

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya",
             "Anu", "Rahul", "Sneha"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE",
                   "ECE", "EEE", "CSE"],
    "Python": [85, 72, 91, 65, 88, 76, 55, 95],
    "Math": [78, 88, 95, 70, 90, 82, 60, 92],
    "Physics": [90, 76, 89, 68, 94, 79, 58, 96],
    "Attendance": [92, 85, 96, 78, 94, 88, 72, 97]
})

print(students)

# ------------ Exercise 1 -----------
students["Average"] = students[["Python", "Math", "Physics"]].mean(axis=1)
print(students[["Name", "Python", "Math", "Physics", "Average"]])

# ------------ Exercise 2 ------------
students["Result"] = students["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)
print(students)

# ------------ Exercise 3 -----------
print(students[(students["Average"]>= 80) &
                (students["Attendance"] >= 85)][["Name", "Department", "Average", "Attendance"]])

# ----------- Exercise 4 -----------
print(students.groupby("Department")[
    ["Python", "Math", "Physics"]
].mean())

# ----------- Exercise 5 ----------
print(students.sort_values("Average",ascending=False)[
    ["Name", "Department", "Average"]])

# ----------- Exercise 6 ----------
print(students["Python"].max())
print(students["Average"].max())
print(students["Average"].mean())
print(students[students["Attendance"] < 80])
print(students["Department"].value_counts())
print(students.groupby("Department")["Attendance"].mean())

print("\nMission Day 39 Completed Successfully!")