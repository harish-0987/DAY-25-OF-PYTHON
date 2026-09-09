# Day 4: Type Conversion in Python 🐍

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 4 of Python**! Today we learn about **Type Conversion** in simple terms.

---

## 📌 What is Type Conversion?

**Type Conversion** means changing the data type of a value into another data type (for example, converting a string `"10"` into a number `10`).

---

## 🔄 Types of Type Conversion

Python has **two** types of type conversion:

### 1. Implicit Type Conversion (Automatic)
Python automatically changes one data type into another without our help. It does this to avoid errors or losing data.

**Example:**
```python
# Adding an integer and a float
a = 10      # int
b = 5.5     # float

c = a + b   # Python automatically makes c a float

print(c)        # Output: 15.5
print(type(c))  # Output: <class 'float'>
```

---

### 2. Explicit Type Conversion (Type Casting / Manual)
We manually change the data type using Python's built-in functions.

#### Basic Functions:
- `int()` - Converts value to an integer (whole number)
- `float()` - Converts value to a float (decimal number)
- `str()` - Converts value to a string (text)

**Example:**
```python
# 1. String to Integer
x = "20"
y = int(x)
print(y + 5)    # Output: 25

# 2. Integer to Float
num = 10
print(float(num))   # Output: 10.0

# 3. Number to String
age = 20
print("My age is " + str(age))  # Output: My age is 20
```

---

## 🚀 How to Run

```bash
python day4.py
```

---

## 👨‍💻 Author

**Harish**
- GitHub: [@harish-0987](https://github.com/harish-0987)
