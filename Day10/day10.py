"""
Mission Day 10
Topic : Exception Handling and Modules in Python

Concepts Learned:
- try and except
- modules(math, random,..)

"""

# --------- Exercise 1 -------
try:
    num = int(input("Enter a number : "))
except ValueError:
    print("Invalid input! Please enter a number")

# --------- Exercise 2 -------
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))
    result = num1/num2
    print("Result =", result)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Number can't be divided by Zero")

# -------- Exercise 3 --------
import math
print("Square root of 64 = ",math.sqrt(64))
print("Value of pi = ",math.pi)
print("5! = ",math.factorial(5))

# -------- Exercise 4 --------
import random
print("Random number b/w 1 and 100 : ",random.randint(1,100))

# -------- Exercise 5 ----------
dice_output = random.randint(1,6)
print("You rolled: ",dice_output)

# -------- MINI CHALLENGE --------
rand_num = random.randint(1,20)
guessed_num = int(input("Guess a number between 1 and 20 : "))
if guessed_num == rand_num:
    print("Congratulations!")
else:
    print("Wrong guess.The correct number was ",rand_num)

print("\nMission Day 10 Completed Successfully!")
