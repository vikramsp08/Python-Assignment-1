# 1. Age Validation System
age = int(input("Enter age: "))
try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")
except ValueError as e:
    print(e)


# 2. Bank Withdrawal System
balance = 10000
amount = int(input("Enter withdrawal amount: "))
try:
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
    print("Remaining balance:", balance)
except ValueError as e:
    print(e)


# 3. Password Validator Using Custom Exception
class PasswordError(Exception):
    pass

p = input("Enter password: ")
try:
    if len(p) < 8:
        raise PasswordError("Password must contain at least 8 characters")
    if not any(ch.isupper() for ch in p):
        raise PasswordError("Password must contain an uppercase letter")
    if not any(ch.isdigit() for ch in p):
        raise PasswordError("Password must contain a number")
    print("Valid Password")
except PasswordError as e:
    print(e)
