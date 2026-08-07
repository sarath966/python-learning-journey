"""
Mission Day 11
Topic: Lists, Dictionaries and Problem Solving

Concepts Learned:
- Lists
- Dictionaries
- Loops
- Conditions
- Functions
"""

# ---------- Exercise 1 --------
numbers = [12, 7, 18, 25, 30, 41, 56, 63]
count_even = 0
count_odd = 0
for num in numbers:
    if num % 2 == 0:
        count_even += 1
    elif num % 2 != 0:
        count_odd += 1
print("Even numbers: ",count_even)
print("Odd numbers: ",count_odd)

# --------- Exercise 2 --------
marks = {"Math": 85,"Physics": 78, "Python": 92,"English": 74}
total_marks = sum(marks.values())
avg_marks = total_marks/len(marks)
highest_mark = marks["Math"]
highest_mark_subject = "Math"
lowest_mark = marks["Math"]
lowest_mark_subject = "Math"
for key, value in marks.items():
    if highest_mark <= value:
        highest_mark = value
        highest_mark_subject = key
    if lowest_mark >= value:
        lowest_mark = value
        lowest_mark_subject = key
print("Total Marks = ",total_marks)
print("Average Marks = ",avg_marks)
print(f"Highest mark is {highest_mark} in the subject {highest_mark_subject}")
print(f"Lowest mark is {lowest_mark} in the subject {lowest_mark_subject}")

# -------- Exercise 3 ----------
words = ["python", "java", "python", "c", "java", "python"]
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

print(words_dict)


# ------- MINI CHALLENGE ---------
products = {"Laptop": 55000, "Phone": 25000, "Headphones": 3000,
            "Keyboard": 1500, "Monitor": 12000}
most_expensive = products["Laptop"]
cheapest = products["Laptop"]
avg_price = 0
product_above_10000 = []
for key, value in products.items():
    if most_expensive <= value:
        most_expensive = value
        expensive_product = key
    if cheapest >= value:
        cheapest = value
        cheapest_product = key
    if value > 10000:
        product_above_10000.append(key)

avg_price = sum(products.values())/len(products)

print(f"Most expensive product: {expensive_product}\nprice:{most_expensive}")
print(f"Cheapest product : {cheapest_product}\nprice:{cheapest}")
print("Average price: ",avg_price)
print("Products costing more than ₹10,000",product_above_10000)


print("\nMission Day 11 Completed Successfully!")