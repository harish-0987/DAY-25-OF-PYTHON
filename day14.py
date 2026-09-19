# =============================================================================
# DAY 14: LIST COMPREHENSION IN PYTHON
# Author: Harish
# Repository: DAY-14-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# 1. WHAT IS LIST COMPREHENSION? (BASIC CONCEPT)
# =============================================================================
# List comprehension offers a shorter, cleaner, and more readable syntax
# to create a new list from an existing iterable (e.g., list, range, string).
#
# Standard Syntax:
#   new_list = [expression for item in iterable]

print("--- 1. TRADITIONAL FOR LOOP VS LIST COMPREHENSION ---")

# Problem: Create a list of squares of numbers from 1 to 5

# Way 1: Traditional for loop approach
squares_loop = []
for num in range(1, 6):
    squares_loop.append(num ** 2)
print("Using traditional for loop   :", squares_loop)

# Way 2: List Comprehension approach (Cleaner, 1 line!)
squares_comp = [num ** 2 for num in range(1, 6)]
print("Using List Comprehension      :", squares_comp)


# =============================================================================
# 2. LIST COMPREHENSION WITH CONDITION (FILTERING WITH 'if')
# =============================================================================
# You can filter items by adding an 'if' condition at the end.
# Only items that satisfy the condition will be included in the new list.
#
# Syntax:
#   new_list = [expression for item in iterable if condition]

print("\n--- 2. LIST COMPREHENSION WITH 'if' CONDITION ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way:
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)
print("Even numbers (Traditional loop):", evens_loop)

# List Comprehension way:
evens_comp = [n for n in numbers if n % 2 == 0]
print("Even numbers (List Comp)       :", evens_comp)

# Example: Filter numbers greater than 5
greater_than_5 = [n for n in numbers if n > 5]
print("Numbers greater than 5         :", greater_than_5)


# =============================================================================
# 3. LIST COMPREHENSION WITH 'if-else' (CONDITIONAL VALUES)
# =============================================================================
# If you want to transform the value based on a condition (if True do this,
# else do that), place 'if-else' BEFORE the 'for' keyword.
#
# Syntax:
#   new_list = [expression_if_true if condition else expression_if_false for item in iterable]

print("\n--- 3. LIST COMPREHENSION WITH 'if-else' ---")

numbers = [1, 2, 3, 4, 5, 6]

# Classify numbers as "Even" or "Odd"
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Numbers                :", numbers)
print("Even/Odd Classification:", labels)

# Example: Double the number if even, keep it same if odd
transformed = [n * 2 if n % 2 == 0 else n for n in numbers]
print("Double if even, else same:", transformed)


# =============================================================================
# 4. LIST COMPREHENSION WITH STRINGS
# =============================================================================
# List comprehension works seamlessly with any iterable, including strings.

print("\n--- 4. LIST COMPREHENSION WITH STRINGS ---")

# Example A: Converting characters to uppercase
word = "python"
letters = [char.upper() for char in word]
print(f"Characters of '{word}' in uppercase:", letters)

# Example B: Filtering vowels from a string
text = "List Comprehension is awesome"
vowels = [char for char in text if char.lower() in 'aeiou']
print("Vowels found in text:", vowels)

# Example C: Converting list of words to uppercase
fruits = ["apple", "banana", "cherry", "mango"]
capitalized_fruits = [fruit.upper() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)


# =============================================================================
# 5. NESTED LIST COMPREHENSION (BASIC LEVEL)
# =============================================================================
# You can use nested loops inside a list comprehension.

print("\n--- 5. NESTED LIST COMPREHENSION ---")

# Example A: Flattening a 2D matrix (nested list) into a 1D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traditional way:
flat_loop = []
for row in matrix:
    for item in row:
        flat_loop.append(item)
print("Flattened matrix (Traditional):", flat_loop)

# List Comprehension way:
flat_comp = [item for row in matrix for item in row]
print("Flattened matrix (List Comp)   :", flat_comp)

# Example B: Generating coordinate pairs (x, y)
colors = ["red", "green"]
objects = ["ball", "pen"]
combinations = [(c, o) for c in colors for o in objects]
print("Combinations of color and object:", combinations)


# =============================================================================
# 6. SUMMARY & KEY TAKEAWAYS
# =============================================================================
# 1. Basic syntax: [expr for item in iterable]
# 2. Filtering syntax: [expr for item in iterable if condition]
# 3. If-Else syntax: [expr1 if cond else expr2 for item in iterable]
# 4. Readability rule: Use list comprehensions for simple, clear transformations.
#    If logic becomes too complicated, stick with regular loops!
