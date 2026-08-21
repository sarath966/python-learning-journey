"""
Mission Day 25
Topic: NumPy Data Analysis

Concepts Learned:
- Aggregation with axis
- Boolean masking
- Student-level statistics
- Subject-level statistics
- argmax()
- argsort()
- Basic numerical data analysis
"""
import numpy as np
# -------- Exercise 1 --------
marks = np.array([
    [85, 72, 91],
    [65, 88, 79],
    [92, 95, 89],
    [70, 68, 75],
    [88, 90, 94]
])
print("Average marks in each subject: ",np.mean(marks,axis=0))
print("Highest mark in each subject: ",np.max(marks,axis=0))
print("Lowest mark in each subject: ",np.min(marks,axis=0))

# --------- Exercise 2 --------
print("Total marks of every student: ",np.sum(marks,axis=1))
print("Average of every student: ",np.mean(marks,axis=1))
print("Highest mark of every student: ",np.max(marks,axis=1))

# -------- Exercise 3 ---------
student_averages = np.mean(marks, axis=1)
top_index = np.argmax(student_averages)
print(top_index,"->", student_averages[top_index])

# -------- MAIN CHALLENGE -------
marks = np.array([
    [85, 72, 91],
    [65, 88, 79],
    [92, 95, 89],
    [70, 68, 75],
    [88, 90, 94]
])
avg = np.mean(marks,axis=1)
print("Average marks of every student: ",avg)
avgmark_above_80 = (avg >= 80)
print(avgmark_above_80)
print("Qualifying averages are: ",avg[avgmark_above_80])
print("Count of students aveage >= 80: ",np.sum(avgmark_above_80))
index_top_student = np.argmax(avg)
print("Top student index: ",index_top_student)
print("Top student average: ",avg[index_top_student])
student_index = np.argsort(avg)[::-1]
for i in student_index:
    print(i, "->", avg[i])
subject = np.array(["Python", "Math", "Physics"])
avg_subject = np.mean(marks,axis=0)
print(avg_subject)
index_high_subject_avg = np.argmax(avg_subject)
print(index_high_subject_avg,":",
      subject[index_high_subject_avg], "->",avg_subject[index_high_subject_avg])
print("Highest marks: ",np.max(marks))
print("Lowest marks: ",np.min(marks))

print("\nMission Day 25 Completed Successfully!")