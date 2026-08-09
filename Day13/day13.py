"""
Mission Day 13
Topic: Data Processing with Lists and Dictionaries

Concepts Learned:
- List of dictionaries
- Filtering data
- Data processing
- Functions
- Basic statistics
"""
# Data
students = [
    {"name": "Sarath", "marks": 85},
    {"name": "Ravi", "marks": 90},
    {"name": "Abhi", "marks": 72},
    {"name": "Kiran", "marks": 95}
]


# ------  Exercise 1 -------
def display_name(data):
    for i in range(len(data)):
        print(data[i]["name"])
    return

display_name(students)

# -------- Exercise 2 --------
def average_marks(data):
    total = 0
    for i in range(len(data)):
        total += data[i]["marks"]
    avg = total/len(data)
    print("Average marks:",avg)
    return

average_marks(students)

# -------- Exercise 3 --------
def students_above_80(data):
    students_80 = []
    for i in range(len(data)):
        if data[i]["marks"] >= 80:
            students_80.append(data[i]["name"])
    print(students_80)
    return

students_above_80(students)

# -------- Exercise 4 --------
def highest_scorer(data):
    highest_scorer = data[0]["name"]
    highest_mark = data[0]["marks"]
    for student in data:
        if student["marks"] > highest_mark:
            highest_mark = student["marks"]
            highest_scorer = student["name"]
    print("Highest scorer",highest_scorer)
    print("Marks: ",highest_mark)
    return
highest_scorer(students)

# ---------- MAIN CHALLENGE --------
products = [
    {"name": "Laptop", "price": 55000, "sold": 5},
    {"name": "Phone", "price": 25000, "sold": 12},
    {"name": "Headphones", "price": 3000, "sold": 20},
    {"name": "Keyboard", "price": 1500, "sold": 8},
    {"name": "Monitor", "price": 12000, "sold": 7}
]

def total_units_sold(data):
    total_sales = 0
    for product in data:
        total_sales += product["sold"]
    print("Total units sold: ",total_sales)
    return
total_units_sold(products)

def revenue(data):
    total_revenue = 0
    for product in data:
        total_revenue = total_revenue + (product["price"] * product["sold"])
    print("Total revenue: ",total_revenue)
    return
revenue(products)

def best_selling_product(data):
    best_selling = data[0]["name"]
    units_sold = data[0]["sold"]
    for product in data:
            if product["sold"] > units_sold:
                units_sold = product["sold"]
                best_selling = product["name"]
    print("Best-selling product: ",best_selling)
    print("Units sold: ",units_sold)
    return
best_selling_product(products)

def highest_revenue_product(data):
    revenue = data[0]["price"] * data[0]["sold"]
    product_highest_revenue = data[0]["name"] 
    for product in data:
        if (product["price"] * product["sold"]) > revenue:
            revenue = ((product["price"] * product["sold"]))
            product_highest_revenue = product["name"]
    print(product_highest_revenue)
    return
highest_revenue_product(products)

def products_above_10000(data):
    products_10000 = []
    for product in data:
        if product["price"] > 10000:
            products_10000.append(product["name"])
    print(products_10000)
    return

products_above_10000(products)

print("\nMission Day 13 Completed Successfully!")