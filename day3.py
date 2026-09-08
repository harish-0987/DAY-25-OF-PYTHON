# =============================================================================
# DAY 3: TOKENS AND DATA TYPES IN PYTHON (BASIC TO INTERMEDIATE)
# Author: Harish
# Repository: PYTHON-DAY-2 / Python Learning Series
# Motto: "Not here to be known, here to build."
# =============================================================================

import keyword

print("=" * 60)
print("DAY 3: TOKENS AND DATA TYPES IN PYTHON")
print("=" * 60)

# =============================================================================
# PART 1: WHAT IS A TOKEN IN PYTHON?
# =============================================================================
# Definition:
# A token is the smallest individual unit in a Python program.
# When Python reads your code, it breaks the source code down into tokens.
# Think of tokens as the words, punctuation marks, and symbols in a sentence.
#
# Python has 5 main types of tokens:
#   1. Keywords
#   2. Identifiers
#   3. Literals (Constants)
#   4. Operators
#   5. Punctuators / Delimiters
# =============================================================================

print("\n--- PART 1: TYPES OF TOKENS ---\n")

# -----------------------------------------------------------------------------
# 1. KEYWORDS
# -----------------------------------------------------------------------------
# Reserved words that have special pre-defined meaning to the Python interpreter.
# You cannot use keywords as variable names, function names, or identifiers.
# Examples: if, else, while, for, def, return, class, import, True, False, None
print("1. Keywords in Python:")
print(f"Total keywords in this Python version: {len(keyword.kwlist)}")
print("Sample Keywords:", keyword.kwlist[:10])

# -----------------------------------------------------------------------------
# 2. IDENTIFIERS
# -----------------------------------------------------------------------------
# Names given to entities like variables, functions, classes, modules, etc.
# Rules for valid identifiers:
#   - Can contain letters (a-z, A-Z), digits (0-9), and underscores (_)
#   - Must NOT start with a digit (e.g., '1name' is invalid, 'name1' is valid)
#   - Cannot be a reserved keyword
#   - Case-sensitive ('age' and 'Age' are different)
user_name = "Harish"    # 'user_name' is a valid identifier
student_score = 95      # 'student_score' is a valid identifier
_temp_val = 36.6        # Identifier starting with underscore is valid
print("\n2. Identifiers:")
print("Valid identifiers example values:", user_name, student_score, _temp_val)

# -----------------------------------------------------------------------------
# 3. LITERALS
# -----------------------------------------------------------------------------
# Raw data or fixed values assigned directly to variables.
# Types of Literals:
#   - String Literals: "Hello", 'Python'
#   - Numeric Literals: 100 (int), 3.14 (float), 2+3j (complex)
#   - Boolean Literals: True, False
#   - Special Literal: None (represents absence of value)
str_lit = "Hello World"   # String literal
int_lit = 42              # Integer literal
float_lit = 99.99         # Float literal
bool_lit = True           # Boolean literal
none_lit = None           # None literal (special)

print("\n3. Literals:")
print("String Literal :", str_lit)
print("Numeric Literals:", int_lit, "(int),", float_lit, "(float)")
print("Boolean Literal :", bool_lit)
print("Special Literal :", none_lit)

# -----------------------------------------------------------------------------
# 4. OPERATORS
# -----------------------------------------------------------------------------
# Symbols that perform mathematical or logical operations on operands.
# Types of Operators:
#   - Arithmetic: +, -, *, /, //, %, **
#   - Comparison / Relational: ==, !=, >, <, >=, <=
#   - Logical: and, or, not
#   - Assignment: =, +=, -=, *=, etc.
#   - Membership: in, not in
#   - Identity: is, is not
num1 = 15
num2 = 4
print("\n4. Operators:")
print(f"Arithmetic ({num1} + {num2}) :", num1 + num2)
print(f"Modulus/Remainder ({num1} % {num2}) :", num1 % num2)
print(f"Exponentiation ({num1} ** 2) :", num1 ** 2)
print(f"Comparison ({num1} > {num2}) :", num1 > num2)
print(f"Logical (True and False) :", True and False)

# -----------------------------------------------------------------------------
# 5. PUNCTUATORS / DELIMITERS
# -----------------------------------------------------------------------------
# Symbols used to organize sentence structure, define blocks, or separate items.
# Examples: () , [] , {} , : , , , . , ; , =
# () : used in function calls, tuples, expressions
# [] : used for lists and indexing
# {} : used for dictionaries and sets
# :  : used for defining blocks (if, loops, functions)
# ,  : separates items
sample_list = [1, 2, 3]               # [ ] and , are punctuators
sample_dict = {"course": "Python"}    # { } and : and , are punctuators
print("\n5. Punctuators / Delimiters:")
print("Sample list using [] and , :", sample_list)
print("Sample dict using {} and : :", sample_dict)


# =============================================================================
# PART 2: WHAT IS A DATA TYPE IN PYTHON?
# =============================================================================
# Definition:
# A data type represents the kind of value a variable holds and determines
# what operations can be performed on that data.
#
# Key Point:
# Python is dynamically typed! You don't need to specify types explicitly.
# Python detects the data type automatically at runtime.
# =============================================================================

