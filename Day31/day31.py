"""
Mission Day 31
Topic: Pandas Sorting and Ranking

Concepts Learned:
- sort_values()
- ascending / descending order
- Multiple-column sorting
- sort_index()
- rank()
- nlargest()
- nsmallest()
- Ranking and sorting data
"""
import pandas as pd

# ------- DATA -------
students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya", "Rahul", "Anu", "Vikram"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE", "CSE", "EEE"],
    "Python": [85, 72, 91, 65, 88, 55, 96, 74],
    "Math": [78, 88, 95, 70, 90, 62, 92, 81],
    "Physics": [90, 76, 89, 68, 94, 58, 98, 79]
})

print(students)

# --------- Exercise 1 --------
print(students.sort_values("Python"))
print(students.sort_values("Python", ascending = False))
print(students.sort_values("Math", ascending=False))
print(students.sort_values("Physics"))

# --------- Exercise 2 ---------
print(students.sort_values("Python",ascending=False)[["Name", "Python"]])
print(students.sort_values("Math",ascending=False)[["Name", "Math"]])
print(students.sort_values("Physics",ascending=False)[["Name", "Physics"]])

# --------- Exercise 3 --------
print(students.sort_values(["Python", "Department"],ascending=[False,True]))
print(students.sort_values(["Math", "Physics"],ascending=[False,False]))
print(students.sort_values(["Math", "Department"],ascending=[False,True]))

# --------- Exercise 4 ---------
students["Math_rank"] = students["Math"].rank(ascending=False)
print(students[["Name", "Math", "Math_rank"]])

# --------- Exercise 5 ---------
print(students.nlargest(3, "Python"))
print(students.nsmallest(3, "Python"))
print(students.nlargest(3, "Math"))
print(students.nsmallest(3, "Physics"))

# ---------- MAIN CHALLENGE --------
import numpy as np
students["Average"] = students[["Python", "Math", "Physics"]].mean(axis=1)
print(students["Average"])

performance = np.where(students["Average"] >= 85, "Excellent",
                       np.where(students["Average"] >= 75, "Good",
                                np.where(students["Average"] >= 60, "Average", "Need Improvement")))
students["Performance"] = performance

students["Overall_Rank"] = students["Average"].rank(ascending=False)
print(students["Overall_Rank"])

new_data = pd.DataFrame({
    "Rank" : students["Overall_Rank"],
    "Name" : students["Name"],
    "Department" : students["Department"],
    "Python" : students["Python"],
    "Math" : students["Math"],
    "Physics" : students["Physics"],
    "Average" : students["Average"],
    "Performance" : students["Performance"]
})
print(new_data)

print(new_data.nlargest(2, "Average")[["Name", "Department", "Average"]])

students_below_70 = new_data[new_data["Average"] < 70]
print(students_below_70[["Name", "Average", "Performance"]])

print("\nMission Day 31 Completed Successfully!")