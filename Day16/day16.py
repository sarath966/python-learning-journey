"""
Mission Day 16
Topic: List and Dictionary Comprehensions

Concepts Learned:
- List comprehensions
- Conditional comprehensions
- Dictionary comprehensions
- Data transformation
- Data filtering
"""
# List Comprehension with Conditions
# ---------- Exercise 1 ----------
numbers = [2, 4, 6, 8, 10]
squares_numbers = [num ** 2 for num in numbers]
print(squares_numbers)

# ---------- Exercise 2 ----------
numbers = [11, 12, 15, 18, 21, 24, 30]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

# ---------- Exercise 3 ----------
numbers = [25, 60, 45, 80, 35, 90, 55]
num_greater_50 = [num for num in numbers if num > 50]
print(num_greater_50)

# Dictionary Comprehension
# ---------- Exercise 4 ----------
numbers = [1, 2, 3, 4, 5]
dict_squares = {num:num**2 for num in numbers}
print(dict_squares)

# ---------- Exercise 5 ----------
students = [
    {"name": "Sarath", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Abhi", "marks": 91},
    {"name": "Kiran", "marks": 65},
    {"name": "Priya", "marks": 88}
]
dict_name_marks = {student["name"]:student["marks"] for student in students}
print(dict_name_marks)

# ---------- MAIN CHALLENGE ----------
students = [
    {"name": "Sarath", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Abhi", "marks": 91},
    {"name": "Kiran", "marks": 65},
    {"name": "Priya", "marks": 88}
]
names_list = [student["name"] for student in students]
print(names_list)

marks_list = [student["marks"] for student in students]
print(marks_list)

marks_greater_80 = [student["name"] 
                    for student in students if student["marks"] >= 80]
print(marks_greater_80)

dict_name_marks = {student["name"]:student["marks"] for student in students}
print(dict_name_marks)

student_result = {student["name"] : "Pass" if student["marks"] >= 50
                   else "Fail" for student in students}
print(student_result)

print("\nMission Day 16 Completed Successfully!")