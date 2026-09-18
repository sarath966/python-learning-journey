import matplotlib.pyplot as plt

# ----------- Exercise 1 ---------
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 170, 160, 190]
profit = [30, 40, 45, 42, 55]
fig, ax = plt.subplots(1, 2)
ax[0].plot(months, sales)
ax[0].set_title("Months vs Sales")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Sales")
ax[1].plot(months, profit)
ax[1].set_title("Months vs Profit")
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Profit")
plt.tight_layout()
plt.show()

# ------------ Exercise 2 -----------
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 170, 160, 190]
expenses = [80, 95, 110, 100, 120]
fig, ax = plt.subplots(2, 1, figsize = (8,6))
ax[0].plot(months, sales)
ax[0].set_title("Months vs Sales")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Sales")
ax[1].bar(months, expenses)
ax[1].set_title("Months vs Expenses")
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Expenses")
plt.tight_layout()
plt.show()

# ---------- Exercise 3 ----------
students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 67, 92, 74]
hours = [5, 7, 4, 8, 6]
fig, ax = plt.subplots(3,1)
ax[0].bar(students, marks)
ax[0].set_title("Student marks")
ax[0].set_xlabel("Student")
ax[0].set_ylabel("Marks")
ax[1].plot(students, hours)
ax[1].set_title("Study hours")
ax[1].set_xlabel("Student")
ax[1].set_ylabel("Study hours")
ax[2].scatter(hours, marks)
ax[2].set_title("Study hours vs marks")
ax[2].set_xlabel("Study hours")
ax[2].set_ylabel("Marks")
plt.tight_layout()
plt.show()

# ------------- Exercise 4 ----------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [100, 120, 140, 130, 160, 180]
customers = [50, 55, 65, 60, 75, 85]
returns = [5, 7, 6, 8, 5, 4]
fig, ax = plt.subplots(3, 1, figsize=(10,7))
ax[0].plot(months, sales, marker = "o")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Sales")
ax[0].set_title("Sales over months")
ax[1].bar(months, customers)
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Customers")
ax[1].set_title("Customers over months")
ax[2].plot(months, returns, marker = "o")
ax[2].set_xlabel("Months")
ax[2].set_ylabel("Returns")
ax[2].set_title("Returns over months")
plt.tight_layout()
plt.show()

print("\nDay47 completed")