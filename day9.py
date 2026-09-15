# =============================================================================
# DAY 9: SETS IN PYTHON (WHAT IS A SET, METHODS & EXAMPLES)
# Author: Harish
# Repository: DAY-9-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("       DAY 9: PYTHON SETS - CONCEPTS, OPERATIONS & KEY METHODS")
print("=" * 70)


# =============================================================================
# PART 1: WHAT IS A SET?
# =============================================================================
# Definition:
# A Set in Python is an unordered, mutable collection of unique elements.
# Sets are written with curly braces: {item1, item2, item3}
#
# Key Features:
# 1. Unordered       : Items do NOT have a defined order; order may change.
# 2. Unindexed       : You CANNOT access items by index like my_set[0].
# 3. No Duplicates   : Duplicate items are automatically removed!
# 4. Mutable         : You can add and remove items after creation.
# 5. Hashable Items  : Elements inside a set MUST be immutable (int, str, tuple).
#                      You CANNOT put a list or a dict inside a set.
# =============================================================================

print("\n--- PART 1: WHAT IS A SET? ---\n")

# 1. Creating basic sets
fruits = {"apple", "banana", "cherry"}
numbers = {10, 20, 30, 40, 50}
mixed_set = {"Harish", 21, True, 99.5}

print("Fruits set        :", fruits)
print("Numbers set       :", numbers)
print("Mixed set         :", mixed_set)

# 2. Sets automatically eliminate duplicates
duplicate_numbers = {1, 2, 2, 3, 4, 4, 4, 5}
print("Duplicates removed:", duplicate_numbers)  # Output: {1, 2, 3, 4, 5}

# 3. Checking type and length
print("Data type         :", type(fruits).__name__)
print("Length of set     :", len(fruits))

# 4. THE EMPTY SET GOTCHA (VERY IMPORTANT!)
# {} creates an empty dictionary, NOT an empty set!
# To create an empty set, you MUST use set()
empty_dict = {}
empty_set = set()

print("\nType of {}        :", type(empty_dict).__name__, "-> (This is a Dictionary!)")
print("Type of set()     :", type(empty_set).__name__, "-> (This is a Set!)")

# 5. Creating a set from a list or string using set()
from_list = set([10, 20, 20, 30, 40])
from_string = set("mississippi")
print("From list         :", from_list)
print("From string       :", from_string)


# =============================================================================
# PART 2: ACCESSING & CHECKING MEMBERSHIP
# =============================================================================
# Since sets are unindexed, we cannot use my_set[0].
# Instead, we iterate with a for loop, or check with 'in' and 'not in'.
# Set membership tests are O(1) time complexity - extremely fast!
# =============================================================================

print("\n--- PART 2: ACCESSING & MEMBERSHIP ---\n")

colors = {"red", "green", "blue", "yellow"}

# 1. Membership test with 'in' and 'not in'
print("Is 'green' in colors?    :", "green" in colors)
print("Is 'purple' in colors?   :", "purple" in colors)
print("Is 'black' not in colors?:", "black" not in colors)

# 2. Iterating through a set
print("\nIterating through colors:")
for color in colors:
    print(f" - {color}")


# =============================================================================
# PART 3: ADDING ELEMENTS TO A SET
# =============================================================================
# 1. add(elem)       : Adds a single element to the set.
# 2. update(iterable): Adds multiple elements from a list, tuple, set, etc.
# =============================================================================

print("\n--- PART 3: ADDING ELEMENTS ---\n")

skills = {"Python", "Git"}
print("Initial skills   :", skills)

# 1. add() - adds one element
skills.add("SQL")
skills.add("Python")  # Adding duplicate has no effect
print("After add()      :", skills)

# 2. update() - adds multiple elements from any iterable
skills.update(["Docker", "Linux", "AWS"])
print("After update()   :", skills)


# =============================================================================
# PART 4: REMOVING ELEMENTS FROM A SET
# =============================================================================
# 1. remove(elem)  : Removes element. Raises KeyError if element not found!
# 2. discard(elem) : Removes element safely. Does NOT raise error if missing!
# 3. pop()         : Removes and returns an arbitrary element.
# 4. clear()       : Empties the entire set.
# =============================================================================

print("\n--- PART 4: REMOVING ELEMENTS ---\n")

programming = {"C", "C++", "Java", "Python", "JavaScript", "Rust"}
print("Original set     :", programming)

# 1. remove() - raises error if not found
programming.remove("C")
print("After remove('C'):", programming)

# 2. discard() - safe remove, no error if missing
programming.discard("Java")
programming.discard("Kotlin")  # 'Kotlin' is not in set, but no error thrown!
print("After discard()  :", programming)

# 3. pop() - removes an arbitrary element and returns it
removed_item = programming.pop()
print(f"Popped item      : '{removed_item}'")
print("After pop()      :", programming)

# 4. clear() - removes all elements
temp_set = {"a", "b", "c"}
temp_set.clear()
print("After clear()    :", temp_set)


# =============================================================================
# PART 5: MATHEMATICAL SET OPERATIONS
# =============================================================================
# Python sets support mathematical set theory operations:
# 1. Union                (A | B) : Elements in A OR B (all elements combined)
# 2. Intersection         (A & B) : Elements in BOTH A AND B (common elements)
# 3. Difference           (A - B) : Elements in A but NOT in B
# 4. Symmetric Difference (A ^ B) : Elements in A or B, but NOT in both
# =============================================================================

print("\n--- PART 5: MATHEMATICAL SET OPERATIONS ---\n")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 1. Union: all unique elements from both sets
union_method = set_a.union(set_b)
union_operator = set_a | set_b
print("\n1. Union (A | B)               :", union_method)

