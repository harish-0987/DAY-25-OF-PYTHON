# Day 10: Dictionaries in Python 📖

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 10 of Python**! Today we cover one of Python's most essential and widely used data structures: **Dictionaries (`dict`)**. Dictionaries power key parts of Python itself (like namespaces, class attributes, and module scopes) and are fundamental in real-world software engineering for JSON parsing, API design, database modeling, and fast data retrieval.

---

## 📌 Table of Contents
1. [What is a Dictionary?](#-what-is-a-dictionary)
2. [Key Characteristics of Python Dictionaries](#-key-characteristics-of-python-dictionaries)
3. [Creating Dictionaries](#-creating-dictionaries)
4. [Accessing Elements (`[]` vs `.get()`)](#-accessing-elements--vs-get)
5. [Adding & Updating Elements](#-adding--updating-elements)
6. [Removing Elements (`pop()`, `popitem()`, `del`, `clear()`)](#-removing-elements)
7. [Dictionary Views & Iteration (`keys()`, `values()`, `items()`)](#-dictionary-views--iteration)
8. [Other Essential Dictionary Methods](#-other-essential-dictionary-methods)
9. [Complete Dictionary Methods Reference Table](#-complete-dictionary-methods-reference-table)
10. [Nested Dictionaries](#-nested-dictionaries)
11. [Dictionary Comprehensions](#-dictionary-comprehensions)
12. [Real-World Practical Projects](#-real-world-practical-projects)
13. [Common Pitfalls & Best Practices](#-common-pitfalls--best-practices)
14. [How to Run the Code](#-how-to-run-the-code)
15. [Summary Checklist](#-summary-checklist)

---

## 📌 What is a Dictionary?

A **Dictionary** in Python is a built-in data structure that stores collections of data in **key-value pairs**. Each item in a dictionary has an identifier called a **key** which maps directly to a **value**:

$$\text{Dictionary} = \{ \text{key}_1: \text{value}_1, \text{key}_2: \text{value}_2, \dots \}$$

Under the hood, Python dictionaries are implemented using **Hash Tables**, which means accessing, inserting, or removing values has an average time complexity of **$O(1)$** (constant time).

```python
# A simple Python dictionary representing a developer profile
developer = {
    "name": "Harish",
    "role": "Backend Engineer",
    "experience_years": 2,
    "skills": ["Python", "FastAPI", "PostgreSQL"],
    "is_certified": True
}

print(developer["name"])  # Output: Harish
```

---

## 💡 Key Characteristics of Python Dictionaries

| Characteristic | Description |
| :--- | :--- |
| **Key-Value Mapping** | Every element is stored as a pair: `key: value`. |
| **Ordered** | Since Python 3.7+, dictionaries preserve insertion order. |
| **Mutable** | You can add, modify, and delete keys and values after creation. |
| **Unique Keys** | Duplicate keys are NOT permitted. Specifying an existing key overwrites the old value. |
| **Hashable Keys** | Keys MUST be immutable types (`str`, `int`, `float`, `tuple`). Lists and dicts cannot be keys. |
| **Flexible Values** | Values can be of **any** type (primitives, lists, sets, nested dicts) and can duplicate. |
| **High Performance** | Key lookups run in $O(1)$ average time complexity via hashing. |

---

## 🛠 Creating Dictionaries

Python offers multiple convenient ways to define dictionaries:

```python
# 1. Empty dictionary
empty_dict_1 = {}
empty_dict_2 = dict()

# 2. Dictionary literal with curly braces
student = {
    "id": "STU101",
    "name": "Harish",
    "gpa": 3.9
}

# 3. Using the dict() constructor with keyword arguments
config = dict(host="localhost", port=5432, debug=True)

# 4. From a list of (key, value) tuples
pairs = [("USD", 83.5), ("EUR", 91.2), ("GBP", 106.8)]
exchange_rates = dict(pairs)
```

> [!NOTE]
> `{}` creates an **empty dictionary**, not an empty set. To create an empty set, you must call `set()`.

---

## 🔍 Accessing Elements (`[]` vs `.get()`)

There are two primary ways to retrieve values by their keys:

### 1. Square Bracket Notation: `dict[key]`
- Fast direct lookup.
- **Raises `KeyError`** if the key is not in the dictionary.

### 2. The `.get(key, default=None)` Method
- **Safe retrieval**: Does **NOT** crash if the key is missing.
- Returns `None` by default, or any custom default value you provide.

```python
user = {"username": "harish_dev", "plan": "pro"}

# 1. Square brackets
print(user["username"])  # Output: harish_dev
# print(user["email"])   # ❌ Raises KeyError: 'email'

# 2. .get() method
print(user.get("plan"))                  # Output: pro
print(user.get("email"))                 # Output: None (No crash!)
print(user.get("email", "not_provided")) # Output: not_provided

# 3. Checking membership with 'in' (checks KEYS, not values)
if "username" in user:
    print("User identifier exists!")
```

---

## ✏️ Adding & Updating Elements

### 1. Direct Assignment
Assigning to an existing key updates its value; assigning to a new key adds it.

```python
car = {"brand": "Tesla", "model": "Model 3"}

# Adding a new key
car["year"] = 2024

# Updating an existing key
car["model"] = "Model Y"
```

### 2. The `.update()` Method
Updates the dictionary with elements from another dictionary or iterable of key-value pairs.

```python
car.update({"color": "Midnight Silver", "price": 45000})
```

### 3. Dictionary Merge Operators (Python 3.9+)
- `|` : Merges two dictionaries into a **new** dictionary.
- `|=` : Merges into the left dictionary **in-place**.

```python
base_specs = {"cpu": "M3", "ram": "16GB"}
upgrade_specs = {"storage": "1TB", "ram": "32GB"}

# Merged into new dict ('storage' added, 'ram' updated to 32GB)
full_specs = base_specs | upgrade_specs

# In-place merge
base_specs |= {"warranty": "3 Years"}
```

---

## 🗑 Removing Elements

| Method / Keyword | Behavior | Missing Key Handling | Return Value |
| :--- | :--- | :--- | :--- |
| `pop(key, [default])` | Removes specified key | Returns `default` if provided, else raises `KeyError` | The removed value |
| `popitem()` | Removes last inserted item (LIFO) | Raises `KeyError` if dictionary is empty | `(key, value)` tuple |
| `del dict[key]` | Deletes specified key | Raises `KeyError` | `None` |
| `clear()` | Removes all items | Safe on empty dictionary | `None` (dict becomes `{}`) |

```python
cart = {"apple": 5, "banana": 12, "mango": 3, "orange": 8}

# 1. pop()
removed_val = cart.pop("mango")           # returns 3
missing_val = cart.pop("kiwi", "Not in cart")  # returns 'Not in cart'

# 2. popitem() - removes last inserted item
last_item = cart.popitem()                # returns ('orange', 8)

# 3. del
del cart["banana"]

# 4. clear()
cart.clear()                              # cart is now {}
```

---

## 🔄 Dictionary Views & Iteration

Python provides three dynamic view objects:
- `dict.keys()`: view of all keys.
- `dict.values()`: view of all values.
- `dict.items()`: view of all `(key, value)` pairs as tuples.

```python
scores = {"Alice": 92, "Bob": 78, "Charlie": 85}

# 1. Iterating through keys (default)
for name in scores:
    print(name)

# 2. Iterating through values
for score in scores.values():
    print(score)

# 3. Iterating through key-value pairs with .items() (Recommended)
for name, score in scores.items():
    print(f"{name} scored {score} points")
```

---

## ⚡ Other Essential Dictionary Methods

### 1. `setdefault(key, default)`
If `key` exists, returns its value without modifying it. If `key` does not exist, inserts `key` with value `default` and returns `default`.

```python
profile = {"name": "Harish"}
city = profile.setdefault("city", "Bengaluru")
# profile is now {'name': 'Harish', 'city': 'Bengaluru'}
```

### 2. `fromkeys(iterable, default_value)`
Creates a new dictionary from a collection of keys, all initialized to `default_value`.

```python
roles = ["admin", "editor", "moderator"]
access = dict.fromkeys(roles, "active")
# {'admin': 'active', 'editor': 'active', 'moderator': 'active'}
```

### 3. `copy()` (Shallow Copy)
Avoids unintended side effects caused by simple variable assignment (`b = a` creates an alias, not a new object).

```python
original = {"a": 1, "b": 2}
cloned = original.copy()
cloned["c"] = 3  # Does NOT affect original!
```

---

## 📊 Complete Dictionary Methods Reference Table

| Method | Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| `get()` | `d.get(k, [def])` | Returns value for key, or `def` (or `None`) if absent. | `d.get('id', 0)` |
| `keys()` | `d.keys()` | Returns a view object displaying all keys. | `list(d.keys())` |
| `values()` | `d.values()` | Returns a view object displaying all values. | `sum(d.values())` |
| `items()` | `d.items()` | Returns a view of all `(key, value)` tuples. | `for k, v in d.items():` |
| `update()` | `d.update(other)` | Updates dictionary in-place with another dict/iterable. | `d.update({'x': 10})` |
| `pop()` | `d.pop(k, [def])` | Removes key and returns its value. | `val = d.pop('temp')` |
| `popitem()` | `d.popitem()` | Removes and returns the last inserted `(key, value)`. | `k, v = d.popitem()` |
| `setdefault()` | `d.setdefault(k, v)` | Gets value if exists; if absent, inserts `k: v`. | `d.setdefault('role', 'user')` |
| `fromkeys()` | `dict.fromkeys(seq, v)`| Creates a new dict with keys from sequence. | `dict.fromkeys(['a','b'], 0)` |
| `copy()` | `d.copy()` | Returns a shallow copy of the dictionary. | `new_d = d.copy()` |
| `clear()` | `d.clear()` | Removes all elements from the dictionary. | `d.clear()` |

---

## 🏗 Nested Dictionaries

Dictionaries can contain other dictionaries as values, forming trees of structured data:

```python
company = {
    "emp_101": {
        "name": "Harish",
        "department": "Engineering",
        "salary": 85000
    },
    "emp_102": {
        "name": "Priya",
        "department": "Design",
        "salary": 78000
    }
}

# Accessing nested fields
print(company["emp_101"]["name"])        # Harish
print(company["emp_102"]["department"])  # Design

# Modifying nested data
company["emp_101"]["salary"] += 5000
```

---

## 🚀 Dictionary Comprehensions

A clean, declarative one-liner for generating or transforming dictionaries:

$$\{ \text{key\_expr}: \text{value\_expr} \;\mathbf{for}\; \text{item} \;\mathbf{in}\; \text{iterable} \;(\mathbf{if}\; \text{condition}) \}$$

```python
# 1. Squares of numbers
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. Filtering items
grades = {"Math": 92, "English": 74, "Physics": 88, "History": 65}
passed_subjects = {sub: mark for sub, mark in grades.items() if mark >= 75}

# 3. Inverting keys and values
users = {"user1": "admin", "user2": "editor"}
inverted = {role: uid for uid, role in users.items()}
```

---

## 💼 Real-World Practical Projects

### 1. Word Frequency Counter
Count occurrences of each word in a paragraph (used in search indexing and NLP):

```python
text = "code test build deploy test build test"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
# {'code': 1, 'test': 3, 'build': 2, 'deploy': 1}
```

### 2. E-Commerce Cart & Bill Calculator
Calculate line-item subtotals, apply discounts, and generate final payable amounts:

```python
price_catalog = {"keyboard": 1200, "mouse": 600, "pad": 250}
cart = {"keyboard": 1, "mouse": 2, "pad": 3}

subtotal = sum(price_catalog[item] * qty for item, qty in cart.items())
print(f"Total Amount: Rs. {subtotal:.2f}")
```

---

## ⚠️ Common Pitfalls & Best Practices

> [!WARNING]
> **1. Unhashable Keys**: Never use lists, sets, or other dictionaries as keys. Keys must be immutable (strings, numbers, or tuples).
> ```python
> bad_dict = {[1, 2]: "points"}   # ❌ Raises TypeError: unhashable type: 'list'
> good_dict = {(1, 2): "points"}  # ✅ Valid!
> ```

> [!CAUTION]
> **2. Modifying Size During Iteration**: Never add or delete keys from a dictionary while directly looping over it.
> ```python
> # ❌ Raises RuntimeError: dictionary changed size during iteration
> for k in my_dict:
>     if my_dict[k] == 0:
>         del my_dict[k]
>
> # ✅ Fix: Iterate over a snapshot list of keys
> for k in list(my_dict.keys()):
>     if my_dict[k] == 0:
>         del my_dict[k]
> ```

> [!TIP]
> **3. Prefer `.get()` for optional fields**: Use `.get(key, default)` when reading configurations, API payloads, or user inputs to avoid unhandled `KeyError` crashes.

---

## 💻 How to Run the Code

Run the accompanying script [day10.py](file:///c:/Users/pedda/OneDrive/Desktop/python%201/day10.py) using your Python interpreter:

```bash
python day10.py
```

---

## ✅ Summary Checklist

- [x] Understand what a dictionary is and how hash tables provide $O(1)$ lookups
- [x] Master accessing elements safely using `.get()`
- [x] Add, update, and merge dictionaries using assignments, `.update()`, and `|`
- [x] Delete elements using `pop()`, `popitem()`, `del`, and `clear()`
- [x] Iterate through keys, values, and pairs with `.items()`
- [x] Utilize helper methods (`setdefault()`, `fromkeys()`, `copy()`)
- [x] Build complex structures with nested dictionaries
- [x] Write concise dictionary comprehensions
- [x] Avoid common pitfalls (unhashable keys, mutating during iteration)
