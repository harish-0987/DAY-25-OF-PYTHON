# Day 2: What is a Variable? 🐍

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Day](https://img.shields.io/badge/Day-02-brightgreen.svg)]()
[![Author](https://img.shields.io/badge/Author-Harish-orange.svg)](https://github.com/harish-0987)

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 2 of Python**! Today's lesson covers the most fundamental building block in programming: **What is a Variable in Python?**

---

## 📌 Table of Contents
- [What is a Variable?](#-what-is-a-variable)
- [How Variables Work](#-how-variables-work)
- [Basic Types of Variables](#-basic-types-of-variables)
- [Updating Variable Values](#-updating-variable-values)
- [Basic Math with Variables](#-basic-math-with-variables)
- [Checking Types with `type()`](#-checking-types-with-type)
- [File Structure](#-file-structure)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 📖 What is a Variable?

A **variable** is like a labeled container or a box in your computer's memory used to store data values.

When you create a variable:
```python
name = "Harish"
```
- `name` is the **variable name** (label on the box).
- `=` is the **assignment operator** (puts data into the box).
- `"Harish"` is the **value** stored inside the box.

---

## 💡 How Variables Work in Python

In Python, you do **not** need to declare variable types explicitly before using them:
- Python automatically knows whether a value is text, a number, or a boolean.
- Variable values can be changed or updated at any point in the program.

---

## 🧱 Basic Types of Variables

| Variable Type | What it Stores | Example |
| :--- | :--- | :--- |
| **String (`str`)** | Text data inside quotes | `name = "Harish"` |
| **Integer (`int`)** | Whole numbers | `age = 25` |
| **Float (`float`)** | Numbers with decimals | `weight = 71.5` |
| **Boolean (`bool`)** | `True` or `False` | `is_student = True` |

---

## 🔄 Updating Variable Values
Variables are called "variable" because their values can change:

```python
age = 25
print(age)   # Output: 25

# Updating age
age = 26
print(age)   # Output: 26
```

---

## ➕ Basic Math with Variables
You can use variables in arithmetic operations:

```python
a = 10
b = 20
total = a + b
print("Sum:", total)  # Output: 30
```

---

## 🔍 Checking Types with `type()`
Python provides the built-in `type()` function to inspect what kind of data is stored in a variable:

```python
name = "Harish"
print(type(name))  # Output: <class 'str'>
```

---

## 📂 File Structure

```text
PYTHON-DAY-2/
├── README.md       # Basic level documentation of What is a Variable
├── day2.py         # Main basic level Python script
└── variable.py     # Practice script
```

---

## 💻 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/harish-0987/PYTHON-DAY-2.git
cd PYTHON-DAY-2
```

### 2. Run the Script
```bash
python day2.py
```

---

## 👤 Author
- **Harish**
- GitHub: [@harish-0987](https://github.com/harish-0987)
- Motto: *"Not here to be known, here to build."*
