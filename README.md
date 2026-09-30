# Day 23: Object-Oriented Programming (OOP) in Python - Introduction & Basics 🧱🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-23-OF-PYTHON](https://github.com/harish-0987/DAY-23-OF-PYTHON)

Welcome to **Day 23 of Python**! Today's session is an introductory dive into **Object-Oriented Programming (OOP)** in Python, focused on mastering the core foundation in a concise, practical, and short format.

> [!NOTE]
> **Scope for Today**: We focus strictly on the fundamental building blocks of OOP: **Classes, Objects, Attributes, Methods, `__init__`, and `self`**.  
> The **Four Pillars of OOP** (*Encapsulation, Inheritance, Polymorphism, Abstraction*) will be explored in depth in **Day 24**.

---

## 📌 Table of Contents

1. [What is OOP? (Short Format)](#-what-is-oop-short-format)
2. [Procedural vs Object-Oriented Programming](#-procedural-vs-object-oriented-programming)
3. [Core Building Blocks](#-core-building-blocks)
   - [1. Class](#1-class)
   - [2. Object](#2-object)
   - [3. The `__init__()` Constructor & `self`](#3-the-__init__-constructor--self)
   - [4. Attributes: Class vs Instance](#4-attributes-class-vs-instance)
   - [5. Methods (Behaviors)](#5-methods-behaviors)
4. [Built-in Object Inspection Tools](#-built-in-object-inspection-tools)
5. [Preview: The Four Pillars of OOP (Coming Day 24)](#-preview-the-four-pillars-of-oop-coming-day-24)
6. [Code Implementation & Running the Code](#-code-implementation--running-the-code)
7. [Summary & Key Takeaways](#-summary--key-takeaways)

---

## 💡 What is OOP? (Short Format)

**Object-Oriented Programming (OOP)** is a programming paradigm organized around **objects** rather than actions or logic alone.

An **object** is a self-contained unit that bundles:
- **State / Data**: Represented by **Attributes** (variables).
- **Behavior / Action**: Represented by **Methods** (functions).

```
┌────────────────────────────────────────────────────────┐
│                        OBJECT                          │
│                                                        │
│   ┌──────────────────────┐    ┌────────────────────┐   │
│   │   ATTRIBUTES (Data)  │    │  METHODS (Actions) │   │
│   │   • name = "Harish"  │    │  • introduce()     │   │
│   │   • roll_no = 101    │    │  • study()         │   │
│   └──────────────────────┘    └────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

### Why Use OOP?
- **Real-World Modeling**: Entities in software mirror physical or conceptual objects (User, Car, Account, Order).
- **Modularity & Organization**: Code is separated into clean, distinct, self-contained components.
- **Reusability**: Define a class once and instantiate infinite distinct objects.
- **Maintainability**: Makes large applications much easier to debug, test, and scale.

---

## ⚖️ Procedural vs Object-Oriented Programming

| Feature | Procedural Programming | Object-Oriented Programming (OOP) |
| :--- | :--- | :--- |
| **Primary Unit** | Functions / Procedures | Classes & Objects |
| **Data & Logic** | Data and functions are separate | Data and functions are bundled together |
| **Focus** | How to do things (Step-by-step) | What entities exist and how they interact |
| **Real-World Mapping** | Abstract & algorithmic | Intuitive and directly models real entities |
| **Reusability** | Through standalone functions | Through objects and classes |

---

## 🧱 Core Building Blocks

### 1. Class
A **Class** is a blueprint or template for creating objects. It defines what attributes and behaviors the objects created from it will possess.

```python
class SimpleCar:
    """Blueprint for creating cars."""
    pass
```

### 2. Object
An **Object** is a concrete instance of a class loaded into memory with its own identity.

```python
car1 = SimpleCar()
car2 = SimpleCar()

print(car1 is not car2)  # True (two distinct objects in memory)
```

---

### 3. The `__init__()` Constructor & `self`

- **`__init__()`**: A special dunder (double underscore) method automatically executed when an object is instantiated. It initializes the object's initial state.
- **`self`**: A reference to the current instance of the class. It allows each object to access and modify its own attributes and methods.

```python
class Student:
    def __init__(self, name: str, roll_no: int, course: str):
        self.name = name          # Instance attribute
        self.roll_no = roll_no    # Instance attribute
        self.course = course      # Instance attribute

    def introduce(self) -> None:
        print(f"Hi, I am {self.name} (Roll No: {self.roll_no}), studying {self.course}.")
```

---

### 4. Attributes: Class vs Instance

```python
class Developer:
    platform = "GitHub"  # Class Attribute: Shared across ALL instances

    def __init__(self, name: str, language: str):
        self.name = name          # Instance Attribute: Unique to this developer
        self.language = language  # Instance Attribute: Unique to this developer
```

- **Class Attribute**: Belongs to the class itself; shared by all instances.
- **Instance Attribute**: Belongs to a specific instance; values differ per object.

---

### 5. Methods (Behaviors)

Methods define what actions an object can perform or how its internal attributes change over time.

```python
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"[+] Deposited ${amount:.2f}. Balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[+] Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            print("[-] Insufficient balance or invalid amount.")
```

---

## 🔍 Built-in Object Inspection Tools

Python offers built-in utilities to inspect and verify objects at runtime:

| Function | Purpose | Example | Result |
| :--- | :--- | :--- | :--- |
| `type(obj)` | Returns the class of an object | `type(s1)` | `<class '__main__.Student'>` |
| `isinstance(obj, Class)` | Checks if `obj` is an instance of `Class` | `isinstance(s1, Student)` | `True` |
| `hasattr(obj, 'attr')` | Checks if object has a given attribute | `hasattr(s1, 'name')` | `True` |
| `getattr(obj, 'attr')` | Reads attribute value dynamically | `getattr(s1, 'course')` | `'Computer Science'` |
| `id(obj)` | Returns unique memory address identifier | `id(s1)` | `14051...` |

---

## 🔮 Preview: The Four Pillars of OOP (Coming Day 24)

While today builds the foundational syntax and mechanics of Classes and Objects, tomorrow (**Day 24**) will deep dive into the **Four Pillars of OOP**:

```
                  ┌───────────────────────────────────────────────┐
                  │              THE FOUR PILLARS OF OOP          │
                  │                 (Coming in Day 24)            │
                  └───────┬───────────┬───────────┬───────────┬───┘
                          │           │           │           │
       ┌──────────────────┘           │           │           └──────────────────┐
       ▼                              ▼           ▼                              ▼
┌──────────────┐              ┌──────────────┐ ┌──────────────┐          ┌──────────────┐
│ ENCAPSULATION│              │ INHERITANCE  │ │ POLYMORPHISM │          │ ABSTRACTION  │
│ Restrict     │              │ Code reuse   │ │ Many forms / │          │ Hide complex │
│ direct access│              │ parent-child │ │ uniform      │          │ internal     │
│ to internal  │              │ hierarchy    │ │ interface    │          │ details      │
│ state        │              │              │ │              │          │              │
└──────────────┘              └──────────────┘ └──────────────┘          └──────────────┘
```

1. **Encapsulation**: Restricting direct access to data using private/protected attributes (`_protected`, `__private`) and getters/setters.
2. **Inheritance**: Creating child classes that inherit attributes and methods from a parent class for code reuse.
3. **Polymorphism**: The ability of different classes to respond to the same method call in their own specialized way.
4. **Abstraction**: Hiding internal implementation complexities and exposing only high-level essential interfaces (using `abc.ABC` and `@abstractmethod`).

---

## 🚀 Code Implementation & Running the Code

### File: `day23.py`
All practical examples, demonstrations, and inspection routines are included in [`day23.py`](day23.py).

### How to Run:
```bash
# Clone the repository
git clone https://github.com/harish-0987/DAY-23-OF-PYTHON.git

# Navigate into the project folder
cd DAY-23-OF-PYTHON

# Run the Day 23 script
python day23.py
```

---

## 📝 Summary & Key Takeaways

- **OOP** is a paradigm that groups related state (data) and behavior (functions) into objects.
- A **Class** is the blueprint; an **Object** is the real instance in memory.
- `__init__()` acts as the constructor to initialize instance attributes when an object is instantiated.
- `self` refers to the current instance and must be the first parameter of any instance method.
- **Class attributes** are shared by all instances, while **Instance attributes** are unique to each instance.
- **Next Step**: Day 24 will tackle the **Four Pillars of OOP** with full practical implementations!

---

> *"Not here to be known, here to build."* — **Harish**
