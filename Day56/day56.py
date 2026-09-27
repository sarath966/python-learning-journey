import pandas as pd
import numpy as np

scores = [45, 52, 58, 61, 64, 67, 69, 72, 74, 78,
          81, 83, 85, 88, 91]

# ---------- Exercise 1 ------------
print("Mean: ", np.mean(scores))
print("Median", np.median(scores))
print()

# ---------- Exercise 2 ------------
# The mean and median are slightly different.
# This suggests the distribution may have some asymmetry,
# but mean and median alone are not enough to fully determine the shape.

# ---------- Exercise 3 ------------
print(np.var(scores,ddof=0))
print(np.std(scores,ddof=0))
print(np.var(scores,ddof=1))
print(np.std(scores,ddof=1))

# --------- Exercise 4 ------------
print(np.percentile(scores, 25))
print(np.percentile(scores, 50))
print(np.percentile(scores, 75))
print(np.percentile(scores, 90))
# The 75th percentile is a statistical value below which 75% of the 
# observations in a group fall, and above which the remaining 25% lie.

# ---------- Exercise 5 ------------
income = [25000, 27000, 29000, 31000, 32000,
          34000, 35000, 36000, 38000, 40000,
          42000, 45000, 48000, 50000, 250000]
q1 = np.percentile(income,25)
q3 = np.percentile(income,75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(iqr)
print(lower_bound)
print(upper_bound)

# ---------- Exercise 6 ------------
for value in income:
    if value < lower_bound or value > upper_bound:
        print(value)

# ---------- Exercise 7 ----------
print(np.mean(income))
print(np.median(income))
# Till 50000 the income is symmetric but when it comes to the last one 
# it is not match with the pattern and it will effect the mean

# --------- Exercise 8 -----------
df = pd.read_csv(r"C:\Users\asara\Desktop\Datascience_per\python_learning-journey\Day52\titanic.csv")
print(df.columns)
print(df["Age"].mean())
print(df["Age"].median())
print(df["Age"].std())
q1 = np.percentile(df["Age"].dropna(),25)
q3 = np.percentile(df["Age"].dropna(),75)
iqr = q3 - q1
print(q1)
print(q3)
print(iqr)

# ---------- Exercise 9 ------------
print(df.groupby("Survived")["Age"].agg(["mean", "median"]))

# ---------- Exercise 10 ----------
print(df.groupby("Survived")["Age"].std())

"""
Survivors have greater age variability if their standard deviation is higher.
This describes the spread of observed ages in the dataset, but it does not
prove that survival status caused the difference in age variability.
"""