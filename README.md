# Day 14: List Comprehension in Python ⚡

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 14 of Python**! Today we dive into **List Comprehension** — one of Python's most loved and powerful features. It offers a concise, elegant, and Pythonic way to construct new lists from existing iterables.

---

## 📌 Table of Contents
1. [What is List Comprehension?](#1-what-is-list-comprehension)
2. [Traditional Loop vs. List Comprehension](#2-traditional-loop-vs-list-comprehension)
3. [List Comprehension with `if` Condition (Filtering)](#3-list-comprehension-with-if-condition-filtering)
4. [List Comprehension with `if-else` (Conditional Values)](#4-list-comprehension-with-if-else-conditional-values)
5. [List Comprehension with Strings & Other Iterables](#5-list-comprehension-with-strings--other-iterables)
6. [Nested List Comprehension (Basic Level)](#6-nested-list-comprehension-basic-level)
7. [Quick Syntax Cheatsheet & Summary](#7-quick-syntax-cheatsheet--summary)
8. [How to Run](#8-how-to-run)

---

## 1. What is List Comprehension?

**List Comprehension** provides a compact way to process all or part of the elements in an iterable and return a list with the results.

### Basic Syntax:
```python
new_list = [expression for item in iterable]
```

- **`expression`**: What gets calculated or returned for each item.
- **`item`**: The variable representing each element from the iterable.
- **`iterable`**: Any collection/sequence (e.g., list, tuple, string, `range()`).

---

## 2. Traditional Loop vs. List Comprehension

Let's generate the squares of numbers from 1 to 5:

### ❌ Traditional `for` Loop:
```python
squares = []
for num in range(1, 6):
    squares.append(num ** 2)

print(squares)  # Output: [1, 4, 9, 16, 25]
```

###  List Comprehension (1 Line):
```python
squares = [num ** 2 for num in range(1, 6)]

print(squares)  # Output: [1, 4, 9, 16, 25]
```

> **Why use List Comprehension?**  
> - **Cleaner**: Reduces 3–4 lines of boilerplate code into a single readable line.
> - **Faster**: Often executes faster in Python than a manual loop with `.append()`.

---

## 3. List Comprehension with `if` Condition (Filtering)

You can filter items by placing an `if` statement at the end. Only elements where the condition evaluates to `True` are added to the list.

### Syntax:
```python
new_list = [expression for item in iterable if condition]
```

### Example 1: Filter Even Numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

### Example 2: Filter Numbers Greater than 5
```python
greater_than_5 = [n for n in numbers if n > 5]
print(greater_than_5)  # Output: [6, 7, 8, 9, 10]
```

---

## 4. List Comprehension with `if-else` (Conditional Values)

When you want to choose between two expressions based on a condition, place the `if-else` **before** the `for` keyword.

### Syntax:
```python
new_list = [expression_if_true if condition else expression_if_false for item in iterable]
```

### Example 1: Label Even and Odd Numbers
```python
numbers = [1, 2, 3, 4, 5, 6]

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
```

### Example 2: Double Even Numbers, Keep Odd Numbers Unchanged
```python
result = [n * 2 if n % 2 == 0 else n for n in numbers]
print(result)  # Output: [1, 4, 3, 8, 5, 12]
```

---

## 5. List Comprehension with Strings & Other Iterables

List comprehension works on any sequence, including strings and word lists.

### Example 1: Uppercase Characters
```python
word = "python"
letters = [char.upper() for char in word]
print(letters)  # Output: ['P', 'Y', 'T', 'H', 'O', 'N']
```

### Example 2: Extracting Vowels from Text
```python
text = "List Comprehension is awesome"
vowels = [char for char in text if char.lower() in 'aeiou']
print(vowels)  # Output: ['i', 'o', 'e', 'e', 'i', 'o', 'i', 'a', 'e', 'o', 'e']
```

### Example 3: Capitalize List of Words
```python
fruits = ["apple", "banana", "cherry"]
capitalized = [fruit.capitalize() for fruit in fruits]
print(capitalized)  # Output: ['Apple', 'Banana', 'Cherry']
```

---

## 6. Nested List Comprehension (Basic Level)

You can write nested loops in list comprehension. The order of `for` clauses matches the order of nested regular loops.

### Example 1: Flattening a 2D Matrix into a 1D List
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 2: Creating Cartesian Product Pairs
```python
colors = ["red", "green"]
objects = ["ball", "pen"]

pairs = [(c, o) for c in colors for o in objects]
print(pairs)
# Output: [('red', 'ball'), ('red', 'pen'), ('green', 'ball'), ('green', 'pen')]
```

---

## 7. Quick Syntax Cheatsheet & Summary

| Use Case | Syntax Pattern | Example |
| :--- | :--- | :--- |
| **Basic Mapping** | `[expr for x in iterable]` | `[x * 2 for x in range(5)]` |
| **Filtering (`if`)** | `[expr for x in iterable if cond]` | `[x for x in nums if x > 0]` |
| **Transforming (`if-else`)** | `[expr1 if cond else expr2 for x in iterable]` | `["Pos" if x > 0 else "Neg" for x in nums]` |
| **String processing** | `[char.upper() for char in text]` | `[c for c in "hello"]` |
| **Nested loops** | `[expr for x in list1 for y in list2]` | `[(x, y) for x in A for y in B]` |

> 💡 **Best Practice Tip**: Use list comprehensions when the logic is straightforward. If the comprehension has too many conditions or loops and becomes hard to read, stick to regular `for` loops!

---

## 8. How to Run

Execute the script directly in your terminal:
```bash
python day14.py
```
