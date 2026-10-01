# Day 24: Object-Oriented Programming (OOP) - Inheritance & Its Types 🧬🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-24-OF-PYTHON](https://github.com/harish-0987/DAY-24-OF-PYTHON)

Welcome to **Day 24 of Python**! Today's session is focused exclusively on **Inheritance and Its Types** in Python at a clear, practical, beginner-friendly basic level.

> [!NOTE]
> **Scope for Today**: We focus strictly on **Inheritance and all its 5 types** along with essential foundational mechanics (`super()`, method overriding, `issubclass()`, `isinstance()`, and MRO). Other OOP topics such as Encapsulation, Polymorphism, and Abstraction are kept separate to ensure deep, focused mastery of inheritance.

---

## 📌 Table of Contents

1. [What is Inheritance? (Basic Level)](#-what-is-inheritance-basic-level)
2. [Why Use Inheritance?](#-why-use-inheritance)
3. [Key Terminology](#-key-terminology)
4. [Core Mechanics of Inheritance](#-core-mechanics-of-inheritance)
   - [1. Basic Inheritance Syntax](#1-basic-inheritance-syntax)
   - [2. The `super()` Function & Constructor Inheritance](#2-the-super-function--constructor-inheritance)
   - [3. Method Overriding](#3-method-overriding)
5. [The 5 Types of Inheritance in Python](#-the-5-types-of-inheritance-in-python)
   - [Type 1: Single Inheritance](#type-1-single-inheritance)
   - [Type 2: Multilevel Inheritance](#type-2-multilevel-inheritance)
   - [Type 3: Multiple Inheritance & MRO](#type-3-multiple-inheritance--mro)
   - [Type 4: Hierarchical Inheritance](#type-4-hierarchical-inheritance)
   - [Type 5: Hybrid Inheritance](#type-5-hybrid-inheritance)
6. [Built-in Verification Tools (`issubclass()` & `isinstance()`)](#-built-in-verification-tools)
7. [Quick Summary Comparison Table](#-quick-summary-comparison-table)
8. [Code Implementation & Running the Code](#-code-implementation--running-the-code)

---

## 💡 What is Inheritance? (Basic Level)

**Inheritance** is an Object-Oriented Programming (OOP) mechanism that allows a new class (**Child / Derived Class**) to acquire the attributes (variables) and methods (functions) of an existing class (**Parent / Base Class**).

Inheritance establishes an **"is-a"** relationship between entities:
- A `Dog` **is-a** `Animal`.
- A `Car` **is-a** `Vehicle`.
- A `Student` **is-a** `Person`.

```
┌──────────────────────────────────────────────┐
│           PARENT CLASS (Base Class)          │
│       Attributes: name, age                  │
│       Methods: eat(), sleep()                │
└──────────────────────┬───────────────────────┘
                       │
                       │ inherits
                       ▼
┌──────────────────────────────────────────────┐
│           CHILD CLASS (Derived Class)        │
│       Inherits: name, age, eat(), sleep()    │
│       Adds: breed, bark()                    │
└──────────────────────────────────────────────┘
```

---

## 🎯 Why Use Inheritance?

1. **Code Reusability**: Define common logic once in the parent class and reuse it across multiple child classes without rewriting code.
2. **DRY Principle (Don't Repeat Yourself)**: Eliminates code duplication across related classes.
3. **Extensibility**: Add child-specific attributes or methods without modifying the parent class.
4. **Logical Organization**: Naturally models real-world hierarchies and domain relationships.

---

## 🏷️ Key Terminology

| Term | Also Known As | Meaning |
| :--- | :--- | :--- |
| **Parent Class** | Base Class, Super Class | The existing class whose features are being inherited. |
| **Child Class** | Derived Class, Sub Class | The new class that inherits features from the parent class. |
| **`super()`** | Super proxy | A built-in helper that calls parent class methods/constructors. |
| **Overriding** | Redefinition | When a child class provides its own implementation of a parent method. |

---

## ⚙️ Core Mechanics of Inheritance

### 1. Basic Inheritance Syntax

To inherit from a class, simply pass the parent class name inside parentheses after the child class name:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

my_dog = Dog("Buddy")
my_dog.eat()   # Inherited from Animal -> Buddy is eating.
my_dog.bark()  # Defined in Dog       -> Buddy says: Woof! Woof!
```

---

### 2. The `super()` Function & Constructor Inheritance

When a child class defines its own `__init__()`, it overrides the parent's `__init__()`.  
To properly initialize the parent attributes, use `super().__init__(...)`:

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name: str, age: int, roll_no: int, course: str):
        # Call Parent's __init__ using super()
        super().__init__(name, age)
        # Child-specific attributes
        self.roll_no = roll_no
        self.course = course

s = Student("Harish", 21, 101, "Python Full Stack")
print(s.name, s.age, s.roll_no, s.course)
```

---

### 3. Method Overriding

**Method Overriding** occurs when a child class implements a method with the same name as a method in its parent class. The child's method overrides the parent's default behavior:

```python
class Vehicle:
    def start(self):
        print("Vehicle starting with a physical key.")

class ElectricCar(Vehicle):
    def start(self):
        # Overrides Vehicle's start method
        print("Electric car starting silently with a push button!")

v = Vehicle()
v.start()  # Vehicle starting with a physical key.

ev = ElectricCar()
ev.start()  # Electric car starting silently with a push button!
```

---

## 🌐 The 5 Types of Inheritance in Python

```
1. Single            2. Multilevel         3. Multiple
  ┌────────┐          ┌────────┐          ┌───┐     ┌───┐
  │ Parent │          │ Grand- │          │ A │     │ B │
  └───┬────┘          │ parent │          └──┬┘     └┬──┘
      │               └───┬────┘             └───┬───┘
      ▼                   ▼                      ▼
  ┌────────┐          ┌────────┐              ┌─────┐
  │ Child  │          │ Parent │              │  C  │
  └────────┘          └───┬────┘              └─────┘
                          ▼
                      ┌────────┐
                      │ Child  │
                      └────────┘

4. Hierarchical                         5. Hybrid
      ┌────────┐                               ┌──────────┐
      │ Parent │                               │  Base A  │
      └───┬────┘                               └──┬────┬──┘
    ┌─────┴─────┐                                 │    │
    ▼           ▼                                 ▼    ▼
┌───────┐   ┌───────┐                         ┌───┐    ┌───┐
│Child 1│   │Child 2│                         │ B │    │ C │
└───────┘   └───────┘                         └──┬┘    └┬──┘
                                                 └───┬──┘
                                                     ▼
                                                  ┌─────┐
                                                  │  D  │
                                                  └─────┘
```

---

### Type 1: Single Inheritance
A child class inherits directly from **exactly one** parent class.

- **Structure**: `Parent -> Child`

```python
class Device:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} powered ON.")

class Smartphone(Device):
    def make_call(self, number: str):
        print(f"Calling {number} from {self.brand} {self.model}...")

phone = Smartphone("Apple", "iPhone 15")
phone.power_on()           # Inherited from Device
phone.make_call("123456")  # Defined in Smartphone
```

---

### Type 2: Multilevel Inheritance
A class inherits from a child class, creating a chain of inheritance (**Grandparent -> Parent -> Child**).

- **Structure**: `A -> B -> C`

```python
class LivingThing:
    def live(self):
        print("LivingThing: Performs metabolic life processes.")

class Bird(LivingThing):
    def lay_eggs(self):
        print("Bird: Lays eggs.")

class Eagle(Bird):
    def hunt(self):
        print("Eagle: Hunts with sharp eyesight.")

eagle = Eagle()
eagle.live()      # From Grandparent (LivingThing)
eagle.lay_eggs()  # From Parent (Bird)
eagle.hunt()      # From Child (Eagle)
```

---

### Type 3: Multiple Inheritance & MRO
A child class inherits from **two or more** parent classes.

- **Structure**: `Parent1, Parent2 -> Child`

```python
class Camera:
    def take_photo(self):
        print("Camera: Capturing 4K photo.")

class MusicPlayer:
    def play_music(self, song: str):
        print(f"MusicPlayer: Playing '{song}'.")

class SmartGadget(Camera, MusicPlayer):
    def browse_internet(self):
        print("SmartGadget: Browsing web.")

gadget = SmartGadget()
gadget.take_photo()            # From Camera
gadget.play_music("Believer")  # From MusicPlayer
gadget.browse_internet()       # From SmartGadget
```

#### Method Resolution Order (MRO)
When methods or attributes have name conflicts in multiple inheritance, Python resolves them using **C3 Linearization** (Method Resolution Order). Inspect the order with `ClassName.__mro__`:

```python
print(SmartGadget.__mro__)
# (<class 'SmartGadget'>, <class 'Camera'>, <class 'MusicPlayer'>, <class 'object'>)
```

---

### Type 4: Hierarchical Inheritance
**Multiple child classes** inherit from a **single parent class**.

- **Structure**: `Parent -> Child1` and `Parent -> Child2`

```python
class BankAccount:
    def __init__(self, holder: str, balance: float):
        self.holder = holder
        self.balance = balance

    def check_balance(self):
        print(f"Holder: {self.holder} | Balance: ${self.balance:,.2f}")

class SavingsAccount(BankAccount):
    def calculate_interest(self, rate: float = 4.0):
        print(f"Interest: ${(self.balance * rate) / 100:,.2f}")

class CurrentAccount(BankAccount):
    def calculate_overdraft(self, limit: float = 50000.0):
        print(f"Overdraft Limit: ${limit:,.2f}")

# Both classes share BankAccount features
sav = SavingsAccount("Harish", 150000.0)
sav.check_balance()
sav.calculate_interest()

cur = CurrentAccount("Build Corp", 500000.0)
cur.check_balance()
cur.calculate_overdraft()
```

---

### Type 5: Hybrid Inheritance
A combination of **two or more** types of inheritance (for example, combining Hierarchical and Multiple inheritance).

- **Structure**: `University -> (Faculty, StudentMember) -> TeachingAssistant`

```python
class University:
    def __init__(self, name: str = "Tech University"):
        self.uni_name = name

    def show_institution(self):
        print(f"Institution: {self.uni_name}")

# Hierarchical from University
class Faculty(University):
    def teach(self, subject: str):
        print(f"Faculty teaching {subject}.")

class StudentMember(University):
    def study(self, subject: str):
        print(f"Student studying {subject}.")

# Multiple from Faculty and StudentMember
class TeachingAssistant(Faculty, StudentMember):
    def assist_lab(self):
        print("Assisting in Python lab.")

ta = TeachingAssistant("National Tech Institute")
ta.show_institution()  # From University (Base)
ta.teach("Python OOP") # From Faculty
ta.study("Algorithms") # From StudentMember
ta.assist_lab()        # From TeachingAssistant
```

---

## 🔍 Built-in Verification Tools

Python provides two built-in functions to verify inheritance and class relationships:

### 1. `issubclass(ChildClass, ParentClass)`
Checks if a class is a direct or indirect subclass of another class.

```python
issubclass(Dog, Animal)                # True
issubclass(Animal, Dog)                # False
issubclass(Eagle, LivingThing)         # True (Multilevel)
issubclass(TeachingAssistant, Faculty) # True (Hybrid)
issubclass(Dog, object)                # True (All Python classes inherit from object)
```

### 2. `isinstance(object, Class)`
Checks if an instance is an object of a class or any of its parent classes.

```python
d = Dog("Rocky")
isinstance(d, Dog)     # True
isinstance(d, Animal)  # True (Inherited)
isinstance(d, object)  # True
```

---

## 📊 Quick Summary Comparison Table

| Type | Parents | Children | Real-World Pattern | Example |
| :--- | :---: | :---: | :--- | :--- |
| **Single** | 1 | 1 | Direct specialization | `Device -> Smartphone` |
| **Multilevel** | 1 per level | Chain | Generational ancestry | `LivingThing -> Bird -> Eagle` |
| **Multiple** | 2+ | 1 | Combining capabilities | `Camera + MusicPlayer -> SmartGadget` |
| **Hierarchical** | 1 | 2+ | Common category | `BankAccount -> Savings, Current` |
| **Hybrid** | Mixed | Mixed | Complex domain modeling | `University -> Faculty, Student -> TA` |

---

## 🚀 Code Implementation & Running the Code

### File: `day24.py`
All practical examples, demonstrations, and inspection routines are included in [`day24.py`](day24.py).

### How to Run:
```bash
# Clone the repository
git clone https://github.com/harish-0987/DAY-24-OF-PYTHON.git

# Navigate into the project folder
cd DAY-24-OF-PYTHON

# Run the Day 24 script
python day24.py
```

---

## 📝 Key Takeaways

- **Inheritance** allows child classes to derive variables and methods from parent classes.
- Models the **"is-a"** relationship and maximizes code reusability.
- Use `super().__init__()` to initialize parent class state without hardcoding parent names.
- **Method Overriding** allows a child class to provide customized behavior for parent methods.
- Python supports **all 5 types of inheritance**: Single, Multilevel, Multiple, Hierarchical, and Hybrid.
- Use `issubclass()` and `isinstance()` to inspect class hierarchies at runtime.
- For multiple inheritance, Python uses **MRO (Method Resolution Order)** via C3 Linearization to prevent ambiguity.

---

> *"Not here to be known, here to build."* — **Harish**
