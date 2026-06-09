# Python Basics - Q1 to Q50

# Q1. Find Data Type
x = 10
print(type(x))            # <class 'int'>
print(isinstance(x, int)) # True

# Q2. String to Integer
num = "100"
print(int(num) + 50)    # 150
print(float(num) + 50)  # 150.0

# Q3. Integer to String
num = 100
print(str(num) + " apples")    # 100 apples
print(f"{num} apples")         # 100 apples

# Q4. Swap Two Variables
a, b = 5, 10
a, b = b, a
print(a, b)   # 10 5

a, b = 5, 10
temp = a; a = b; b = temp
print(a, b)   # 10 5

# Q5. Check Variable Type
x = [1, 2, 3]
print(isinstance(x, list))   # True
print(type(x) == list)       # True

# Q6. Reverse a String
text = "python"
print(text[::-1])                 # nohtyp
print("".join(reversed(text)))    # nohtyp

# Q7. Check Palindrome
text = "madam"
print(text == text[::-1])   # True
def is_palindrome(s): return s == s[::-1]
print(is_palindrome("madam"))   # True

# Q8. Count Vowels
text = "data analyst"
print(sum(1 for c in text.lower() if c in "aeiou"))   # 4
print(len([c for c in text.lower() if c in "aeiou"])) # 4

# Q9. Count Consonants
text = "python"
print(sum(1 for c in text if c.isalpha() and c.lower() not in "aeiou"))   # 4
print(len([c for c in text if c.isalpha() and c.lower() not in "aeiou"])) # 4

# Q10. Count Words
sentence = "I love data analytics"
print(len(sentence.split()))   # 4
import re; print(len(re.findall(r'\w+', sentence)))   # 4

# Q11. Remove Spaces
text = "data analyst"
print(text.replace(" ", ""))   # dataanalyst
print("".join(text.split()))   # dataanalyst

# Q12. Find Duplicate Characters
text = "programming"
print({c for c in text if text.count(c) > 1})   # {'r','g','m'}
print([c for c in set(text) if text.count(c) > 1])   # ['r','g','m']

# Q13. First Non-Repeating Character
text = "swiss"
for c in text:
    if text.count(c) == 1:
        print(c); break
# Alternative using collections
from collections import Counter
cnt = Counter(text)
print([c for c in text if cnt[c] == 1][0])   # w

# Q14. Check Anagram
a, b = "listen", "silent"
print(sorted(a) == sorted(b))   # True
print(set(a) == set(b) and len(a) == len(b)) # True

# Q15. Character Frequency
text = "apple"
print({c: text.count(c) for c in text})
from collections import Counter
print(dict(Counter(text)))

# Q16. Capitalize Every Word
text = "data analyst"
print(text.title())   # Data Analyst
print(" ".join(w.capitalize() for w in text.split()))

# Q17. Find Longest Word
sentence = "I love business analytics"
print(max(sentence.split(), key=len))   # analytics
words = sentence.split()
print(sorted(words, key=len)[-1])       # analytics

# Q18. Count Substring Occurrences
text = "banana"
print(text.count("an"))   # 2
print(len([i for i in range(len(text)) if text.startswith("an", i)]))   # 2

# Q19. Replace Word
text = "I love SQL"
print(text.replace("SQL", "Python"))
print(text[:7] + "Python")

# Q20. Check Digits
text = "12345"
print(text.isdigit())   # True
print(all(c.isdigit() for c in text))   # True

# Q21. Largest Element
numbers = [10,20,50,30]
print(max(numbers))   # 50
print(sorted(numbers)[-1])   # 50

# Q22. Smallest Element
numbers = [10,20,50,30]
print(min(numbers))   # 10
print(sorted(numbers)[0])    # 10

# Q23. Second Largest
numbers = [10,20,50,30]
print(sorted(set(numbers))[-2])   # 30
numbers.sort(); print(numbers[-2]) # 30

# Q24. Remove Duplicates Preserve Order
numbers = [1,2,2,3,1,4]
result=[]
for n in numbers:
    if n not in result: result.append(n)
print(result)
print(list(dict.fromkeys(numbers)))   # [1,2,3,4]

# Q25. Common Elements
a,b=[1,2,3,4],[3,4,5,6]
print(list(set(a)&set(b)))   # [3,4]
print([x for x in a if x in b])   # [3,4]

