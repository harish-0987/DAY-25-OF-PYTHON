# Day 12: Loops & Jump Statements in Python 🔁

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 12 of Python**! Today we cover the fundamentals of **Loops** and **Jump Statements**. Loops allow us to execute a block of code multiple times without writing repetitive code, while jump statements help us control the loop flow.

---

## 📌 Table of Contents
1. [For Loop](#1-for-loop)
2. [While Loop](#2-while-loop)
3. [Jump Statements](#3-jump-statements)
   - [`break`](#a-break-statement)
   - [`continue`](#b-continue-statement)
   - [`pass`](#c-pass-statement)
4. [Quick Summary](#4-quick-summary)
5. [How to Run](#5-how-to-run)

---

## 1. For Loop

A **`for` loop** is used when you know in advance how many times you want to run a statement or when iterating over items in a collection (range, list, string, etc.).

### Examples:

#### A. Using `range()`
```python
# Prints numbers 1 through 5
for i in range(1, 6):
    print(i)
```

#### B. Looping Through a List
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

#### C. Looping Through a String
```python
for char in "Python":
    print(char)
```

---

## 2. While Loop

A **`while` loop** repeatedly executes a block of code as long as a specified condition remains **`True`**.

### Examples:

#### A. Basic Counter
```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```

#### B. Simple Countdown
```python
timer = 3
while timer > 0:
    print(timer)
    timer -= 1
print("Time's up!")
```

---

## 3. Jump Statements

Jump statements are used to alter the normal execution sequence of a loop.

### A. `break` Statement
Terminates the loop immediately when a condition is met.

```python
for i in range(1, 6):
    if i == 3:
        break  # Stops the loop when i reaches 3
    print(i)

# Output: 1, 2
```

### B. `continue` Statement
Skips the rest of the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue  # Skips 3
    print(i)

# Output: 1, 2, 4, 5
```

### C. `pass` Statement
A null statement used as a syntactic placeholder (does nothing).

```python
for i in range(1, 4):
    if i == 2:
        pass  # Placeholder for future logic
    print(i)

# Output: 1, 2, 3
```

---

## 4. Quick Summary

| Statement | Purpose | Key Usage |
|---|---|---|
| `for` | Iterates over a sequence or range | Known number of iterations |
| `while` | Loops while condition is `True` | Unknown number of iterations |
| `break` | Exits the loop immediately | Stopping on a specific condition |
| `continue` | Skips current iteration to next | Bypassing certain values |
| `pass` | Does nothing (placeholder) | Writing skeleton code |

---

## 5. How to Run

Run the script directly using Python:

```bash
python day12.py
```

---

## 👨‍💻 Author & Repository
- **Author**: Harish
- **Repository**: [DAY-12-OF-PYTHON-](https://github.com/harish-0987/DAY-12-OF-PYTHON-)
