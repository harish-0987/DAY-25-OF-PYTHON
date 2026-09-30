# =============================================================================
# DAY 23: OBJECT-ORIENTED PROGRAMMING (OOP) - INTRODUCTION & BASIC CONCEPTS
# Author: Harish
# Repository: DAY-23-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
WHAT IS OOP? (SHORT & CLEAR FORMAT)
-----------------------------------
Object-Oriented Programming (OOP) is a programming paradigm based on the concept
of "objects". An object bundles together:
  1. Data / State    -> Stored as "Attributes" (Variables)
  2. Behavior / Action -> Defined as "Methods" (Functions)

PROCEDURAL VS OBJECT-ORIENTED:
  - Procedural: Focuses on step-by-step procedures/functions acting on separate data.
  - OOP: Focuses on self-contained objects combining data and functions together.

WHY USE OOP?
  - Real-World Modeling: Maps real-world entities (cars, users, bank accounts) directly into code.
  - Modularity: Code is divided into independent, organized units.
  - Reusability: Write once, create multiple instances.
  - Maintainability: Easier to debug, modify, and extend.

CORE BUILDING BLOCKS COVERED TODAY (BASIC LEVEL):
  1. Class      : Blueprint / Template for creating objects.
  2. Object     : Concrete instance created from a class.
  3. Attributes : Variables that belong to an object or class (State).
  4. Methods    : Functions defined inside a class that define actions (Behavior).
  5. __init__() : Constructor method in Python, initializes an object's attributes.
  6. self       : Reference to the current instance of the class.

NOTE:
  The "Four Pillars of OOP" (Encapsulation, Inheritance, Polymorphism, Abstraction)
  will be covered in detail in the next day (Day 24).
