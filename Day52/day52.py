import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# --------- Exercise 1 --------
print(df.shape)
print(df.head())
print(df.info())
print(df.dtypes)
print(df.describe())

print(df.isnull().sum())
print(df.duplicated().sum())

"""
The dataset contains 418 rows and 11 columns.
Column age and fare has missing values.
Age column has 86 missing values and fare has 1 missing value.
PassengerId, Survived, Pclass, age, SibSp, Parch, Fare has numeric values.
The min value in age is 0.17 and max is 76.
In survived column the data is in form of boolean.
"""

# --------- Exercise 2 --------
missing_percent = df.isnull().mean() * 100
print(missing_percent)

"""
Age column has max number of missing values.
Fare has only one missing value.
Age and fare columns need cleanup before analysis.
"""

# --------- Exercise 3 -------
print(df["Survived"].value_counts())
print(df["Survived"].value_counts(normalize=True) * 100)

plt.bar(df["Survived"].unique(), df["Survived"].value_counts(normalize=True) * 100)
plt.title("Percentage of Survived count")
plt.xticks(df["Survived"].unique(),["Not Survived", "Survived"])
plt.xlabel("Survived")
plt.ylabel("Percentage")
plt.grid(axis="y")
plt.show()

"""
The Survived percent is much lower then not survived.
"""

# ---------- Exercise 4 --------
gender_survival = df.groupby("Sex")["Survived"].mean()
print(gender_survival)

"""
The survival rate of female is 0.355 and male is 0.409.
Male has high survival rate.
The approximate difference is 0.05251
"""

# --------- Exercise 5 --------
class_survival = df.groupby("Pclass")["Survived"].mean()
print(class_survival)
plt.bar(df["Pclass"].unique(),class_survival)
plt.title("Survival grouped by Pclass")
plt.xticks(df["Pclass"].unique())
plt.xlabel("Survived")
plt.ylabel("Rate")
plt.show()

"""
Class 2 has highest survival rate.
class 1 has lowest.
"""

# --------- Exercise 6 --------
print(df["Age"].describe())
plt.hist(df["Age"].dropna(), bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.grid(True)

plt.show()
"""
The Average age of the passengers is 30.27.
Most of the passengers are in the range 20-30.
"""

# ---------- Exercise 7 --------
bins = [0, 12, 18, 35, 60, 100]
labels = ["Child", "Teenager", "Young Adult", "Adult", "Senior"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)
print(df["Age_Group"].value_counts())
age_survival = df.groupby("Age_Group", observed=True)["Survived"].mean()
print(age_survival)

"""
Senior(60-100) has highest survival rate.
Adult(35-60) has lowest survival rate.
Young Adult contains most passengers.
"""