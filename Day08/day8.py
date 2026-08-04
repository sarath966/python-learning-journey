"""
Mission Day 8
Topic: Strings in Python

Concepts Learned:
- String indexing
- String slicing
- Methods

"""

# Exercise 1
name = "Sarath"

print(name[0])
print(name[-1])
print(len(name))

# Exercise 2
name = input("Enter full name : ")
print(name.upper())
print(name.lower())
num_char = len(name) - name.count(" ")
print(num_char)

# Exercise 3
sentence = "Python is fun"
print(sentence[0:6])
print(sentence[-3:])

# Exercise 4
sentence = input("Enter a sentence that contain word python : ")
sentence = sentence.lower()
print(sentence.replace("python","Data Science"))

# Exercise 5
word = input("Enter a word : ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# ------- MINI CHALLENGE -------
email = input("Enter Email ID : ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

print("\nMission Day 8 Completed Successfully!")