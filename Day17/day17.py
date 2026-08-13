"""
Mission Day 17
Topic: enumerate(), zip(), any() and all()

Concepts Learned:
- enumerate()
- zip()
- any()
- all()
- Data pairing
- Data validation
"""
# -------- Exercise 1 --------
subjects = ["Python", "Math", "Physics", "English"]
for i, subject in enumerate(subjects):
    print(i," -> ",subject)

# --------- Exercise 2 --------
subjects = ["Python", "Math", "Physics"]
marks = [90, 85, 78]
for subject, mark in zip(subjects, marks):
    print(subject," -> ",mark)

# ---------- Exercise 3 --------
subjects = ["Python", "Math", "Physics", "English"]
marks = [90, 85, 78, 88]
dict_info = dict(zip(subjects, marks))
print(dict_info)

# ----------- MAIN CHALLENGE ---------
students = ["Sarath", "Ravi", "Abhi", "Kiran", "Priya"]

marks = [85, 72, 91, 65, 88]
student_info = zip(students, marks)
for i, student in enumerate(student_info):
    print(f"{i}. {student[0]} -> {student[1]}")

student_dict = dict(zip(students, marks))
print(student_dict)

print("There is a scorer(>= 90): ",any(mark >= 90 for mark in marks))
print("Everyone passed: ",all(mark >= 50 for mark in marks))
print("Everyone scored 60+: ",all(mark > 60 for mark in marks))

print("\nMission Day 17 Completed Successfully!")