# day4 coding Exercise

# Exercise 1
for i in range(5):
    print("Hello Python")

# Exercise 2
print("\n")
for i in range(1,21):
    print(i,end = ",")

# Exercise 3
print("\n")
n = 1
while n < 50 :
    if n % 2 == 0:
        print(n,end = ",")
    n += 1

# Exercise 4
print("\n")
num = int(input("Enter a number : "))
i = 1
while i < 11:
    print(f"{num} * {i} = {num * i}")
    i += 1

# Exercise 5
print("\n")
n = int(input("Enter a number : "))
total = 0
for i in range(1,n+1):
    total += i
print(f" sum of first {n} numbers = {total}")


# ----- MINI CHALLENGE -----
print("\n")
password = "python123"
entered_pass = input("Enter the password : ")

while password != entered_pass:
    print("incorrect password,Try again!")
    entered_pass = input("Enter the password : ")
print("you entered the password correctly and the password is : ",password)