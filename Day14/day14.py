"""
Mission Day 14
Topic: Sorting, Filtering and Data Transformation

Concepts Learned:
- sorted()
- reverse=True
- key=
- Sorting structured data
- Filtering data
- Multiple conditions
- Data analysis
"""
# -------- Exercise 1 --------
numbers = [45, 12, 89, 34, 7, 56]
print("Ascending: ",sorted(numbers))
print("Descending: ",sorted(numbers,reverse = True))

# --------- Exercise 2 --------
marks = [85, 72, 95, 60, 88, 76]
marks_sort = sorted(marks)
print("Lowest mark: ",marks_sort[0])
print("Highest mark: ",marks_sort[-1])
print("Marks in ascending order: ",marks_sort)
print("Marks in descending order: ",marks_sort[::-1])

# --------- Exercise 3 ---------
students = [
    {"name": "Sarath", "marks": 85},
    {"name": "Ravi", "marks": 90},
    {"name": "Abhi", "marks": 72},
    {"name": "Kiran", "marks": 95},
    {"name": "Rahul", "marks": 65}
]
sort_students = sorted(students, key = lambda student: student["marks"],reverse = True)
for student in sort_students:
    print(student["name"],"->",student["marks"])

# --------- MAIN CHALLENGE ---------
students = [
    {"name": "Sarath", "marks": 85, "attendance": 92},
    {"name": "Ravi", "marks": 90, "attendance": 88},
    {"name": "Abhi", "marks": 72, "attendance": 95},
    {"name": "Kiran", "marks": 95, "attendance": 90},
    {"name": "Rahul", "marks": 65, "attendance": 78},
    {"name": "Priya", "marks": 88, "attendance": 96}
]

def average_marks(students):
    total = 0
    for student in students:
        total += student["marks"]
    avg = total/len(students)
    return avg
print("Average: ", average_marks(students))

def top_three_students(students):
    sorted_students = sorted(students,key = lambda student: student["marks"], reverse = True)
    print("Top 3 students: ")
    for i in range(3):
        print(sorted_students[i]["name"],"->",sorted_students[i]["marks"])

    return
top_three_students(students)

def high_attendance_students(students):
    for student in students:
        if student["attendance"] >= 90:
            print(student["name"])
    return
print("Attendance more than or equal to 90: ")
high_attendance_students(students)

def eligible_students(students):
    for student in students:
        if student["marks"] >= 80 and student["attendance"] >= 90:
            print(student["name"])
    return
print("Eligible Students:")
eligible_students(students)

def sort_by_attendance(students):
    sorted_attendance = sorted(students,key = lambda student: student["attendance"], reverse = True)
    print("Attendance order: ")
    for student in sorted_attendance:
        print(student["name"],"-",student["attendance"])
    return
sort_by_attendance(students)

print("\nMission Day 14 Completed Successfully!")