# Day 13: Functions and Their Types in Python ⚡

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 13 of Python**! Today we cover the essentials of **Functions** and their **Types** in Python. Functions help avoid repetitive code, break problems into smaller blocks, and make programs easy to read, test, and maintain.

---

## 📌 Table of Contents
1. [What is a Function?](#1-what-is-a-function)
2. [Types of Functions in Python](#2-types-of-functions-in-python)
   - [A. Built-in Functions](#a-built-in-functions)
   - [B. User-Defined Functions](#b-user-defined-functions)
   - [C. Lambda / Anonymous Functions](#c-lambda--anonymous-functions)
3. [4 Types of Functions (Input & Output)](#3-4-types-of-functions-input--output)
   - [Type 1: Without arguments & without return value](#type-1-without-arguments-and-without-return-value)
   - [Type 2: With arguments & without return value](#type-2-with-arguments-and-without-return-value)
   - [Type 3: Without arguments & with return value](#type-3-without-arguments-and-with-return-value)
   - [Type 4: With arguments & with return value](#type-4-with-arguments-and-with-return-value)
4. [Basic Types of Arguments](#4-basic-types-of-arguments)
   - [Positional Arguments](#a-positional-arguments)
   - [Keyword Arguments](#b-keyword-arguments)
   - [Default Arguments](#c-default-arguments)
5. [Quick Summary](#5-quick-summary)
6. [How to Run](#6-how-to-run)

---

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task. A function runs only when it is called.

### Syntax:
```python
def function_name(parameters):
    # code to execute
    return value  # optional
```

### Basic Example:
```python
def greet():
    print("Hello, welcome to Day 13 of Python!")

greet()  # Calling the function
```

---

## 2. Types of Functions in Python

Python functions are primarily classified into three types:

### A. Built-in Functions
Functions that come built into Python:
```python
numbers = [10, 20, 30, 40]
print(len(numbers))  # 4
print(max(numbers))  # 40
print(min(numbers))  # 10
```

### B. User-Defined Functions
Functions created by the programmer using the `def` keyword:
```python
def square(num):
    return num * num

print(square(5))  # 25
```

### C. Lambda / Anonymous Functions
Small, single-line functions without a name created using the `lambda` keyword:
```python
double = lambda x: x * 2
print(double(6))  # 12
```

---

## 3. 4 Types of Functions (Input & Output)

Based on whether a function takes parameters and returns a value:

### Type 1: Without Arguments and Without Return Value
Does not accept input and does not return anything.
```python
def say_hello():
    print("Hello!")

say_hello()
```

### Type 2: With Arguments and Without Return Value
Accepts input parameters but does not return a value.
```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Harish")
```

### Type 3: Without Arguments and With Return Value
Does not accept inputs, but returns a value back to the caller.
```python
def get_pi():
    return 3.14159

result = get_pi()
print(result)  # 3.14159
```

### Type 4: With Arguments and With Return Value
Accepts input parameters and returns a calculated result.
```python
def add(a, b):
    return a + b

total = add(10, 20)
print(total)  # 30
```

---

## 4. Basic Types of Arguments

### A. Positional Arguments
Arguments matched by their position/order:
```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Harish", 21)
```

### B. Keyword Arguments
Arguments passed with explicit parameter names:
```python
display_info(age=21, name="Harish")
```

### C. Default Arguments
Parameters that have a default fallback value if no argument is passed:
```python
def welcome_country(name, country="India"):
    print(f"Hello {name}, from {country}!")

welcome_country("Harish")            # Uses default "India"
welcome_country("Alex", "Canada")     # Overrides default
```

---

## 5. Quick Summary

| Category | Description | Example |
| :--- | :--- | :--- |
| **Definition** | Reusable code block | `def func():` |
| **Built-in** | Provided out-of-the-box by Python | `print()`, `len()` |
| **User-defined** | Custom created functions | `def square(x):` |
| **Lambda** | Anonymous one-liner function | `lambda x: x * 2` |
| **Positional Arg** | Passed according to position | `add(5, 10)` |
| **Keyword Arg** | Passed using parameter name | `add(b=10, a=5)` |
| **Default Arg** | Fallback parameter value | `def greet(c="India"):` |

---

## 6. How to Run

Run the script in your terminal using:
```bash
python day13.py
```
