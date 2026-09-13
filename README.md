# Day 7: Tuples in Python 📦

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 7 of Python**! Today we explore **Tuples in Python**—understanding what tuples are, why immutability matters, how indexing/slicing works, all built-in tuple methods, tuple packing & unpacking, and practical basic-level code examples.

---

## 📌 What is a Tuple?

A **Tuple** in Python is a built-in data structure used to store an **ordered, immutable (unchangeable)** collection of elements. Tuples are written using **parentheses `()`**, with items separated by commas.

### Creating Tuples:
```python
# 1. Tuple of strings
fruits = ("apple", "banana", "cherry")

# 2. Tuple of integers
numbers = (10, 20, 30, 40)

# 3. Mixed data types (heterogeneous)
profile = ("Harish", 21, True, 99.5)

# 4. Empty tuple
empty_tuple = ()

# 5. Tuple without parentheses (tuple packing)
coords = 10, 20, 30

print(fruits)       # Output: ('apple', 'banana', 'cherry')
print(type(fruits)) # Output: <class 'tuple'>
print(len(fruits))  # Output: 3
```

---

## ⚠️ The Single-Element Tuple Quirk (Important!)

If you create a tuple with only **one element**, you **MUST include a trailing comma**. Without a comma, Python interprets the parentheses as a simple grouping operator (string, integer, etc.):

```python
not_a_tuple = ("apple")    # Type: str  ❌
single_tuple = ("apple",)  # Type: tuple ✅

print(type(not_a_tuple))   # <class 'str'>
print(type(single_tuple))  # <class 'tuple'>
```

---

## 💡 Key Characteristics of Python Tuples

- **Ordered**: Elements maintain their fixed sequence throughout their lifetime.
- **Immutable**: Once created, items cannot be added, changed, or removed.
- **Allows Duplicates**: Like lists, tuples can have repeating values (e.g. `(1, 2, 2, 3)`).
- **Heterogeneous**: Can hold any combination of data types (integers, strings, booleans, lists, etc.).
- **Memory Efficient & Fast**: Faster to iterate over and consume less memory than lists.
- **Hashable**: Because they are immutable, tuples can be used as keys in Python dictionaries (as long as all elements inside are hashable).

---

## ⚖️ Tuples vs Lists: What's the Difference?

| Feature | Tuple (`tuple`) | List (`list`) |
| :--- | :--- | :--- |
| **Syntax** | Parentheses `()` or comma | Square brackets `[]` |
| **Mutability** | **Immutable** (cannot be modified) | **Mutable** (can add, remove, change items) |
| **Methods** | Only 2 methods (`count`, `index`) | Many methods (`append`, `pop`, `sort`, etc.) |
| **Performance** | Faster execution & less memory | Slightly slower & more memory overhead |
| **Dictionary Key** | Can be used as a key | Cannot be used as a key |
| **Primary Use** | Write-protected data, fixed records | Dynamic collections that change frequently |

---

## 🔍 Indexing & Slicing

Tuples support standard zero-based positive indexing and negative indexing from the end:

```python
languages = ("Python", "JavaScript", "C++", "Java", "Go", "Rust")

# Indexing
print(languages[0])    # 'Python' (first element)
print(languages[-1])   # 'Rust' (last element)

# Slicing: tuple[start:stop:step]
print(languages[1:4])  # ('JavaScript', 'C++', 'Java')
print(languages[:3])   # ('Python', 'JavaScript', 'C++')
print(languages[::-1]) # ('Rust', 'Go', 'Java', 'C++', 'JavaScript', 'Python') - Reversed
```

---

## 🔒 Immutability in Action

```python
colors = ("red", "green", "blue")

# Attempting to modify an element:
colors[0] = "yellow"
# ❌ Raises TypeError: 'tuple' object does not support item assignment
```

### How to modify a tuple (Workaround):
Convert the tuple to a `list`, modify the list, and convert it back to a `tuple`:
```python
colors = ("red", "green", "blue")
temp_list = list(colors)
temp_list.append("yellow")
colors = tuple(temp_list)
print(colors)  # ('red', 'green', 'blue', 'yellow')
```

---

## 🛠️ Built-in Tuple Methods

Because tuples are immutable, Python only defines **two built-in methods**:

### 1. `count(value)`
Returns the total number of times `value` appears in the tuple:
```python
scores = (10, 20, 30, 20, 40, 20)
print(scores.count(20))  # Output: 3
print(scores.count(99))  # Output: 0
```

### 2. `index(value, [start], [stop])`
Returns the index of the **first occurrence** of `value`. Raises `ValueError` if the value is not found:
```python
scores = (10, 20, 30, 20, 40, 20)
print(scores.index(20))      # Output: 1
print(scores.index(20, 2))   # Output: 3 (searches from index 2 onward)
```

---

## 📦 Tuple Packing & Unpacking

### Packing:
Packing is bundling multiple values into a single tuple:
```python
person = ("Harish", 21, "Developer")
```

### Unpacking:
Extracting values from a tuple directly into variables:
```python
name, age, role = person
print(name)  # Harish
print(age)   # 21
print(role)  # Developer
```

### Extended Unpacking with Asterisk (`*`):
```python
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4] (captured as a list)
print(last)    # 5
```

### Elegant Variable Swapping:
```python
a = 10
b = 20
a, b = b, a  # Swaps values using tuple packing/unpacking
print(a, b)  # 20 10
```

---

## 🚀 Practical Real-World Use Cases

### 1. Returning Multiple Values from Functions
```python
def get_dimensions():
    width = 1920
    height = 1080
    return width, height  # Returns a tuple (1920, 1080)

w, h = get_dimensions()
print(f"{w}x{h}")  # 1920x1080
```

### 2. Immutable Coordinates / RGB Values
```python
delhi_coords = (28.6139, 77.2090)
primary_color = (255, 0, 0)
```

### 3. Tuples as Dictionary Keys
```python
locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai"
}
print(locations[(28.6139, 77.2090)])  # New Delhi
```

---

## 📂 Repository Structure

```text
DAY---7---PYTHON/
├── day7.py       # Complete Python source code with examples and explanations
└── README.md     # Comprehensive notes, diagrams, and reference guide
```

---

## 🏃 How to Run the Code

1. Clone or download this repository:
   ```bash
   git clone https://github.com/harish-0987/DAY---7---PYTHON.git
   ```
2. Navigate into the directory:
   ```bash
   cd DAY---7---PYTHON
   ```
3. Run the script:
   ```bash
   python day7.py
   ```

---

## 👤 Author

- **Author**: Harish ([@harish-0987](https://github.com/harish-0987))
- **Motto**: *"Not here to be known, here to build."*
