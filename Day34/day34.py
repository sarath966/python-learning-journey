"""
Mission Day 34
Topic: Pandas Data Cleaning

Concepts Learned:
- dtypes
- astype()
- pd.to_numeric()
- duplicated()
- drop_duplicates()
- subset
- keep
- reset_index()
- Data type conversion
- Duplicate handling
"""
import pandas as pd

students = pd.DataFrame({
    "Name": [
        "Sarath", "Ravi", "Abhi", "Kiran",
        "Priya", "Ravi", "Anu", "Kiran"
    ],
    "Department": [
        "CSE", "ECE", "CSE", "EEE",
        "CSE", "ECE", "CSE", "EEE"
    ],
    "Python": [
        "85", "72", "91", "65",
        "88", "72", "96", "65"
    ],
    "Math": [
        78, 88, 95, 70,
        90, 88, 92, 70
    ]
})

print(students)
# --------- Exercise 1 ---------
print(students.dtypes)
print(students["Python"].dtype)

# --------- Exercise 2 ---------
students["Python"] = students["Python"].astype(int)
print(students.dtypes)

# --------- Exercise 3 --------
test = students.copy()

test["Python"] = test["Python"].astype(str)

print(test["Python"].sum())
print(students["Python"].sum())

# ---------- Exercise 4 --------
print(students.duplicated())
print(students.duplicated().sum())

# ---------- Exercise 5 --------
cleaned = students.drop_duplicates()
print(cleaned)
print(len(students))
print(len(cleaned))

# ---------- Exercise 6 --------
names = students.duplicated(subset=["Name"])
print(names)
print(len(names))
print(students.drop_duplicates(subset=["Name"]))

# --------- Exercise 7 ---------
print(students.drop_duplicates(subset=["Name"]))
print(students.drop_duplicates(
    subset=["Name"],
    keep="last"
))

# --------- Exercise 8 ----------
copy = students.copy()
copy["Python"] = pd.to_numeric(
    copy["Python"]
)
print(copy["Python"].dtype)

# ----------- Exercise 9 --------
cleaned = students.copy()
cleaned["Python"] = pd.to_numeric(cleaned["Python"])
print(cleaned.drop_duplicates())
print(cleaned["Name"].drop_duplicates())
cleaned = cleaned.reset_index(drop=True)
print(cleaned)
print(cleaned.dtypes)

# ---------- Exercise 10 ---------
data = students.copy()
data["Python"] = pd.to_numeric(data["Python"])
data["Name"].drop_duplicates()
data = data.reset_index(drop=True)
print(data[["Name", "Department", "Python", "Math"]])
print(data.sort_values(["Python"],ascending=False))

# ----------- Exercise 11 ---------
final = students.copy()
final["Python"].astype(int)
final = final.drop_duplicates()
final = final.sort_values("Python",ascending=False)
final = final.reset_index(drop=True)
print(final)

print("\nMission Day 34 Completed Successfully!")