"""
Mission Day 9
Topic : Sets and Basic File Handling in Python

Concepts Learned:
- set Creation
- There Methods
- Read and write operations in file handling

"""
# Exercise 1
fruits = {"Apple", "Banana", "Mango"}
fruits.add("Orange")
fruits.discard("Banana")
print(fruits)

# Exercise 2
numbers = [10, 20, 20, 30, 40, 40, 50]
numbers_set = set(numbers)
print(numbers_set)

# Exercise 3
subject_set = set()
for _ in range(5):
    subject = input("Enter your fav subject : ")
    subject_set.add(subject)
print(subject_set)

# Exercise 4
with open("about_me.txt","w") as file:
    file.write("Name : Sarath\nCollege : Amrita\nGoal : Data Scientist")
with open("about_me.txt","r") as file:
    print(file.read())

# Exercise 5
sentence = input("Enter a sentence : ")
word_sentence = sentence.split(" ")
unique_word = set(word_sentence)
print(unique_word)
print(len(unique_word))

# ------ MINI CHALLENGE -------
names_student = set()
student_count = int(input("How many students attended today : "))
for _ in range(student_count):
    student = (input("Enter student name : ")).lower()
    names_student.add(student)

print("Unique student names : ",names_student)
print("Total number of unique students : ",len(names_student))