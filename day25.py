# =============================================================================
# DAY 25: OBJECT-ORIENTED PROGRAMMING (OOP) - POLYMORPHISM IN PYTHON
# Author: Harish
# Repository: DAY-25-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
WHAT IS POLYMORPHISM? (BASIC LEVEL GUIDE)
----------------------------------------
The word "Polymorphism" is derived from two Greek words:
  - "Poly"  : Many
  - "Morph" : Forms / Shapes

In Object-Oriented Programming (OOP), Polymorphism refers to the ability of
different objects to respond to the same method call (or operator) in their own
unique way.

KEY INTUITION:
  Think of a person:
  - At home, the person acts like a parent or child.
  - In an office, the person acts like an employee.
  - In a market, the person acts like a customer.
  The same person exhibits different behaviors depending on the situation!

  Similarly, in code:
  - We call the same method name (e.g., .speak(), .area(), .render()) on different
    objects, and each object executes its own customized behavior.

WHY USE POLYMORPHISM?
  1. Loose Coupling   : Code depends on an interface or behavior, not a rigid class type.
  2. Extensibility    : New classes can be added without changing the caller's code.
  3. Clean Code       : Eliminates redundant `if-elif-else` checks based on object types.
  4. Code Reusability : Write a single generic function that works with multiple classes.

FORMS OF POLYMORPHISM IN PYTHON:
  1. Built-in Polymorphism (Built-in functions & operators)
  2. Duck Typing ("If it walks like a duck and quacks like a duck, it's a duck")
  3. Method Overriding (Inheritance-based runtime polymorphism)
  4. Polymorphic Functions (Functions taking any polymorphic object)
  5. Operator Overloading (Custom behavior for operators using dunder methods)
  6. Method Overloading Workarounds (Handling different argument signatures)
  7. Real-World Case Study (E-commerce Payment Gateway & Notification System)
