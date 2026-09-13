# =============================================================================
# DAY 7: TUPLES IN PYTHON (WHAT IS A TUPLE, METHODS & EXAMPLES)
# Author: Harish
# Repository: DAY---7---PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("       DAY 7: PYTHON TUPLES - CONCEPTS, OPERATIONS & KEY METHODS")
print("=" * 70)


# =============================================================================
# PART 1: WHAT IS A TUPLE?
# =============================================================================
# Definition:
# A tuple in Python is an ordered, immutable (unchangeable) collection of items.
# Tuples are written with parentheses: (item1, item2, ...)
#
# Key features:
# 1. Ordered      : Items have a fixed order that does not change.
# 2. Immutable    : Elements cannot be added, changed, or removed after creation.
# 3. Duplicates   : Tuples allow duplicate values.
# 4. Mixed types  : Can hold strings, numbers, booleans, lists, other tuples, etc.
# 5. Faster       : Tuples are faster and use less memory than lists.
# =============================================================================

print("\n--- PART 1: WHAT IS A TUPLE? ---\n")

# 1. Creating basic tuples
fruits = ("apple", "banana", "cherry")
numbers = (10, 20, 30, 40)
mixed_tuple = ("Harish", 21, True, 99.5)

print("Fruits tuple      :", fruits)
print("Numbers tuple     :", numbers)
print("Mixed data tuple  :", mixed_tuple)

# 2. Checking type and length
print("Data type         :", type(fruits).__name__)
print("Length of tuple   :", len(fruits), "items")

# 3. The Single-Element Tuple Quirk (IMPORTANT!)
# A single item without a trailing comma is treated as a regular data type (str, int).
# You MUST include a trailing comma for Python to recognize it as a tuple.
not_a_tuple = ("apple")    # Type: str
single_tuple = ("apple",)  # Type: tuple

print("\nWithout comma     :", type(not_a_tuple).__name__, "->", not_a_tuple)
print("With comma        :", type(single_tuple).__name__, "->", single_tuple)

# 4. Creating tuples without parentheses (Tuple packing by default)
coordinates = 10, 20, 30
print("Implicit tuple    :", coordinates, "type:", type(coordinates).__name__)

# 5. Empty tuple
empty_tuple = ()
print("Empty tuple       :", empty_tuple, "Length:", len(empty_tuple))


# =============================================================================
# PART 2: ACCESSING ELEMENTS (INDEXING & SLICING)
# =============================================================================
# Indexing starts at 0 for the first element.
# Negative indexing starts at -1 from the right end.
# Slicing syntax: tuple[start:stop:step] (stop index is excluded).
# =============================================================================

print("\n--- PART 2: INDEXING & SLICING ---\n")

languages = ("Python", "JavaScript", "C++", "Java", "Go", "Rust")
print("Original tuple    :", languages)

# Indexing
print("First item  (languages[0])   :", languages[0])
print("Third item  (languages[2])   :", languages[2])
print("Last item   (languages[-1])  :", languages[-1])
print("Second last (languages[-2])  :", languages[-2])

# Slicing
print("Slice [1:4] (index 1 to 3)   :", languages[1:4])
print("Slice [:3]  (first three)    :", languages[:3])
print("Slice [3:]  (from index 3)   :", languages[3:])
print("Every 2nd   (languages[::2]) :", languages[::2])
print("Reversed    (languages[::-1]):", languages[::-1])


# =============================================================================
# PART 3: IMMUTABILITY (TUPLES CANNOT BE MODIFIED)
# =============================================================================
# Unlike lists, tuples are immutable. You cannot reassign items, append, or pop.
# =============================================================================

print("\n--- PART 3: IMMUTABILITY DEMONSTRATION ---\n")

colors = ("red", "green", "blue")
print("Colors tuple:", colors)

try:
    # Attempting to modify an element
    colors[0] = "yellow"
except TypeError as error:
    print("Trying `colors[0] = 'yellow'` raised TypeError:")
    print("-->", error)

# Workaround: How to modify a tuple if ever needed
# Convert tuple to list -> modify list -> convert back to tuple
colors_list = list(colors)
colors_list.append("yellow")
colors = tuple(colors_list)
print("Updated tuple via list conversion:", colors)

# Note on nested mutable items:
# If a tuple contains a mutable object (like a list), that list can be modified!
nested_tuple = (1, 2, ["a", "b"])
print("\nNested tuple before:", nested_tuple)
nested_tuple[2].append("c")
print("Nested tuple after :", nested_tuple)


# =============================================================================
# PART 4: TUPLE OPERATIONS (CONCATENATION, REPETITION & MEMBERSHIP)
# =============================================================================

print("\n--- PART 4: TUPLE OPERATIONS ---\n")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 1. Concatenation (+)
combined = tuple1 + tuple2
print("Concatenation (tuple1 + tuple2) :", combined)

