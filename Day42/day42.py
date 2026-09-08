"""
Mission Day 42
Topic: Pandas Real CSV Mini Project

Concepts:
- read_csv()
- Missing values
- isna()
- fillna()
- mean()
- Boolean filtering
- groupby()
- idxmax()
- loc
- to_csv()
"""
import pandas as pd

students = pd.read_csv(r"C:\Users\asara\Desktop\Datascience_per\python_learning-journey\Day42\students.csv")

# ------------ Exercise 1 ----------
print(students.head())
print(students.shape)
students.info()
print(students.describe())

# ----------- Exercise 2 ------------
print(students.isna().sum())
students["Math"] = students["Math"].fillna(
    students["Math"].mean()
)

students["Physics"] = students["Physics"].fillna(
    students["Physics"].mean()
)
print(students.isna().sum())

# ----------- Exercise 3 ---------
students["Average"] = students[
    ["Python", "Math", "Physics"]
].mean(axis=1)

students["Result"] = students["Average"].apply(
    lambda x: "Pass" if x >=50 else "Fail"
)
print(students)

# ---------- Exercise 4 ----------
avg_python = students.groupby("Department")["Python"].mean()
avg_dept = students.groupby("Department")["Average"].mean()
avg_attendance = students.groupby("Department")["Attendance"].mean()
department_report = pd.DataFrame({
    "Average_Python" : avg_python,
    "Average_Department" : avg_dept,
    "student_count" : students["Department"].value_counts(),
    "Average_Attendance" : avg_attendance

})
print(department_report)

# ----------- Exercise 5 --------
top_student = students.loc[students["Average"].idxmax()]
print(top_student)
print(students["Python"].max())
print(students["Math"].max())
print(students["Physics"].max())
print(students["Average"].mean())

print("\nDay 42 completed")