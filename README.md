# Day 21: File Handling in Python (Basic Level) 📁🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-21-OF-PYTHON](https://github.com/harish-0987/DAY-21-OF-PYTHON)

Welcome to **Day 21 of Python**! Today's focus is on **File Handling in Python (Basic Level)**.

In programming, variables and data stored in memory are volatile—they disappear once program execution finishes. File handling bridges this gap by allowing programs to persist, retrieve, update, and manage data stored permanently on secondary storage disks.

---

## 📌 Table of Contents

1. [Overview & Learning Objectives](#-overview--learning-objectives)
2. [What is File Handling?](#-what-is-file-handling)
3. [The File Lifecycle](#-the-file-lifecycle)
4. [File Opening Modes Comparison](#-file-opening-modes-comparison)
5. [Key Operations](#-key-operations)
   - [1. Writing to Files (`w` and `writelines`)](#1-writing-to-files-w-and-writelines)
   - [2. Reading from Files (`read`, `readline`, `readlines`, and loops)](#2-reading-from-files-read-readline-readlines-and-loops)
   - [3. Appending to Files (`a` mode)](#3-appending-to-files-a-mode)
   - [4. The `with` Statement (Context Manager)](#4-the-with-statement-context-manager)
   - [5. File Pointer Navigation (`tell` & `seek`)](#5-file-pointer-navigation-tell--seek)
   - [6. Safe File Handling with `try...except`](#6-safe-file-handling-with-tryexcept)
   - [7. Practical Mini-Project: File Analyzer](#7-practical-mini-project-file-analyzer)
6. [Best Practices](#-best-practices)
7. [How to Run the Code](#-how-to-run-the-code)
8. [Summary & Takeaways](#-summary--takeaways)

---

## 🎯 Overview & Learning Objectives

By completing Day 21, you will understand:
- Why data persistence matters and how files work in Python.
- How to open, read, write, append, and close files.
- The differences between file modes (`'r'`, `'w'`, `'a'`, `'x'`, text vs. binary).
- Why the `with` statement (Context Manager) is the gold standard for file handling.
- How to navigate the internal file pointer using `tell()` and `seek()`.
- How to handle `FileNotFoundError` and `IOError` gracefully to prevent crashes.

---

## 📂 What is File Handling?

File handling refers to reading data from files or saving data into files stored on your hard drive, SSD, or external storage.

- **Volatile Storage (RAM)**: Variables, lists, and objects live here while the script runs; destroyed when the program stops.
- **Non-Volatile Storage (Disk)**: Files (`.txt`, `.csv`, `.json`, `.log`) persist permanently across program executions, reboots, and systems.

---

## 🔄 The File Lifecycle

Every file operation in Python follows a 3-step lifecycle:

```
┌─────────────┐       ┌────────────────────────┐       ┌─────────────┐
│ 1. OPEN     │ ────> │ 2. OPERATE             │ ────> │ 3. CLOSE    │
│ open(file)  │       │ read() / write() / app │       │ close()     │
└─────────────┘       └────────────────────────┘       └─────────────┘
```

> **Note**: Forgetting to close files can cause resource leaks and locked files. Modern Python solves this automatically with the `with` statement.

---

## 📊 File Opening Modes Comparison

| Mode | Name | Description | If File Does NOT Exist | If File Already Exists |
| :---: | :---: | :--- | :---: | :---: |
| `'r'` | **Read** | Default mode. Opens file for reading only. | Raises `FileNotFoundError` | Reads from beginning |
| `'w'` | **Write** | Opens file for writing. | Creates a new file | **Truncates (erases)** content |
| `'a'` | **Append** | Opens file for writing at the end. | Creates a new file | Keeps content & appends |
| `'x'` | **Exclusive** | Creates a new file for writing. | Creates a new file | Raises `FileExistsError` |
| `'r+'`| **Read/Write** | Opens file for both reading and writing. | Raises `FileNotFoundError` | Pointer at beginning |
| `'t'` | **Text** | Default text format (strings). | - | - |
| `'b'` | **Binary** | Raw byte format (images, audio, etc.). | - | - |

---

## 🛠️ Key Operations

### 1. Writing to Files (`w` and `writelines`)

- `file.write(str)` writes a single string into the file.
- `file.writelines(list)` writes a sequence of strings (does not automatically append newline `\n`).

```python
# Writing initial text
file = open("notes.txt", "w", encoding="utf-8")
file.write("Hello, World!\n")
file.writelines(["First line\n", "Second line\n"])
file.close()
```

---

### 2. Reading from Files (`read`, `readline`, `readlines`, and loops)

Python offers four flexible techniques to read content:

1. **`file.read()`**: Reads entire file content as a single string.
2. **`file.read(N)`**: Reads up to `N` characters/bytes.
3. **`file.readline()`**: Reads one line at a time.
4. **`file.readlines()`**: Reads all lines into a Python `list` of strings.
5. **Direct iteration (`for line in file:`)**: **Recommended for large files** because it streams lines into memory without loading the entire file at once.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

### 3. Appending to Files (`a` mode)

When you want to record logs, add new user records, or save results without erasing existing data, use append mode `'a'`.

```python
with open("activity.log", "a", encoding="utf-8") as log:
    log.write("[INFO] User authenticated successfully.\n")
```

---

### 4. The `with` Statement (Context Manager)

The modern Python standard for opening files:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# The file is GUARANTEED to be closed here, even if an exception was raised!
```

**Why it matters:**
- Automatically invokes `__enter__()` when entering and `__exit__()` when leaving.
- Frees file descriptors and operating system handles immediately.
- Eliminates manual `file.close()` calls.

---

### 5. File Pointer Navigation (`tell` & `seek`)

The file pointer acts as a cursor indicating where the next read or write will occur.

- `file.tell()`: Returns an integer representing the current byte offset of the pointer.
- `file.seek(offset)`: Relocates the pointer to the specified position (`seek(0)` resets to the beginning).

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.tell())       # 0 (at start)
    chunk = f.read(10)
    print(f.tell())       # 10
    f.seek(0)             # Rewind back to start
    print(f.read(10))     # Re-reads first 10 characters
```

---

### 6. Safe File Handling with `try...except`

Handle missing or inaccessible files gracefully without crashing your software:

```python
try:
    with open("config.json", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("Configuration file was not found. Initializing with defaults.")
except IOError as err:
    print(f"I/O error encountered: {err}")
```

---

### 7. Practical Mini-Project: File Analyzer

In `day21.py`, we implement a simple file analyzer utility that reads any text file and reports:
- Number of lines
- Number of words
- Total character count

---

## 🌟 Best Practices

1. **Always use `with` blocks**: Prevents leaks and dangling open file descriptors.
2. **Explicitly specify `encoding="utf-8"`**: Guarantees cross-platform consistency between Windows, macOS, and Linux.
3. **Stream large files**: Use `for line in file:` instead of `file.read()` or `file.readlines()` when dealing with large files (GBs).
4. **Be cautious with `'w'` mode**: Remember that `'w'` mode will completely wipe out any existing content in the file without asking for confirmation.
5. **Always catch `FileNotFoundError`**: When reading files created outside your script or based on user input.

---

## 🚀 How to Run the Code

Run the Day 21 script directly using Python:

```bash
python day21.py
```

All demonstrations run in a self-contained manner and clean up any temporary demo files created during execution.

---

## 📌 Summary & Takeaways

| Concept | Key Syntax | Benefit |
| :--- | :--- | :--- |
| **Open File** | `with open(filename, mode, encoding="utf-8") as f:` | Clean, safe, resource-friendly |
| **Write** | `f.write("text\n")` | Saves text to disk |
| **Read All** | `content = f.read()` | Retrieves entire file |
| **Read Line-by-Line**| `for line in f:` | Memory-efficient streaming |
| **Append** | `open(filename, 'a')` | Adds data without overwriting |
| **Position** | `f.tell()` / `f.seek(0)` | Inspects and resets reading cursor |

---

*Keep building every day. See you in Day 22!*
