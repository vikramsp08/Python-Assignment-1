# 1. Electricity Bill Calculator
u = int(input("Enter units: "))
if u <= 100:
    bill = u * 5
elif u <= 300:
    bill = 500 + (u - 100) * 7
else:
    bill = 1900 + (u - 300) * 10
if bill > 2000:
    bill = bill * 1.05
print("Bill:", bill)


# 2. Loan Approval System
s = int(input("Enter salary: "))
c = int(input("Enter credit score: "))
a = int(input("Enter age: "))
if s >= 30000 and c >= 700 and 21 <= a <= 60:
    print("Approved")
elif s >= 25000 and c >= 650 and 21 <= a <= 60:
    print("Conditionally Approved")
else:
    print("Rejected")


# 3. Number Classification
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# 4. Exam Result Analyzer
marks = []
for i in range(5):
    marks.append(int(input("Enter marks: ")))
p = sum(marks) / 5
print("Percentage:", p)
if min(marks) < 33:
    print("Fail")
elif p >= 60:
    print("First Division")
elif p >= 50:
    print("Second Division")
elif p >= 40:
    print("Third Division")
else:
    print("Fail")
