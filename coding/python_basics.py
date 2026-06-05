# Python Basics - Q1 to Q50

## Q1. Find Data Type

```python
x = 10
print(type(x))
# Output: <class 'int'>
```

## Q2. String to Integer

```python
num = "100"
print(int(num) + 50)
# Output: 150
```

## Q3. Integer to String

```python
num = 100
print(str(num) + " apples")
# Output: 100 apples
```

## Q4. Swap Two Variables

```python
a, b = 5, 10
a, b = b, a
print(a, b)
# Output: 10 5
```

## Q5. Check Variable Type

```python
x = [1, 2, 3]
print(isinstance(x, list))
# Output: True
```

## Q6. Reverse a String

```python
text = "python"
print(text[::-1])
# Output: nohtyp
```

## Q7. Check Palindrome

```python
text = "madam"
print(text == text[::-1])
# Output: True
```

## Q8. Count Vowels

```python
text = "data analyst"
count = sum(1 for c in text.lower() if c in "aeiou")
print(count)
# Output: 4
```

## Q9. Count Consonants

```python
text = "python"
count = sum(1 for c in text if c.isalpha() and c.lower() not in "aeiou")
print(count)
# Output: 4
```

## Q10. Count Words

```python
sentence = "I love data analytics"
print(len(sentence.split()))
# Output: 4
```

## Q11. Remove Spaces

```python
text = "data analyst"
print(text.replace(" ", ""))
# Output: dataanalyst
```

## Q12. Find Duplicate Characters

```python
text = "programming"
duplicates = {c for c in text if text.count(c) > 1}
print(duplicates)
# Output: {'r', 'g', 'm'}
```

## Q13. First Non-Repeating Character

```python
text = "swiss"

for c in text:
    if text.count(c) == 1:
        print(c)
        break

# Output: w
```

## Q14. Check Anagram

```python
a = "listen"
b = "silent"

print(sorted(a) == sorted(b))
# Output: True
```

## Q15. Character Frequency

```python
text = "apple"
freq = {c: text.count(c) for c in text}

print(freq)
```
# Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

## Q16. Capitalize Every Word

```python
text = "data analyst"
print(text.title())
# Output: Data Analyst
```

## Q17. Find Longest Word

```python
sentence = "I love business analytics"

print(max(sentence.split(), key=len))
# Output: analytics
```

## Q18. Count Substring Occurrences

```python
text = "banana"
print(text.count("an"))
# Output: 2
```

## Q19. Replace Word

```python
text = "I love SQL"
print(text.replace("SQL", "Python"))
# Output: I love Python
```

## Q20. Check If String Contains Only Digits

```python
text = "12345"
print(text.isdigit())
# Output: True
```

## Q21. Find Largest Element

```python
numbers = [10, 20, 50, 30]
print(max(numbers))
# Output: 50
```

## Q22. Find Smallest Element

```python
numbers = [10, 20, 50, 30]
print(min(numbers))
# Output: 10
```

## Q23. Find Second Largest Element

```python
numbers = [10, 20, 50, 30]

numbers = sorted(set(numbers))

print(numbers[-2])
# Output: 30
```

## Q24. Remove Duplicates While Preserving Order

```python
numbers = [1, 2, 2, 3, 1, 4]

result = []

for n in numbers:
    if n not in result:
        result.append(n)

print(result)
# Output: [1, 2, 3, 4]
```

## Q25. Find Common Elements Between Two Lists

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(list(set(a) & set(b)))
# Output: [3, 4]
```

## Q26. Merge Two Lists

```python
a = [1, 2]
b = [3, 4]

print(a + b)

# Output: [1, 2, 3, 4]
```

## Q27. Flatten a Nested List

```python
nested = [[1, 2], [3, 4], [5, 6]]

flat = []

for sublist in nested:
    flat.extend(sublist)

print(flat)

# Output: [1, 2, 3, 4, 5, 6]
```

## Q28. Reverse a List

```python
numbers = [1, 2, 3, 4]

print(numbers[::-1])

# Output: [4, 3, 2, 1]
```

## Q29. Sort a List

```python
numbers = [4, 1, 3, 2]

numbers.sort()

print(numbers)

# Output: [1, 2, 3, 4]
```

## Q30. Find Frequency of List Elements

```python
numbers = [1, 2, 2, 3, 3, 3]

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print(freq)

# Output: {1: 1, 2: 2, 3: 3}
```

## Q31. Count Frequencies Using Dictionary

```python
items = ["apple", "banana", "apple"]

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print(freq)

# Output: {'apple': 2, 'banana': 1}
```

## Q32. Merge Two Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}

result = {**d1, **d2}

print(result)

# Output: {'a': 1, 'b': 2, 'c': 3}
```

## Q33. Sort Dictionary by Value

```python
sales = {"A": 300, "B": 100, "C": 200}

result = sorted(sales.items(), key=lambda x: x[1])

print(result)

# Output: [('B', 100), ('C', 200), ('A', 300)]
```

## Q34. Find Key with Maximum Value

```python
sales = {"A": 300, "B": 100, "C": 500}

print(max(sales, key=sales.get))

# Output: C
```

## Q35. Invert a Dictionary

```python
d = {"a": 1, "b": 2}

result = {v: k for k, v in d.items()}

print(result)

# Output: {1: 'a', 2: 'b'}
```

## Q36. Group Records Using Dictionary

```python
employees = [
    ("IT", "John"),
    ("HR", "Alice"),
    ("IT", "Bob")
]

groups = {}

for dept, name in employees:
    groups.setdefault(dept, []).append(name)

print(groups)

# Output: {'IT': ['John', 'Bob'], 'HR': ['Alice']}
```

## Q37. Access Nested Dictionary

```python
employee = {
    "name": "John",
    "address": {
        "city": "Hyderabad"
    }
}

print(employee["address"]["city"])

# Output: Hyderabad
```

## Q38. Union of Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Output: {1, 2, 3, 4, 5}
```

## Q39. Intersection of Sets

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)

# Output: {2, 3}
```

## Q40. Difference of Sets

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)

# Output: {1}
```

## Q41. Function to Calculate Average

```python
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))

# Output: 20.0
```

## Q42. Function with Default Arguments

```python
def greet(name="Guest"):
    print("Hello", name)

greet()

# Output: Hello Guest
```

## Q43. Lambda Function

```python
square = lambda x: x * x

print(square(5))

# Output: 25
```

## Q44. map()

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)

# Output: [2, 4, 6, 8]
```

## Q45. filter()

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output: [2, 4, 6]
```

## Q46. zip()

```python
names = ["John", "Alice"]
scores = [80, 90]

result = list(zip(names, scores))

print(result)

# Output: [('John', 80), ('Alice', 90)]
```

## Q47. enumerate()

```python
names = ["John", "Alice"]

for index, value in enumerate(names):
    print(index, value)

# Output:
# 0 John
# 1 Alice
```

## Q48. Read a CSV File

```python
import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head())

# Output:
# First 5 rows of the file
```

## Q49. Handle Division by Zero

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output: Cannot divide by zero
```

## Q50. Handle File Not Found

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")

# Output: File not found
```
