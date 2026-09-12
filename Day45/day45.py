import matplotlib.pyplot as plt

# ----------- Exercise 1 ---------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 13500, 18000, 21000, 19500]

plt.plot(months, sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Months vs Sales")
plt.show()

# ----------- Exercise 2 ----------
departments = ["CSE", "ECE", "EEE", "ME"]
students = [45, 35, 30, 25]
plt.bar(departments, students)
plt.xlabel("Department")
plt.ylabel("Students")
plt.title("Students in each department")
plt.show()

# --------- Exercise 3 -----------
hours = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 52, 60, 68, 75, 82, 90]
plt.scatter(hours,marks)
plt.xlabel("Hours of study")
plt.ylabel("Marks")
plt.title("Hours vs marks")
plt.show()

# ---------- Exercise 4 ------------
import pandas as pd

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Python": [85, 72, 91, 65, 88],
    "Math": [80, 75, 89, 70, 92]
})
plt.bar(students["Name"], students["Python"])
plt.xlabel("Names")
plt.ylabel("Python Marks")
plt.title("Python marks of each student")
plt.show()

plt.bar(students["Name"], students["Math"])
plt.xlabel("Names")
plt.ylabel("Math Marks")
plt.title("Math marks of each student")
plt.show()

# ----------- Exercise 5 ----------
students["Average"] = students[["Python", "Math"]].mean(axis=1)

plt.bar(students["Name"], students["Average"])
plt.xlabel("Student Name")
plt.ylabel("Average")
plt.title("Average marks of each student")
plt.show()

print("\nDay45 completed")