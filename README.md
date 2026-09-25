# Day 19: Exception Handling in Python (Basic Level) 🛡️🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-19-OF-PYTHON](https://github.com/harish-0987/DAY-19-OF-PYTHON)

Welcome to **Day 19 of Python**! Today we dive into **Exception Handling in Python**—the foundational technique for building crash-proof, resilient, and production-ready applications.

---

## 📌 Table of Contents
1. [What is an Error vs. an Exception?](#1-what-is-an-error-vs-an-exception)
2. [Why Do We Need Exception Handling?](#2-why-do-we-need-exception-handling)
3. [The Complete Exception Architecture](#3-the-complete-exception-architecture)
   - [`try` Block](#the-try-block)
   - [`except` Block](#the-except-block)
   - [`else` Block](#the-else-block)
   - [`finally` Block](#the-finally-block)
4. [Common Built-in Python Exceptions](#4-common-built-in-python-exceptions)
5. [Catching Specific & Multiple Exceptions](#5-catching-specific--multiple-exceptions)
6. [Raising Exceptions Manually (`raise`)](#6-raising-exceptions-manually-raise)
7. [Creating Custom (User-Defined) Exceptions](#7-creating-custom-user-defined-exceptions)
8. [Code Structure in this Repository](#8-code-structure-in-this-repository)
9. [Best Practices (PEP 8 & Clean Code)](#9-best-practices-pep-8--clean-code)
10. [How to Run the Code](#10-how-to-run-the-code)
11. [Summary & Key Takeaways](#11-summary--key-takeaways)

---

## 1. What is an Error vs. an Exception?

In Python, issues encountered during development fall into two distinct categories:

```
                          ┌───────────────────────────┐
                          │   ISSUES IN PYTHON CODE   │
                          └─────────────┬─────────────┘
                                        │
                 ┌──────────────────────┴──────────────────────┐
                 ▼                                             ▼
     ┌───────────────────────┐                     ┌───────────────────────┐
     │     SYNTAX ERRORS     │                     │      EXCEPTIONS       │
     │   (Parsing Phase)     │                     │    (Runtime Phase)    │
     └───────────┬───────────┘                     └───────────┬───────────┘
                 │                                             │
      • Missing colons (:)                          • Division by zero (10 / 0)
      • Unmatched brackets ()                       • Invalid conversions int("abc")
      • Misspelled keywords                         • Missing dictionary keys
      • CANNOT be handled via                       • CAN be caught and handled
        try / except blocks                           using try / except!
```

- **Syntax Errors**: Python fails to parse the script before execution starts. Must be fixed by the developer in the code editor.
- **Exceptions**: The syntax is completely valid, but an unforeseen condition occurs while the code is actively running. If not handled, Python halts execution, crashes, and prints an ugly traceback.

---

## 2. Why Do We Need Exception Handling?

| Benefit | Explanation |
| :--- | :--- |
| 🛡️ **Prevents Application Crashes** | Your program gracefully recovers from unexpected inputs or failures instead of terminating abruptly. |
| 👤 **User-Friendly Feedback** | Instead of showing raw technical tracebacks, you present clear, helpful messages to users. |
| 🧹 **Guaranteed Resource Cleanup** | Ensures database connections, files, and network sockets are closed cleanly via `finally`. |
| 🔍 **Predictable Flow & Debugging** | Isolates risk-prone operations and handles specific errors precisely where they occur. |

---

## 3. The Complete Exception Architecture

Python provides four keywords that work together in harmony:

```
┌────────────────────────────────────────────────────────┐
│                        try:                            │
│         Run this code (Code that might fail)           │
└───────────────────────────┬────────────────────────────┘
                            │
            Did an exception occur?
           /                       \
        YES                         NO
         ▼                           ▼
┌──────────────────┐        ┌──────────────────┐
│     except:      │        │      else:       │
│ Catch and handle │        │ Runs ONLY if NO  │
│  the exception   │        │ error occurred   │
└────────┬─────────┘        └────────┬─────────┘
         │                           │
         └─────────────┬─────────────┘
                       ▼
┌────────────────────────────────────────────────────────┐
│                      finally:                          │
│        ALWAYS runs, no matter what happens!            │
│         (Perfect for cleanup / reset logic)            │
└────────────────────────────────────────────────────────┘
```

### The `try` Block
Wraps code that might raise an exception:
```python
try:
    number = int(input("Enter an integer: "))
```

### The `except` Block
Executes only when an exception occurs inside the corresponding `try` block:
```python
except ValueError as e:
    print(f"Invalid input! Please enter digits only. Error: {e}")
```

### The `else` Block
Executes **only if no exception** was raised in the `try` block:
```python
else:
    print(f"Number successfully entered: {number}")
```

### The `finally` Block
**Always executes**, whether an exception occurred or not:
```python
finally:
    print("Execution completed.")
```

---

## 4. Common Built-in Python Exceptions

| Exception Name | Trigger Condition | Example |
| :--- | :--- | :--- |
| `ZeroDivisionError` | Division or modulo by zero | `10 / 0` |
| `ValueError` | Correct data type, but inappropriate value | `int("hello")` |
| `TypeError` | Operation applied to incompatible data types | `10 + "5"` |
| `IndexError` | Accessing a sequence index out of range | `[1, 2][5]` |
| `KeyError` | Accessing a non-existent dictionary key | `{"a": 1}["b"]` |
| `FileNotFoundError` | Attempting to open a file that does not exist | `open("missing.txt")` |
| `AttributeError` | Accessing an attribute/method that doesn't exist | `"text".sort()` |

---

## 5. Catching Specific & Multiple Exceptions

### A. Granular Handling with Multiple `except` Blocks
Handle different error types with customized responses:
```python
try:
    num_a = float(val_a)
    num_b = float(val_b)
    result = num_a / num_b
except ValueError:
    print("Please enter valid numeric values!")
except ZeroDivisionError:
    print("Cannot divide a number by zero!")
```

### B. Catching Multiple Exceptions in a Tuple
When multiple errors should trigger the same recovery logic:
```python
try:
    result = a / b
except (ZeroDivisionError, TypeError) as err:
    print(f"Calculation failed due to: {err}")
```

---

## 6. Raising Exceptions Manually (`raise`)

You can deliberately raise exceptions using the `raise` keyword when business rules or validation constraints fail:

```python
def register_voter(name: str, age: int):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age < 18:
        raise ValueError(f"Voter must be at least 18 years old (given: {age})")
    return f"Registered voter {name} successfully!"
```

---

## 7. Creating Custom (User-Defined) Exceptions

In professional software development, you create custom domain exceptions by subclassing Python's built-in `Exception`:

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available account balance."""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}! Available balance is only ${balance:.2f}."
        )

# Usage:
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
```

---

## 8. Code Structure in this Repository

```
DAY-19-OF-PYTHON/
│
├── day19.py                 # Main executable script with all demonstrations
├── README.md                # Complete documentation and study guide
└── .gitignore               # Ignored files and Python cache
```

---

## 9. Best Practices (PEP 8 & Clean Code)

1. 🎯 **Be Specific**: Never use a bare `except:` without specifying the exception class. It can accidentally catch `KeyboardInterrupt` (Ctrl+C) and `SystemExit`.
   ```python
   # ❌ BAD
   except:
       pass

   # ✅ GOOD
   except ValueError as e:
       print(f"Invalid input: {e}")
   ```
2. 📦 **Keep `try` Blocks Minimal**: Wrap only the lines of code that are genuinely prone to errors.
3. 🧹 **Use `finally` for Clean-Up**: Always close files, release locks, and terminate network connections in `finally`.
4. 🚫 **Never Silently Suppress Errors**: Avoid `except Exception: pass` unless there is a very deliberate and documented reason.

---

## 10. How to Run the Code

Run the demonstration script from your terminal:

```bash
# Clone the repository
git clone https://github.com/harish-0987/DAY-19-OF-PYTHON.git

# Navigate into the project folder
cd DAY-19-OF-PYTHON

# Execute the Day 19 script
python day19.py
```

---

## 11. Summary & Key Takeaways

- **Syntax Errors** happen at compile/parse time; **Exceptions** happen at runtime.
- **`try`** contains code that might fail; **`except`** catches and handles specific failures.
- **`else`** executes only when everything in `try` runs smoothly.
- **`finally`** is guaranteed to execute, making it ideal for resource cleanup.
- **`raise`** allows you to enforce business logic and validate inputs.
- Custom exceptions inherit from `Exception` and clarify domain errors.

---
⭐ *Keep building and coding every single day!*
