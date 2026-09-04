"""
Mission Day 38
Topic: Pandas Apply, Map and Derived Columns

Concepts Learned:
- apply()
- map()
- lambda
- Custom functions
- Derived columns
- DataFrame analysis
"""

import pandas as pd

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE"],
    "Python": [85, 72, 91, 65, 88],
    "Math": [78, 88, 95, 70, 90],
    "Physics": [90, 76, 89, 68, 94]
})

# ---------- Exercise 1 -----------
students["Average"] = students[["Python", "Math", "Physics"]].mean(axis=1)
print(students)

# ---------- Exercise 2 -----------
students["Result"] = students["Average"].apply(
    lambda x : "Pass" if x >= 50 else "Fail"
)

print(students[["Name", "Average", "Result"]])

# ---------- Exercise 3 ----------
def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

students["Grade"] = students["Average"].apply(grade)
print(students)

# ---------- Exercise 4 ----------
department_names = {
    "CSE": "Computer Science",
    "ECE": "Electronics",
    "EEE": "Electrical"
}
students["Department_Name"] = students["Department"].map(department_names)
print(students)

# ---------- Exercise 5 -----------
students_top80 = students[students["Average"] >= 80]
students_top80 = students_top80.sort_values("Average",ascending=False)
print(students_top80[["Name", "Department", "Average", "Grade"]])

# ----------- Exercise 6 ---------
print(students.sort_values("Average", ascending=False))
high_avg = students["Average"].max()
print(students[students["Average"] == high_avg])
print(students["Average"].mean())
print((students["Result"] == "Pass").sum())
print(students["Grade"].value_counts())

print("\nMission Day 38 Completed Successfully!")