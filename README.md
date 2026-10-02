# Day 25: Object-Oriented Programming (OOP) - Polymorphism in Python 🎭🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-25-OF-PYTHON](https://github.com/harish-0987/DAY-25-OF-PYTHON)

Welcome to **Day 25 of Python**! Today's session is focused on **Polymorphism in Python** at a clear, practical, beginner-friendly foundational level.

> [!NOTE]
> **Scope for Today**: We explore the core concept of **Polymorphism** ("many forms") in Python OOP. We cover built-in polymorphism, Duck Typing, runtime method overriding, polymorphic functions, operator overloading with dunder methods, method overloading workarounds, and a real-world multi-payment gateway case study.

---

## 📌 Table of Contents

1. [What is Polymorphism? (Basic Level)](#-what-is-polymorphism-basic-level)
2. [Why Use Polymorphism?](#-why-use-polymorphism)
3. [The 4 Dimensions of Polymorphism in Python](#-the-4-dimensions-of-polymorphism-in-python)
   - [1. Built-in Polymorphism (Functions & Operators)](#1-built-in-polymorphism-functions--operators)
   - [2. Duck Typing (Polymorphism Without Inheritance)](#2-duck-typing-polymorphism-without-inheritance)
   - [3. Method Overriding (Inheritance-Based Runtime Polymorphism)](#3-method-overriding-inheritance-based-runtime-polymorphism)
   - [4. Polymorphism via Common Functions / Interfaces](#4-polymorphism-via-common-functions--interfaces)
4. [Operator Overloading (Syntactic Polymorphism)](#-operator-overloading-syntactic-polymorphism)
5. [Method Overloading in Python (Workarounds)](#-method-overloading-in-python-workarounds)
6. [Real-World Project: Multi-Payment Checkout System](#-real-world-project-multi-payment-checkout-system)
7. [Quick Summary Comparison Table](#-quick-summary-comparison-table)
8. [Code Implementation & Running the Code](#-code-implementation--running-the-code)

---

## 💡 What is Polymorphism? (Basic Level)

The word **Polymorphism** comes from two Greek words:
- **Poly**: Many
- **Morph**: Forms / Shapes

In Object-Oriented Programming, **Polymorphism** is the ability of different objects to respond to the **same method call** (or operator) in their own customized, specific way.

### 🎭 Real-World Analogy
Think of a person:
- At home with family, they act as a **parent** or **child**.
- At work in the office, they act as an **employee**.
- At a shopping mall, they act as a **customer**.

The **same person** takes on **many forms and behaviors** depending on the context!

```
                      ┌────────────────────────┐
                      │   Same Method Call:    │
                      │       .speak()         │
                      └───────────┬────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│       Dog       │      │       Cat       │      │       Cow       │
│  "Woof! Woof!"  │      │  "Meow! Purr!"  │      │   "Moo! Moo!"   │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

---

## 🚀 Why Use Polymorphism?

1. **Loose Coupling**: Calling code doesn't need to know the exact class type of an object; it only needs to know that the object responds to the required method.
2. **Extensibility**: You can introduce brand-new classes into your application without rewriting or modifying existing consumer functions.
3. **Cleaner Code**: Removes bloated chains of `if-elif-else isinstance(...)` checks.
4. **Consistency**: Uniform method naming across related and unrelated components.

---

## ⚙️ The 4 Dimensions of Polymorphism in Python

### 1. Built-in Polymorphism (Functions & Operators)
Python has polymorphism natively integrated into standard functions and operators:

- **`len()` function**:
  - `len("Python")` -> Calculates number of characters (`6`)
  - `len([1, 2, 3])` -> Calculates number of list elements (`3`)
  - `len({"a": 1, "b": 2})` -> Calculates number of dictionary keys (`2`)

- **`+` operator**:
  - `10 + 20` -> Performs numerical addition (`30`)
  - `"Hello, " + "World"` -> Performs string concatenation (`Hello, World`)
  - `[1, 2] + [3, 4]` -> Performs list merging (`[1, 2, 3, 4]`)

---

### 2. Duck Typing (Polymorphism Without Inheritance)
> *"If it walks like a duck and quacks like a duck, it's a duck."*

In Python's dynamic type system, classes do **not** need to inherit from the same parent to behave polymorphically. If an object has the expected method name, Python will call it:

```python
class Duck:
    def sound(self):
        print("Duck: Quack, quack!")

class Person:
    def sound(self):
        print("Person: Imitating quack!")

class Robot:
    def sound(self):
        print("Robot: Beep-boop quack!")

def play_sound(entity):
    entity.sound()  # Duck typing: Works for any entity with sound()
```

---

### 3. Method Overriding (Inheritance-Based Runtime Polymorphism)
When a child class re-implements a method already declared in its parent class:

```python
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
```

When you loop over animals and invoke `animal.make_sound()`, Python dynamically calls the child's overridden version at runtime.

---

### 4. Polymorphism via Common Functions / Interfaces
Writing generic utility functions that accept any object satisfying an expected interface:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def calculate_area(self):
        return self.w * self.h

def display_area(shape):
    # Polymorphic function: doesn't care if shape is Circle or Rectangle
    print(f"Calculated Area: {shape.calculate_area():.2f}")
```

---

## ➕ Operator Overloading (Syntactic Polymorphism)

Python allows custom classes to define their own behavior for standard operators (`+`, `-`, `*`, `==`, `>`, etc.) using special **dunder (double underscore) methods**:

| Operator | Dunder Method | Purpose |
| :--- | :--- | :--- |
| `+` | `__add__(self, other)` | Addition / Combining |
| `-` | `__sub__(self, other)` | Subtraction / Difference |
| `*` | `__mul__(self, other)` | Multiplication / Scaling |
| `==` | `__eq__(self, other)` | Equality comparison |
| `>` | `__gt__(self, other)` | Greater-than comparison |
| `<` | `__lt__(self, other)` | Less-than comparison |
| `str()` / `print()` | `__str__(self)` | User-friendly string display |

### Example: 2D Point Vector Addition
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Output: Point(6, 8)
```

---

## 🔀 Method Overloading in Python (Workarounds)

In languages like C++ or Java, **Method Overloading** allows multiple methods with the exact same name but different parameter lists.

> [!WARNING]
> **Python Does NOT Natively Support Traditional Method Overloading!**  
> If you write multiple methods with the same name in the same class, the **last defined method silently overwrites** all previous ones.

### Pythonic Solutions for Overloading Behavior:
1. **Default Parameter Values**:
   ```python
   def add(self, a, b, c=0):
       return a + b + c
   ```
2. **Variable-Length Arguments (`*args`)**:
   ```python
   def sum_all(self, *args):
       return sum(args)
   ```
3. **Optional Parameters with `None` Check**:
   ```python
   def greet(self, name=None):
       if name:
           return f"Hello, {name}!"
       return "Hello, Guest!"
   ```

---

## 💳 Real-World Project: Multi-Payment Checkout System

In enterprise web applications, checkout systems interact with dozens of payment gateways (Credit Card, PayPal, UPI, Crypto, Stripe). 

Polymorphism allows the checkout engine to process any payment method through a single uniform `process_payment(amount)` interface:

```
                  ┌───────────────────────────────┐
                  │        PaymentGateway         │
                  │   process_payment(amount)     │
                  └───────────────┬───────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ CreditCardPayment│    │  PayPalPayment   │    │    UPIPayment    │
│  Validates CVV   │    │ Redirects Portal │    │  Verifies PIN    │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

The checkout function:
```python
def checkout(payment_method: PaymentGateway, amount: float):
    print(f"Charging ${amount}...")
    payment_method.process_payment(amount)
    print("Order confirmed!")
```

---

## 📊 Quick Summary Comparison Table

| Polymorphism Type | Mechanism | Inheritance Needed? | Example |
| :--- | :--- | :---: | :--- |
| **Built-in** | Language engine | No | `len("abc")`, `len([1, 2])`, `1 + 2`, `'a' + 'b'` |
| **Duck Typing** | Dynamic method dispatch | No | Any object implementing `.sound()` or `.swim()` |
| **Method Overriding** | Subclass redefines parent method | Yes | `Dog.make_sound()` overriding `Animal.make_sound()` |
| **Operator Overloading** | Dunder magic methods | No | `p1 + p2` via `__add__()`, `b1 > b2` via `__gt__()` |
| **Method Overloading** | Default args / `*args` | No | `calc.add(10, 20)` & `calc.add(10, 20, 30)` |

---

## 💻 Code Implementation & Running the Code

The complete source code is provided in [`day25.py`](file:///c:/Users/pedda/OneDrive/Desktop/python%201/day25.py).

### How to Run:
```bash
python day25.py
```

### Sample Output:
```text
======================================================================
 DAY 25: OBJECT-ORIENTED PROGRAMMING (OOP) - POLYMORPHISM IN PYTHON
 Author: Harish | Repository: DAY-25-OF-PYTHON
 Motto: 'Not here to be known, here to build.'
======================================================================

--- Polymorphism with len() ---
len(str)  : len('Python OOP')                  -> 10 characters
len(list) : len([10, 20, 30, 40, 50])       -> 5 items

--- Polymorphism with '+' Operator ---
Integer Addition      : 15 + 25           = 40
String Concatenation  : 'Hello, ' + 'Dev' = Hello, Dev

--- Duck Typing ---
Testing entity: Duck
Duck: Quack, quack!
Duck: Swimming gracefully in the pond.

--- Method Overriding ---
I am Buddy, and I say: Woof! Woof!
I am Luna, and I say: Meow! Purr!

--- Operator Overloading ---
p1 + p2     = Point(8, 11)
Total Pages : 1558 pages

--- Real-World Payment Gateways ---
[Credit Card] Charging $149.99 to card ****-****-****-4567... Payment Approved!
[PayPal] Debited $49.50 from PayPal balance... Order placed successfully!
[UPI] Transaction Success for $25.00!

======================================================================
 DAY 25 COMPLETE: Polymorphism in Python Mastered Successfully!
 'Not here to be known, here to build.'
======================================================================
```

---

> *"Not here to be known, here to build."* — **Harish**
