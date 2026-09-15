# Day 9: Sets in Python 🔮

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 9 of Python**! Today we dive deep into **Sets in Python**—understanding what sets are, why they are useful, how hashing gives them blazing fast $O(1)$ lookups, all built-in set methods, mathematical set operations, in-place updates, and practical real-world code examples.

---

## 📌 Table of Contents
1. [What is a Set?](#-what-is-a-set)
2. [The Empty Set Gotcha](#️-the-empty-set-gotcha-important)
3. [Key Characteristics of Python Sets](#-key-characteristics-of-python-sets)
4. [Set Methods Summary Table](#-set-methods-summary-table)
5. [Adding & Removing Elements](#-adding--removing-elements)
6. [Mathematical Set Operations](#-mathematical-set-operations)
7. [In-Place Set Updates](#-in-place-set-updates)
8. [Set Relationships & Comparisons](#-set-relationships--comparisons)
9. [Copying Sets](#-copying-sets)
10. [Frozenset (Immutable Sets)](#-frozenset-immutable-set)
11. [Practical Real-World Use Cases](#-practical-real-world-use-cases)
12. [Summary Checklist](#-summary-checklist)

---

## 📌 What is a Set?

A **Set** in Python is a built-in data type that represents an **unordered, mutable collection of unique, hashable items**. Sets are defined using curly braces `{}` or the built-in `set()` constructor.

```python
# 1. Basic set of strings
fruits = {"apple", "banana", "cherry"}

# 2. Set of integers
numbers = {10, 20, 30, 40}

# 3. Mixed data types
profile = {"Harish", 21, True, 99.5}

# 4. Sets automatically eliminate duplicates!
duplicate_nums = {1, 2, 2, 3, 3, 3, 4}
print(duplicate_nums)  # Output: {1, 2, 3, 4}
```

---

## ⚠️ The Empty Set Gotcha (Important!)

In Python, `{}` creates an **empty dictionary**, NOT an empty set! To create an empty set, you **must** use `set()`:

```python
empty_dict = {}     # Type: <class 'dict'> ❌
empty_set = set()   # Type: <class 'set'>  ✅

print(type(empty_dict))  # <class 'dict'>
print(type(empty_set))   # <class 'set'>
```

---

## 💡 Key Characteristics of Python Sets

| Characteristic | Description |
| :--- | :--- |
| **Unordered** | Elements have no defined position. Items may appear in any order. |
| **Unindexed** | Slicing and indexing like `my_set[0]` are **not supported** (`TypeError`). |
| **Unique Elements** | Duplicate values are never stored. Great for deduplication. |
| **Mutable** | You can add, remove, and update elements at runtime. |
| **Hashable Elements Only** | Members must be immutable (numbers, strings, tuples). Lists or dicts cannot be set members. |
| **Fast Lookups** | Backed by a hash table, membership checks (`x in my_set`) run in average **$O(1)$ time complexity**. |

---

## 📋 Set Methods Summary Table

| Method | Description | Equivalent Operator |
| :--- | :--- | :---: |
| `add(elem)` | Adds a single element to the set | — |
| `update(iterable)` | Adds all elements from an iterable (list, tuple, set) | `\|=` |
| `remove(elem)` | Removes element; raises `KeyError` if not found | — |
| `discard(elem)` | Removes element safely; **no error** if not found | — |
| `pop()` | Removes and returns an arbitrary element | — |
| `clear()` | Removes all elements from the set | — |
| `copy()` | Returns a shallow copy of the set | — |
| `union(*others)` | Returns a new set with elements from both sets | `\|` |
| `intersection(*others)` | Returns a new set with shared elements | `&` |
| `difference(*others)` | Returns a new set with elements in first set but not second | `-` |
| `symmetric_difference(other)` | Returns elements in either set, but not both | `^` |
| `intersection_update(*others)` | Modifies set in-place to keep only common elements | `&=` |
| `difference_update(*others)` | Modifies set in-place by removing items in other sets | `-=` |
| `symmetric_difference_update(other)` | Modifies set to keep only symmetric differences | `^=` |
| `issubset(other)` | Returns `True` if current set is contained in another | `<=` |
| `issuperset(other)` | Returns `True` if current set contains all items of another | `>=` |
| `isdisjoint(other)` | Returns `True` if two sets share **no common elements** | — |

---

## ➕ Adding & Removing Elements

### 1. Adding Elements: `add()` vs `update()`
```python
skills = {"Python", "Git"}

# add() takes a single item
skills.add("SQL")
print(skills)  # {'Python', 'Git', 'SQL'}

# update() takes any iterable (list, set, tuple)
skills.update(["Docker", "Linux"])
print(skills)  # {'Python', 'Git', 'SQL', 'Docker', 'Linux'}
```

### 2. Removing Elements: `remove()` vs `discard()` vs `pop()` vs `clear()`
```python
languages = {"C", "Java", "Python", "Rust"}

# remove() raises KeyError if item is missing
languages.remove("C")

# discard() is safe: does NOT raise error if missing
languages.discard("HTML")  # No error!

# pop() removes and returns an arbitrary element
removed = languages.pop()
print("Popped:", removed)

# clear() empties the set
languages.clear()
print(languages)  # set()
```

---

## 📐 Mathematical Set Operations

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

### 1. Union (`|` or `union()`)
Combines all elements from both sets without duplicates:
```python
print(A | B)        # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))   # {1, 2, 3, 4, 5, 6, 7, 8}
```

### 2. Intersection (`&` or `intersection()`)
Finds only elements present in **both** sets:
```python
print(A & B)               # {4, 5}
print(A.intersection(B))  # {4, 5}
```

### 3. Difference (`-` or `difference()`)
Finds elements in the first set that are **not** in the second set:
```python
print(A - B)              # {1, 2, 3}
print(B - A)              # {6, 7, 8}
print(A.difference(B))    # {1, 2, 3}
```

### 4. Symmetric Difference (`^` or `symmetric_difference()`)
Finds elements that are in either set, but **not in both**:
```python
print(A ^ B)                         # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))     # {1, 2, 3, 6, 7, 8}
```

---

## 🔄 In-Place Set Updates

Instead of creating a new set, these methods mutate the caller set directly:

```python
x = {"apple", "banana", "cherry"}
y = {"google", "apple"}

# Keep only common items
x.intersection_update(y)
print(x)  # {'apple'}

# Remove items found in y
x = {"apple", "banana", "cherry"}
x.difference_update(y)
print(x)  # {'banana', 'cherry'}

# Keep only items unique to each
x = {"apple", "banana", "cherry"}
x.symmetric_difference_update(y)
print(x)  # {'banana', 'cherry', 'google'}
```

---

## 🔍 Set Relationships & Comparisons

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {7, 8, 9}

# 1. issubset() / <=
print(A.issubset(B))   # True (All elements of A are in B)
print(A <= B)          # True

# 2. issuperset() / >=
print(B.issuperset(A)) # True (B contains all elements of A)
print(B >= A)          # True

# 3. isdisjoint()
print(A.isdisjoint(C)) # True (A and C share NO elements)
print(A.isdisjoint(B)) # False (They share 1, 2, 3)
```

---

## 📋 Copying Sets

```python
original = {1, 2, 3}

# Shallow copy using copy()
cloned = original.copy()
cloned.add(4)

print("Original:", original)  # {1, 2, 3}
print("Cloned:  ", cloned)    # {1, 2, 3, 4}
```

---

## ❄️ Frozenset (Immutable Set)

If you need an immutable, hashable set (for example, to use as a dictionary key or as an element inside another set), use `frozenset()`:

```python
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # frozenset({1, 2, 3, 4})

# Dictionary using frozenset as a key
permissions = {
    frozenset({"read", "write"}): "Editor",
    frozenset({"read"}): "Viewer"
}
print(permissions[frozenset({"read", "write"})])  # Editor
```

---

## 🚀 Practical Real-World Use Cases

### 1. Removing Duplicates from a List
```python
raw_data = ["apple", "banana", "apple", "orange", "banana"]
unique_data = list(set(raw_data))
print(unique_data)  # ['orange', 'banana', 'apple']
```

### 2. Fast Membership Testing ($O(1)$)
```python
allowed_users = {"alice", "bob", "harish", "charlie"}

username = input("Enter username: ")
if username in allowed_users:
    print("Access Granted!")
```

### 3. Mutual Friends / Common Interests
```python
user1_friends = {"Alice", "Bob", "Charlie", "David"}
user2_friends = {"Charlie", "David", "Eve", "Frank"}

mutual = user1_friends & user2_friends
print("Mutual Friends:", mutual)  # {'Charlie', 'David'}
```

---

## ✅ Summary Checklist

- [x] Set definition: Unordered, mutable, unique elements
- [x] Empty set syntax: `set()` (not `{}`)
- [x] Adding: `add()` and `update()`
- [x] Removing: `remove()`, `discard()`, `pop()`, `clear()`
- [x] Operations: `union (|)`, `intersection (&)`, `difference (-)`, `symmetric_difference (^)`
- [x] Comparisons: `issubset()`, `issuperset()`, `isdisjoint()`
- [x] In-place updates: `intersection_update()`, `difference_update()`, etc.
- [x] Immutable sets: `frozenset()`

---

*Authored by Harish — "Not here to be known, here to build."*
