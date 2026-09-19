# =============================================================================
# DAY 13: FUNCTIONS AND THEIR TYPES IN PYTHON
# Author: Harish
# Repository: DAY-13-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# 1. WHAT IS A FUNCTION? (BASIC LEVEL)
# =============================================================================
# A function is a reusable block of code that performs a specific task.
# It runs only when it is called.
# We define a function using the 'def' keyword.

print("--- 1. BASIC FUNCTION DEFINITION & CALL ---")

def greet():
    print("Hello, welcome to Day 13 of Python!")

# Calling the function
greet()


# =============================================================================
# 2. TYPES OF FUNCTIONS IN PYTHON
# =============================================================================
# In Python, functions are mainly classified into:
# 1. Built-in Functions: Predefined in Python (e.g., print(), len(), max(), min())
# 2. User-Defined Functions: Functions created by the user using 'def'
# 3. Anonymous Functions (Lambda): Small single-line functions created with 'lambda'

print("\n--- 2. TYPES OF FUNCTIONS ---")

# A. Built-in Functions Example
numbers = [10, 20, 30, 40]
print("Built-in len():", len(numbers))
print("Built-in max():", max(numbers))
print("Built-in min():", min(numbers))

# B. User-Defined Function Example
def square(num):
    return num * num

print("User-defined square(5):", square(5))

# C. Anonymous / Lambda Function Example (Basic 1-liner)
double = lambda x: x * 2
print("Lambda double(6):", double(6))


# =============================================================================
# 3. 4 BASIC TYPES OF USER-DEFINED FUNCTIONS
# =============================================================================
# Based on arguments (input) and return values (output), functions have 4 types:
# Type 1: Function without arguments and without return value
# Type 2: Function with arguments and without return value
# Type 3: Function without arguments and with return value
# Type 4: Function with arguments and with return value

print("\n--- 3. 4 TYPES BASED ON ARGUMENTS & RETURN VALUES ---")

# Type 1: No arguments, No return value
def say_hello():
    print("Type 1: Hello from a function with no parameters and no return!")

say_hello()

# Type 2: With arguments, No return value
def greet_user(name):
    print(f"Type 2: Hello, {name}!")

greet_user("Harish")

# Type 3: No arguments, With return value
def get_pi():
    return 3.14159

pi_value = get_pi()
print("Type 3: Value of Pi is:", pi_value)

# Type 4: With arguments, With return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Type 4: Addition of 10 and 20 is:", result)


# =============================================================================
# 4. BASIC TYPES OF ARGUMENTS
# =============================================================================
# Arguments are values passed into a function when calling it:
# - Positional Arguments: Passed in order based on position.
# - Keyword Arguments: Passed with parameter names (key=value).
# - Default Arguments: Uses a default value if no argument is passed.

print("\n--- 4. TYPES OF ARGUMENTS ---")

# A. Positional Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

print("\nPositional Arguments:")
display_info("Harish", 21)

# B. Keyword Arguments
print("\nKeyword Arguments:")
display_info(age=21, name="Harish")

# C. Default Arguments
def welcome_country(name, country="India"):
    print(f"Hello {name}, from {country}!")

print("\nDefault Arguments:")
welcome_country("Harish")             # Uses default "India"
welcome_country("Alex", "Canada")      # Overrides default with "Canada"