"""


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# 1. BUILT-IN POLYMORPHISM (FUNCTIONS & OPERATORS)
# =============================================================================
# Python has polymorphism baked right into the core language!
#
# Examples:
#   - len() works on strings, lists, tuples, dictionaries, and sets.
#   - '+' operator performs addition for numbers, and concatenation for strings/lists.
#   - '*' operator performs multiplication for numbers, and repetition for strings/lists.

def demo_builtin_polymorphism():
    print_section("1. BUILT-IN POLYMORPHISM (FUNCTIONS & OPERATORS)")

    # Built-in Function Polymorphism: len()
    text = "Python OOP"
    numbers = [10, 20, 30, 40, 50]
    student_scores = {"Harish": 95, "Alex": 88, "Sara": 92}
    unique_tags = {"code", "python", "developer"}

    print("--- Polymorphism with len() ---")
    print(f"len(str)  : len('{text}')                  -> {len(text)} characters")
    print(f"len(list) : len({numbers})       -> {len(numbers)} items")
    print(f"len(dict) : len(student_scores)          -> {len(student_scores)} keys")
    print(f"len(set)  : len(unique_tags)             -> {len(unique_tags)} items")

    # Operator Polymorphism: '+'
    print("\n--- Polymorphism with '+' Operator ---")
    print(f"Integer Addition      : 15 + 25           = {15 + 25}")
    print(f"Float Addition        : 10.5 + 4.5        = {10.5 + 4.5}")
    print(f"String Concatenation  : 'Hello, ' + 'Dev' = {'Hello, ' + 'Dev'}")
    print(f"List Concatenation    : [1, 2] + [3, 4]   = {[1, 2] + [3, 4]}")

    # Operator Polymorphism: '*'
    print("\n--- Polymorphism with '*' Operator ---")
    print(f"Multiplication        : 5 * 4             = {5 * 4}")
    print(f"String Repetition     : 'Py!' * 3         = {'Py!' * 3}")
    print(f"List Repetition       : [0] * 4           = {[0] * 4}")


# =============================================================================
# 2. DUCK TYPING (POLYMORPHISM WITHOUT INHERITANCE)
# =============================================================================
# "If it walks like a duck and quacks like a duck, it's a duck."
# In Python, we do not care about the explicit class hierarchy or type of an object.
# As long as the object implements the required method, Python executes it happily!

class Duck:
    """Represents a real duck."""
    def sound(self) -> None:
        print("Duck: Quack, quack!")

    def swim(self) -> None:
        print("Duck: Swimming gracefully in the pond.")


class Person:
    """Represents a human who can imitate a duck."""
    def sound(self) -> None:
        print("Person: Quack! (Imitating a duck sound)")

    def swim(self) -> None:
        print("Person: Swimming in the pool like a duck.")


class Robot:
    """A mechanical robot programmed to act like a duck."""
    def sound(self) -> None:
        print("Robot: Beep-boop... [Synthesized Quack Sound]!")

    def swim(self) -> None:
        print("Robot: Navigating water with waterproof propellers.")


def make_entity_perform(entity) -> None:
    """
    Polymorphic function using Duck Typing.
    Does NOT check isinstance(entity, Duck).
    It only cares that entity has .sound() and .swim() methods!
    """
    print(f"Testing entity: {entity.__class__.__name__}")
    entity.sound()
    entity.swim()
    print("-" * 40)


def demo_duck_typing():
    print_section("2. DUCK TYPING (POLYMORPHISM WITHOUT INHERITANCE)")
    print("Duck, Person, and Robot do NOT share any common parent class.")
    print("Yet, they all respond to the exact same interface: .sound() & .swim()!\n")

    duck = Duck()
    person = Person()
    robot = Robot()

    entities = [duck, person, robot]
    for entity in entities:
        make_entity_perform(entity)


# =============================================================================
# 3. METHOD OVERRIDING (RUNTIME POLYMORPHISM VIA INHERITANCE)
# =============================================================================
# When a child class provides a specific implementation of a method that is
# already defined in its parent class, it is called Method Overriding.
#
# Calling the overridden method on a child object dynamically executes the child's
# version at runtime.

class Animal:
    """Parent base class."""
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        """Default sound method to be overridden by subclasses."""
        return "Some generic animal sound"

    def describe(self) -> None:
        print(f"I am {self.name}, and I say: {self.make_sound()}")


class Dog(Animal):
    """Child class overriding make_sound."""
    def make_sound(self) -> str:
        return "Woof! Woof!"


class Cat(Animal):
    """Child class overriding make_sound."""
    def make_sound(self) -> str:
        return "Meow! Purr!"


class Cow(Animal):
    """Child class overriding make_sound."""
    def make_sound(self) -> str:
        return "Moo! Moo!"


def demo_method_overriding():
    print_section("3. METHOD OVERRIDING (RUNTIME POLYMORPHISM VIA INHERITANCE)")
    print("All subclasses inherit from Animal, but each overrides make_sound().\n")

    animals = [
        Dog("Buddy"),
        Cat("Luna"),
        Cow("Daisy"),
    ]

    for animal in animals:
        # Same method call: describe() -> which calls overridden make_sound()
        animal.describe()


# =============================================================================
# 4. POLYMORPHISM WITH A COMMON FUNCTION (GENERIC INTERFACE)
# =============================================================================
# We can create generic functions that accept any object supporting a specific
# method. This illustrates runtime polymorphism in clean application code.

class Circle:
    """Represents a circle shape."""
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

    def shape_name(self) -> str:
        return f"Circle (radius={self.radius})"


class Rectangle:
    """Represents a rectangle shape."""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def shape_name(self) -> str:
        return f"Rectangle ({self.width}x{self.height})"


class Triangle:
    """Represents a triangle shape."""
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

    def shape_name(self) -> str:
        return f"Triangle (base={self.base}, height={self.height})"


def print_shape_details(shape) -> None:
    """
    Generic polymorphic function:
    Works with ANY shape that implements calculate_area() and shape_name().
    """
    area = shape.calculate_area()
    print(f"Shape: {shape.shape_name():<30} | Area: {area:8.2f}")


def demo_polymorphic_functions():
    print_section("4. POLYMORPHISM WITH A COMMON FUNCTION (SHAPES EXAMPLE)")
    print("The function 'print_shape_details' handles any shape object uniformly:\n")

    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(10.0, 3.0),
        Circle(2.5),
        Rectangle(12.0, 5.0)
    ]

    for s in shapes:
        print_shape_details(s)


# =============================================================================
# 5. OPERATOR OVERLOADING (SPECIAL / DUNDER METHODS)
# =============================================================================
# Operator Overloading is syntactic polymorphism.
# By implementing special methods (dunder methods like __add__, __sub__, __str__,
# __gt__), we can define how standard operators work with our custom objects.
#
# Common Dunder Methods for Operators:
#   +  : __add__(self, other)
#   -  : __sub__(self, other)
#   *  : __mul__(self, other)
#   >  : __gt__(self, other)
#   <  : __lt__(self, other)
#   == : __eq__(self, other)
#   str(): __str__(self)

class Point:
    """2D Coordinate Point with operator overloading."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        """Overload '+' operator to add two Point objects."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Point") -> "Point":
        """Overload '-' operator to subtract two Point objects."""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """Overload '==' operator to check equality of two Points."""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        """Overload str() / print() representation."""
        return f"Point({self.x}, {self.y})"


