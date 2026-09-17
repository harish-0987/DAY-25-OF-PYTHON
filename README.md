# Day 11: Conditional Statements in Python 🔀

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 11 of Python**! Today we dive deep into **Conditional Statements** (also known as decision-making or branching statements). In software development, your code rarely runs in a straight line from start to finish—it must make decisions, react to user input, validate data, and choose between multiple pathways. Conditional statements are the brain of any program.

---

## 📌 Table of Contents
1. [What is a Conditional Statement?](#-what-is-a-conditional-statement)
2. [Control Flow Diagram](#-control-flow-diagram)
3. [Operators Used in Conditions](#-operators-used-in-conditions)
   - [Comparison Operators](#1-comparison-operators)
   - [Logical Operators & Short-Circuit Evaluation](#2-logical-operators--short-circuit-evaluation)
   - [Identity & Membership Operators](#3-identity--membership-operators)
4. [Truthy and Falsy Values in Python](#-truthy-and-falsy-values-in-python)
5. [Types of Conditional Statements](#-types-of-conditional-statements)
   - [1. The `if` Statement](#1-the-if-statement)
   - [2. The `if...else` Statement](#2-the-ifelse-statement)
   - [3. The `if...elif...else` Ladder](#3-the-ifelifelse-ladder)
   - [4. Nested `if` Statements](#4-nested-if-statements)
   - [5. Short-Hand `if` & Ternary Operator](#5-short-hand-if--ternary-operator)
   - [6. Modern `match...case` Statement (Python 3.10+)](#6-modern-matchcase-statement-python-310)
6. [Summary Comparison Table of All Types](#-summary-comparison-table-of-all-types)
7. [Basic Level Coding Examples](#-basic-level-coding-examples)
   - [Example 1: Even or Odd Number](#example-1-even-or-odd-number)
   - [Example 2: Voting & License Eligibility](#example-2-voting--license-eligibility)
   - [Example 3: Student Grading System](#example-3-student-grading-system)
   - [Example 4: Traffic Signal Controller](#example-4-traffic-signal-controller)
   - [Example 5: ATM Withdrawal with Nested Conditions](#example-5-atm-withdrawal-with-nested-conditions)
   - [Example 6: Leap Year Checker](#example-6-leap-year-checker)
   - [Example 7: Triangle Classification](#example-7-triangle-classification)
   - [Example 8: Simple Arithmetic Calculator](#example-8-simple-arithmetic-calculator)
   - [Example 9: Movie Ticket Pricing with Multi-Discount](#example-9-movie-ticket-pricing-with-multi-discount)
   - [Example 10: HTTP Status Code Router (`match...case`)](#example-10-http-status-code-router-matchcase)
8. [Best Practices & Pythonic Conditions](#-best-practices--pythonic-conditions)
9. [Common Pitfalls & How to Avoid Them](#-common-pitfalls--how-to-avoid-them)
10. [Practice Exercises & Challenges](#-practice-exercises--challenges)
11. [How to Run the Code](#-how-to-run-the-code)
12. [Author & Repository](#-author--repository)

---

## 📌 What is a Conditional Statement?

A **Conditional Statement** in Python is an instruction that controls the execution flow of a program based on a condition that evaluates to a boolean value: **`True`** or **`False`**.

- When a condition evaluates to **`True`**, the corresponding code block is **executed**.
- When a condition evaluates to **`False`**, the block is **skipped** or an alternative block is triggered.

Python uses **indentation** (typically 4 spaces) rather than curly braces `{}` to define code blocks inside conditions.

---

## 🔄 Control Flow Diagram

```text
                        ┌────────────────────────┐
                        │   Start / Expression   │
                        └───────────┬────────────┘
                                    │
                                    ▼
                        ┌────────────────────────┐
                        │  Is Condition True?    │◄────── Condition Check
                        └─────┬────────────┬─────┘
                              │            │
                      [ YES ] │            │ [ NO ]
                              ▼            ▼
                     ┌────────────────┐   ┌────────────────────────┐
                     │ Execute Block  │   │ Execute Else Block or  │
                     │ of Statements  │   │ Skip Condition         │
                     └────────┬───────┘   └──────────┬─────────────┘
                              │                      │
                              └──────────┬───────────┘
                                         │
                                         ▼
                             ┌───────────────────────┐
                             │ Next Program Step...  │
                             └───────────────────────┘
```

---

## ⚙️ Operators Used in Conditions

Conditional expressions are built using Python's comparison, logical, identity, and membership operators.

### 1. Comparison Operators
Comparison operators evaluate relationships between values and always return `True` or `False`:

| Operator | Name | Example | Result (`x = 10, y = 5`) |
| :---: | :--- | :--- | :--- |
| `==` | Equal to | `x == y` | `False` |
| `!=` | Not equal to | `x != y` | `True` |
| `>` | Greater than | `x > y` | `True` |
| `<` | Less than | `x < y` | `False` |
| `>=` | Greater than or equal to | `x >= 10` | `True` |
| `<=` | Less than or equal to | `y <= 5` | `True` |

### 2. Logical Operators & Short-Circuit Evaluation
Logical operators combine multiple conditions:

| Operator | Description | Syntax | Truth Condition |
| :---: | :--- | :--- | :--- |
| **`and`** | Logical AND | `cond1 and cond2` | `True` only if **both** operands are `True` |
| **`or`** | Logical OR | `cond1 or cond2` | `True` if **at least one** operand is `True` |
| **`not`** | Logical NOT | `not cond` | Inverts boolean state (`not True` $\to$ `False`) |

> [!TIP]
> **Short-Circuit Evaluation**:
> - In `A and B`, if `A` is `False`, Python stops immediately and returns `False` without checking `B`.
> - In `A or B`, if `A` is `True`, Python stops immediately and returns `True` without checking `B`.

### 3. Identity & Membership Operators

- **`in` / `not in`**: Checks whether an element is present in an iterable (list, string, tuple, set, dict keys).
  ```python
  if "admin" in ["admin", "moderator", "user"]:
      print("Access granted!")
  ```
- **`is` / `is not`**: Checks object identity (whether two variables point to the exact same location in memory). Always use `is` when comparing against `None`.
  ```python
  data = None
  if data is None:
      print("Data is not initialized.")
  ```

---

## 🔍 Truthy and Falsy Values in Python

In Python, any object can be tested for truth value. You do not always need an explicit comparison (`x == True`).

### Falsy Values (Always evaluate to `False`):
- Constants: `None`, `False`
- Numeric zeros: `0`, `0.0`, `0j`
- Empty sequences and collections: `""` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `set()`
- Empty ranges: `range(0)`

### Truthy Values (Evaluate to `True`):
- Any non-zero number: `1`, `-42`, `3.14`
- Any non-empty string: `"hello"`, `" "` (even a space!)
- Any non-empty container: `[1, 2]`, `{"key": "val"}`

```python
name = "Harish"
if name:
    print(f"Hello, {name}!")  # Executes because non-empty string is Truthy
```

---

## 💡 Types of Conditional Statements

Python provides multiple structured ways to make decisions:

---

### 1. The `if` Statement
The simplest decision-making statement. It executes the code block **only if** the condition is `True`.

#### Syntax:
```python
if condition:
    # Statement(s) executed when condition is True
```

#### Example:
```python
temperature = 35

if temperature > 30:
    print("It's a hot day! Drink plenty of water.")
```

---

### 2. The `if...else` Statement
Provides two mutual paths: one if the condition is `True`, and an alternative path if the condition is `False`.

#### Syntax:
```python
if condition:
    # Runs when condition is True
else:
    # Runs when condition is False
```

#### Example:
```python
user_age = 16

if user_age >= 18:
    print("Eligible for voting.")
else:
    print("Not eligible yet. Wait until you turn 18.")
```

---

### 3. The `if...elif...else` Ladder
When there are **multiple mutually exclusive possibilities**, use `elif` (short for *else if*). Python checks conditions from top to bottom and executes the first block whose condition is `True`.

#### Syntax:
```python
if condition_1:
    # Runs if condition_1 is True
elif condition_2:
    # Runs if condition_1 is False and condition_2 is True
elif condition_3:
    # Runs if previous conditions are False and condition_3 is True
else:
    # Runs if ALL conditions above are False
```

#### Example:
```python
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Student Marks: {marks} | Final Grade: {grade}")
```

---

### 4. Nested `if` Statements
A conditional statement nested inside another conditional statement. Used when a secondary decision depends directly on the success of a primary decision.

#### Syntax:
```python
if primary_condition:
    if secondary_condition:
        # Runs when both conditions are True
    else:
        # Runs when primary is True, secondary is False
else:
    # Runs when primary condition is False
```

#### Example:
```python
account_pin = 1234
balance = 5000.0
withdrawal = 1500.0

if account_pin == 1234:
    print("PIN accepted.")
    if withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal approved! New balance: ${balance:.2f}")
    else:
        print("Declined: Insufficient funds.")
else:
    print("Declined: Incorrect PIN entered.")
```

---

### 5. Short-Hand `if` & Ternary Operator

#### A. One-Line `if` (Short-hand `if`):
When you have only a single statement to execute inside an `if`:
```python
x = 10
if x > 5: print("x is greater than 5")
```

#### B. Ternary Operator (Conditional Expression):
Evaluates an expression and returns a value based on a condition in a single concise line.

#### Syntax:
```python
variable = value_if_true if condition else value_if_false
```

#### Example:
```python
num = 14
status = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {status}")  # Output: 14 is Even
```

---

### 6. Modern `match...case` Statement (Python 3.10+)
Introduced in **Python 3.10**, structural pattern matching provides a powerful, readable alternative to extensive `if-elif-else` chains (similar to `switch-case` in other languages, but much more capable).

#### Syntax:
```python
match subject:
    case pattern_1:
        # Code block
    case pattern_2:
        # Code block
    case _:
        # Default / Fallback wildcard
```

#### Example:
```python
role = "editor"

match role:
    case "admin":
        permissions = "Full read/write/delete access"
    case "editor":
        permissions = "Read and write access"
    case "viewer" | "guest":   # Pipe '|' allows OR patterns
        permissions = "Read-only access"
    case _:
        permissions = "No permissions assigned"

print(f"Role '{role}': {permissions}")
```

---

## 📊 Summary Comparison Table of All Types

| Type | Keyword(s) | Typical Use Case | Number of Branches |
| :--- | :--- | :--- | :---: |
| **Simple `if`** | `if` | Executing an action only if a flag or rule holds | 1 |
| **`if...else`** | `if`, `else` | Two binary outcomes (e.g., pass/fail, yes/no) | 2 |
| **`if...elif...else`** | `if`, `elif`, `else` | Multiple distinct categories or ranges | 3+ |
| **Nested `if`** | `if` inside `if` | Multi-step validation / dependent checks | Hierarchical |
| **Ternary Operator** | `if...else` inline | Inline variable assignment / return statement | 2 |
| **`match...case`** | `match`, `case`, `_` | Pattern matching against constants or shapes | Unlimited |

---

## 💻 Basic Level Coding Examples

All examples below are simple, practical, and beginner-friendly:

### Example 1: Even or Odd Number
```python
number = 43

if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")
```

---

### Example 2: Voting & License Eligibility
```python
age = 19
has_id = True

if age >= 18 and has_id:
    print("Eligible to vote and apply for a driver's license.")
elif age >= 18 and not has_id:
    print("Age is sufficient, but government ID is required.")
else:
    print(f"You must wait {18 - age} more year(s) to apply.")
```

---

### Example 3: Student Grading System
```python
score = 82

if score >= 90:
    print("Grade: A+ (Outstanding)")
elif score >= 80:
    print("Grade: A (Excellent)")
elif score >= 70:
    print("Grade: B (Good)")
elif score >= 50:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Needs Improvement)")
```

---

### Example 4: Traffic Signal Controller
```python
light = "yellow"

if light == "red":
    print("STOP immediately!")
elif light == "yellow":
    print("PREPARE to stop / proceed with caution.")
elif light == "green":
    print("GO! Path is clear.")
else:
    print("Unknown traffic signal.")
```

---

### Example 5: ATM Withdrawal with Nested Conditions
```python
pin = 1234
entered_pin = 1234
current_balance = 10000
requested_amount = 4000

if entered_pin == pin:
    print("Authentication successful.")
    if requested_amount <= current_balance:
        current_balance -= requested_amount
        print(f"Please collect your cash: ${requested_amount}")
        print(f"Remaining balance: ${current_balance}")
    else:
        print("Transaction failed: Insufficient funds.")
else:
    print("Transaction failed: Incorrect PIN.")
```

---

### Example 6: Leap Year Checker
A year is a **Leap Year** if it is divisible by 4, but **not** by 100, unless it is **also** divisible by 400.

```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a LEAP YEAR (366 days).")
else:
    print(f"{year} is a COMMON YEAR (365 days).")
```

---

### Example 7: Triangle Classification
Given 3 side lengths, determine if they form a valid triangle and what type it is.

```python
a, b, c = 5, 5, 5

# Validation: sum of any two sides must exceed third side
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral Triangle (All sides equal)")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle (Two sides equal)")
    else:
        print("Scalene Triangle (All sides different)")
else:
    print("The given side lengths cannot form a triangle.")
```

---

### Example 8: Simple Arithmetic Calculator
```python
num1 = 20
num2 = 4
operator = "/"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
elif operator == "%":
    result = num1 % num2 if num2 != 0 else "Error: Modulo by zero"
else:
    result = "Error: Invalid operator"

print(f"{num1} {operator} {num2} = {result}")
```

---

### Example 9: Movie Ticket Pricing with Multi-Discount
```python
age = 22
is_student = True
is_weekend = False

# 1. Base price based on age
if age < 5:
    price = 0.0
elif age <= 12:
    price = 100.0
elif age >= 65:
    price = 120.0
else:
    price = 200.0

# 2. Weekend surcharge
if is_weekend and price > 0:
    price += 50.0

# 3. Student discount (20% off)
if is_student and price > 0:
    price -= price * 0.20

print(f"Final Ticket Price: ${price:.2f}")
```

---

### Example 10: HTTP Status Code Router (`match...case`)
```python
def describe_status(code: int) -> str:
    match code:
        case 200:
            return "200: OK"
        case 201:
            return "201: Created"
        case 400:
            return "400: Bad Request"
        case 401 | 403:
            return "401/403: Authentication or Permission Error"
        case 404:
            return "404: Not Found"
        case 500:
            return "500: Internal Server Error"
        case _:
            return f"{code}: Unhandled Status Code"

print(describe_status(200))
print(describe_status(403))
print(describe_status(404))
```

---

## 💡 Best Practices & Pythonic Conditions

### 1. Avoid Comparing Directly to `True` or `False`
```python
# ❌ Anti-pattern
if is_active == True:
    do_something()

# ✅ Pythonic
if is_active:
    do_something()
```

### 2. Take Advantage of Chained Comparisons
Python allows mathematical range chaining:
```python
# ❌ Clunky
if age >= 18 and age <= 65:
    pass

# ✅ Clean & Pythonic
if 18 <= age <= 65:
    pass
```

### 3. Check for `None` Using `is`
```python
# ❌ Avoid
if response == None:
    pass

# ✅ Pythonic
if response is None:
    pass
```

### 4. Guard Clauses (Early Exit Pattern)
Instead of deep nesting, exit early to keep code clean and readable:
```python
# ❌ Deeply nested
def process_user(user):
    if user is not None:
        if user.is_authenticated:
            if user.has_permission:
                execute_task()

# ✅ Clean Guard Clauses
def process_user(user):
    if user is None or not user.is_authenticated:
        return
    if not user.has_permission:
        return
    execute_task()
```

---

## ⚠️ Common Pitfalls & How to Avoid Them

| Pitfall | Problem | Solution |
| :--- | :--- | :--- |
| **`=` vs `==`** | Accidentally using assignment `=` instead of equality check `==` | Python will raise a `SyntaxError: invalid syntax`. Always use `==` for comparison. |
| **Indentation Errors** | Mixing tabs and spaces or misaligning blocks | Always use 4 consistent spaces per indentation level. |
| **Floating Point Precision** | `0.1 + 0.2 == 0.3` evaluates to `False` due to IEEE 754 precision | Use `math.isclose(a, b)` for comparing floating point values. |
| **Evaluating Empty Lists** | Checking `len(my_list) > 0` | Use Python truthiness: `if my_list:` directly. |

---

## 🎯 Practice Exercises & Challenges

Try solving these mini-challenges using conditional statements:

1. **BMI Calculator**: Given weight (kg) and height (m), calculate $\text{BMI} = \frac{\text{weight}}{\text{height}^2}$ and print whether the user is Underweight ($<18.5$), Normal ($18.5-24.9$), Overweight ($25-29.9$), or Obese ($\ge 30$).
2. **Electricity Bill Slabs**: Calculate bill amount:
   - First 100 units: Free
   - Next 100 units: $5 per unit
   - Above 200 units: $10 per unit
3. **Quadrant Locator**: Given Cartesian coordinates $(x, y)$, determine whether the point is in Quadrant I, II, III, IV, or on an axis.

---

## 🚀 How to Run the Code

Run the accompanying Python script (`day11.py`) from your terminal:

```bash
python day11.py
```

Expected Output:
```text
======================================================================
     DAY 11: PYTHON CONDITIONAL STATEMENTS - CONCEPTS & CODE EXAMPLES
======================================================================

--- PART 1: WHAT IS A CONDITIONAL STATEMENT? ---
Action: Take an umbrella! (Condition is True)
...
[Mini-Project 1: Leap Year Checker]
  -> Year 2024: LEAP YEAR (366 days)
...
======================================================================
     DAY 11 COMPLETED SUCCESSFULLY: CONDITIONAL STATEMENTS MASTERED!
======================================================================
```

---

## 👤 Author & Repository

- **Author**: Harish
- **Repository**: [harish-0987/DAY-11-OF-PYTHON](https://github.com/harish-0987/DAY-11-OF-PYTHON)
- **Motto**: *"Not here to be known, here to build."*
