"""
Mission Day 26
Topic: NumPy Reshaping and Combining Arrays

Concepts Learned:
- reshape()
- flatten()
- ravel()
- concatenate()
- vstack()
- hstack()
- Combining datasets
- 2D data analysis
"""
import numpy as np
# -------- Exercise 1 --------
numbers = np.arange(1, 13)
num_mat = numbers.reshape(3,4)
print(num_mat)
num_mat2 = numbers.reshape(4,3)
print(num_mat2)

# -------- Exercise 2 --------
marks = np.array([
    [85, 72, 91],
    [65, 88, 79]
])
print(marks.flatten())
print(marks.ravel())

# -------- Exercise 3 --------
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
a_b = np.vstack((a, b))
a_b_T = np.hstack((a, b))
print(a_b)
print(a_b_T)
print(np.concatenate((a,b)))

# --------- MAIN CHALLENGE --------
names = np.array(["Sarath", "Ravi", "Abhi", "Kiran"])

python_marks = np.array([85, 72, 91, 65])

math_marks = np.array([78, 88, 95, 70])

physics_marks = np.array([90, 76, 89, 68])
marks_list = (np.vstack((python_marks,math_marks,physics_marks)))
marks_list = marks_list.transpose()
print(marks_list)

avg = np.mean(marks_list,axis=1)
print(avg)
index_top_student = np.argmax(avg)
print("Top Student: ",names[index_top_student])

subjects = np.array(["Python", "Math", "Physics"])
avg_subjects = np.mean(marks_list,axis=0)
high_avg_subject = np.argmax(avg_subjects)
print("Subject with high average: ",subjects[high_avg_subject])

index_avg = np.argsort(avg)[::-1]
for i in index_avg:
    print(names[i],"->",avg[i])

print("\nMission Day 26 Completed Successfully!")
