# =============================================================================
# DAY 24: OBJECT-ORIENTED PROGRAMMING (OOP) - INHERITANCE & ITS TYPES
# Author: Harish
# Repository: DAY-24-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
WHAT IS INHERITANCE? (BASIC LEVEL GUIDE)
----------------------------------------
Inheritance is one of the foundational pillars of Object-Oriented Programming (OOP).
It allows a new class (Child/Derived class) to inherit attributes and methods
from an existing class (Parent/Base class).

RELATIONSHIP:
  Inheritance models the "is-a" relationship.
  Example: A Dog "is-a" Animal. A Car "is-a" Vehicle. A Student "is-a" Person.

TERMINOLOGY:
  1. Parent Class (Base / Super Class)   : The class whose properties are inherited.
  2. Child Class  (Derived / Sub Class)  : The class that inherits from the parent.

WHY USE INHERITANCE?
  - Code Reusability : Write code once in parent class, reuse across multiple child classes.
  - DRY Principle    : Don't Repeat Yourself - prevents duplicate logic.
  - Extensibility    : Add or override behavior without touching existing classes.
  - Hierarchy        : Creates clean, real-world logical relationships.

TYPES OF INHERITANCE IN PYTHON:
  1. Single Inheritance       : One child inherits from one parent (A -> B).
  2. Multilevel Inheritance   : Inheritance through multiple levels (A -> B -> C).
  3. Multiple Inheritance     : One child inherits from multiple parents (A, B -> C).
  4. Hierarchical Inheritance : Multiple children inherit from a single parent (A -> B, A -> C).
  5. Hybrid Inheritance       : Combination of two or more types of inheritance.

KEY MECHANICS COVERED:
  - super()            : Built-in function to access parent class methods and constructor.
  - Method Overriding  : Child class redefines a parent method with custom behavior.
  - issubclass()       : Check if a class inherits from another class.
  - isinstance()       : Check if an object is an instance of a class or its ancestors.
  - MRO (Method Resolution Order) : Order in which Python looks for methods in multiple inheritance.
"""


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# 1. BASIC INHERITANCE SYNTAX & CONCEPT
# =============================================================================
# Syntax:
#   class ParentClass:
#       # Parent attributes and methods
#
#   class ChildClass(ParentClass):
#       # Inherits everything from ParentClass + adds child-specific code

class Animal:
    """Base (Parent) class representing a generic animal."""

    def __init__(self, name: str):
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} is eating food.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    """Derived (Child) class inheriting from Animal."""

    def bark(self) -> None:
        """Dog-specific method."""
        print(f"{self.name} says: Woof! Woof!")


def demo_basic_inheritance():
    print_section("1. BASIC INHERITANCE SYNTAX & CONCEPT")
    print("- Dog inherits 'name', 'eat()', and 'sleep()' from Animal.")
    print("- Dog also adds its own unique method: 'bark()'.\n")

    my_dog = Dog("Buddy")

    # Accessing inherited attributes and methods
    print(f"Dog's Name: {my_dog.name}")
    my_dog.eat()    # Inherited from Animal
    my_dog.sleep()  # Inherited from Animal

    # Accessing child-specific method
    my_dog.bark()   # Defined in Dog


# =============================================================================
# 2. THE super() FUNCTION & CONSTRUCTOR INHERITANCE
# =============================================================================
# When a child class defines its own __init__(), it overrides the parent's __init__().
# To call the parent's constructor and initialize inherited attributes,
# we use the super() function: super().__init__(...)

class Person:
    """Parent class representing a generic person."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """Child class extending Person with student-specific attributes."""

    def __init__(self, name: str, age: int, roll_no: int, course: str):
        # Call Parent's __init__ using super() to initialize name and age
        super().__init__(name, age)
        # Initialize child-specific attributes
        self.roll_no = roll_no
        self.course = course

    def display_student_info(self) -> None:
        # Reusing parent's method using super() or self
        super().display_info()
        print(f"Roll Number: {self.roll_no}, Course: {self.course}")


def demo_super_function():
    print_section("2. THE super() FUNCTION & CONSTRUCTOR INHERITANCE")
    print("- super().__init__() allows child classes to reuse parent initialization logic.\n")

    student = Student(name="Harish", age=21, roll_no=101, course="Python Full Stack")
    student.display_student_info()


# =============================================================================
# 3. METHOD OVERRIDING
# =============================================================================
# Method Overriding occurs when a child class provides a specific implementation
# for a method that is already defined in its parent class.

class Vehicle:
    """Parent class with a default start() method."""

    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> None:
        print(f"{self.brand} vehicle is starting with a key.")


class ElectricCar(Vehicle):
    """Child class overriding start() method for electric startup."""

    def start(self) -> None:
        # Overrides Vehicle's start method completely
        print(f"{self.brand} electric car starts silently with a push button!")


def demo_method_overriding():
    print_section("3. METHOD OVERRIDING")
    print("- Child redefines an existing parent method with child-specific behavior.\n")

    v = Vehicle("Standard")
    v.start()

    ev = ElectricCar("Tesla")
    ev.start()  # Overridden behavior called


# =============================================================================
# 4. TYPE 1: SINGLE INHERITANCE
# =============================================================================
# A child class inherits from exactly ONE parent class.
# Structure: Parent -> Child

class Device:
    """Parent class representing an electronic device."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def power_on(self) -> None:
        print(f"{self.brand} {self.model} powered ON.")


