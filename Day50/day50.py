import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": [
        "E01", "E02", "E03", "E04", "E05",
        "E06", "E07", "E08", "E09", "E10",
        "E11", "E12", "E13", "E14", "E15",
        "E16", "E17", "E18", "E19", "E20"
    ],

    "Department": [
        "IT", "HR", "Finance", "IT", "Marketing",
        "Finance", "IT", "HR", "Marketing", "IT",
        "Finance", "HR", "IT", "Marketing", "Finance",
        "HR", "IT", "Finance", "Marketing", "HR"
    ],

    "Experience_Years": [
        1, 3, 5, 2, 4,
        7, 1, 6, 3, 8,
        5, 2, 4, 7, 6,
        3, 9, 2, 5, 4
    ],

    "Monthly_Salary": [
        35000, 48000, 65000, 40000, 52000,
        78000, 37000, 62000, 50000, 85000,
        70000, 45000, 55000, 80000, 72000,
        50000, 90000, 42000, 68000, 56000
    ],

    "Performance_Score": [
        62, 75, 88, 68, 79,
        91, 65, 84, 77, 95,
        89, 72, 81, 92, 87,
        74, 96, 70, 90, 82
    ],

    "Projects_Completed": [
        2, 4, 6, 3, 5,
        8, 2, 7, 4, 9,
        6, 3, 5, 8, 7,
        4, 10, 3, 6, 5
    ]
}

df = pd.DataFrame(data)

# --------------- Exercise 1 -------------
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df["Department"].unique())
"""
The dataset contains 20 rows and 6 columns.
Each row contains the details of a employee.
It contains 4 different departments["IT", "HR", "Finance", "Marketing"]
Salary range : 35000 - 90000
Experience range : 1 - 9 years
Performance score : 62 - 96
"""

# --------------- Exercise 2 -------------
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Department"].value_counts())

"""
No missing value is present in the dataset hence no need to replace any value.
No duplicate row.
Employees in each dept : {
"IT" : 6
"HR" : 5
"Finance" : 5
"Marketing" : 4 
}
The dataset is completely fine, No need of any data cleaning.
"""

# -------------- Exercise 3 -----------
print(df.groupby("Department")["Monthly_Salary"].mean())
print(df.groupby("Department")["Performance_Score"].mean())
print(df.groupby("Department")["Experience_Years"].mean())
department_summary = df.groupby("Department").agg({
    "Monthly_Salary": "mean",
    "Performance_Score": "mean",
    "Experience_Years": "mean"
})

print(department_summary)
"""
Finance department has the highest average monthly salary and performance.
HR has the lowest average salary and lower average experience compared
with the other departments.
IT has a higher average experience than HR and Marketing.
"""

plt.bar(df["Department"].unique(), df.groupby("Department")["Monthly_Salary"].mean())
plt.title("Department vs Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# -------------- Exercise 4 -----------
plt.scatter(df["Experience_Years"], df["Monthly_Salary"])
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.title("Experience vs Monthly Salary")
plt.grid(True)
plt.show()
"""
The dataset shows a general positive association between Exprience vs 
Monthly salary.
Also there are some exceptions.
"""

# -------------- Exercise 5 -----------
plt.scatter(df["Projects_Completed"], df["Performance_Score"])
plt.xlabel("Projects Completed")
plt.ylabel("Performance Score")
plt.title("Projects Completed vs Performance")
plt.grid(True)
plt.show()
"""
There is a general positive association between projects completed
and performance score.
Employees who completed more projects generally have higher
performance scores, although there are some exceptions.
"""

# -------------- Exercise 6 -----------
df = df.sort_values("Performance_Score", ascending=False)
top5_employees = df.head()
print(top5_employees)

"""
1. Highest performance score:
The highest performance score is 96.

2. What department appears among the high performers:
The top 5 employees include employees from IT, Finance, and Marketing.

3. Do the top performers all have the most experience:
No. The top performers have different levels of experience.

4. Do the top performers all have the highest salaries:
No. The top performers do not all have the highest salaries.
"""

# -------------- Exercise 7 -----------
print(df.describe())
# -------------- Exercise 7 -----------

plt.scatter(df["Experience_Years"], df["Performance_Score"])
plt.xlabel("Experience Years")
plt.ylabel("Performance Score")
plt.title("Experience vs Performance")
plt.grid(True)
plt.show()

"""
Why I chose this analysis:
I chose to investigate the relationship between experience
and performance because experience may be related to how
employees perform.

Observations:
1. There is a general positive association between experience
   and performance score.
2. Employees with higher experience generally have higher
   performance scores.
3. There are some exceptions where employees with lower
   experience also have relatively high performance scores.
"""
# -------------- Exercise 8 -----------
# -------------- EDA FINDINGS ----------

# 1. Dataset overview:
# The dataset contains 20 Employees and 6 columns.
# It includes Employee details, department, etc.

# 2. Data quality:
# The dataset has no missing values and no duplicate rows,
# so no data cleaning is required for these issues.

# 3. Department pattern:
# IT has the highest number of employees, followed by HR, Finance
# and Marketing.

# 4. Salary pattern:
# There is a general positive association between experience
# and monthly salary. Employees with more experience generally
# have higher salaries, although there are some exceptions.

# 5. Performance pattern:
# There is a general positive association between Performance
# and projects, although there are some exceptions.

# 6. Most interesting observation:
# Experience generally shows a positive association with salary
# and performance, but individual employees do not always follow
# the overall pattern.

# 7. Further question I would investigate:
# I would investigate whether the relationship between experience
# and salary remains similar across different departments.