# Python Concepts for Data Analyst Interviews

## 1. What are Python's built-in data types?

Python provides built-in data types such as int, float, str, bool, list, tuple, set, and dict. These data types are used to store different kinds of values. Each type supports specific operations and methods. Choosing the appropriate data type improves code readability and efficiency.

**Example:**

```python
age = 25
salary = 50000.50
name = "John"
is_active = True

print(type(age))
print(type(salary))
print(type(name))
print(type(is_active))
```

**Output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

## 2. What is the difference between mutable and immutable objects?

Mutable objects can be modified after creation, while immutable objects cannot. Changes to immutable objects create a new object in memory. Lists, dictionaries, and sets are mutable, whereas strings, tuples, integers, and floats are immutable. This behavior impacts memory usage and object references.

**Example:**

```python
my_list = [1, 2]
my_list.append(3)

name = "John"
name = name + " Doe"

print(my_list)
print(name)
```

**Output:**

```text
[1, 2, 3]
John Doe
```

---

## 3. What is dynamic typing in Python?

Python is dynamically typed, meaning the data type of a variable is determined at runtime. Variables do not need explicit type declarations. A variable can hold different types of values during program execution. This flexibility makes Python easy to write and maintain.

**Example:**

```python
value = 100
print(type(value))

value = "Python"
print(type(value))
```

**Output:**

```text
<class 'int'>
<class 'str'>
```

---

## 4. What is type casting?

Type casting is the process of converting one data type into another. Python provides functions such as int(), float(), str(), and bool() for conversion. It is commonly used while cleaning or transforming data. Invalid conversions may result in exceptions.

**Example:**

```python
salary = "50000"

salary_int = int(salary)

print(salary_int)
print(type(salary_int))
```

**Output:**

```text
50000
<class 'int'>
```

---

## 5. What is None in Python?

None represents the absence of a value. It is a special object of type NoneType. Functions that do not explicitly return a value return None by default. It is often used as a placeholder or default value.

**Example:**

```python
result = None

print(result)
print(type(result))
```

**Output:**

```text
None




## 6. What is a string in Python?

A string is a sequence of characters enclosed within single quotes, double quotes, or triple quotes. Strings are used to store and manipulate textual data. They support numerous built-in methods for searching, formatting, and cleaning text. Strings are immutable objects in Python.

**Example:**

```python
name = "Data Analyst"

print(name)
print(len(name))
```

**Output:**

```text
Data Analyst
12
```

---

## 7. Why are strings immutable?

Strings cannot be modified after they are created. Any operation that appears to change a string actually creates a new string object in memory. Immutability improves data integrity and memory optimization. It also allows strings to be used as dictionary keys.

**Example:**

```python
name = "John"

name = name.replace("John", "David")

print(name)
```

**Output:**

```text
David
```

---

## 8. What is the difference between split() and join()?

split() breaks a string into a list based on a specified delimiter. join() combines elements from an iterable into a single string. These methods are commonly used in data cleaning and preprocessing tasks. They are especially useful when handling CSV and text data.

**Example:**

```python
text = "A,B,C"

items = text.split(",")

result = "-".join(items)

print(items)
print(result)
```

**Output:**

```text
['A', 'B', 'C']
A-B-C
```

---

## 9. What does strip() do?

strip() removes leading and trailing whitespace characters from a string. It helps clean unwanted spaces that may exist in imported data. Variants such as lstrip() and rstrip() remove whitespace from one side only. The original string remains unchanged.

**Example:**

```python
name = "   John   "

print(name.strip())
```

**Output:**

```text
John
```

---

## 10. What does replace() do?

replace() substitutes occurrences of a specified substring with another substring. It returns a new string without modifying the original object. This method is commonly used for standardizing inconsistent text values. Multiple occurrences can be replaced in a single operation.

**Example:**

```python
city = "New Delhi"

city = city.replace("New", "Old")

print(city)
```

**Output:**

```text
Old Delhi
```

---

## 11. What is a list in Python?

A list is an ordered and mutable collection that can store multiple values. Lists allow duplicate elements and can contain different data types. They support indexing, slicing, and various modification operations. Lists are one of the most frequently used data structures in Python.

**Example:**

```python
employees = ["John", "Emma", "David"]

print(employees)
print(employees[1])
```

**Output:**

```text
['John', 'Emma', 'David']
Emma
```

---

## 12. What is the difference between append() and extend()?

append() adds a single element to the end of a list. extend() adds each element from an iterable individually. append() can create nested lists, whereas extend() merges values into the existing list. Both methods modify the original list.

**Example:**

```python
numbers = [1, 2]

numbers.append([3, 4])
print(numbers)

numbers = [1, 2]