# 2. Intersection: common elements in both sets
intersection_method = set_a.intersection(set_b)
intersection_operator = set_a & set_b
print("2. Intersection (A & B)        :", intersection_method)

# 3. Difference: elements in A but NOT in B
diff_a_b = set_a.difference(set_b)      # set_a - set_b
diff_b_a = set_b.difference(set_a)      # set_b - set_a
print("3. Difference (A - B)          :", diff_a_b)
print("   Difference (B - A)          :", diff_b_a)

# 4. Symmetric Difference: elements in A or B, but NOT both
sym_diff = set_a.symmetric_difference(set_b)  # set_a ^ set_b
print("4. Symmetric Difference (A ^ B):", sym_diff)


# =============================================================================
# PART 6: IN-PLACE UPDATE METHODS
# =============================================================================
# Instead of returning a new set, these modify the original set directly:
# 1. intersection_update() (&=) : Keeps only common elements
# 2. difference_update()   (-=) : Removes elements found in the other set
# 3. symmetric_difference_update() (^=) : Keeps only elements unique to each
# =============================================================================

print("\n--- PART 6: IN-PLACE UPDATE METHODS ---\n")

# 1. intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print("intersection_update() result:", x)  # {'apple'}

# 2. difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print("difference_update() result  :", x)  # {'banana', 'cherry'}

# 3. symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("sym_diff_update() result    :", x)  # {'banana', 'cherry', 'google', 'microsoft'}


# =============================================================================
# PART 7: SET COMPARISONS & RELATIONSHIPS
# =============================================================================
# 1. issubset()   (<=) : True if all elements of set A are in set B
# 2. issuperset() (>=) : True if set A contains all elements of set B
# 3. isdisjoint()      : True if set A and set B have NO elements in common
# =============================================================================

print("\n--- PART 7: SET RELATIONSHIPS & COMPARISONS ---\n")

small_set = {1, 2, 3}
big_set = {1, 2, 3, 4, 5, 6}
other_set = {7, 8, 9}

print(f"Small set : {small_set}")
print(f"Big set   : {big_set}")
print(f"Other set : {other_set}")

# 1. issubset()
print("\nIs small_set a subset of big_set?      :", small_set.issubset(big_set))
print("Using operator (small_set <= big_set)  :", small_set <= big_set)

# 2. issuperset()
print("Is big_set a superset of small_set?    :", big_set.issuperset(small_set))
print("Using operator (big_set >= small_set)  :", big_set >= small_set)

# 3. isdisjoint() - no shared elements
print("Are small_set and other_set disjoint?  :", small_set.isdisjoint(other_set))
print("Are small_set and big_set disjoint?    :", small_set.isdisjoint(big_set))


# =============================================================================
# PART 8: COPYING A SET
# =============================================================================
# copy(): Returns a shallow copy of the set.
# Using assignment (=) only creates a reference, not a copy!
# =============================================================================

print("\n--- PART 8: COPYING A SET ---\n")

original = {10, 20, 30}
cloned = original.copy()

cloned.add(40)
print("Original set :", original)  # {10, 20, 30}
print("Cloned set   :", cloned)    # {10, 20, 30, 40}


# =============================================================================
# PART 9: REAL-WORLD PRACTICAL EXAMPLES
# =============================================================================
# Common set use cases:
# 1. Removing duplicates from a list in one line
# 2. Finding common elements between two user friend lists
# 3. Fast item lookup (O(1) vs list O(N))
# =============================================================================

print("\n--- PART 9: REAL-WORLD PRACTICAL EXAMPLES ---\n")

# Example 1: Removing duplicates from a list
raw_scores = [95, 88, 95, 100, 72, 88, 65, 100]
unique_scores = list(set(raw_scores))
print("Original list with duplicates :", raw_scores)
print("Unique list via set()         :", sorted(unique_scores))

# Example 2: Common interests between two users
alice_hobbies = {"reading", "cycling", "cooking", "gaming"}
bob_hobbies = {"gaming", "cooking", "photography", "traveling"}

common_hobbies = alice_hobbies & bob_hobbies
unique_to_alice = alice_hobbies - bob_hobbies
all_hobbies = alice_hobbies | bob_hobbies

print("\nAlice's hobbies     :", alice_hobbies)
print("Bob's hobbies       :", bob_hobbies)
print("Mutual hobbies      :", common_hobbies)
print("Only Alice's hobbies:", unique_to_alice)
print("Combined hobbies    :", all_hobbies)


# =============================================================================
# PART 10: FROZENSET (IMMUTABLE SET)
# =============================================================================
# What if you need an immutable set? Use frozenset()!
# Frozensets cannot be modified after creation, and CAN be used as dictionary keys!
# =============================================================================

print("\n--- PART 10: FROZENSET (IMMUTABLE SET) ---\n")

frozen = frozenset([1, 2, 3, 4])
print("Frozenset        :", frozen)
print("Type of frozenset:", type(frozen).__name__)

# frozen.add(5)  # Raises AttributeError: 'frozenset' object has no attribute 'add'

# Frozenset as a dictionary key (regular set would throw TypeError: unhashable type)
lookup_table = {
    frozenset({"admin", "superuser"}): "Full Access",
    frozenset({"guest"}): "Read Only"
}
print("Dictionary with frozenset key:", lookup_table[frozenset({"admin", "superuser"})])

print("\n" + "=" * 70)
print("              DAY 9 COMPLETED SUCCESSFULLY! KEEP BUILDING!            ")
print("=" * 70)
