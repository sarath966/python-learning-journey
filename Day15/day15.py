"""
Mission Day 15
Topic: Lambda, Map and Filter

Concepts Learned:
- Lambda functions
- map()
- filter()
- Data transformation
- Data filtering
"""
# ------------ Exercise 1 (lambda function) ----------
square = lambda x:x ** 2
print(square(5))

cube = lambda x:x**3
print(cube(5))

double = lambda x:x*2
print(double(5))

even = lambda x:x%2 == 0
print("8 is even: ",even(8))
print("15 is even: ",even(15))

# ------------ Exercise 2 (map()) -----------
numbers = [2, 4, 6, 8, 10]
sq_nums = list(map(square,numbers))
print(sq_nums)

cube_nums = list(map(cube,numbers))
print(cube_nums)

num_mult_5 = list(map(lambda x:x*5,numbers))
print(num_mult_5)

# ------------ Exercise 3 (filter()) ----------
numbers = [12, 7, 25, 40, 13, 60, 9, 80]

even_nums = list(filter(even,numbers))
print(even_nums)

nums_greater_20 = list(filter(lambda x:x >= 20,numbers))
print(nums_greater_20)

nums_div_5 = list(filter(lambda x:x % 5 == 0,numbers))
print(nums_div_5)

# ------------- MAIN CHALLENGE --------
students = [
    {"name": "Sarath", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Abhi", "marks": 91},
    {"name": "Kiran", "marks": 65},
    {"name": "Priya", "marks": 88}
]
def get_names(students):
    names = list(map(lambda student:student["name"],students))
    return names
print(get_names(students))

def get_marks(students):
    marks = list(map(lambda student: student["marks"], students))
    return marks
print(get_marks(students))

def high_scorers(students):
    greater_80 = list(filter(lambda student:student["marks"] >= 80,students))
    names_greater_80 = list(map(lambda student:student["name"],greater_80))
    return names_greater_80
print(high_scorers(students))

def add_bonus_marks(students):
    students_bonus = list(map(lambda student:student["marks"] + 5,students))
    return students_bonus
print(add_bonus_marks(students))


print("\nMission Day 15 Completed Successfully!")