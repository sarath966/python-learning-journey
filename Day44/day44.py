"""
Mission Day 44
Topic: Introduction to Matplotlib

Concepts:
- matplotlib
- line plot
- bar chart
- scatter plot
- xlabel()
- ylabel()
- title()
- show()
- Pandas + Matplotlib
"""
import matplotlib.pyplot as plt

# ---------- Exercise 1 ----------
days = [1, 2, 3, 4, 5]
marks = [65, 72, 68, 80, 85]
plt.plot(days, marks)

plt.xlabel("Day")
plt.ylabel("Marks")
plt.title("Marks Over 5 Days")

plt.show()

# ---------- Exercise 2 ---------
subjects = ["Python", "Math", "Physics"]
marks = [85, 78, 90]
plt.bar(subjects, marks)
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Subject marks")
plt.show()

# --------- Exercise 3 --------
hours = [1, 2, 3, 4, 5, 6]
marks = [50, 55, 65, 70, 80, 88]
plt.scatter(hours, marks)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs marks")
plt.show()

# ---------- Exercise 4 ----------
import pandas as pd
students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Python": [85, 72, 91, 65, 88]
})

plt.bar(students["Name"], students["Python"])
plt.xlabel("Student Name")
plt.ylabel("Python marks")
plt.show()

# --------- Exercise 5 ---------
department = ["CSE", "ECE", "EEE"]
students_count = [4, 3, 3]
plt.bar(department, students_count)
plt.xlabel("Department")
plt.ylabel("Student count")
plt.show()

# ----------- Exercise 6 ------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 13500, 18000, 21000, 19500]
plt.plot(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly sales analysis")
plt.show()

print(months[sales.index(max(sales))])
print(max(sales))
print(months[sales.index(min(sales))])
print(min(sales))

print("\nDay44 completed")