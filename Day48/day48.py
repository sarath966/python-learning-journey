import matplotlib.pyplot as plt

# ------------ Exercise 1 ------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
actual_sales = [120, 150, 170, 160, 190, 210]
target_sales = [130, 145, 165, 175, 185, 200]
plt.figure(figsize=(8,5))
plt.plot(months, actual_sales, marker = "o",label = "Actual Sales")
plt.plot(months, target_sales, marker = "s",label = "Target Sales")
plt.title("Actual vs Target Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# ------------ Exercise 2 -----------
products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [85, 120, 70, 95]
for i, value in enumerate(sales):
    plt.text(i, value, str(value), ha="center")
plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(axis="y")
plt.show()

# ------------ Exercise 3 -----------
months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 120, 140, 130, 160]
profit = [20, 25, 30, 28, 35]
customers = [50, 65, 70, 80, 95]
returns = [5, 7, 4, 6, 3]
fig, ax = plt.subplots(2, 2, figsize=(10, 7))
ax[0,0].plot(months,sales)
ax[0,0].set_title("Monthly Sales")
ax[0,0].set_xlabel("Months")
ax[0,0].set_ylabel("Sales")
ax[0,0].grid(True)

ax[0,1].plot(months,profit)
ax[0,1].set_title("Monthly Profit")
ax[0,1].set_xlabel("Months")
ax[0,1].set_ylabel("Profit")
ax[0,1].grid(True)

ax[1,0].bar(months,customers)
ax[1,0].set_title("Monthly Customers count")
ax[1,0].set_xlabel("Months")
ax[1,0].set_ylabel("Customers")

ax[1,1].plot(months,returns)
ax[1,1].set_title("Monthly returns")
ax[1,1].set_xlabel("Months")
ax[1,1].set_ylabel("Returns")
ax[1,1].grid(True)

plt.tight_layout()
plt.show()

# ------------- Exercise 4 ------------
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Department": ["CSE", "ECE", "CSE", "EEE", "ECE", "EEE"],
    "Students": [60, 50, 55, 40, 45, 35],
    "Average_Marks": [82, 76, 88, 72, 80, 75]
}

df = pd.DataFrame(data)
fig, ax = plt.subplots(2, 1, figsize=(10,5))
ax[0].bar(df["Department"].unique(), df.groupby("Department")["Average_Marks"].mean())
ax[0].set_title("Average marks of each department")
ax[0].set_xlabel("Department")
ax[0].set_ylabel("Average")

ax[1].bar(df["Department"].unique(), df.groupby("Department")["Students"].sum())
ax[1].set_title("Student count of each department")
ax[1].set_xlabel("Department")
ax[1].set_ylabel("No of students")
plt.tight_layout()
plt.show()

print("\nDay 48 completed")