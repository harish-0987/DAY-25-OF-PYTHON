# =============================================================================
# DAY 4: TYPE CONVERSION IN PYTHON (BASIC TO ADVANCED)
# Author: Harish
# Repository: DAY-4-OF-PYTHON / Python Learning Series
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("DAY 4: TYPE CONVERSION (TYPE CASTING) IN PYTHON")
print("=" * 70)

# =============================================================================
# PART 1: WHAT IS TYPE CONVERSION?
# =============================================================================
# Definition:
# Type Conversion is the process of converting the value of one data type
# (such as an integer, string, or float) into another data type.
#
# Why is it needed?
# In Python, operations between incompatible data types can cause errors
# (e.g., adding a string "10" to an integer 5). Type conversion ensures that
# data is in the expected format for operations, calculations, and inputs.
#
# Python supports two types of Type Conversion:
#   1. Implicit Type Conversion (Automatic)
#   2. Explicit Type Conversion (Manual / Type Casting)
# =============================================================================

print("\n--- PART 1: OVERVIEW OF TYPE CONVERSION ---\n")
print("Type Conversion = Changing an object's data type into another type.")
print("Two types: 1. Implicit (Automatic) | 2. Explicit (Type Casting)")


# =============================================================================
# PART 2: IMPLICIT TYPE CONVERSION (AUTOMATIC)
# =============================================================================
# In Implicit Type Conversion:
# - Python automatically converts one data type to another without programmer intervention.
# - Python always promotes the smaller data type to a larger/wider data type
#   to prevent data loss (e.g., int -> float).
# =============================================================================

print("\n--- PART 2: IMPLICIT TYPE CONVERSION ---\n")

# Example 1: Adding Integer and Float
integer_number = 15          # int
float_number = 4.5           # float

result_implicit = integer_number + float_number

print(f"integer_number: {integer_number} | Type: {type(integer_number).__name__}")
print(f"float_number:   {float_number}   | Type: {type(float_number).__name__}")
print(f"Result (15 + 4.5): {result_implicit} | Type: {type(result_implicit).__name__}")
print("-> Python automatically converted 'int' to 'float' to avoid loss of precision.")

# Example 2: Integer and Boolean
# In Python, True is internally treated as 1, and False as 0 in arithmetic
flag_true = True
flag_false = False
score = 50

print(f"\nscore + True:  {score + flag_true}  (50 + 1) | Type: {type(score + flag_true).__name__}")
print(f"score + False: {score + flag_false} (50 + 0) | Type: {type(score + flag_false).__name__}")

# Note: Python does NOT implicitly convert incompatible types like string and int:
# "Age: " + 25 -> Raises TypeError: can only concatenate str (not "int") to str


# =============================================================================
# PART 3: EXPLICIT TYPE CONVERSION (TYPE CASTING)
# =============================================================================
# In Explicit Type Conversion:
# - The programmer manually converts the data type using Python's built-in functions.
# - Also known as "Type Casting".
#
# Common Built-in Conversion Functions:
#   - int()   : Converts compatible value to integer
#   - float() : Converts compatible value to floating-point number
#   - str()   : Converts any data type into its string representation
#   - bool()  : Converts value to Boolean (True or False)
#   - list()  : Converts iterable (string, tuple, set) into a list
#   - tuple() : Converts iterable into a tuple
#   - set()   : Converts iterable into a set (removes duplicates)
#   - dict()  : Converts sequence of (key, value) pairs into a dictionary
# =============================================================================

print("\n--- PART 3: EXPLICIT TYPE CONVERSION (TYPE CASTING) ---\n")

# 1. Converting to Integer: int()
str_num = "100"
converted_int = int(str_num)
float_val = 99.85
truncated_int = int(float_val)  # Note: Discards decimal part, does NOT round

print("1. int() Conversions:")
print(f"   String '100' -> int: {converted_int} (Type: {type(converted_int).__name__})")
print(f"   Float 99.85  -> int: {truncated_int} (Truncated decimal part)")

# 2. Converting to Float: float()
int_val = 42
str_float = "3.14159"
converted_float1 = float(int_val)
converted_float2 = float(str_float)

