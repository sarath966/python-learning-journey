"""
Mission Day 6
Topic: Lists in Python

Concepts Learned:
- List Creation
- Indexing
- Slicing
- List Methods
- Iterating through Lists

"""

# Exercise 1

fruit = ["apple", "orange", "guava", "grapes", "cherry"]
print(fruit[0])
print(fruit[-1])
print(fruit)

# Exercise 2
marks = [65, 72, 91, 48, 85]
total = sum(marks)
print("Maximum marks = ",max(marks))
print("Minimum marks = ",min(marks))
print("Total marks = ",total)
if len(marks) > 0:
    Average = total/len(marks)
print("Average = ",Average)

# Exercise 3
names_list = []
for i in range(1,6):
    name = input(f"Enter name {i} : ")
    names_list.append(name)
print(names_list)

# Exercise 4
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
numbers[1] = 35
print(numbers)

# Exercise 5
nums_list = [20,55,60,40,33,78,99,45,9,10]
for i in nums_list:
    if i % 2 == 0:
        print(i,end = " ")


# ------ MINI CHALLENGE -------
marks = []
tot_stud = int(input("\nEnter total no of students : "))
for i in range(1,tot_stud + 1):
    mark = int(input(f"Enter marks of student {i} : "))
    marks.append(mark)

print("Marks : ",marks)
print("Highest mark : ",max(marks))
print("Lowest mark : ",min(marks))
if len(marks) > 0:
    Average = sum(marks)/len(marks)
print("Average = ",Average)