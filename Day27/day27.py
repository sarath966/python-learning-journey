"""
Mission Day 27
Topic: NumPy Filtering and Data Analysis

Concepts Learned:
- Row and column selection
- Boolean masking
- Multiple conditions
- np.where()
- Data classification
- Aggregation
- Student performance analysis
"""
import numpy as np
# -------- DATA -------
students = np.array([
    ["Sarath", 85, 78, 90],
    ["Ravi", 72, 88, 76],
    ["Abhi", 91, 95, 89],
    ["Kiran", 65, 70, 68],
    ["Priya", 88, 90, 94]
])

name =  students[:,0]
marks = students[:, 1:].astype(int)
subjects = np.array(["Python", "Math", "Physics"])

# --------- Exercise 1 --------
print("Sarath marks: ",marks[0])
print("Abhi marks: ",marks[2])
print("Python marks: ",marks[:,0])
print("Physics marks: ",marks[:,2])

# -------- Exercise 2 -------
print("Top students in math:")
math_score_80 = marks[:,1] >= 80
index = np.argwhere(math_score_80)
print(name[index])

# -------- Exercise 3 --------
python_math_80 = (marks[:,0] >= 80) & (marks[:,1] >= 80)
index_python_math = np.argwhere(python_math_80)
print("Top students in both python and math:")
print(name[index_python_math])

python_phy_90 = (marks[:,0] >= 90) | (marks[:,2] >= 90)
index_python_phy = np.argwhere(python_phy_90)
print("Top students in python or Physics:")
print(name[index_python_phy])

# -------- Exercise 4 --------
labels = np.where(marks[:,0] >= 80, "Good", "Needs Improvement")
print(labels)

# --------- MAIN CHALLENGE -------
avg_student = np.mean(marks,axis=1)
print(avg_student)

remark = np.where(avg_student >= 80, "Good", "Needs Improvement")
for i in range(len(name)):
    print(name[i], "->", remark[i])

poor_students = np.any(marks < 70, axis=1)
print(name[poor_students])

top_student = np.argmax(avg_student)
print("Best student: ",name[top_student])
print("Average: ",avg_student[top_student])

avg_subject = np.mean(marks,axis=0)
best_subject = np.argmax(avg_subject)
print("Best subject: ",subjects[best_subject])
print("Average: ",avg_subject[best_subject])

print("Overall Average: ",np.mean(marks))

print("\nMission Day 27 Completed Successfully!")