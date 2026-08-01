# Day 5 - Functions

# Exercise 1
def greet():
    print("Welcome to Python Programming")

greet()

# Exercise 2
def square(num):
    return num ** 2

print("15^2 = ",square(15))

# Exercise 3
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("max(25,15) = ",largest(25, 15))

# Exercise 4
def is_even(num):
    return num % 2 == 0
print("18 is a even number -> ",is_even(18))
print("15 is a even number -> ",is_even(15))

# Exercise 5
def calculate_bmi(weight, height):
    bmi = weight/(height ** 2)
    return bmi
print(f"BMI of a person with weight 70KG and height 1.72M is,{calculate_bmi(70, 1.72):.2f}")


#------MINI CHALLENGE-------
def calculate_grade(marks):
    grade = None
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade

def display_result(name, marks):
    grade = calculate_grade(marks)
    print("Name : ",name)
    print("Marks :",marks)
    print("Grade :",grade)
    status = None
    if grade == "F":
        status = "FAIL"
    else:
        status = "PASS"
    print("Status : ",status)

display_result("Siva", 40)