print("\n2. float() Conversions:")
print(f"   Integer 42     -> float: {converted_float1}")
print(f"   String '3.14159' -> float: {converted_float2}")

# 3. Converting to String: str()
count = 250
temp = 36.6
is_active = True

print("\n3. str() Conversions:")
print(f"   int {count}      -> str: '{str(count)}'")
print(f"   float {temp}    -> str: '{str(temp)}'")
print(f"   bool {is_active} -> str: '{str(is_active)}'")

# 4. Converting to Boolean: bool()
# Rules:
# - Falsy values: 0, 0.0, "", [], (), {}, None, False -> evaluate to False
# - Truthy values: Any non-zero number, non-empty collection/string -> evaluate to True
print("\n4. bool() Conversions (Truthy vs Falsy):")
print(f"   bool(1)        -> {bool(1)}")
print(f"   bool(0)        -> {bool(0)}")
print(f"   bool('Python') -> {bool('Python')}")
print(f"   bool('')       -> {bool('')} (empty string)")
print(f"   bool([])       -> {bool([])} (empty list)")
print(f"   bool([1, 2])   -> {bool([1, 2])} (non-empty list)")

# 5. Converting Collections: list(), tuple(), set(), dict()
message = "HELLO"
char_list = list(message)
char_tuple = tuple(char_list)
unique_chars = set("ABRAKADABRA")

# Dictionary from list of key-value tuples
pairs = [("name", "Harish"), ("day", 4), ("language", "Python")]
profile_dict = dict(pairs)

print("\n5. Collection Conversions:")
print(f"   str '{message}' to list:   {char_list}")
print(f"   list to tuple:            {char_tuple}")
print(f"   'ABRAKADABRA' to set:     {unique_chars} (Duplicates removed)")
print(f"   List of pairs to dict:    {profile_dict}")


# =============================================================================
# PART 4: COMMON ERRORS & SAFE TYPE CASTING
# =============================================================================
# When a type conversion cannot be performed, Python raises exceptions:
#   1. ValueError: When the value is incompatible (e.g., int("hello") or int("12.5"))
#   2. TypeError: When converting an unsupported data type
# =============================================================================

print("\n--- PART 4: COMMON ERRORS & SAFE CASTING ---\n")

invalid_numeric_str = "abc"
float_str = "45.67"

# Trying to convert invalid string to int:
try:
    bad_result = int(invalid_numeric_str)
except ValueError as error:
    print(f"[Handled Error] int('{invalid_numeric_str}') failed: {error}")

# Converting float string to int directly: int("45.67") -> raises ValueError
try:
    bad_int = int(float_str)
except ValueError as error:
    print(f"[Handled Error] int('{float_str}') directly failed: {error}")
    # Correct two-step conversion:
    correct_int = int(float(float_str))
    print(f"   -> Correct approach: int(float('{float_str}')) = {correct_int}")


# =============================================================================
# PART 5: REAL-WORLD PRACTICAL EXAMPLES
# =============================================================================

print("\n--- PART 5: REAL-WORLD PRACTICAL EXAMPLES ---\n")

# Practical Example 1: Calculating Total Price from String Input
raw_price = "49.99"
raw_quantity = "3"

total_price = float(raw_price) * int(raw_quantity)
print("1. Shopping Cart Calculation:")
print(f"   Unit Price: ${raw_price}, Quantity: {raw_quantity}")
print(f"   Total Price: ${total_price:.2f} (Calculated after explicit conversion)")

# Practical Example 2: Removing Duplicates from a List using set()
raw_ids = [101, 102, 101, 103, 104, 102, 105]
unique_ids = list(set(raw_ids))
print("\n2. Deduplicating IDs:")
print(f"   Original IDs: {raw_ids}")
print(f"   Deduplicated: {unique_ids}")

# Practical Example 3: Formatting Strings with Numbers
user_age = 22
welcome_msg = "Hello Harish, your age is " + str(user_age) + " years."
print("\n3. String Concatenation:")
print(f"   {welcome_msg}")

print("\n" + "=" * 70)
print("DAY 4 COMPLETE: Mastered Implicit and Explicit Type Conversion in Python!")
print("=" * 70)
