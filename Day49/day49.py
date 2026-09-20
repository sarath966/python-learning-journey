import pandas as pd
import matplotlib.pyplot as plt

# ---------- DATA ---------
data = {
    "Student": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O"
    ],
    "Department": [
        "CSE", "CSE", "ECE", "ECE", "EEE",
        "CSE", "EEE", "ECE", "CSE", "EEE",
        "CSE", "ECE", "EEE", "CSE", "ECE"
    ],
    "Study_Hours": [
        5, 7, 3, 6, 8,
        4, 2, 7, 9, 3,
        6, 5, 4, 8, 2
    ],
    "Attendance": [
        85, 92, 70, 88, 95,
        78, 65, 90, 96, 72,
        84, 87, 75, 94, 68
    ],
    "Assignments": [
        8, 9, 6, 8, 10,
        7, 5, 9, 10, 6,
        8, 9, 7, 10, 5
    ],
    "Marks": [
        72, 85, 55, 78, 91,
        65, 48, 82, 94, 58,
        75, 80, 62, 89, 51
    ]
}

df = pd.DataFrame(data)

# ------------ Exercise 1 --------------
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
"""
No of rows - 15
No of columns - 6
Columns with numerical values - study hours, attendance, assignment, marks
department column is categorical
student column identifies student
"""

# ------------ Exercise 2 ------------
print(df.describe())
print(df["Study_Hours"].mean())
print(df["Study_Hours"].median())
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Attendance"].mean())

"""
Average of study hours - 5.2666
Median of study hours - 5.0
Average marks - 72.333
Median marks - 75.0
Average attendance - 82.6
Average mark is lower than median mark
"""

# ------------ Exercise 3 ----------
print(df.isnull().sum())
print(df.isnull().sum().sum())
"""
No missing values
No need of missing-value clean up
"""

# ------------ Exercise 4 ----------
print(df.duplicated().sum())
print(df[df.duplicated()])
"""
No duplicate row
Doesn't need any row to removed
"""

# ----------- Exercise 5 -----------
print(df["Department"].value_counts())
print(df["Department"].value_counts(normalize=True) * 100)

"""
Students in each dept : CSE - 6, ECE - 5, EEE - 4;
Percentage of student by dept:
CSE - 40.000000
ECE - 33.333333
EEE - 26.666667
CSE has more student count
"""
df["Department"].value_counts().plot(kind="bar")

plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.grid(axis="y")
plt.show()

# ------------ Exercise 6 ----------
print(df.groupby("Department")["Marks"].mean())
print(df.groupby("Department")["Study_Hours"].mean())
print(df.groupby("Department")["Attendance"].mean())

summary = df.groupby("Department").agg({
    "Marks": "mean",
    "Study_Hours": "mean",
    "Attendance": "mean"
})

print(summary)

# ------------ Exercise 7 -----------
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.show()

"""
The dataset shows a general positive association between study 
hours and marks, although there are some exceptions.
There are a few students who study fewer hours but still achieve
relatively good marks.
"""

# ------------ Exercise 8 ----------
plt.figure(figsize=(8, 5))

plt.scatter(df["Attendance"], df["Marks"])

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.grid(True)

plt.show()

"""
There is a general positive association between attendance and marks, 
although some students do not follow the overall pattern.
"""

# ----------- Exercise 9 -----------
plt.figure(figsize=(8, 5))

plt.hist(df["Marks"], bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y")

plt.show()

# EDA FINDINGS
# ------------

# 1. Dataset overview:
# The dataset contains 15 students and 6 columns.
# It includes student details, department, study hours,
# attendance, assignments, and marks.

# 2. Data quality:
# The dataset has no missing values and no duplicate rows,
# so no data cleaning is required for these issues.

# 3. Department pattern:
# CSE has the highest number of students, followed by ECE
# and EEE. The average marks, study hours, and attendance
# vary across the departments.

# 4. Study hours vs marks:
# There is a general positive association between study hours
# and marks, although some students do not follow the overall pattern.

# 5. Attendance vs marks:
# There is a general positive association between attendance
# and marks, although there are some exceptions.

# 6. Marks distribution:
# The marks are spread across a range of values, with most
# students having marks around the middle-to-higher range.

# 7. Most interesting observation:
# Study hours and attendance both show a general positive
# association with marks, but individual students do not
# always follow the overall pattern.