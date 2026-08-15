"""
Mission Day 19
Topic: CSV Files and Data Processing

Concepts Learned:
- CSV files
- csv.reader
- csv.DictReader
- csv.DictWriter
- Reading structured data
- Processing CSV data
"""
import csv
# --------- Exercise 1 -------
with open("info.csv","r") as data:
    reader = csv.DictReader(data)
    for row in reader:
        print(row["name"])

# --------- Exercise 2 -------
with open("info.csv","r") as data:
    reader = csv.DictReader(data)
    list_mark = []
    for row in reader:
        list_mark.append(int(row["marks"]))
    avg_mark = sum(list_mark)/len(list_mark)
    print("\nAverage marks: ",avg_mark)

# --------- Exercise 3 -------
with open("info.csv","r") as data:
    reader = csv.DictReader(data)
    print("\nHigh Scorers:")
    for row in reader:
        if int(row["marks"]) >= 80:
            print(row["name"])

# --------- Exercise 4 -------
with open("info.csv","r") as data:
    reader = csv.DictReader(data)
    print("\nAttendance greate 90 :")
    for row in reader:
        if int(row["attendance"]) >= 90:
            print(row["name"])

# --------- MAIN CHALLENGE --------
with open("info.csv","r") as data:
    with open("passed_students.csv","w", newline="") as students_passed:
        reader = csv.DictReader(data)
        writer = csv.DictWriter(students_passed,fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if int(row["marks"]) >= 50:
                writer.writerow(row)

with  open("passed_students.csv","r") as file:
    print(file.read())