print("\n" + "=" * 60)
print("PART 2: DATA TYPES IN PYTHON")
print("=" * 60 + "\n")

# -----------------------------------------------------------------------------
# 1. NUMERIC TYPES (int, float, complex)
# -----------------------------------------------------------------------------
integer_val = 100               # int: whole numbers (positive or negative)
float_val = 10.5                # float: decimal numbers
complex_val = 3 + 4j            # complex: real + imaginary numbers

print("1. Numeric Types:")
print("int value    :", integer_val, "| Type:", type(integer_val))
print("float value  :", float_val, "| Type:", type(float_val))
print("complex value:", complex_val, "| Type:", type(complex_val))

# -----------------------------------------------------------------------------
# 2. SEQUENCE TYPES (str, list, tuple)
# -----------------------------------------------------------------------------
# str   : Immutable sequence of characters
# list  : Ordered, mutable (changeable) collection of items
# tuple : Ordered, immutable (unchangeable) collection of items
greeting = "Hello, Python!"     # str
fruits = ["apple", "mango"]     # list
coordinates = (10.0, 20.0)      # tuple

print("\n2. Sequence Types:")
print("str   :", greeting, "| Type:", type(greeting))
print("list  :", fruits, "| Type:", type(fruits))
print("tuple :", coordinates, "| Type:", type(coordinates))

# -----------------------------------------------------------------------------
# 3. MAPPING TYPE (dict)
# -----------------------------------------------------------------------------
# dict: Stores data in key-value pairs (mutable and indexed by keys)
student = {
    "name": "Harish",
    "track": "Python Full Stack",
    "day": 3
}

print("\n3. Mapping Type:")
print("dict :", student, "| Type:", type(student))
print("Accessing dict key 'name':", student["name"])

# -----------------------------------------------------------------------------
# 4. SET TYPES (set, frozenset)
# -----------------------------------------------------------------------------
# set: Unordered collection of unique items (no duplicates allowed)
unique_numbers = {1, 2, 2, 3, 4, 4, 5}  # Duplicates automatically removed
frozen_numbers = frozenset([1, 2, 3])   # Immutable version of set

print("\n4. Set Types:")
print("set (duplicates removed):", unique_numbers, "| Type:", type(unique_numbers))
print("frozenset               :", frozen_numbers, "| Type:", type(frozen_numbers))

# -----------------------------------------------------------------------------
# 5. BOOLEAN TYPE (bool)
# -----------------------------------------------------------------------------
# bool: Represents one of two values: True or False
is_active = True
has_errors = False

print("\n5. Boolean Type:")
print("is_active  :", is_active, "| Type:", type(is_active))
print("has_errors :", has_errors, "| Type:", type(has_errors))

# -----------------------------------------------------------------------------
# 6. BINARY TYPES (bytes, bytearray, memoryview)
# -----------------------------------------------------------------------------
# Used to handle raw binary data (e.g., images, files, network packets)
b_data = b"Python"              # bytes: immutable sequence of bytes
ba_data = bytearray(b"Python")  # bytearray: mutable sequence of bytes

print("\n6. Binary Types:")
print("bytes     :", b_data, "| Type:", type(b_data))
print("bytearray :", ba_data, "| Type:", type(ba_data))

# -----------------------------------------------------------------------------
# 7. NONE TYPE (NoneType)
# -----------------------------------------------------------------------------
# Represents the absence of a value or null state.
result = None

print("\n7. None Type:")
print("result :", result, "| Type:", type(result))

# -----------------------------------------------------------------------------
# 8. TYPE CHECKING AND TYPE CONVERSION (TYPE CASTING)
# -----------------------------------------------------------------------------
# Checking type using type() and isinstance()
x = 20
print("\n8. Type Checking & Conversion:")
print("isinstance(x, int) :", isinstance(x, int))

# Explicit Type Conversion (Type Casting)
num_str = "50"
converted_int = int(num_str)      # Convert str to int
float_from_int = float(x)         # Convert int to float
str_from_num = str(100)           # Convert int to str

print("Converted '50' to int   :", converted_int, "| Type:", type(converted_int))
print("Converted 20 to float   :", float_from_int, "| Type:", type(float_from_int))
print("Converted 100 to string :", repr(str_from_num), "| Type:", type(str_from_num))

# =============================================================================
# SUMMARY
# =============================================================================
"""
SUMMARY:
1. TOKENS:
   - Smallest individual building block of a program.
   - 5 Types: Keywords, Identifiers, Literals, Operators, Punctuators/Delimiters.

2. DATA TYPES:
   - Defines the category of data a variable holds and how it behaves.
   - Built-in types:
     * Numeric: int, float, complex
     * Sequence: str, list, tuple
     * Mapping: dict
     * Set: set, frozenset
     * Boolean: bool
     * Binary: bytes, bytearray, memoryview
     * None: NoneType
   - Python is dynamically typed; types are inferred at runtime.
   - Check types using type() or isinstance().
   - Convert types using int(), float(), str(), list(), etc.
"""

print("\n" + "=" * 60)
print("Day 3 program completed successfully!")
print("=" * 60)
