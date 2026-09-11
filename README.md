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

## 💡 Key Characteristics of Python Strings

- **Zero-Indexed**: The first character is at index `0`, the second at index `1`.
- **Negative Indexing**: Access characters from the end; `-1` refers to the last character.
- **Immutable**: Once created, a string's content cannot be changed in place.
- **Case-Sensitive**: `"Python"` and `"python"` are completely different strings.
- **Supports Iteration**: You can loop through each character using a `for` loop (`for char in word:`).

---

## 🔒 String Immutability

In Python, strings are **immutable**. Once created, characters inside a string **cannot be modified in-place**.
```python
text = "Hello"
# text[0] = "J"  -> Raises TypeError: 'str' object does not support item assignment

# To modify, create a new string:
new_text = "J" + text[1:]   # "Jello"
```

> **Remember**: When you run a method like `text.upper()`, Python returns a **brand new string**. If you want to keep the change, reassign it:
> ```python
> text = text.upper()
> ```

---

## ⚙️ Basic String Operations

| Operation | Operator / Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| **Concatenation** | `+` | Merges two strings together | `"Py" + "thon"` -> `"Python"` |
| **Repetition** | `*` | Repeats a string `n` times | `"Hi! " * 2` -> `"Hi! Hi! "` |
| **Indexing** | `[index]` | Fetches a single character (0-based) | `"Python"[0]` -> `'P'`, `[-1]` -> `'n'` |
| **Slicing** | `[start:stop:step]` | Extracts a substring | `"Python"[0:2]` -> `'Py'` |
| **Membership** | `in` / `not in` | Checks if substring exists | `'th' in 'Python'` -> `True` |
| **Length** | `len(str)` | Returns total count of characters | `len("Python")` -> `6` |

### Indexing & Slicing Visual Guide:
```text
 Characters:   P   y   t   h   o   n
 + Index   :   0   1   2   3   4   5
 - Index   :  -6  -5  -4  -3  -2  -1
```

```python
word = "Python"
print(word[0])       # 'P' (first character)
print(word[-1])      # 'n' (last character)
print(word[0:4])     # 'Pyth' (stop index 4 is excluded)
print(word[::2])     # 'Pto' (step by 2)
print(word[::-1])    # 'nohtyP' (reverse string trick!)
```

---

## 🔤 Escape Characters & Raw Strings

Escape characters let you include special characters inside your strings using a backslash `\`:

| Sequence | Meaning | Example |
| :--- | :--- | :--- |
| `\n` | New line | `"Hello\nWorld"` |
| `\t` | Tab space | `"Name:\tHarish"` |
| `\\` | Backslash | `"C:\\folder\\file"` |
| `\'` / `\"` | Single / Double quote | `"He said \"Hi!\""` |

> **Tip - Raw Strings**: Prefix a string with `r` (e.g. `r"C:\Users\name"`) to treat backslashes as literal characters without escaping.

---

## 🛠️ Essential String Methods

Methods are built-in actions called using the dot operator: `string.method()`.

### 1. Case Conversion
- `text.upper()` : Converts all characters to UPPERCASE.
- `text.lower()` : Converts all characters to lowercase.
- `text.title()` : Capitalizes the first letter of each word.
- `text.capitalize()` : Capitalizes only the first letter of the sentence.
- `text.swapcase()` : Inverts uppercase to lowercase and vice versa.

### 2. Trimming Whitespace
- `text.strip()` : Removes whitespace from both ends.
- `text.lstrip()` : Removes whitespace from the left side only.
- `text.rstrip()` : Removes whitespace from the right side only.

### 3. Searching & Counting
- `text.find("sub")` : Returns the index of first occurrence (or `-1` if not found).
- `text.count("sub")` : Counts how many times the substring occurs.
- `text.startswith("H")` : Returns `True` if string begins with given prefix.
- `text.endswith("!")` : Returns `True` if string ends with given suffix.

### 4. Modifying & Splitting
- `text.replace(old, new)` : Replaces matching occurrences with new text.
- `text.split(delimiter)` : Splits a string into a list based on delimiter.
- `"delimiter".join(list)` : Combines list of strings into one string.

### 5. Checking & Validation (Returns `True` or `False`)
- `text.isalpha()` : `True` if string contains ONLY alphabet letters.
- `text.isdigit()` : `True` if string contains ONLY numbers.
- `text.isalnum()` : `True` if string contains ONLY letters and numbers.
- `text.isspace()` : `True` if string contains ONLY whitespace.

---

## 🎨 Modern String Formatting (f-strings)

Modern Python (3.6+) uses **f-strings** (formatted string literals) to easily insert variables:

```python
name = "Harish"
day = 5
score = 95.5

print(f"Welcome {name} to Day {day} of Python! Score: {score:.1f}%")
# Output: Welcome Harish to Day 5 of Python! Score: 95.5%
```

---

## ⚠️ Common Beginner Pitfalls & Tips

1. **Item Assignment Error**: You cannot do `s[0] = 'a'`. Strings are immutable.
2. **IndexError**: Trying to access an index beyond string length (e.g., `"abc"[10]`).
3. **Concatenating Strings with Numbers**:
   ```python
   # ❌ Wrong (Causes TypeError):
   # "Day " + 5
   
   # ✅ Correct:
   "Day " + str(5)  # or f"Day {5}"
   ```
4. **Strings are Case-Sensitive**: Always use `.lower()` when comparing user input to prevent matching errors (e.g., `user_choice.lower() == "yes"`).

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
