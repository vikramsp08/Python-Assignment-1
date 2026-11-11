# 1. Math Module
import math
print(math.sqrt(25))
print(math.pow(2, 3))
print(math.factorial(5))
print(math.sin(math.radians(30)))
print(math.cos(math.radians(60)))
print(math.tan(math.radians(45)))


# 2. Random Module
import random
import string
print("OTP:", random.randint(100000, 999999))
password = ""
for i in range(8):
    password += random.choice(string.ascii_letters + string.digits)
print("Password:", password)
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 100))
print(numbers)


# 3. Datetime Module
from datetime import datetime, date
print("Current date and time:", datetime.now())
y = int(input("Enter birth year: "))
m = int(input("Enter birth month: "))
d = int(input("Enter birth day: "))
dob = date(y, m, d)
today = date.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
print("Age:", age)


# 4. Geometry Package - Circle and Rectangle
r = 5
print("Circle area:", math.pi * r * r)
print("Circle circumference:", 2 * math.pi * r)
l = 10
b = 5
print("Rectangle area:", l * b)
print("Rectangle perimeter:", 2 * (l + b))
