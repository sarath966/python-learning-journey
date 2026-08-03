"""
Mission Day 7
Topic: Tuples and Dictionaries in Python

Concepts Learned:
- Tuple and Dictionaries Creation
- Indexing
- There Methods
- Traversal using Loops

"""

# Exercise 1
prog_lang = ("C", "JAVA", "Python", "R", "C++")
print("First language in the tuple : ",prog_lang[0])
print("Last language in the tuple : ",prog_lang[-1])
print(prog_lang)

# Exercise 2
student = {"name": "Siva", "age": 19, "branch": "CSE"}
for key, value in student.items():
    print(f"{key}: {value}")

# Exercise 3
student["college"] = "amrita"
student["age"] += 1
print(student)

# Exercise 4
marks = {"Math": 90, "Physics": 82, "Python": 95, "IOT": 89}
print("Highest mark = ",max(marks.values()))
print("Lowest mark = ",min(marks.values()))
average = sum(marks.values())/len(marks.values())
print(f"Average marks = {average:.2f}")

# Exercise 5
user_details = {}
detail_key = ["Name","Age","City"]
for key in detail_key:
    value = input(f"Enter {key} : ")
    user_details[key] = value

print(user_details)

# -------- MINI CHALLENGE ------------
student_data = {}
count_student = int(input("Enter total number of students : "))
for i in range(1,count_student + 1):
    name = input(f"Enter name of student{i} : ")
    marks = int(input(f"Enter marks of {name} : "))
    student_data[name] = marks
print(student_data)
largest = max(student_data.values())
lowest = min(student_data.values())
for key in student_data.keys():
    if student_data[key] == largest:
        highest_student = key
    elif student_data[key] == lowest:
        lowest_student = key
print("Highest scoring student is ",highest_student)
print("Lowest scoring student is ",lowest_student)

print("\nMission Day 7 Completed Successfully!")