class Book:
    """Book with price comparison operator overloading."""
    def __init__(self, title: str, pages: int, price: float):
        self.title = title
        self.pages = pages
        self.price = price

    def __add__(self, other: "Book") -> int:
        """Overload '+' to combine total pages of two books."""
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    def __gt__(self, other: "Book") -> bool:
        """Overload '>' to compare book prices."""
        if isinstance(other, Book):
            return self.price > other.price
        return NotImplemented

    def __str__(self) -> str:
        return f"'{self.title}' ({self.pages} pages, ${self.price:.2f})"


def demo_operator_overloading():
    print_section("5. OPERATOR OVERLOADING (SYNTACTIC POLYMORPHISM)")

    # 1. Point addition & subtraction
    print("--- 2D Point Vector Math ---")
    p1 = Point(3, 4)
    p2 = Point(5, 7)
    p3 = p1 + p2  # Calls p1.__add__(p2)
    p4 = p2 - p1  # Calls p2.__sub__(p1)

    print(f"p1          = {p1}")
    print(f"p2          = {p2}")
    print(f"p1 + p2     = {p3}")
    print(f"p2 - p1     = {p4}")
    print(f"p1 == Point(3, 4) : {p1 == Point(3, 4)}")
    print(f"p1 == p2          : {p1 == p2}")

    # 2. Book comparisons
    print("\n--- Book Pages & Price Comparison ---")
    book1 = Book("Python Crash Course", 544, 29.99)
    book2 = Book("Fluent Python", 1014, 49.99)

    print(f"Book 1: {book1}")
    print(f"Book 2: {book2}")
    print(f"Total Pages (book1 + book2) : {book1 + book2} pages")
    print(f"Is book2 more expensive than book1? (book2 > book1) : {book2 > book1}")


# =============================================================================
# 6. METHOD OVERLOADING IN PYTHON (HOW PYTHON HANDLES IT)
# =============================================================================
# IMPORTANT NOTE:
# Traditional Method Overloading (same method name with different parameters
# in the same class) is NOT supported natively in Python in the same way as C++ or Java.
# If you define two methods with the same name, the latest definition OVERWRITES the previous one!
#
# HOW PYTHON ACHIEVES METHOD OVERLOADING:
#   Approach A: Default Arguments (most common & clean)
#   Approach B: Variable-length Arguments (*args, **kwargs)
#   Approach C: Type checking inside the method

class Calculator:
    """Demonstrating how to achieve method overloading in Python."""

    # Approach A: Default Arguments
    def add(self, a: int, b: int, c: int = 0) -> int:
        """
        Can be called with 2 arguments or 3 arguments!
        calculator.add(5, 10)       -> 15
        calculator.add(5, 10, 20)   -> 35
        """
        return a + b + c

    # Approach B: Variable Arguments (*args)
    def sum_all(self, *args: float) -> float:
        """
        Can be called with ANY number of arguments!
        calculator.sum_all(1, 2)
        calculator.sum_all(1, 2, 3, 4, 5)
        """
        return sum(args)

    # Approach C: Flexible data type handling
    def greet(self, name: str = None) -> str:
        """Overloaded behavior depending on whether name is supplied."""
        if name is not None:
            return f"Hello, {name}! Welcome back."
        return "Hello, Guest! Welcome to our platform."


