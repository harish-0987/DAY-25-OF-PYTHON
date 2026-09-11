# Day 5: Strings in Python 🐍

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 5 of Python**! Today we learn about **Strings**, **String Operations**, and essential **String Methods** at a simple, beginner-friendly level.

---

## 📌 What is a String?

A **String** is a sequence of characters enclosed inside quotation marks. In Python, strings have the type `str`. Characters can be alphabets, numbers, symbols, spaces, or emojis.

### Creating Strings:
```python
# 1. Single Quotes
name = 'Harish'

# 2. Double Quotes
message = "Python is fun!"

# 3. Triple Quotes (multi-line)
story = """Line 1
Line 2
Line 3"""

print(len(name))        # Output: 6 (number of characters)
print(type(name))       # Output: <class 'str'>
```

---

## 🔒 String Immutability

In Python, strings are **immutable**. Once created, characters inside a string **cannot be modified in-place**.
```python
text = "Hello"
# text[0] = "J"  -> Raises TypeError!

# To modify, create a new string:
new_text = "J" + text[1:]   # "Jello"
```

---

## ⚙️ Basic String Operations

| Operation | Operator / Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| **Concatenation** | `+` | Merges two strings | `"Py" + "thon"` -> `"Python"` |
| **Repetition** | `*` | Repeats a string `n` times | `"Hi! " * 2` -> `"Hi! Hi! "` |
| **Indexing** | `[index]` | Fetches single character (0-based) | `"Python"[0]` -> `'P'`, `[-1]` -> `'n'` |
| **Slicing** | `[start:stop:step]` | Extracts a substring | `"Python"[0:2]` -> `'Py'` |
| **Membership** | `in` / `not in` | Checks if substring exists | `'th' in 'Python'` -> `True` |
| **Length** | `len(str)` | Returns total characters | `len("Python")` -> `6` |

### Indexing & Slicing Visual Guide:
```text
 Characters:   P   y   t   h   o   n
 + Index   :   0   1   2   3   4   5
 - Index   :  -6  -5  -4  -3  -2  -1
```

```python
word = "Python"
print(word[0])       # 'P'
print(word[-1])      # 'n'
print(word[0:4])     # 'Pyth' (index 4 excluded)
print(word[::-1])    # 'nohtyP' (reversed)
```

---

## 🛠️ Essential String Methods

Methods are built-in actions called using the dot operator: `string.method()`.

### 1. Case Conversion
- `text.upper()` : Converts all characters to uppercase.
- `text.lower()` : Converts all characters to lowercase.
- `text.title()` : Capitalizes the first letter of each word.
- `text.capitalize()` : Capitalizes only the first letter of the sentence.

### 2. Trimming Whitespace
- `text.strip()` : Removes whitespace from both ends.
- `text.lstrip()` : Removes whitespace from the left side.
- `text.rstrip()` : Removes whitespace from the right side.

### 3. Searching & Counting
- `text.find("sub")` : Returns the index of the first occurrence (or `-1` if not found).
- `text.count("sub")` : Returns the number of times a substring appears.
- `text.startswith("H")` : Returns `True` if string begins with prefix.
- `text.endswith("!")` : Returns `True` if string finishes with suffix.

### 4. Modifying & Splitting
- `text.replace(old, new)` : Replaces matching text with new text.
- `text.split(delimiter)` : Splits a string into a list of substrings.
- `"delimiter".join(list)` : Combines list items into one string.

### 5. Checking & Validation
- `text.isalpha()` : Returns `True` if string has only letters.
- `text.isdigit()` : Returns `True` if string has only numbers.
- `text.isalnum()` : Returns `True` if string has letters and/or numbers.

---

## 🎨 Modern String Formatting (f-strings)

Modern Python (3.6+) uses **f-strings** to embed variables and expressions inside strings:

```python
name = "Harish"
day = 5
print(f"Welcome {name} to Day {day} of Python!")
```

---

## 🚀 How to Run

Run the complete example code with:

```bash
python day5.py
```

---

## 👨‍💻 Author

**Harish**
- GitHub: [@harish-0987](https://github.com/harish-0987)
- Repository: [Day-5-of-python](https://github.com/harish-0987/Day-5-of-python)
