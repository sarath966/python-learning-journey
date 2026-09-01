"""
Mission Day 35
Topic: Pandas String Operations

Concepts Learned:
- str.upper()
- str.lower()
- str.strip()
- str.len()
- str.contains()
- str.startswith()
- str.endswith()
- str.replace()
- str.split()
- str.title()
- String data cleaning
"""
import pandas as pd

students = pd.DataFrame({
    "Name": [
        "  Sarath", "RAVI", "Abhi  ", "kiran",
        " Priya ", "rahul", "ANU", " vikram "
    ],
    "Department": [
        "CSE", "ece", "CSE", "EEE",
        "cse", "ECE", "cse", "eee"
    ],
    "Email": [
        "sarath@gmail.com",
        "ravi@gmail.com",
        "abhi@gmail.com",
        "kiran@gmail.com",
        "priya@gmail.com",
        "rahul@gmail.com",
        "anu@gmail.com",
        "vikram@gmail.com"
    ]
})

print(students)

# ------------ Exercise 1 -----------
print(students["Name"].str.upper())

# ------------ Exercise 2 -----------
print(students["Name"].str.lower())

# ------------ Exercise 3 ----------
students["Name"] = students["Name"].str.strip()

print(students)

# ---------- Exercise 4 ----------
students["Department"] = students["Department"].str.upper()

# ----------- Exercise 5 ---------
students["Name_Length"] = students["Name"].str.len()
print(students)

# ---------- Exercise 6 ----------
print(students["Email"].str.contains("@gmail.com"))
print(students[students["Email"].str.contains("@gmail.com")])

# ---------- Exercise 7 ---------
print(students[students["Name"].str.startswith("S")])
print(students[students["Name"].str.endswith("i")])

# ---------- Exercise 8 ---------
students["Department_Full"] = (students["Department"].str.replace("CSE", "Computer Science").
                               replace("ECE", "Electronics").replace("EEE", "Electrical"))

print(students)

# ----------- Exercise 9 --------
students_username = students["Email"].str.split("@")
students["Username"] = students_username.str[0]
print(students)

# ----------- Exercise 10 --------
cleaned = students.copy()
cleaned["Name"] = cleaned["Name"].str.strip()

cleaned["Name"] = cleaned["Name"].str.title()

cleaned["Department"] = cleaned["Department"].str.upper()

print(cleaned)

# ----------- Exercise 11 ---------
cleaned = students.copy()
cleaned = cleaned[cleaned["Department"].isin(["CSE","ECE"])]
cleaned["Name"] = cleaned["Name"].sort_values()
print(cleaned)
print(cleaned[["Name", "Department", "Username"]])

print("\nMission Day 35 Completed Successfully!")