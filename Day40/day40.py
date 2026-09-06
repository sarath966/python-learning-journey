import pandas as pd

students = pd.DataFrame({
    "Name": ["Sarath", "Ravi", "Abhi", "Kiran", "Priya",
             "Anu", "Rahul", "Sneha", "Arjun", "Meena"],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE",
                   "ECE", "EEE", "CSE", "ECE", "EEE"],
    "Python": [85, 72, 91, 65, 88, 76, 55, 95, 81, 69],
    "Math": [78, 88, 95, 70, 90, 82, 60, 92, 85, 74],
    "Physics": [90, 76, 89, 68, 94, 79, 58, 96, 83, 71],
    "Attendance": [92, 85, 96, 78, 94, 88, 72, 97, 90, 80]
})

print(students)

# ------------- Exercise 1 ------------
students["Average"] = students[["Python", "Math", "Physics"]].mean(axis=1)
print(students[["Name", "Python", "Math", "Physics", "Average"]])

# ------------- Exercise 2 ------------
students["Result"] = students["Average"].apply(
    lambda x : "Pass" if x >= 50 else "Fail"
)
print(students)

# ------------- Exercise 3 -----------
def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    return
students["Grade"] = students["Average"].apply(
    lambda x : grade(x)
)
print(students)

# ------------ Exercise 4 ------------
top_students = (students[(students["Average"] >= 80) &
                         (students["Attendance"] >= 85)])
top_students = top_students[["Name", "Department", "Average", "Attendance", "Grade"]]
print(top_students.sort_values("Average",ascending=False))

# ------------ Exercise 5 ------------
print(students.groupby("Department")["Python"].mean())
print(students.groupby("Department")["Math"].mean())
print(students.groupby("Department")["Physics"].mean())
print(students.groupby("Department")["Average"].mean())

# ------------ Exercise 6 ------------
print(students.iloc[students["Average"].idxmax()])
print(students.iloc[students["Python"].idxmax()])
print(students["Average"].mean())
print((students["Grade"] == "Pass").count())
print(students["Department"].value_counts())
print(students.groupby("Department")["Grade"].value_counts())