# 2. Repetition (*)
repeated = ("Hi",) * 3
print("Repetition (('Hi',) * 3)        :", repeated)

# 3. Membership test (`in` and `not in`)
numbers = (10, 20, 30, 40, 50)
print("Is 20 in numbers?               :", 20 in numbers)
print("Is 99 in numbers?               :", 99 in numbers)
print("Is 100 not in numbers?          :", 100 not in numbers)


# =============================================================================
# PART 5: TUPLE METHODS (ALL BUILT-IN METHODS)
# =============================================================================
# Because tuples are immutable, Python only provides TWO built-in methods:
# 1. count(value) : Returns how many times a value occurs.
# 2. index(value) : Returns the index of the FIRST occurrence of a value.
# =============================================================================

print("\n--- PART 5: TUPLE METHODS ---\n")

scores = (10, 20, 30, 20, 40, 20, 50)
print("Scores tuple:", scores)

# 1. count(value)
count_20 = scores.count(20)
count_99 = scores.count(99)
print("scores.count(20) :", count_20, "(number of times 20 appears)")
print("scores.count(99) :", count_99, "(not present)")

# 2. index(value)
first_index_20 = scores.index(20)
first_index_40 = scores.index(40)
print("scores.index(20) :", first_index_20, "(first index where 20 appears)")
print("scores.index(40) :", first_index_40, "(index of 40)")

# index() with start and stop range: index(value, start, end)
index_after_pos2 = scores.index(20, 2)
print("scores.index(20, 2):", index_after_pos2, "(first 20 at or after index 2)")

# Searching for non-existent item raises ValueError
try:
    scores.index(999)
except ValueError as e:
    print("scores.index(999) raised ValueError:", e)


# =============================================================================
# PART 6: TUPLE PACKING & UNPACKING
# =============================================================================
# Packing   : Assigning multiple values to a single tuple variable.
# Unpacking : Extracting values from a tuple into separate variables.
# =============================================================================

print("\n--- PART 6: TUPLE PACKING & UNPACKING ---\n")

# Tuple Packing
user_data = ("Harish", 21, "India", "Software Engineer")
print("Packed tuple:", user_data)

# Tuple Unpacking (variables must match the number of elements)
name, age, country, role = user_data
print(f"Unpacked -> Name: {name}, Age: {age}, Country: {country}, Role: {role}")

# Extended Unpacking with asterisk (*)
marks = (95, 88, 76, 82, 90, 99)
first, *middle, last = marks
print("\nExtended Unpacking with `*`:")
print("First score  :", first)
print("Middle scores:", middle)
print("Last score   :", last)

# Swapping variables without a temp variable (Powered by tuple packing/unpacking!)
a = 100
b = 200
print(f"\nBefore Swap: a = {a}, b = {b}")
a, b = b, a
print(f"After Swap : a = {a}, b = {b}")


# =============================================================================
# PART 7: USEFUL BUILT-IN FUNCTIONS WITH TUPLES
# =============================================================================

print("\n--- PART 7: USEFUL BUILT-IN FUNCTIONS ---\n")

vals = (45, 12, 89, 33, 70)
print("Values tuple   :", vals)
print("min(vals)      :", min(vals))
print("max(vals)      :", max(vals))
print("sum(vals)      :", sum(vals))
print("sorted(vals)   :", sorted(vals), "(returns a new list, tuple is unchanged)")

# Iterating through a tuple
print("\nLooping with enumerate():")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")


# =============================================================================
# PART 8: REAL-WORLD USE CASES: WHY USE TUPLES OVER LISTS?
# =============================================================================
# 1. Returning multiple values from functions
# 2. Immutable constants (e.g. RGB color values, geographic coordinates)
# 3. Usable as dictionary keys (lists cannot be dictionary keys because they are unhashable)
# =============================================================================

print("\n--- PART 8: REAL-WORLD USE CASES ---\n")

# Use case 1: Returning multiple values from a function
def get_user_stats():
    # Returns a tuple implicitly
    username = "harish-0987"
    commits = 42
    rating = 4.9
    return username, commits, rating

user, total_commits, user_rating = get_user_stats()
print(f"User Stats -> Username: {user}, Commits: {total_commits}, Rating: {user_rating}")

# Use case 2: Geographic coordinates & RGB Colors
delhi_coords = (28.6139, 77.2090)
rgb_cyan = (0, 255, 255)
print("Coordinates tuple :", delhi_coords)
print("RGB color tuple   :", rgb_cyan)

# Use case 3: Using a tuple as a Dictionary Key
locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
    (13.0827, 80.2707): "Chennai"
}
print("Dictionary with tuple keys lookup:", locations[(28.6139, 77.2090)])

print("\n" + "=" * 70)
print("               DAY 7: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)