numbers.extend([3, 4])
print(numbers)
```

**Output:**

```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```

---

## 13. What is the difference between remove() and pop()?

remove() deletes the first occurrence of a specified value from a list. pop() removes an element based on its index and returns the removed value. remove() works with values, whereas pop() works with positions. Both modify the original list.

**Example:**

```python
numbers = [10, 20, 30]

numbers.remove(20)
print(numbers)

removed = numbers.pop()

print(removed)
print(numbers)
```

**Output:**

```text
[10, 30]
30
[10]
```

---

## 14. What is the difference between sort() and sorted()?

sort() sorts a list in place and modifies the original list. sorted() returns a new sorted object without changing the original iterable. Both support ascending and descending sorting. sorted() can be used with tuples, sets, and other iterables.

**Example:**

```python
numbers = [3, 1, 2]

print(sorted(numbers))
print(numbers)

numbers.sort()
print(numbers)
```

**Output:**

```text
[1, 2, 3]
[3, 1, 2]
[1, 2, 3]
```

---

## 15. What is list comprehension?

List comprehension is a concise way to create lists using a single expression. It combines iteration and optional conditions into one statement. It improves readability and often performs better than traditional loops. It is commonly used for data transformation.

**Example:**

```python
squares = [x**2 for x in range(5)]

print(squares)
```

**Output:**

```text
[0, 1, 4, 9, 16]
```


## 16. What is a tuple?

A tuple is an ordered and immutable collection of elements. It can store values of different data types and allows duplicate elements. Once created, a tuple cannot be modified. Tuples are commonly used when data should remain unchanged.

**Example:**

```python
coordinates = (10, 20, 30)

print(coordinates)
print(coordinates[0])
```

**Output:**

```text
(10, 20, 30)
10
```

---

## 17. What is the difference between a list and a tuple?

Lists are mutable, whereas tuples are immutable. Both support indexing, slicing, and storing multiple values. Tuples generally use less memory and offer slightly better performance. Lists are preferred when data needs to be modified frequently.

**Example:**

```python
my_list = [1, 2, 3]
my_list.append(4)

my_tuple = (1, 2, 3)

print(my_list)
print(my_tuple)
```

**Output:**

```text
[1, 2, 3, 4]
(1, 2, 3)
```

---

## 18. What is tuple packing and unpacking?

Tuple packing refers to storing multiple values in a tuple. Tuple unpacking extracts tuple elements into separate variables. It simplifies assignment and improves code readability. The number of variables should generally match the number of values.

**Example:**

```python
employee = ("John", 50000, "IT")

name, salary, department = employee

print(name)
print(salary)
print(department)
```

**Output:**

```text
John
50000
IT
```

---

## 19. What is a dictionary?

A dictionary is a mutable collection of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries provide fast lookup and retrieval operations. They are widely used for storing structured data.

**Example:**

```python
employee = {
    "name": "John",
    "salary": 50000
}

print(employee["name"])
```

**Output:**

```text
John
```

---

## 20. What are dictionary keys?

Dictionary keys uniquely identify values stored in a dictionary. Keys must be immutable and hashable objects. Duplicate keys are not allowed because each key must map to a single value. Strings, integers, and tuples are common key types.

**Example:**

```python
employee = {
    "id": 101,
    "name": "John"
}

print(employee.keys())
```

**Output:**

```text
dict_keys(['id', 'name'])
```

---

## 21. What is the difference between get() and [] in dictionaries?

The [] operator directly accesses a value using its key and raises a KeyError if the key does not exist. The get() method safely retrieves values and returns None or a specified default value when the key is missing. This makes get() useful when handling uncertain data.

**Example:**

```python
employee = {
    "name": "John"
}

print(employee.get("salary"))
print(employee.get("salary", 0))
```

**Output:**

```text
None
0
```

---

## 22. What do keys(), values(), and items() return?

keys() returns all dictionary keys, values() returns all stored values, and items() returns key-value pairs. These methods provide dictionary views that can be iterated over efficiently. They are commonly used when processing dictionary data.

**Example:**

```python
employee = {
    "name": "John",
    "salary": 50000
}

print(employee.keys())
print(employee.values())
print(employee.items())
```

**Output:**

```text
dict_keys(['name', 'salary'])
dict_values(['John', 50000])
dict_items([('name', 'John'), ('salary', 50000)])
```

---

## 23. What is dictionary comprehension?

Dictionary comprehension provides a concise way to create dictionaries using a single expression. It combines looping and optional conditions into one statement. It improves readability and reduces the amount of code required. It is similar to list comprehension.

**Example:**

```python
squares = {
    x: x**2
    for x in range(1, 4)
}