class Smartphone(Device):
    """Child class inheriting solely from Device (Single Inheritance)."""

    def make_call(self, number: str) -> None:
        print(f"Calling {number} from {self.brand} {self.model}...")


def demo_single_inheritance():
    print_section("4. TYPE 1: SINGLE INHERITANCE (1 Parent -> 1 Child)")
    print("Structure: Device -> Smartphone\n")

    phone = Smartphone("Apple", "iPhone 15")
    phone.power_on()           # Inherited from Device
    phone.make_call("9876543210")  # Defined in Smartphone


# =============================================================================
# 5. TYPE 2: MULTILEVEL INHERITANCE
# =============================================================================
# A child class inherits from a parent class, which in turn inherits
# from another parent class (Grandparent -> Parent -> Child).
# Structure: Grandparent -> Parent -> Child

class LivingThing:
    """Grandparent class."""

    def live(self) -> None:
        print("LivingThing: Performs metabolic life processes.")


class Bird(LivingThing):
    """Parent class inheriting from LivingThing."""

    def lay_eggs(self) -> None:
        print("Bird: Lays eggs.")


class Eagle(Bird):
    """Child class inheriting from Bird (and transitively from LivingThing)."""

    def hunt(self) -> None:
        print("Eagle: Hunts with sharp eyesight and talons.")


def demo_multilevel_inheritance():
    print_section("5. TYPE 2: MULTILEVEL INHERITANCE (Grandparent -> Parent -> Child)")
    print("Structure: LivingThing -> Bird -> Eagle\n")

    eagle = Eagle()
    eagle.live()      # Inherited from Grandparent (LivingThing)
    eagle.lay_eggs()  # Inherited from Parent (Bird)
    eagle.hunt()      # Defined in Child (Eagle)


# =============================================================================
# 6. TYPE 3: MULTIPLE INHERITANCE
# =============================================================================
# A child class inherits from TWO OR MORE parent classes.
# Structure: Parent A, Parent B -> Child

class Camera:
    """First parent class."""

    def take_photo(self) -> None:
        print("Camera: Capturing high-resolution 4K photo.")


class MusicPlayer:
    """Second parent class."""

    def play_music(self, song: str) -> None:
        print(f"MusicPlayer: Playing '{song}'.")


class SmartGadget(Camera, MusicPlayer):
    """Child class inheriting from BOTH Camera and MusicPlayer."""

    def browse_internet(self) -> None:
        print("SmartGadget: Browsing the web.")


def demo_multiple_inheritance():
    print_section("6. TYPE 3: MULTIPLE INHERITANCE (Multiple Parents -> 1 Child)")
    print("Structure: Camera + MusicPlayer -> SmartGadget\n")

    gadget = SmartGadget()
    gadget.take_photo()            # Inherited from Camera
    gadget.play_music("Believer")  # Inherited from MusicPlayer
    gadget.browse_internet()       # Defined in SmartGadget

    # Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO) for SmartGadget:")
    for idx, cls in enumerate(SmartGadget.__mro__, start=1):
        print(f"  {idx}. {cls.__name__}")


# =============================================================================
# 7. TYPE 4: HIERARCHICAL INHERITANCE
# =============================================================================
# MULTIPLE child classes inherit from a SINGLE parent class.
# Structure: Parent -> Child 1, Parent -> Child 2

class BankAccount:
    """Single Parent class with common account attributes and methods."""

    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self) -> None:
        print(f"Account Holder: {self.account_holder} | Balance: ${self.balance:,.2f}")


class SavingsAccount(BankAccount):
    """Child 1 inheriting from BankAccount."""

    def calculate_interest(self, rate: float = 4.0) -> None:
        interest = (self.balance * rate) / 100
        print(f"Savings Account Interest at {rate}%: ${interest:,.2f}")


class CurrentAccount(BankAccount):
    """Child 2 inheriting from BankAccount."""

    def calculate_overdraft(self, limit: float = 50000.0) -> None:
        print(f"Current Account Overdraft Facility Limit: ${limit:,.2f}")


