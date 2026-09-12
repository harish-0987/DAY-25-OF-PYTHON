# Day 6: Lists in Python 📋

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 6 of Python**! Today we dive into **Python Lists**, exploring what a list is, how it works, its mutability, and essential list methods with simple, clean, beginner-friendly examples.

---

## 📌 What is a List?

A **List** in Python is a built-in data structure used to store an **ordered collection** of items under a single variable name. Lists are created using **square brackets `[]`**, with items separated by commas.

### Creating Lists:
```python
# 1. List of strings
fruits = ["apple", "banana", "cherry"]

# 2. List of integers
numbers = [10, 20, 30, 40]

# 3. Mixed data types (heterogeneous)
profile = ["Harish", 21, True, 99.5]

# 4. Empty list
empty_list = []

print(fruits)       # Output: ['apple', 'banana', 'cherry']
print(type(fruits)) # Output: <class 'list'>
print(len(fruits))  # Output: 3
```

---

## 💡 Key Characteristics of Python Lists

- **Ordered**: Items maintain the exact order in which they were added.
- **Mutable (Changeable)**: You can add, replace, or delete items in place without creating a new list.
- **Allows Duplicates**: A list can store the same value multiple times (e.g. `[1, 2, 2, 3]`).
- **Heterogeneous**: Elements can be of different data types (strings, ints, floats, booleans, even other lists).
- **Indexed**: Elements are accessible via zero-based positive indexing (`0, 1, 2...`) or negative indexing (`-1, -2...`).

---

## 🔄 Mutability: Lists vs Strings

Unlike strings (which are immutable), **lists are mutable**. You can update any element directly using its index:

```python
numbers = [10, 20, 30]

# Modifying index 1 in-place:
numbers[1] = 99
print(numbers)  # Output: [10, 99, 30]
```

---

## 🔍 Indexing & Slicing

```text
 List items :  ["apple", "banana", "cherry", "orange"]
 + Index    :      0        1         2         3
 - Index    :     -4       -3        -2        -1
```

```python
fruits = ["apple", "banana", "cherry", "orange"]

# Indexing
print(fruits[0])    # 'apple' (first element)
print(fruits[-1])   # 'orange' (last element)

# Slicing: list[start:stop] (stop index is excluded)
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']
```

---

## ⚙️ Basic List Operations

| Operation | Operator / Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| **Concatenation** | `+` | Merges two lists together | `[1, 2] + [3, 4]` -> `[1, 2, 3, 4]` |
| **Repetition** | `*` | Duplicates items `n` times | `['A'] * 3` -> `['A', 'A', 'A']` |
| **Membership** | `in` / `not in` | Checks if element exists | `'apple' in fruits` -> `True` |
| **Length** | `len(list)` | Counts total elements | `len([1, 2, 3])` -> `3` |

---

## 🛠️ Essential List Methods

Python provides built-in methods called using the dot operator: `list.method()`.

| Method | Description | Example |
| :--- | :--- | :--- |
| `append(x)` | Adds element `x` to the end of the list | `nums.append(5)` |
| `insert(i, x)` | Inserts element `x` at specified index `i` | `nums.insert(0, 100)` |
| `remove(x)` | Removes the first occurrence of value `x` | `nums.remove(20)` |
| `pop([i])` | Removes and returns item at index (last by default) | `val = nums.pop()` |
| `sort()` | Sorts the list in ascending order in-place | `nums.sort()` |
| `reverse()` | Reverses the list elements in-place | `nums.reverse()` |
| `count(x)` | Returns number of times value `x` occurs | `nums.count(2)` |
| `clear()` | Removes all elements, leaving list empty | `nums.clear()` |

### Quick Code Example:
```python
data = [5, 2, 8, 1]

data.append(10)      # [5, 2, 8, 1, 10]
data.insert(1, 99)   # [5, 99, 2, 8, 1, 10]
data.remove(99)      # [5, 2, 8, 1, 10]
last_item = data.pop() # removes 10, list is [5, 2, 8, 1]
data.sort()          # [1, 2, 5, 8]
data.reverse()       # [8, 5, 2, 1]
```

---

## 🧮 Useful Built-in Functions with Lists

When working with numbers in lists:

```python
scores = [45, 88, 72, 95, 60]

print(len(scores))  # 5 (total items)
print(min(scores))  # 45 (smallest value)
print(max(scores))  # 95 (largest value)
print(sum(scores))  # 360 (sum of all items)
```

---

## ⚠️ Common Beginner Pitfalls & Tips

1. **`IndexError: list index out of range`**:
   Trying to access an index that doesn't exist (e.g. `items[5]` when the list only has 3 items).
2. **`ValueError: list.remove(x): x not in list`**:
   Calling `.remove()` on a value that does not exist in the list. Use `if x in list:` before removing.
3. **Methods that return `None`**:
   Methods like `.sort()`, `.reverse()`, and `.append()` modify the list **in-place** and return `None`.
   ```python
   # ❌ Wrong:
   sorted_list = nums.sort() # sorted_list will be None!

   # ✅ Correct:
   nums.sort()               # nums is now sorted
   ```

---

## 🚀 How to Run

Run the example script with:

```bash
python day6.py
```

---

## 👨‍💻 Author

**Harish**
- GitHub: [@harish-0987](https://github.com/harish-0987)
- Repository: [Day---6-of-python](https://github.com/harish-0987/Day---6-of-python)