print(squares)
```

**Output:**

```text
{1: 1, 2: 4, 3: 9}
```

---

## 24. What is a set?

A set is an unordered collection of unique elements. Duplicate values are automatically removed when a set is created. Sets support mathematical operations such as union and intersection. They are useful for membership testing and duplicate removal.

**Example:**

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

**Output:**

```text
{1, 2, 3, 4}
```

---

## 25. What is the difference between a set and a list?

Lists preserve order and allow duplicate values, whereas sets store only unique values and do not support indexing. Sets generally provide faster membership checks. They are commonly used when uniqueness is more important than order.

**Example:**

```python
numbers_list = [1, 2, 2, 3]

numbers_set = {1, 2, 2, 3}

print(numbers_list)
print(numbers_set)
```

**Output:**

```text
[1, 2, 2, 3]
{1, 2, 3}
```


## 26. What is union in sets?

Union combines all unique elements from two or more sets into a single set. Duplicate values appear only once in the result. It can be performed using the union() method or the | operator. Union is useful when merging distinct categories or records.

**Example:**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

---

## 27. What is intersection in sets?

Intersection returns only the elements that are common between two or more sets. It can be performed using the intersection() method or the & operator. Elements not present in all sets are excluded. It is useful for finding overlapping records.

**Example:**

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))
```

**Output:**

```text
{2, 3}
```

---

## 28. What is difference in sets?

Difference returns elements that exist in one set but not in another. The operation is directional, meaning changing the order may produce different results. It can be performed using the difference() method or the - operator. It helps identify unique records between datasets.

**Example:**

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.difference(set2))
```

**Output:**

```text
{1}
```

---

## 29. What is a function in Python?

A function is a reusable block of code designed to perform a specific task. Functions help reduce code duplication and improve readability. They can accept inputs, process data, and return outputs. Functions make programs easier to maintain and test.

**Example:**

```python
def greet():
    return "Hello"

print(greet())
```

**Output:**

```text
Hello
```

---

## 30. What is the difference between parameters and arguments?

Parameters are variables defined in a function declaration, while arguments are the actual values passed during a function call. Parameters act as placeholders for incoming data. Arguments provide the values used during execution. Understanding this distinction is important when designing reusable functions.

**Example:**

```python
def greet(name):   # parameter
    return f"Hello {name}"

print(greet("John"))   # argument
```

**Output:**

```text
Hello John
```

---

## 31. What is a return statement?

The return statement sends a value back to the caller of a function. It immediately terminates function execution once encountered. A function can return any Python object, including numbers, strings, lists, or dictionaries. If no return statement is provided, the function returns None.

**Example:**

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

**Output:**

```text
30
```

---

## 32. What are default arguments?

Default arguments are parameter values assigned during function definition. They are used automatically when the caller does not provide a value. Default arguments make functions more flexible and reduce repetitive code. They help avoid creating multiple versions of the same function.

**Example:**

```python
def greet(name="Guest"):
    return f"Hello {name}"

print(greet())
print(greet("Emma"))
```

**Output:**

```text
Hello Guest
Hello Emma
```

---

## 33. What are *args?

*args allows a function to accept a variable number of positional arguments. The arguments are collected into a tuple within the function. This is useful when the number of inputs is unknown beforehand. It increases function flexibility.

**Example:**

```python
def total(*args):
    return sum(args)

print(total(10, 20, 30))
```

**Output:**

```text
60
```

---

## 34. What are **kwargs?

**kwargs allows a function to accept a variable number of keyword arguments. The arguments are collected into a dictionary inside the function. It is useful when handling dynamic input parameters. This approach makes functions highly configurable.

**Example:**

```python
def display(**kwargs):
    print(kwargs)

display(name="John", salary=50000)
```

**Output:**

```text
{'name': 'John', 'salary': 50000}
```

---

## 35. What is variable scope?

Variable scope determines where a variable can be accessed within a program. Local variables exist only inside the function where they are created. Global variables can be accessed throughout the module. Proper scope management helps prevent unintended modifications and naming conflicts.

**Example:**

```python
name = "Global"

def show():
    name = "Local"
    print(name)

show()
print(name)
```

**Output:**

```text
Local
Global
```


## 36. What is a lambda function?

A lambda function is a small anonymous function defined using the lambda keyword. It can accept multiple arguments but contains only one expression. Lambda functions are commonly used when a simple function is required for a short duration. They are frequently used with map(), filter(), and sorting operations.

**Example:**

```python
square = lambda x: x ** 2

print(square(5))
```

**Output:**

```text
25
```

---

## 37. What is map()?

map() applies a function to every element of an iterable and returns a map object containing the transformed values. It is useful when the same operation needs to be performed on multiple records. The original iterable remains unchanged. The result is often converted into a list for display.

**Example:**

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

**Output:**

```text
[2, 4, 6, 8]
```

---

## 38. What is filter()?

filter() selects elements from an iterable that satisfy a specified condition. It returns a filter object containing only the matching values. The filtering condition is usually defined using a function or lambda expression. It is commonly used during data cleaning and preprocessing.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

**Output:**

```text
[2, 4]
```

---

## 39. What is the difference between map() and filter()?

map() transforms every element in an iterable and returns the transformed values. filter() evaluates a condition and returns only the elements that satisfy it. map() changes data, while filter() reduces data. Both return iterator objects in Python 3.

**Example:**

```python
numbers = [1, 2, 3, 4]

