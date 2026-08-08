"""
Mission Day 12
Topic: Functions and Problem Solving

Concepts Learned:
- Functions
- Parameters
- Return values
- Lists
- Dictionaries
- Problem decomposition
"""
# --------- Exercise 1 --------
def check_even_odd(number):
    if number % 2 == 0:
        print("Even number")
    elif number % 2 != 0:
        print("Odd number")
    return

check_even_odd(35)
check_even_odd(60)
check_even_odd(9)
check_even_odd(18)   

# ----------- Exercise 2 --------
def find_max(numbers):
    largest_num = numbers[0]
    for num in numbers:
        if largest_num <= num:
            largest_num = num
    return largest_num

print(find_max([15, 72, 31, 94, 28]))

# ----------- Exercise 3 --------
def calculate_average(numbers):
    avg = sum(numbers)/len(numbers)
    return avg

print(calculate_average([80, 70, 90, 60]))

# ----------- Exercise 4 --------
def count_positive_negative(numbers):
    count_positive = 0
    count_negative = 0
    for num in numbers:
        if num >= 0:
            count_positive += 1
        elif num < 0:
            count_negative += 1
    return count_positive, count_negative

print(count_positive_negative([10, -5, 8, -2, 0, 7, -9]))

# -------- MINI CHALLENGE --------
sales = {
    "Laptop": 5,
    "Phone": 12,
    "Headphones": 20,
    "Keyboard": 8,
    "Monitor": 7
}

def total_sales(sales):
    print("Total units sold: ",sum(sales.values()))
    return

def best_selling_product(sales):
    highest_product_units = 0
    for key, value in sales.items():
        if highest_product_units <= value:
            highest_product_units = value
            highest_selling_product = key
    print("Best-selling product:",highest_selling_product)
    print("Units sold:",highest_product_units)
    return

def products_above_10(sales):
    units_saled_above_10 = []
    for key, value in sales.items():
        if value > 10:
            units_saled_above_10.append(key)
    return units_saled_above_10

def average_sales(sales):
    average = sum(sales.values())/len(sales)
    return average

total_sales(sales)
best_selling_product(sales)
print(products_above_10(sales))
print(average_sales(sales))

print("\nMission Day 12 Completed Successfully!")