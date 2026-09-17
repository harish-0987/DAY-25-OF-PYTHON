# Day 11: Conditional Statements in Python 🔀

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 11 of Python**! Today we explore **Conditional Statements**, the core mechanism for decision-making and flow control in programming. Conditional statements allow your Python programs to make decisions dynamically based on whether conditions evaluate to `True` or `False`.

---

## 📌 Table of Contents
1. [What is a Conditional Statement?](#-what-is-a-conditional-statement)
2. [Types of Conditional Statements](#-types-of-conditional-statements)
   - [1. The `if` Statement](#1-the-if-statement)
   - [2. The `if...else` Statement](#2-the-ifelse-statement)
   - [3. The `if...elif...else` Ladder](#3-the-ifelifelse-ladder)
   - [4. Nested `if` Statements](#4-nested-if-statements)
   - [5. Ternary Operator (Conditional Expressions)](#5-ternary-operator-conditional-expressions)
   - [6. The `match...case` Statement (Python 3.10+)](#6-the-matchcase-statement-python-310)
3. [Operators Used in Conditions](#-operators-used-in-conditions)
4. [Truthy and Falsy Values](#-truthy-and-falsy-values)
5. [Basic Level Coding Examples](#-basic-level-coding-examples)
6. [Common Pitfalls & Best Practices](#-common-pitfalls--best-practices)
7. [How to Run the Code](#-how-to-run-the-code)

---

## 📌 What is a Conditional Statement?

A **conditional statement** executes different blocks of code depending on whether a boolean expression evaluates to `True` or `False`.

```
                  ┌──────────────────────┐
                  │  Evaluate Condition  │
                  └──────────┬───────────┘
                             │
                  ┌──────────┴──────────┐
               [True]                [False]
                  │                     │
                  ▼                     ▼
          ┌───────────────┐     ┌───────────────┐
          │ Execute Block │     │ Skip or Run   │
          │               │     │ Alternative   │
          └───────┬───────┘     └───────┬───────┘
                  │                     │
                  └──────────┬──────────┘
                             ▼
                    [ Continue Flow ]
```

---

## 💡 Types of Conditional Statements

| Type | When to Use | Syntax Summary |
| :--- | :--- | :--- |
| **`if`** | When you want to run code only if a condition is met | `if condition:` |
| **`if...else`** | When you have two clear alternative outcomes | `if condition: ... else: ...` |
| **`if...elif...else`** | When evaluating multiple exclusive conditions sequentially | `if ...: elif ...: else: ...` |
| **Nested `if`** | When a decision depends on a previous decision | `if cond1: if cond2: ...` |
| **Ternary Operator** | For concise, single-line value assignments | `val = x if cond else y` |
| **`match...case`** | When matching a value against multiple patterns (Python 3.10+) | `match val: case pattern: ...` |

---

### 1. The `if` Statement

Executes a block of code **only** if the specified condition is `True`.

```python
age = 20

if age >= 18:
    print("You are eligible to vote!")
```

---

### 2. The `if...else` Statement

Provides an alternative execution path when the condition evaluates to `False`.

```python
number = 17

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

---

### 3. The `if...elif...else` Ladder

Tests multiple conditions from top to bottom. The first condition that evaluates to `True` executes, and the rest are skipped.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

---

### 4. Nested `if` Statements

An `if` or `if...else` block placed inside another `if` block for multi-level validation.

```python
pin_correct = True
balance = 5000
withdraw_amount = 2000

if pin_correct:
    if withdraw_amount <= balance:
        print("Withdrawal approved!")
    else:
        print("Insufficient balance.")
else:
    print("Incorrect PIN.")
```

---

### 5. Ternary Operator (Conditional Expressions)

A clean, one-line syntax to assign values based on a condition.

```python
# Syntax: value_if_true if condition else value_if_false
a = 15
b = 25
max_val = a if a > b else b
print(f"Maximum: {max_val}")
```

---

### 6. The `match...case` Statement (Python 3.10+)

Modern structural pattern matching, offering an elegant alternative to long `if-elif-else` chains.

```python
status_code = 404

match status_code:
    case 200:
        print("OK: Request succeeded")
    case 404:
        print("Not Found: Resource unavailable")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")
```

---

## ⚙️ Operators Used in Conditions

### 1. Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `>`  : Greater than
- `<`  : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

### 2. Logical Operators
- `and` : Returns `True` if **both** statements are true
- `or`  : Returns `True` if **at least one** statement is true
- `not` : Reverses the result (`not True` becomes `False`)

### 3. Membership & Identity Operators
- `in` / `not in` : Checks if an item exists inside a sequence (string, list, tuple, dict keys)
- `is` / `is not` : Checks if two variables refer to the exact same object in memory

---

## 🔍 Truthy and Falsy Values

In Python, every object has an inherent boolean value when evaluated inside an `if` condition:

| Falsy Values (Evaluates to `False`) | Truthy Values (Evaluates to `True`) |
| :--- | :--- |
| `False` | `True` |
| `0`, `0.0` | Any non-zero number (e.g., `1`, `-5`, `3.14`) |
| `""` (Empty string) | Any non-empty string (`"hello"`, `" "`) |
| `[]` (Empty list) | Any non-empty collection (`[1, 2]`) |
| `{}`, `set()` | Any non-empty dict or set (`{"a": 1}`) |
| `None` | Any valid object instance |

---

## 💻 Basic Level Coding Examples

### Example 1: Simple Traffic Light System
```python
signal = "yellow"

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("SLOW DOWN")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal")
```

### Example 2: Leap Year Checker
```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is not a Leap Year.")
```

### Example 3: Simple Arithmetic Calculator
```python
num1 = 10
num2 = 5
op = "+"

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Invalid Operator"

print("Result:", result)
```

---

## ⚠️ Common Pitfalls & Best Practices

1. **Avoid redundant boolean comparisons:**
   ```python
   # ❌ Avoid
   if is_logged_in == True:
       pass

   # ✅ Pythonic
   if is_logged_in:
       pass
   ```

2. **Check for `None` using `is`, not `==`:**
   ```python
   # ✅ Recommended
   if response is None:
       pass
   ```

3. **Take advantage of chained comparisons:**
   ```python
   # ✅ Pythonic and readable
   if 18 <= age <= 65:
       print("Working age group")
   ```

4. **Mind indentation:** Python uses whitespace indentation (standard is 4 spaces). Incorrect indentation will raise an `IndentationError`.

---

## 🚀 How to Run the Code

Run the accompanying Python script from your terminal:

```bash
python day11.py
```

---

## 👤 Author
- **Harish**
- **Repository**: [DAY-11-OF-PYTHON](https://github.com/harish-0987/DAY-11-OF-PYTHON)
- **Motto**: *"Not here to be known, here to build."*