mapped = list(map(lambda x: x * 10, numbers))
filtered = list(filter(lambda x: x > 2, numbers))

print(mapped)
print(filtered)
```

**Output:**

```text
[10, 20, 30, 40]
[3, 4]
```

---

## 40. What is zip()?

zip() combines elements from multiple iterables into tuples based on their positions. The resulting iterator stops when the shortest iterable is exhausted. It is useful when processing related datasets together. The output can be converted into lists, dictionaries, or tuples.

**Example:**

```python
names = ["John", "Emma"]
scores = [85, 90]

result = list(zip(names, scores))

print(result)
```

**Output:**

```text
[('John', 85), ('Emma', 90)]
```

---

## 41. What is enumerate()?

enumerate() adds an index to each element of an iterable and returns both the index and value. It eliminates the need to manually manage counters in loops. The starting index can be customized if required. It improves readability when working with indexed data.

**Example:**

```python
names = ["John", "Emma"]

for index, value in enumerate(names):
    print(index, value)
```

**Output:**

```text
0 John
1 Emma
```

---

## 42. What is file handling in Python?

File handling allows programs to read from and write to files stored on disk. Python provides built-in functions for opening, reading, writing, and closing files. It enables data persistence beyond program execution. File handling is commonly used when working with CSV, text, and log files.

**Example:**

```python
with open("sample.txt", "w") as file:
    file.write("Hello World")
```

**Output:**

```text
sample.txt created successfully
```

---

## 43. Why is with open() preferred for file handling?

The with statement automatically manages file resources and ensures files are properly closed after use. It prevents resource leaks even if exceptions occur. This approach results in cleaner and safer code. It is considered the standard practice for file operations.

**Example:**

```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

**Output:**

```text
Hello World
```

---

## 44. What is the difference between read(), readline(), and readlines()?

read() retrieves the entire file content as a single string. readline() reads one line at a time. readlines() returns all lines as a list of strings. The choice depends on file size and processing requirements.

**Example:**

```python
with open("sample.txt", "r") as file:
    print(file.readline())
```

**Output:**

```text
Hello World
```

---

## 45. What is the difference between write() and writelines()?

write() writes a single string to a file. writelines() writes multiple strings from an iterable. Neither method automatically adds newline characters. Newline characters must be added explicitly if needed.

**Example:**

```python
with open("sample.txt", "w") as file:
    file.writelines(["A\n", "B\n", "C\n"])
```

**Output:**

```text
A
B
C
```

---

## 46. What is exception handling?

Exception handling is a mechanism used to manage runtime errors without terminating the program abruptly. It allows developers to anticipate and handle unexpected situations. Proper exception handling improves application reliability. It also provides meaningful error messages.

**Example:**

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Output:**

```text
Cannot divide by zero
```

---

## 47. What is the purpose of try and except blocks?

The try block contains code that may generate an exception. The except block defines how the program should respond if an error occurs. This prevents crashes and allows graceful error recovery. Multiple except blocks can be used for different exception types.

**Example:**

```python
try:
    num = int("abc")

except ValueError:
    print("Invalid number")
```

**Output:**

```text
Invalid number
```

---

## 48. What is the finally block?

The finally block contains code that executes regardless of whether an exception occurs. It is typically used for cleanup operations such as closing files or releasing resources. The block runs after try and except execution. Its execution is guaranteed before the program exits the structure.

**Example:**

```python
try:
    print("Processing")

finally:
    print("Cleanup completed")
```

**Output:**

```text
Processing
Cleanup completed
```

---

## 49. What is the difference between shallow copy and deep copy?

A shallow copy creates a new object but shares references to nested objects with the original. A deep copy creates completely independent copies of all nested objects. Changes to nested objects affect shallow copies but not deep copies. This distinction is important when working with complex data structures.

**Example:**

```python
import copy

original = [[1, 2]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(3)

print(shallow)
print(deep)
```

**Output:**

```text
[[1, 2, 3]]
[[1, 2]]
```

---

## 50. What are generators and the yield keyword?

Generators are special functions that produce values one at a time instead of returning all values at once. They use the yield keyword to pause execution and preserve state between iterations. Generators are memory efficient because values are generated only when needed. They are useful when processing large datasets.

**Example:**

```python
def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
```

**Output:**

```text
1
2
3
```

<class 'NoneType'>
```
