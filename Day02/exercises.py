# ------------ Exercise 1 --------------
print("Exercise 1")
name = input("Enter your name : ")
age = int(input("Enter age : "))
print(f"Hello {name}")
print(f"Next year you will be {age + 1} years old")

# ------------ Exercise 2 --------------
print("\nExercise 2")
num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

total = num1 + num2
dif = num1 - num2
prod = num1 * num2
quotient = num1 / num2

print(f"{num1} + {num2} = {total}")
print(f"{num1} - {num2} = {dif}")
print(f"{num1} * {num2} = {prod}")
print(f"{num1} / {num2} = {quotient}")

# ------------ Exercise 3 ---------------
print("\nExercise 3")
height = float(input("Enter height in metres : "))
weight = float(input("Enter weight in KG : "))

bmi = weight / (height ** 2)
print("Body mass index : ",bmi)


# Mini Challenge (simple Student profile)
print("\nMini Challenge")
name = input("Enter name : ")
age = int(input("Enter your age : "))
branch = input("Enter your Branch : ")
gpa = input("Enter CGPA : ")

print("-" * 10,"Student Profile","-" * 10)
print("Name : ",name)
print("Age : ",age)
print("Branch : ",branch)
print("CGPA : ",gpa)
print("-"*20)