# 1. Factorial Using Loop
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(input("Enter number: "))
print(factorial(n))


# 2. Sum of First N Natural Numbers Using Recursion
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

n = int(input("Enter number: "))
print(total(n))


# 3. Reverse String Using Recursion
def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]

s = input("Enter string: ")
print(reverse(s))


# 4. Power Using Recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = int(input("Enter base: "))
n = int(input("Enter power: "))
print(power(x, n))
