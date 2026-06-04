Q1. Find the data type of a variable

Question: Determine the data type of a variable.

x = 10
print(type(x))

Output

<class 'int'>
Q2. Convert String to Integer
num = "100"
num = int(num)
print(num + 50)

Output

150
Q3. Convert Integer to String
num = 100
num = str(num)
print(num + " is a number")

Output

100 is a number
Q4. Swap Two Variables
a = 5
b = 10

a, b = b, a

print(a, b)

Output

10 5
Q5. Check Variable Type
x = [1, 2, 3]

if isinstance(x, list):
    print("List")

Output

List
Q6. Reverse a String
text = "python"
print(text[::-1])

Output

nohtyp
Q7. Check Palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")

Output

Palindrome
Q8. Count Vowels
text = "data analyst"

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)

Output

4
Q9. Count Consonants
text = "python"

count = 0

for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        count += 1

print(count)

Output

4
Q10. Count Words
sentence = "I love data analytics"
print(len(sentence.split()))

Output

4
Q11. Remove Spaces
text = "data analyst"
print(text.replace(" ", ""))

Output

dataanalyst
Q12. Find Duplicate Characters
text = "programming"

duplicates = set()

for char in text:
    if text.count(char) > 1:
        duplicates.add(char)

print(duplicates)

Output

{'r', 'g', 'm'}
Q13. First Non-Repeating Character
text = "swiss"

for char in text:
    if text.count(char) == 1:
        print(char)
        break

Output

w
Q14. Check Anagram
a = "listen"
b = "silent"

print(sorted(a) == sorted(b))

Output

True
Q15. Character Frequency
text = "apple"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)

Output

{'a': 1, 'p': 2, 'l': 1, 'e': 1}
Q16. Capitalize Every Word
text = "data analyst"
print(text.title())

Output

Data Analyst
Q17. Find Longest Word
sentence = "I love business analytics"

print(max(sentence.split(), key=len))

Output

analytics
Q18. Count Substring Occurrences
text = "banana"
print(text.count("an"))

Output

2
Q19. Replace a Word
text = "I love SQL"
print(text.replace("SQL", "Python"))

Output

I love Python
Q20. Check If String Contains Only Digits
text = "12345"
print(text.isdigit())

Output

True
Q21. Find Largest Element
numbers = [10, 20, 50, 30]
print(max(numbers))

Output

50
Q22. Find Smallest Element
numbers = [10, 20, 50, 30]
print(min(numbers))

Output

10
Q23. Find Second Largest Element
numbers = [10, 20, 50, 30]
numbers.sort()

print(numbers[-2])

Output

30
Q24. Remove Duplicates
numbers = [1,1,2,2,3,4]
print(list(set(numbers)))

Output

[1, 2, 3, 4]
Q25. Common Elements in Two Lists
a = [1,2,3]
b = [2,3,4]

print(list(set(a) & set(b)))

Output

[2, 3]
Q26. Merge Two Lists
a = [1,2]
b = [3,4]

print(a + b)

Output

[1, 2, 3, 4]
Q27. Flatten Nested List
nested = [[1,2],[3,4]]

flat = []

for sublist in nested:
    flat.extend(sublist)

print(flat)

Output

[1, 2, 3, 4]
Q28. Reverse a List
numbers = [1,2,3]
print(numbers[::-1])

Output

[3, 2, 1]
Q29. Sort a List
numbers = [4,1,3,2]
numbers.sort()

print(numbers)

Output

[1, 2, 3, 4]
Q30. Frequency of Elements
numbers = [1,2,2,3,3,3]

freq = {}

for num in numbers:
    freq[num] = freq.get(num,0)+1

print(freq)

Output

{1: 1, 2: 2, 3: 3}
Q31. Find Missing Number

Use sum of expected range minus actual sum.

Output Example

Missing Number = 4
Q32. Find Duplicate Numbers

Output Example

[2, 4]
Q33. Rotate List by K Positions

Output Example

[4, 5, 1, 2, 3]
Q34. Split List into Chunks

Output Example

[[1,2],[3,4],[5,6]]
Q35. Find Pairs with Given Sum

Output Example

[(2,5), (3,4)]
Q36. Count Frequencies Using Dictionary

Output Example

{'apple': 2, 'banana': 1}
Q37. Merge Dictionaries

Output Example

{'a':1,'b':2,'c':3}
Q38. Sort Dictionary by Value

Output Example

[('a',1), ('b',2), ('c',3)]
Q39. Key with Maximum Value

Output Example

sales
Q40. Invert Dictionary

Output Example

{1:'a',2:'b'}
Q41. Union of Sets
{1,2,3,4,5}
Q42. Intersection of Sets
{3,4}
Q43. Difference of Sets
{1,2}
Q44. FizzBuzz

Output

1
2
Fizz
4
Buzz
...
Q45. Prime Number Check

Output

Prime
Q46. Generate Prime Numbers in Range

Output

2 3 5 7 11 13 17 19
Q47. Factorial
import math
print(math.factorial(5))

Output

120
Q48. Fibonacci Series

Output

0 1 1 2 3 5 8 13
Q49. Function to Calculate Average
def average(nums):
    return sum(nums)/len(nums)

print(average([10,20,30]))

Output

20.0
Q50. Employee Class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

Output

John 50000
