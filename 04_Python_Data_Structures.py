# 1. List Rotation
a = [1, 2, 3, 4, 5]
k = int(input("Enter k: "))
k = k % len(a)
print("Left:", a[k:] + a[:k])
print("Right:", a[-k:] + a[:-k] if k else a[:])


# 2. Remove Duplicates Without Set
a = [1, 2, 3, 2, 4, 1, 5]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)


# 3. Find Missing Number
a = [1, 2, 3, 5, 6]
n = 6
print("Missing number:", n * (n + 1) // 2 - sum(a))


# 4. Tuple of 5 Subjects
t = ("Python", "Java", "C++", "DBMS", "OS")
print(t[2])
print(len(t))
print(t.index("DBMS"))


# 5. Convert Tuple to Dictionary
t = ((1, "A"), (2, "B"))
d = dict(t)
print(d)


# 6. Tuple Unpacking - Swap First and Last
t = (10, 20, 30, 40, 50)
a, *middle, b = t
t = (b, *middle, a)
print(t)


# 7. Subset Checker
a = {1, 2}
b = {1, 2, 3, 4}
if a.issubset(b):
    print("Subset")
else:
    print("Not Subset")


# 8. Student Marks Analyzer
students = {"Rahul": 85, "Aman": 45, "Vikram": 92, "Rohit": 28}
topper = max(students, key=students.get)
print("Topper:", topper)
print("Average:", sum(students.values()) / len(students))
for name, marks in students.items():
    if marks < 33:
        print("Fail:", name)


# 9. Library Management Using Dictionary
library = {"Python": 5, "Java": 3, "C++": 4}
book = input("Enter book name: ")
if book in library:
    print("Quantity:", library[book])
else:
    print("Book not found")
print(library)
