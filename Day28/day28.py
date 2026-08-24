"""
Mission Day 28
Topic: NumPy Student Performance Analyzer

Concepts Learned:
- np.any()
- np.all()
- Boolean masking
- np.where()
- np.argmax()
- np.argmin()
- np.argsort()
- np.unravel_index()
- 2D data analysis
"""
import numpy as np
# ------ DATA -----
names = np.array([
    "Sarath",
    "Ravi",
    "Abhi",
    "Kiran",
    "Priya",
    "Rahul",
    "Anu",
    "Vikram"
])

marks = np.array([
    [85, 78, 90],
    [72, 88, 76],
    [91, 95, 89],
    [65, 70, 68],
    [88, 90, 94],
    [55, 62, 58],
    [96, 92, 98],
    [74, 81, 79]
])

subjects = np.array([
    "Python",
    "Math",
    "Physics"
])

# -------- Operations ------
student_average = np.mean(marks,axis=1)
subject_average = np.mean(marks,axis=0)
class_average = np.mean(marks)
print(student_average)
print(subject_average)
print(class_average)

passed = np.all(marks >= 50,axis=1)
print(names[passed])

needs_improvement = student_average < 70
print(needs_improvement)
print("Students need Improvement",names[needs_improvement])

remark = np.where(student_average >=80, "Excellent",
                  np.where(student_average >= 70, "Good","Need Improvement"))
for i in range(len(names)):
    print(names[i], "->",remark[i])

for i in range(len(names)):
    print(f"{names[i]} -> {student_average[i]}")

top_student = np.argmax(student_average)
print("Top student: ",names[top_student])
print("Average: ",student_average[top_student])

ranking = np.argsort(student_average)[::-1]
for index,value in enumerate(ranking):
    print(f"{index + 1}. {names[value]} -> {student_average[value]}")

best_subject = np.argmax(subject_average)
print("Best subject: ",subjects[best_subject])
print("Average: ",subject_average[best_subject])

weakest_subject = np.argmin(subject_average)
print("Weakest subject: ",subjects[weakest_subject])
print("Average: ",subject_average[weakest_subject])

highest = np.argmax(marks)

row, column = np.unravel_index(highest, marks.shape)

print("Highest mark:", marks[row, column])
print("Student:", names[row])
print("Subject:", subjects[column])

print("\nMission Day 28 Completed Successfully!")