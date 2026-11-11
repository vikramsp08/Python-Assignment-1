# 1. Palindrome String Check
s = input("Enter string: ")
s = s.replace(" ", "").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 2. Find the Longest Word
s = input("Enter sentence: ")
words = s.split()
if words:
    print("Longest word:", max(words, key=len))
else:
    print("No words")


# 3. Check Anagram
a = input("Enter first string: ").replace(" ", "").lower()
b = input("Enter second string: ").replace(" ", "").lower()
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")


# 4. Remove Duplicate Characters
s = input("Enter string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)


# 5. String Compression
s = input("Enter string: ")
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1
if s:
    result += s[-1] + str(count)
print(result)
