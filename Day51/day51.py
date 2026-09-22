import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": [
        "E01","E02","E03","E04","E05",
        "E06","E07","E08","E09","E10",
        "E11","E12","E13","E14","E15",
        "E16","E17","E18","E19","E20"
    ],

    "Department": [
        "IT","HR","Finance","IT","Marketing",
        "Finance","IT","HR","Marketing","IT",
        "Finance","HR","IT","Marketing","Finance",
        "HR","IT","Finance","Marketing","HR"
    ],

    "Experience_Years": [
        1,3,5,2,4,
        7,1,6,3,8,
        5,2,4,7,6,
        3,9,2,5,4
    ],

    "Monthly_Salary": [
        35000,48000,65000,40000,52000,
        78000,37000,62000,50000,85000,
        70000,45000,55000,80000,72000,
        50000,90000,42000,68000,56000
    ],

    "Performance_Score": [
        62,75,88,68,79,
        91,65,84,77,95,
        89,72,81,92,87,
        74,96,70,90,82
    ],

    "Projects_Completed": [
        2,4,6,3,5,
        8,2,7,4,9,
        6,3,5,8,7,
        4,10,3,6,5
    ]
}

df = pd.DataFrame(data)

# ------------ Exercise 1 -----------
print(df.shape)
print(df.dtypes)
print(df.describe())
print(df["Department"].value_counts())

"""
Dataset contains 20 rows and 6 columns.
Each row represents a Employee.
Salary has general positive relation with experience.
Experience has mean of 4.35 and min experience 1 year and max is 9 years
There are 4 different departments in the dataset.
"""

# ------------- Exercise 2 -----------
department_summary = df.groupby("Department").agg({
    "Monthly_Salary": "mean",
    "Performance_Score": "mean",
    "Projects_Completed": "mean",
    "Experience_Years": "mean"
})

print(department_summary)

"""
Finance dept has highest average salary, It is also highest in performance.
Finance dept has 6 project it is the dept with max projects.
Finance has highest average Experience.
Finance department is in lead amoung all four categories.
"""

# ------------- Exercise 3 ----------
plt.bar(df["Department"].unique(), df.groupby("Department")["Performance_Score"].mean())
plt.title("Department vs Average Performance Score")
plt.xlabel("Department")
plt.ylabel("Performance Score")
plt.grid(axis="y")
plt.show()

# ------------- Exercise 4 ----------
it = df[df["Department"] == "IT"]

plt.scatter(
    it["Experience_Years"],
    it["Monthly_Salary"]
)

plt.title("IT - Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.grid(True)
plt.show()

hr = df[df["Department"] == "HR"]

plt.scatter(
    hr["Experience_Years"],
    hr["Monthly_Salary"]
)

plt.title("HR - Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.grid(True)
plt.show()

finance = df[df["Department"] == "Finance"]

plt.scatter(
    finance["Experience_Years"],
    finance["Monthly_Salary"]
)

plt.title("Finance - Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.grid(True)
plt.show()

marketing = df[df["Department"] == "Marketing"]

plt.scatter(
    marketing["Experience_Years"],
    marketing["Monthly_Salary"]
)

plt.title("Marketing - Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.grid(True)
plt.show()

# -------------- Exercise 5 -------------
plt.scatter(
    df["Projects_Completed"],
    df["Performance_Score"]
)

plt.xlabel("Projects Completed")
plt.ylabel("Performance Score")
plt.title("Projects vs Performance")
plt.grid(True)
plt.show()

print(df.sort_values("Projects_Completed"))

print(df.sort_values("Projects_Completed"))

"""
In gereral the employees with more projects has higher performance.
Projects and Performance has genaral positive relation.
There are also some expections.
for some employees there is difference in pattern
"""

# ------------ Exercise 6 -----------
level = ["Low", "Medium", "High"]
level_range = [0,70,85,100]

df["Performance_Level"] = pd.cut(df["Performance_Score"], bins=level_range,
                                 labels=level)
print(df[["Employee", "Performance_Score", "Performance_Level"]])
print(df["Performance_Level"].value_counts())