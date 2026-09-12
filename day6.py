# =============================================================================
# DAY 6: LISTS IN PYTHON (WHAT IS A LIST, METHODS & EXAMPLES)
# Author: Harish
# Repository: Day---6-of-python
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("       DAY 6: PYTHON LISTS - CONCEPTS, OPERATIONS & KEY METHODS")
print("=" * 70)


# =============================================================================
# PART 1: WHAT IS A LIST?
# =============================================================================
# Definition:
# A list in Python is an ordered, changeable (mutable) collection of items.
# Lists are written with square brackets: [item1, item2, ...]
#
# Key features:
# 1. Ordered    : Items have a defined order that does not change unless modified.
# 2. Mutable    : You can add, change, or remove items after creating the list.
# 3. Duplicates : Lists allow duplicate values.
# 4. Mixed types: A single list can hold strings, numbers, booleans, etc.
# =============================================================================

print("\n--- PART 1: WHAT IS A LIST? ---\n")

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed_list = ["Harish", 21, True, 99.5]

print("Fruits list      :", fruits)
print("Numbers list     :", numbers)
print("Mixed data list  :", mixed_list)

# Checking type and length
print("Data type of list:", type(fruits).__name__)
print("Length of list   :", len(fruits), "items")


# =============================================================================
# PART 2: ACCESSING ELEMENTS (INDEXING & SLICING)
# =============================================================================
# Like strings, list indexing starts at 0.
# Negative indexing starts at -1 (from the end).
# Slicing syntax: list[start:stop] (stop index is excluded).
# =============================================================================

print("\n--- PART 2: INDEXING & SLICING ---\n")

colors = ["red", "green", "blue", "yellow", "purple"]
print("Original colors:", colors)

# Indexing
print("First item  (colors[0])  :", colors[0])
print("Last item   (colors[-1]) :", colors[-1])

# Slicing
print("Slice [1:4] (index 1 to 3):", colors[1:4])
print("Slice [:2]  (first two)   :", colors[:2])


# =============================================================================
# PART 3: LISTS ARE MUTABLE (CHANGING ITEMS)
# =============================================================================
# Unlike strings, lists can be changed in place without creating a new list.
# =============================================================================

print("\n--- PART 3: MUTABILITY (CHANGING ITEMS) ---\n")

animals = ["dog", "cat", "elephant"]
print("Before modification:", animals)

animals[1] = "tiger"  # Modifying index 1
print("After modification :", animals)


# =============================================================================
# PART 4: ESSENTIAL LIST METHODS (FEW KEY EXAMPLES)
# =============================================================================
# Python provides built-in methods to easily manipulate lists:
# - append()  : Adds an item at the end of the list.
# - insert()  : Inserts an item at a specific index.
# - remove()  : Removes the first occurrence of a specified value.
# - pop()     : Removes and returns the item at an index (default: last).
# - sort()    : Sorts the list in ascending order.
# - reverse() : Reverses the order of the list in place.
# - count()   : Returns the number of times a value appears.
# - clear()   : Removes all elements from the list.
# =============================================================================

print("\n--- PART 4: ESSENTIAL LIST METHODS ---\n")

my_list = [5, 2, 8, 1, 3]
print("Starting list:", my_list)

# 1. append(item) - add to the end
my_list.append(10)
print("1. After .append(10)      :", my_list)

# 2. insert(index, item) - insert at position
my_list.insert(2, 99)
print("2. After .insert(2, 99)   :", my_list)

# 3. remove(item) - remove first matching value
my_list.remove(99)
print("3. After .remove(99)      :", my_list)

# 4. pop() - remove last item (or specify index)
removed_val = my_list.pop()
print(f"4. After .pop()           : {my_list} (removed: {removed_val})")

# 5. sort() - sort items ascending
my_list.sort()
print("5. After .sort()          :", my_list)

# 6. reverse() - reverse the list
my_list.reverse()
print("6. After .reverse()       :", my_list)

# 7. count(item) - count occurrences
test_list = [1, 2, 2, 3, 2, 4]
twos_count = test_list.count(2)
print("7. Count of 2 in test list:", twos_count)

# 8. clear() - empty the list
demo_list = [1, 2, 3]
demo_list.clear()
print("8. After .clear()         :", demo_list)


# =============================================================================
# PART 5: BASIC LIST OPERATIONS & USEFUL BUILT-INS
# =============================================================================
# List operations:
# - Concatenation (+) : Merges two lists together.
# - Repetition    (*) : Repeats a list n times.
# - Membership (in)   : Checks if an item exists in the list.
# - Built-in functions: len(), min(), max(), sum()
# =============================================================================

print("\n--- PART 5: OPERATIONS & BUILT-INS ---\n")

list_a = [1, 2]
list_b = [3, 4]

# Operations
merged = list_a + list_b
repeated = list_a * 3
exists = 3 in merged

print("Concatenation (list_a + list_b) :", merged)
print("Repetition (list_a * 3)         :", repeated)
print("Membership (3 in merged)        :", exists)

# Built-in functions with numeric list
scores = [45, 88, 72, 95, 60]
print("\nScores list:", scores)
print("Count (len) :", len(scores))
print("Minimum     :", min(scores))
print("Maximum     :", max(scores))
print("Total (sum) :", sum(scores))

print("\n" + "=" * 70)
print("          DAY 6: COMPLETED SUCCESSFULLY! KEEP CODING!")
print("=" * 70)
