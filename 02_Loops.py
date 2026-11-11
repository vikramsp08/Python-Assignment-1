# 1. Automorphic Number
n = int(input("Enter number: "))
if str(n * n).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")


# 2. Palindrome Number Series
a = int(input("Enter start: "))
b = int(input("Enter end: "))
for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        print(i)


# 3. LCM and HCF Using Loops
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i
lcm = abs(a * b) // hcf
print("HCF:", hcf)
print("LCM:", lcm)


# 4. Password Retry System
password = "python123"
for i in range(3):
    p = input("Enter password: ")
    if p == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
else:
    print("Account Blocked")


# 5. Triangle Pattern
for i in range(1, 6):
    print("*" * i)

# 6. Pyramid Pattern
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# 7. Diamond Pattern
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)