# Q26. Merge Lists
a,b=[1,2],[3,4]
print(a+b)
print([*a,*b])

# Q27. Flatten Nested List
nested=[[1,2],[3,4],[5,6]]
flat=[]
for sub in nested: flat.extend(sub)
print(flat)
print([x for sub in nested for x in sub])

# Q28. Reverse List
numbers=[1,2,3,4]
print(numbers[::-1])
numbers.reverse(); print(numbers)

# Q29. Sort List
numbers=[4,1,3,2]
numbers.sort(); print(numbers)
print(sorted(numbers, reverse=True))

# Q30. Frequency of List Elements
numbers=[1,2,2,3,3,3]
freq={}
for n in numbers: freq[n]=freq.get(n,0)+1
print(freq)
from collections import Counter
print(dict(Counter(numbers)))

# Q31. Count Frequencies
items=["apple","banana","apple"]
freq={}
for i in items: freq[i]=freq.get(i,0)+1
print(freq)
from collections import Counter
print(dict(Counter(items)))

# Q32. Merge Dictionaries
d1,d2={"a":1,"b":2},{"c":3}
print({**d1,**d2})
d1.update(d2); print(d1)

# Q33. Sort Dict by Value
sales={"A":300,"B":100,"C":200}
print(sorted(sales.items(), key=lambda x:x[1]))
print(dict(sorted(sales.items(), key=lambda x:x[1])))

# Q34. Key with Max Value
sales={"A":300,"B":100,"C":500}
print(max(sales, key=sales.get))
print(max(sales.items(), key=lambda x:x[1])[0])

# Q35. Invert Dictionary
d={"a":1,"b":2}
print({v:k for k,v in d.items()})
print(dict(zip(d.values(), d.keys())))

# Q36. Group Records
employees=[("IT","John"),("HR","Alice"),("IT","Bob")]
groups={}
for dept,name in employees: groups.setdefault(dept,[]).append(name)
print(groups)
from collections import defaultdict
dd=defaultdict(list)
for dept,name in employees: dd[dept].append(name)
print(dict(dd))

# Q37. Access Nested Dict
employee={"name":"John","address":{"city":"Hyderabad"}}
print(employee["address"]["city"])
print(employee.get("address",{}).get("city"))

# Q38. Union of Sets
a,b={1,2,3},{3,4,5}
print(a|b)
print(a.union(b))

# Q39. Intersection of Sets
a,b={1,2,3},{2,3,4}
print(a&b)
print(a.intersection(b))

# Q40. Difference of Sets
a,b={1,2,3},{2,3,4}
print(a-b)
print(a.difference(b))

# Q41. Function Average
def average(nums): return sum(nums)/len(nums)
print(average([10,20,30]))
print(sum([10,20,30])/3)

# Q42. Function Default Args
def greet(name="Guest"): print("Hello",name)
greet()
greet("Alice")

# Q43. Lambda Function
square=lambda x:x*x
print(square(5))
print((lambda x:x**2)(6))

# Q44. map()
numbers=[1,2,3,4]
print(list(map(lambda x:x*2,numbers)))
print([x*2 for x in numbers])

# Q45. filter()
numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, numbers)))   # [2,4,6]
print([x for x in numbers if x % 2 == 0])            # [2,4,6]

# Q46. zip()
names = ["John", "Alice"]
scores = [80, 90]
print(list(zip(names, scores)))   # [('John', 80), ('Alice', 90)]
print(dict(zip(names, scores)))   # {'John': 80, 'Alice': 90}

# Q47. enumerate()
names = ["John", "Alice"]
for index, value in enumerate(names):
    print(index, value)
# 0 John
# 1 Alice

# Alternative: start index at 1
for index, value in enumerate(names, start=1):
    print(index, value)
# 1 John
# 2 Alice

# Q48. Read a CSV File
import pandas as pd
df = pd.read_csv("employees.csv")
print(df.head())   # First 5 rows

# Alternative: using csv module
import csv
with open("employees.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Q49. Handle Division by Zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Alternative: check before dividing
a, b = 10, 0
if b == 0:
    print("Cannot divide by zero")
else:
    print(a / b)

# Q50. Handle File Not Found
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")

# Alternative: using pathlib
from pathlib import Path
path = Path("data.txt")
if path.exists():
    print(path.read_text())
else:
    print("File not found")