def demo_method_overloading():
    print_section("6. METHOD OVERLOADING WORKAROUNDS IN PYTHON")
    print("Python does not have traditional method overloading.")
    print("Instead, we use Default Arguments and *args:\n")

    calc = Calculator()

    # Default arguments
    print("--- Default Arguments ---")
    print(f"calc.add(10, 20)        = {calc.add(10, 20)}  (2 arguments)")
    print(f"calc.add(10, 20, 30)    = {calc.add(10, 20, 30)} (3 arguments)")

    # Variable-length arguments
    print("\n--- Variable-Length Arguments (*args) ---")
    print(f"calc.sum_all(5, 15)             = {calc.sum_all(5, 15)}")
    print(f"calc.sum_all(1, 2, 3, 4, 5, 6)  = {calc.sum_all(1, 2, 3, 4, 5, 6)}")

    # None checking
    print("\n--- Optional Parameters ---")
    print(f"calc.greet()          -> {calc.greet()}")
    print(f"calc.greet('Harish')  -> {calc.greet('Harish')}")


# =============================================================================
# 7. REAL-WORLD PROJECT: POLYMORPHIC PAYMENT GATEWAYS & NOTIFICATIONS
# =============================================================================
# A clean real-world scenario: An e-commerce system that can process payments
# via Credit Card, PayPal, or UPI, and send notifications via Email or SMS.
#
# The checkout processor doesn't care which payment method is selected;
# it calls .process_payment() polymorphically!

class PaymentGateway:
    """Base Payment Gateway interface."""
    def __init__(self, provider_name: str):
        self.provider_name = provider_name

    def process_payment(self, amount: float) -> bool:
        """Interface method to be implemented by payment providers."""
        raise NotImplementedError("Subclasses must implement process_payment()")


class CreditCardPayment(PaymentGateway):
    def __init__(self, card_number: str, card_holder: str):
        super().__init__("Credit Card")
        self.card_number = card_number
        self.card_holder = card_holder

    def process_payment(self, amount: float) -> bool:
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        print(f"[{self.provider_name}] Charging ${amount:.2f} to card {masked_card} (Holder: {self.card_holder})")
        print(f"[{self.provider_name}] Verified CVV & 3D Secure OTP... Payment Approved!")
        return True


class PayPalPayment(PaymentGateway):
    def __init__(self, email: str):
        super().__init__("PayPal")
        self.email = email

    def process_payment(self, amount: float) -> bool:
        print(f"[{self.provider_name}] Redirecting to PayPal secure portal for {self.email}...")
        print(f"[{self.provider_name}] Successfully debited ${amount:.2f} from PayPal balance!")
        return True


class UPIPayment(PaymentGateway):
    def __init__(self, upi_id: str):
        super().__init__("UPI")
        self.upi_id = upi_id

    def process_payment(self, amount: float) -> bool:
        print(f"[{self.provider_name}] Sending payment request for ${amount:.2f} to UPI ID: {self.upi_id}...")
        print(f"[{self.provider_name}] PIN entered on mobile device... Transaction Success!")
        return True


# Polymorphic Checkout Processor
def checkout(payment_method: PaymentGateway, amount: float) -> None:
    """
    Polymorphic Checkout function:
    Works with ANY payment provider seamlessly!
    """
    print(f"\nInitiating checkout for amount: ${amount:.2f}")
    success = payment_method.process_payment(amount)
    if success:
        print(">> Status: Order placed successfully!\n" + "-" * 50)
    else:
        print(">> Status: Payment failed!\n" + "-" * 50)


def demo_real_world_polymorphism():
    print_section("7. REAL-WORLD PROJECT: POLYMORPHIC PAYMENT GATEWAYS")
    print("Checkout logic interacts with all payment providers through one interface:\n")

    card = CreditCardPayment("4111222233334567", "Harish P.")
    paypal = PayPalPayment("harish.dev@example.com")
    upi = UPIPayment("harish@okaxis")

    # The checkout processor treats all payment methods uniformly:
    checkout(card, 149.99)
    checkout(paypal, 49.50)
    checkout(upi, 25.00)


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 25: OBJECT-ORIENTED PROGRAMMING (OOP) - POLYMORPHISM IN PYTHON")
    print(" Author: Harish | Repository: DAY-25-OF-PYTHON")
    print(" Motto: 'Not here to be known, here to build.'")
    print("=" * 70)

    demo_builtin_polymorphism()
    demo_duck_typing()
    demo_method_overriding()
    demo_polymorphic_functions()
    demo_operator_overloading()
    demo_method_overloading()
    demo_real_world_polymorphism()

    print("\n" + "=" * 70)
    print(" DAY 25 COMPLETE: Polymorphism in Python Mastered Successfully!")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
