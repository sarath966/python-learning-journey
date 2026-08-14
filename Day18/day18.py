"""
Mission Day 18
Topic: Python Modules and Standard Library

Concepts Learned:
- import
- from ... import ...
- math
- random
- statistics
- datetime
- Creating custom modules
"""
# ---------- Exercise 1 --------
import math
num_sqrt = math.sqrt(144)
print("Square root of 144: ",num_sqrt)

num_ceil = math.ceil(8.2)
print("Ceiling of 8.2: ",num_ceil)

num_floor = math.floor(8.9)
print("Floor of 8.9: ",num_floor)

fact_num = math.factorial(5)
print("5! = ",fact_num)

# ---------- Exercise 2 --------
import statistics
marks = [78, 85, 91, 67, 85, 72, 95]
mean_marks = statistics.mean(marks)
median_marks = statistics.median(marks)
mode_marks = statistics.mode(marks)
print("Mean = ",mean_marks)
print("Median = ",median_marks)
print("Mode = ",mode_marks)

# ---------- Exercise 3 --------
import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)

# ---------- Exercise 4 --------
import random
lang_list = ["python", "R", "Java", "C++", "HTML"]
print(random.choice(lang_list))

# ------------ MAIN CHALLENGE ----------
import student_utils
marks = [85, 72, 91, 65, 88, 45, 30]
avg = student_utils.calculate_average(marks)
print("Average = ",avg)
highest_mark = student_utils.find_highest(marks)
lowest_mark = student_utils.find_lowest(marks)
pass_count = student_utils.count_passed(marks)
print("Highest marks = ",highest_mark)
print("Lowest marks = ",lowest_mark)
print("Passed students = ",pass_count)

print("\nMission Day 18 Completed Successfully!")