"""


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# 1. WHAT IS A CLASS AND AN OBJECT?
# =============================================================================
# Class  = Blueprint / Template (e.g., Blueprint of a Car)
# Object = Real, concrete instance built from the blueprint (e.g., Your specific Red Sedan)

class SimpleCar:
    """A minimal class representing a car."""
    pass  # An empty class definition


def demo_class_and_object():
    print_section("1. WHAT IS A CLASS AND OBJECT?")
    print("- Class  : The blueprint or blueprint template.")
    print("- Object : An instance of that class allocated in memory.\n")

    # Creating instances (objects) of SimpleCar
    car1 = SimpleCar()
    car2 = SimpleCar()

    print(f"car1 object: {car1}")
    print(f"car2 object: {car2}")
    print(f"Type of car1: {type(car1)}")
    print(f"Are car1 and car2 distinct objects? {car1 is not car2}")


# =============================================================================
# 2. THE CONSTRUCTOR (__init__) AND THE 'self' PARAMETER
# =============================================================================
# __init__() is a special method (constructor) automatically called when a new
# instance of a class is created.
# 'self' represents the specific instance being created or manipulated.

class Student:
    """A class representing a student with attributes and methods."""

    def __init__(self, name: str, roll_no: int, course: str):
        """Constructor to initialize student attributes."""
        # Instance Attributes (unique to each student)
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def introduce(self) -> None:
        """Instance method to introduce the student."""
        print(f"Hello, I am {self.name} (Roll No: {self.roll_no}), studying {self.course}.")


def demo_constructor_and_self():
    print_section("2. THE CONSTRUCTOR (__init__) AND 'self'")
    print("- __init__ : Initializes the attributes as soon as the object is created.")
    print("- self     : Refers to the current instance of the class.\n")

    # Creating student objects
    s1 = Student("Harish", 101, "Computer Science")
    s2 = Student("Ananya", 102, "Data Science")

    # Calling instance methods
    s1.introduce()
    s2.introduce()

    # Accessing instance attributes directly
    print(f"\nDirect attribute access: s1.name = '{s1.name}', s2.course = '{s2.course}'")


# =============================================================================
# 3. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
# =============================================================================
# Class Attribute    : Shared by ALL instances of the class. Defined directly in class body.
# Instance Attribute : Unique to EACH instance. Defined inside __init__ using self.

class Developer:
    """Demonstrating class attributes vs instance attributes."""
    # Class Attribute (shared across all developers)
    platform = "GitHub"
    motto = "Not here to be known, here to build."

    def __init__(self, name: str, language: str):
        # Instance Attributes (unique to each developer)
        self.name = name
        self.language = language

    def show_profile(self) -> None:
        print(f"Developer: {self.name} | Primary Language: {self.language}")
        print(f"  Platform: {Developer.platform} | Motto: '{self.motto}'")


def demo_class_vs_instance_attributes():
    print_section("3. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES")
    print("- Class Attribute    : Shared by ALL objects of the class.")
    print("- Instance Attribute : Unique to EACH individual object.\n")

    dev1 = Developer("Harish", "Python")
    dev2 = Developer("Alex", "Rust")

    dev1.show_profile()
    print()
    dev2.show_profile()

    print(f"\nShared Class Attribute (Developer.platform): {Developer.platform}")
    print(f"Shared Class Attribute via instance (dev1.platform): {dev1.platform}")


# =============================================================================
# 4. INSTANCE METHODS (BEHAVIORS)
# =============================================================================
# Methods define what actions an object can perform or how its state changes.

class BankAccount:
    """A simple bank account showing state modification via methods."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"[+] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("[-] Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """Withdraws money if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[+] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        else:
            print(f"[-] Insufficient funds or invalid amount! Balance: ${self.balance:.2f}")

    def get_balance(self) -> float:
        """Returns the current account balance."""
        return self.balance


def demo_instance_methods():
    print_section("4. INSTANCE METHODS & STATE MODIFICATION")
    print("Methods define behaviors that read or modify the object's state.\n")

    account = BankAccount("Harish", 1000.0)
    print(f"Account created for: {account.account_holder} with ${account.get_balance():.2f}\n")

    account.deposit(500.0)
    account.withdraw(300.0)
    account.withdraw(2000.0)  # Attempt overdraft


# =============================================================================
# 5. USEFUL BUILT-IN FUNCTIONS FOR OBJECTS
# =============================================================================
# Python provides built-in functions to inspect objects:
# - isinstance(obj, Class): Check if an object is an instance of a class
# - hasattr(obj, 'attr')  : Check if an object has an attribute
# - getattr(obj, 'attr')  : Get attribute value dynamically
# - type(obj)             : Get the class/type of an object

def demo_builtin_object_functions():
    print_section("5. BUILT-IN INSPECTION FUNCTIONS FOR OBJECTS")

    s = Student("Harish", 101, "Python")

    print(f"isinstance(s, Student) : {isinstance(s, Student)}")
    print(f"isinstance(s, object)  : {isinstance(s, object)}  (Everything in Python inherits from object!)")
    print(f"hasattr(s, 'name')     : {hasattr(s, 'name')}")
    print(f"hasattr(s, 'salary')   : {hasattr(s, 'salary')}")
    print(f"getattr(s, 'course')   : {getattr(s, 'course')}")


# =============================================================================
# 6. ROADMAP: WHAT COMES NEXT? (THE FOUR PILLARS IN DAY 24)
# =============================================================================

def preview_four_pillars():
    print_section("6. PREVIEW: THE FOUR PILLARS OF OOP (COMING IN DAY 24)")
    print("Today we covered the foundational basics: Class, Object, Attributes, and Methods.")
    print("Tomorrow in Day 24, we explore the Four Core Pillars of OOP in detail:\n")
    print("  1. ENCAPSULATION : Bundling data & restricting direct access (private/protected).")
    print("  2. INHERITANCE   : Deriving new classes from existing ones to reuse code.")
    print("  3. POLYMORPHISM  : Same interface/method name behaving differently across types.")
    print("  4. ABSTRACTION   : Hiding internal complexity and showing only essential features.")


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 23: OBJECT-ORIENTED PROGRAMMING (OOP) - INTRODUCTION & BASICS")
    print(" Author: Harish | Repository: DAY-23-OF-PYTHON")
    print(" Motto: 'Not here to be known, here to build.'")
    print("=" * 70)

    demo_class_and_object()
    demo_constructor_and_self()
    demo_class_vs_instance_attributes()
    demo_instance_methods()
    demo_builtin_object_functions()
    preview_four_pillars()

    print("\n" + "=" * 70)
    print(" DAY 23 COMPLETE: Basics of OOP Mastered Successfully!")
    print(" Next Step (Day 24): The Four Pillars of OOP in Detail.")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
