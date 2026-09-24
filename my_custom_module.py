# =============================================================================
# HELPER MODULE: my_custom_module.py
# Used to demonstrate User-Defined Modules in Day 18
# Author: Harish
# Repository: DAY-18-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================
"""
A simple custom user-defined module demonstrating:
- Module variables/constants
- Custom functions
- The importance of `if __name__ == '__main__':`
"""

# 1. Module Variables / Constants
MODULE_NAME = "Harish Custom Math & Utility Module"
VERSION = "1.0.0"
PI_APPROX = 3.14159


# 2. Module Functions
def greet_user(name: str) -> str:
    """Returns a friendly greeting message."""
    return f"Hello, {name}! Welcome to Python Modules."


def add_numbers(a: float, b: float) -> float:
    """Calculates the sum of two numbers."""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Calculates the product of two numbers."""
    return a * b


def get_circle_area(radius: float) -> float:
    """Calculates the area of a circle using PI_APPROX."""
    return PI_APPROX * (radius ** 2)


# 3. Special __name__ check
# This block runs ONLY when this file is executed directly (e.g., `python my_custom_module.py`).
# It will NOT run when this file is imported as a module into another script!
if __name__ == "__main__":
    print("=" * 60)
    print("Running my_custom_module.py directly as a standalone script!")
    print(f"Module Name: {MODULE_NAME} (v{VERSION})")
    print(greet_user("Developer"))
    print(f"Sample calculation: 5 + 10 = {add_numbers(5, 10)}")
    print("=" * 60)
