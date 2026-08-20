"""
Mission Day 24
Topic: NumPy Random Data, Sorting and Searching

Concepts Learned:
- np.arange()
- np.linspace()
- np.random
- np.sort()
- np.argmax()
- np.argmin()
- np.argsort()
- Ranking data
"""
import numpy as np
# ------- Exercise 1 --------
list1 = np.arange(10, 51, 10)
list2 = np.arange(1,20,3)
print(list1)
print(list2)

# -------- Exercise 2 -------
data1 = np.linspace(0, 100, 6)
data2 = np.linspace(10,50,5)
print(data1)
print(data2)

# --------- Exercise 3 --------
marks = np.random.randint(0,101,10)
print("Marks: ",marks)
print("Average: ",np.mean(marks))
print("Highest mark: ",np.max(marks))
print("Lowest mark: ",np.min(marks))

# -------- Exercise 4 --------
marks = np.array([78, 45, 91, 62, 88, 53])
print(np.sort(marks))
print(np.sort(marks)[::-1])

# -------- Exercise 5 ---------
students = np.array(["Sarath", "Ravi", "Abhi", "Kiran", "Priya"])

marks = np.array([85, 72, 91, 65, 88])
ind = np.argmax(marks)
print(ind)
print("Top student: ",students[ind])
print("Marks: ",marks[ind])

# -------- MINI CHALLENGE --------
students = np.array([
    "Sarath",
    "Ravi",
    "Abhi",
    "Kiran",
    "Priya"
])

marks = np.array([85, 72, 91, 65, 88])
inx_top_mark = np.argmax(marks)
print("Top student: ",students[inx_top_mark])
print("Marks: ",marks[inx_top_mark])

inx_low_mark = np.argmin(marks)
print("Lowest student: ",students[inx_low_mark])
print("Marks: ",marks[inx_low_mark])

sort_inx = np.argsort(marks)[::-1]
print(sort_inx)
for i in sort_inx:
    print(students[i], "->", marks[i])

print("\nMission Day 24 Completed Successfully!")