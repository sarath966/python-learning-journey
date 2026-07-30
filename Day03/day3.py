# --- Day-3 - Decision Making in python ----

# Exercise 1
print("Exercise 1")
age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Exercise 2
print("\nExercise 2")
num = float(input("Enter a number : "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("The number is zero")

# Exercise 3
print("\nExercise 3")
marks = float(input("Enter the marks : "))
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
    grade = "Fail"
print("Grade : ",grade)


# -------- MINI Challenge ---------
print("\nMini Challenge")

name = input("Enter your Name : ")
marks = float(input("Enter Marks : "))
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
    grade = "Fail"

print("Name : ",name)
print("Marks : ",marks)
print("Grade : ",grade)
if grade != "Fail":
    print("PASS")
else:
    print("FAIL")