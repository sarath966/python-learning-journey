"""
Mission Day 30
Topic: Pandas Filtering and Data Selection

Concepts Learned:
- Boolean filtering
- Multiple conditions
- AND / OR
- loc()
- isin()
- between()
- query()
- Conditional data selection
"""
import pandas as pd

# ------- DATA ------
students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya", "Rahul", "Anu", "Vikram"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE", "CSE", "EEE"],
    "Python": [85, 72, 91, 65, 88, 55, 96, 74],
    "Math": [78, 88, 95, 70, 90, 62, 92, 81],
    "Physics": [90, 76, 89, 68, 94, 58, 98, 79]
})

print(students)

# ----------- Exercise 1 --------
print(students[students["Python"] >= 80])
print(students[students["Math"] < 70])
print(students[students["Physics"] >= 90])
print(students[students["Python"].between(70,90)])

# --------- Exercise 2 ----------
top_students_python_math = (students["Python"] >= 80) & (students["Math"] >= 80)
print(students[top_students_python_math])

top_python_or_phy = (students["Python"] >= 90) | (students["Physics"] >= 90)
print(students[top_python_or_phy])

top_students_math_phy = (students["Math"] >= 80) & (students["Physics"] >= 80)
print(students[top_students_math_phy])

# ---------- Exercise 3 --------
print(students[students["Department"] == "CSE"])
print(students[students["Department"] == "ECE"])
print(students[students["Department"] == "EEE"])

print(students[(students["Department"] == "CSE") &
                (students["Python"] >= 85)])

# ---------- Exercise 4 --------
print(students[students["Department"].isin(["CSE", "EEE"])])
print(students[students["Department"].isin(["ECE", "EEE"])])

# ---------- Exercise 5 --------
print(students.loc[students["Math"] >= 85,
    ["Name", "Math"]])

print(students.loc[students["Department"] == "CSE",
      ["Name", "Department", "Python"]])

print(students.loc[students["Physics"] >= 90,
    ["Name", "Physics"]])

# ---------- Exercise 6 --------
print(students.query("Python >= 80"))
print(students.query("Math >= 80 & Physics >= 80"))
print(students.query("Department == 'CSE'"))


# ------- MAIN CHALLENGE --------
high_performers = ((students["Python"] >= 80) 
                   & (students["Math"] >= 80)) & (students["Physics"] >= 80)
print(students.loc[high_performers,
                   ["Name", "Department"]])

students_below_60 = ((students["Python"] < 60)|
                      (students["Math"] < 60)) | (students["Physics"] < 60)
print(students.loc[students_below_60,
                   ["Name", "Department", "Python", "Math", "Physics"]])

top_student_cse = ((students["Python"] >= 80) &
                    (students["Math"] >= 80)) & (students["Department"] == "CSE")
print(students.loc[top_student_cse,
                   ["Name", "Python", "Math"]])

top_cse_eee = (students["Department"].isin(["CSE", "EEE"])) & (
    students["Physics"] >= 80
)
print(students.loc[top_cse_eee,
                   ["Name", "Department", "Physics"]])

python_70_90 = students["Python"].between(70,90)
print(students.loc[python_70_90,
                   ["Name", "Python"]])

qualifing_students = ((students["Department"].isin(["CSE", "ECE"])) &
                      ((students["Python"] >= 75) & (students["Math"] >= 80)))
print(students.loc[qualifing_students,
                   ["Name", "Department", "Python", "Math"]])

print("\nMission Day 30 Completed Successfully!")