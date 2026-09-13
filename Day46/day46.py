import matplotlib.pyplot as plt

# ----------- Exercise 1 ------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 13500, 18000, 21000, 19500]
plt.plot(months, sales, marker = "o", linestyle = "--")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Estimation")
plt.grid(True)
plt.show()

# ----------- Exercise 2 -----------
months = ["Jan", "Feb", "Mar", "Apr"]
product_a = [100, 130, 120, 160]
product_b = [90, 110, 140, 150]
plt.plot(months, product_a, marker = "o",label = "product_a")
plt.plot(months, product_b, marker = "o",label = "product_b")
plt.legend()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales analysis")
plt.grid(True)
plt.show()

# ----------- Exercise 3 ------------
subjects = ["Python", "Math", "Physics", "English"]
marks = [85, 78, 90, 72]
plt.bar(subjects, marks)
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Subject marks analysis")
plt.ylim(0, 100)
plt.show()

# ------------ Exercise 4 ------------
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 60, 70, 82, 88]
plt.figure(figsize=(8, 4))
plt.scatter(hours, marks)
plt.grid(True)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs Marks")
plt.show()

# ------------ Exercise 5 -------------
import pandas as pd

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"],
    "Python": [85, 72, 91, 65, 88],
    "Math": [80, 75, 89, 70, 92]
})
plt.plot(students["Name"], students["Python"], marker = "o", label = "Python")
plt.plot(students["Name"], students["Math"], marker = "o", label = "Math")
plt.legend()
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks analysis")
plt.show()

print("\nDay 46 completed")