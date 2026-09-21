# Day 15: Generators in Python ⚡

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 15 of Python**! Today we explore **Generators** — a powerful feature in Python that allows you to generate sequences of values lazily and efficiently on-the-fly without consuming massive amounts of memory.

---

## 📌 Table of Contents
1. [What is a Generator?](#1-what-is-a-generator)
2. [How Generators Work (`yield` vs. `return` & `next()`)](#2-how-generators-work-yield-vs-return--next)
3. [Key Advantages of Generators](#3-key-advantages-of-generators)
4. [Generator Expressions](#4-generator-expressions)
5. [Basic Code Examples](#5-basic-code-examples)
6. [Summary & Key Takeaways](#6-summary--key-takeaways)
7. [How to Run](#7-how-to-run)

---

## 1. What is a Generator?

A **Generator** is a special type of function in Python that returns an iterator object (called a generator object). Instead of computing all values at once and storing them in memory, a generator produces values **one at a time, on demand** (lazy evaluation).

### Defining a Generator Function:
You define a generator function just like a normal function with `def`, but instead of using `return`, you use the **`yield`** keyword.

```python
def simple_generator():
    yield "First item"
    yield "Second item"
    yield "Third item"

# Iterating over generator values
for item in simple_generator():
    print(item)
```

---

## 2. How Generators Work (`yield` vs. `return` & `next()`)

| Feature | `return` | `yield` |
| :--- | :--- | :--- |
| **Execution** | Terminates the function immediately | Pauses the function execution |
| **State** | Discards local state and variables | Saves state and local variables |
| **Value Count** | Returns a single value | Yields a sequence of values over time |
| **Resumption** | Cannot be resumed | Resumes execution from where it paused |

### Step-by-Step Execution with `next()`:
When a generator is called, it returns a generator object without executing the function body. The code runs each time `next()` is called until it hits `yield`.

```python
def count_to_three():
    yield 1
    yield 2
    yield 3

gen = count_to_three()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen)) -> Raises StopIteration error (all items exhausted)
```

---

## 3. Key Advantages of Generators

### 1. 💾 Memory Efficiency (Lazy Evaluation)
Unlike lists that allocate memory for all items at once, generators produce items on demand.
- A list of **100,000 integers** takes **~800 KB** of memory.
- A generator producing the same **100,000 integers** takes only **~200 bytes**!

```python
import sys

# List: stores all numbers in RAM
list_mem = sys.getsizeof([i for i in range(100_000)])  # ~800,984 bytes

# Generator: stores only generator state in RAM
gen_mem = sys.getsizeof((i for i in range(100_000)))   # ~200 bytes
```

### 2. ⚡ High Performance & Faster Startup
Generators start yielding values immediately. You don't need to wait for the complete dataset to be processed before you start consuming the first result.

### 3. ♾️ Handling Infinite Sequences
Because generators are lazy, they can generate an infinite sequence of data without causing memory overflow errors (`MemoryError`).

```python
def infinite_counter(start=1):
    current = start
    while True:
        yield current
        current += 1

counter = infinite_counter()
print(next(counter))  # 1
print(next(counter))  # 2
```

### 4. 🛠️ Cleaner Iterator Implementation
Building a custom iterator class requires implementing `__iter__()` and `__next__()` methods with boilerplate code. A generator automatically implements the iterator protocol with a simple function and `yield`.

---

## 4. Generator Expressions

Python provides a concise one-line syntax for creating generators, known as **Generator Expressions**. They look just like list comprehensions, but use parentheses `()` instead of square brackets `[]`.

```python
# List comprehension (creates full list in memory):
squares_list = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# Generator expression (creates lazy generator object):
squares_gen = (x ** 2 for x in range(1, 6))   # <generator object>

# Consume values:
for val in squares_gen:
    print(val)
```

---

## 5. Basic Code Examples

### Example A: Even Numbers Generator
```python
def even_numbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            yield num

print(list(even_numbers(10)))  # [0, 2, 4, 6, 8, 10]
```

### Example B: Countdown Generator
```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num, end=" ")  # 5 4 3 2 1
```

---

## 6. Summary & Key Takeaways

1. **`yield` is the core of generators**: It pauses the function and yields values on demand.
2. **Lazy Evaluation**: Items are generated only when requested, saving memory and compute time.
3. **Memory Friendly**: Ideal for processing large files, data streams, and infinite series.
4. **Generator Expressions**: Provide a clean, single-line syntax `(expr for item in iterable)`.

---

## 7. How to Run

Clone the repository and run the Python script:

```bash
python day15.py
```