def demo_hierarchical_inheritance():
    print_section("7. TYPE 4: HIERARCHICAL INHERITANCE (1 Parent -> Multiple Children)")
    print("Structure: BankAccount -> SavingsAccount AND BankAccount -> CurrentAccount\n")

    savings = SavingsAccount("Harish", 150000.0)
    savings.check_balance()        # Inherited from BankAccount
    savings.calculate_interest()   # Defined in SavingsAccount

    print()
    current = CurrentAccount("Build Corp", 500000.0)
    current.check_balance()        # Inherited from BankAccount
    current.calculate_overdraft()  # Defined in CurrentAccount


# =============================================================================
# 8. TYPE 5: HYBRID INHERITANCE
# =============================================================================
# Hybrid Inheritance is a combination of two or more types of inheritance
# (e.g., Hierarchical + Multiple).
#
# Structure:
#        University (Base)
#         /        \
#     Faculty     Student      <- Hierarchical (from University)
#         \        /
#      TeachingAssistant       <- Multiple (from Faculty and Student)

class University:
    """Base class for all university members."""

    def __init__(self, uni_name: str = "Tech University"):
        self.uni_name = uni_name

    def show_university(self) -> None:
        print(f"Institution: {self.uni_name}")


class Faculty(University):
    """Child 1 derived from University."""

    def teach(self, subject: str) -> None:
        print(f"Faculty: Teaching {subject} lecture.")


class StudentMember(University):
    """Child 2 derived from University."""

    def study(self, subject: str) -> None:
        print(f"Student: Studying {subject} coursework.")


class TeachingAssistant(Faculty, StudentMember):
    """Child derived from both Faculty and StudentMember (Multiple + Hierarchical = Hybrid)."""

    def assist_lab(self) -> None:
        print("Teaching Assistant: Assisting students in the Python lab session.")


def demo_hybrid_inheritance():
    print_section("8. TYPE 5: HYBRID INHERITANCE (Combination of Inheritance Types)")
    print("Structure: University -> (Faculty, StudentMember) -> TeachingAssistant\n")

    ta = TeachingAssistant("National Tech Institute")
    ta.show_university()          # Inherited from University (Base)
    ta.teach("Python OOP")        # Inherited from Faculty
    ta.study("Data Structures")   # Inherited from StudentMember
    ta.assist_lab()               # Defined in TeachingAssistant

    print("\nMethod Resolution Order (MRO) for TeachingAssistant:")
    for idx, cls in enumerate(TeachingAssistant.__mro__, start=1):
        print(f"  {idx}. {cls.__name__}")


# =============================================================================
# 9. BUILT-IN VERIFICATION TOOLS: issubclass() & isinstance()
# =============================================================================
# Python provides two essential built-in functions to verify inheritance:
#   1. issubclass(sub, sup) : True if sub is a subclass of sup.
#   2. isinstance(obj, cls) : True if obj is an instance of cls or its subclasses.

def demo_inspection_functions():
    print_section("9. BUILT-IN FUNCTIONS: issubclass() & isinstance()")

    # Testing issubclass()
    print("--- issubclass(Child, Parent) ---")
    print(f"issubclass(Dog, Animal)               : {issubclass(Dog, Animal)}")
    print(f"issubclass(Animal, Dog)               : {issubclass(Animal, Dog)}")
    print(f"issubclass(Eagle, LivingThing)        : {issubclass(Eagle, LivingThing)} (Multilevel)")
    print(f"issubclass(TeachingAssistant, Faculty): {issubclass(TeachingAssistant, Faculty)} (Hybrid)")
    print(f"issubclass(Dog, object)               : {issubclass(Dog, object)} (All classes inherit from object!)")

    # Testing isinstance()
    print("\n--- isinstance(object, Class) ---")
    d = Dog("Rocky")
    print(f"isinstance(d, Dog)                    : {isinstance(d, Dog)}")
    print(f"isinstance(d, Animal)                 : {isinstance(d, Animal)} (Inherited)")
    print(f"isinstance(d, object)                 : {isinstance(d, object)}")


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 24: OBJECT-ORIENTED PROGRAMMING (OOP) - INHERITANCE & ITS TYPES")
    print(" Author: Harish | Repository: DAY-24-OF-PYTHON")
    print(" Motto: 'Not here to be known, here to build.'")
    print("=" * 70)

    demo_basic_inheritance()
    demo_super_function()
    demo_method_overriding()
    demo_single_inheritance()
    demo_multilevel_inheritance()
    demo_multiple_inheritance()
    demo_hierarchical_inheritance()
    demo_hybrid_inheritance()
    demo_inspection_functions()

    print("\n" + "=" * 70)
    print(" DAY 24 COMPLETE: Inheritance and All 5 Types Mastered Successfully!")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
