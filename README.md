# Day 20: Practice Questions on Exception Handling (Basic Level) 🛡️🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-20-OF-PYTHON](https://github.com/harish-0987/DAY-20-OF-PYTHON)

Welcome to **Day 20 of Python**! Following our foundational journey into Exception Handling on Day 19, today is dedicated entirely to **hands-on practice and real-world problem solving**. 

This repository contains **10 carefully curated practice questions** designed to solidify your understanding of Python's exception handling mechanisms (`try`, `except`, `else`, `finally`, and `raise`), along with custom exception classes and robust data validation patterns.

---

## 📌 Table of Contents

1. [Overview & Learning Objectives](#-overview--learning-objectives)
2. [Exception Handling Architecture Recap](#-exception-handling-architecture-recap)
3. [10 Practice Questions & Detailed Solutions](#-10-practice-questions--detailed-solutions)
   - [Question 1: Safe Division Calculator](#question-1-safe-division-calculator)
   - [Question 2: Safe String-to-Integer Converter](#question-2-safe-string-to-integer-converter)
   - [Question 3: Safe List Element Access](#question-3-safe-list-element-access)
   - [Question 4: Safe Dictionary Lookup](#question-4-safe-dictionary-lookup)
   - [Question 5: Safe File Reader with Cleanup](#question-5-safe-file-reader-with-cleanup)
   - [Question 6: Enforcing Constraints with `raise`](#question-6-enforcing-constraints-with-raise)
   - [Question 7: Mixed Data Summation with Error Filtering](#question-7-mixed-data-summation-with-error-filtering)
   - [Question 8: Custom Exception for Negative Numbers](#question-8-custom-exception-for-negative-numbers)
   - [Question 9: Bank Account Transaction System](#question-9-bank-account-transaction-system)
   - [Question 10: User Registration Validator Pipeline](#question-10-user-registration-validator-pipeline)
4. [Summary Table of Practice Questions](#-summary-table-of-practice-questions)
5. [Code Structure in this Repository](#-code-structure-in-this-repository)
6. [Best Practices for Exception Handling](#-best-practices-for-exception-handling)
7. [How to Run the Code](#-how-to-run-the-code)
8. [Key Takeaways](#-key-takeaways)

---

## 🎯 Overview & Learning Objectives

Writing code that works under ideal conditions is easy; writing code that gracefully handles missing files, corrupt user inputs, network drops, and boundary conditions is what distinguishes professional software engineers.

By completing Day 20, you will be able to:
- Intercept and handle common runtime errors (`ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`).
- Master the four-part control flow: `try`, `except`, `else`, and `finally`.
- Enforce business logic and domain constraints using the `raise` keyword.
- Design custom domain-specific exception classes inheriting from `Exception`.
- Build resilient input validation pipelines and data processing routines.

---

## 🏗️ Exception Handling Architecture Recap

```
┌────────────────────────────────────────────────────────┐
│                        try:                            │
│           Code that might raise an exception           │
└───────────────────────────┬────────────────────────────┘
                            │
            Did an exception occur?
           /                       \
        YES                         NO
         ▼                           ▼
┌──────────────────┐        ┌──────────────────┐
│     except:      │        │      else:       │
│ Catch and handle │        │ Runs ONLY if NO  │
│  the exception   │        │ error occurred   │
└────────┬─────────┘        └────────┬─────────┘
         │                           │
         └─────────────┬─────────────┘
                       ▼
┌────────────────────────────────────────────────────────┐
│                      finally:                          │
│        ALWAYS runs, no matter what happens!            │
│         (Guaranteed resource cleanup & logging)        │
└────────────────────────────────────────────────────────┘
```

| Keyword | Purpose | When Does It Run? |
| :--- | :--- | :--- |
| `try` | Tests a block of code for errors | Always first |
| `except` | Handles specific exceptions | Only if an error matches the specified type |
| `else` | Executes code when no exceptions are raised | Only if the `try` block completes successfully |
| `finally` | Performs mandatory cleanup / termination | Always, regardless of success or failure |
| `raise` | Manually triggers an exception | When explicit validation or domain rules fail |

---

## 💻 10 Practice Questions & Detailed Solutions

### Question 1: Safe Division Calculator
- **Problem**: Write a function `safe_divide(a, b)` that performs division of `a` by `b`. Catch division by zero (`ZeroDivisionError`) and invalid operand types (`TypeError`). Use `else` to return the quotient and `finally` to log completion.
- **Concepts**: `ZeroDivisionError`, `TypeError`, `else`, `finally`.
- **Implementation**:
```python
def safe_divide(a: Any, b: Any) -> Optional[float]:
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"   [Error] Cannot divide {a} by zero!")
        return None
    except TypeError:
        print(f"   [Error] Unsupported operand types: {type(a).__name__} and {type(b).__name__}!")
        return None
    else:
        print(f"   [Success] Division successful: {a} / {b} = {result:.4f}")
        return result
    finally:
        print("   [Log] Division operation finalized.")
```

---

### Question 2: Safe String-to-Integer Converter
- **Problem**: Write a function `safe_str_to_int(value, default=0)` that safely converts a string or any input to an integer. If conversion fails due to invalid characters (`ValueError`) or wrong type (`TypeError`), catch it and return `default`.
- **Concepts**: Multiple exception handling in a single tuple `(ValueError, TypeError)`, fallback defaults.
- **Implementation**:
```python
def safe_str_to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError) as err:
        print(f"   [Handled {type(err).__name__}] Could not convert {repr(value)}. Default: {default}")
        return default
```

---

### Question 3: Safe List Element Access
- **Problem**: Write a function `get_list_element(items, index, default=None)` that retrieves an element from a sequence. Catch `IndexError` when index is out of bounds and `TypeError` when items is not subscriptable or index is invalid.
- **Concepts**: Sequence boundary safety, `IndexError`, `TypeError`.
- **Implementation**:
```python
def get_list_element(items: Any, index: Any, default: Any = None) -> Any:
    try:
        return items[index]
    except IndexError:
        print(f"   [IndexError] Index {index} is out of bounds!")
        return default
    except TypeError as err:
        print(f"   [TypeError] Invalid access operation: {err}")
        return default
```

---

### Question 4: Safe Dictionary Lookup
- **Problem**: Write a function `safe_dict_lookup(data, key, default=None)` that retrieves a value for `key` without using `.get()`. Catch `KeyError` if key is absent and `TypeError` if `data` is not a mapping.
- **Concepts**: Explicit `KeyError` interception vs `dict.get()`, mapping safety.
- **Implementation**:
```python
def safe_dict_lookup(data: Any, key: Any, default: Any = None) -> Any:
    try:
        return data[key]
    except KeyError:
        print(f"   [KeyError] Key {repr(key)} does not exist. Default: {repr(default)}")
        return default
    except TypeError as err:
        print(f"   [TypeError] Provided object is not a subscriptable dictionary: {err}")
        return default
```

---

### Question 5: Safe File Reader with Cleanup
- **Problem**: Write a function `read_file_safely(filepath)` that attempts to open and read a file. Catch `FileNotFoundError` and `PermissionError`. Ensure that any open file handle is closed using a `finally` block.
- **Concepts**: I/O resource management, `FileNotFoundError`, `PermissionError`, `finally` cleanup.
- **Implementation**:
```python
def read_file_safely(filepath: str) -> Optional[str]:
    file_handle = None
    try:
        file_handle = open(filepath, "r", encoding="utf-8")
        content = file_handle.read()
        print(f"   [Success] Read {len(content)} characters from '{filepath}'.")
        return content
    except FileNotFoundError:
        print(f"   [FileNotFoundError] The file '{filepath}' was not found.")
        return None
    except PermissionError:
        print(f"   [PermissionError] Insufficient permissions to read '{filepath}'.")
        return None
    finally:
        if file_handle is not None and not file_handle.closed:
            file_handle.close()
            print(f"   [Cleanup] File handle for '{filepath}' successfully closed.")
```

---

### Question 6: Enforcing Constraints with `raise`
- **Problem**: Write a function `validate_voting_age(name, age)` that validates voter eligibility:
  - Raise `TypeError` if `age` is not an int or float.
  - Raise `ValueError` if `age < 0` or `age > 125`.
  - Return `True` if `age >= 18`, otherwise `False`.
- **Concepts**: Input validation, custom exception messages with `raise`, boundary rules.
- **Implementation**:
```python
def validate_voting_age(name: str, age: Any) -> bool:
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be a numeric integer or float, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 125:
        raise ValueError(f"Age {age} exceeds maximum realistic human lifespan (125)")

    return age >= 18
```

---

### Question 7: Mixed Data Summation with Error Filtering
- **Problem**: Write a function `sum_valid_numbers(elements)` that processes a heterogeneous list (integers, floats, string numbers, words, `None`, nested lists). Convert valid elements to float and sum them, while skipping invalid items and keeping count.
- **Concepts**: Data cleansing, batch parsing, resilient accumulator pattern.
- **Implementation**:
```python
def sum_valid_numbers(elements: List[Any]) -> Tuple[float, int, int]:
    total_sum = 0.0
    valid_count = 0
    skipped_count = 0

    for item in elements:
        try:
            numeric_val = float(item)
            total_sum += numeric_val
            valid_count += 1
        except (ValueError, TypeError):
            skipped_count += 1

    return total_sum, valid_count, skipped_count
```

---

### Question 8: Custom Exception for Negative Numbers
- **Problem**: Define a custom exception `NegativeNumberError`. Write a function `calculate_square_root(value)` that computes the square root. If `value < 0`, raise `NegativeNumberError`. If `value` is not numeric, raise `TypeError`.
- **Concepts**: Subclassing `Exception`, domain-specific error handling.
- **Implementation**:
```python
class NegativeNumberError(Exception):
    """Raised when an operation requires a non-negative number but receives negative."""
    def __init__(self, value: Union[int, float], message: str = "Negative numbers are not allowed!"):
        self.value = value
        self.message = f"{message} (Received: {value})"
        super().__init__(self.message)

def calculate_square_root(value: Any) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    if value < 0:
        raise NegativeNumberError(value, "Cannot compute real square root of a negative number")
    return math.sqrt(value)
```

---

### Question 9: Bank Account Transaction System
- **Problem**: Implement a `BankAccount` class with a `withdraw(amount)` method:
  - Raise `TypeError` for non-numeric amounts.
  - Raise `ValueError` for `amount <= 0`.
  - Raise custom `InsufficientFundsError` when withdrawal exceeds balance.
  - Execute transactions inside a full `try-except-else-finally` driver that prints an ATM receipt.
- **Concepts**: OOP with custom exceptions, defensive state mutation, guaranteed audit logs.
- **Implementation**:
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        super().__init__(
            f"Withdrawal failed: Requested ${amount:.2f}, but current balance is ${balance:.2f}."
        )

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def withdraw(self, amount: Any) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Withdrawal amount must be numeric, got {type(amount).__name__}")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be strictly positive (got: {amount})")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        return self.balance
```

---

### Question 10: User Registration Validator Pipeline
- **Problem**: Write a function `validate_user_registration(user_data)` that validates user payload dictionaries.
  - Required fields: `username` (non-empty string), `email` (valid format with `@` and `.`), `age` (integer between 13 and 120).
  - Catch `KeyError`, `TypeError`, and `ValueError`, returning a structured status dictionary.
- **Concepts**: Enterprise payload validation, dictionary key safety, status reporting without crashes.
- **Implementation**:
```python
def validate_user_registration(user_data: Any) -> Dict[str, Any]:
    try:
        if not isinstance(user_data, dict):
            raise TypeError(f"Payload must be a dictionary, got {type(user_data).__name__}")

        username = user_data["username"]
        email = user_data["email"]
        age_raw = user_data["age"]

        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")

        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ValueError(f"Invalid email format: '{email}'")

        try:
            age = int(age_raw)
        except (ValueError, TypeError):
            raise ValueError(f"Age must be convertable to an integer (got: {repr(age_raw)})")

        if age < 13:
            raise ValueError(f"User is underage ({age}). Minimum required age is 13.")
        if age > 120:
            raise ValueError(f"Age {age} exceeds realistic threshold.")

    except KeyError as ke:
        return {"is_valid": False, "error_type": "KeyError", "message": f"Missing mandatory field: {ke}"}
    except TypeError as te:
        return {"is_valid": False, "error_type": "TypeError", "message": str(te)}
    except ValueError as ve:
        return {"is_valid": False, "error_type": "ValueError", "message": str(ve)}
    else:
        return {
            "is_valid": True,
            "error_type": None,
            "message": f"User '{username}' registered successfully! (Age: {age}, Email: {email})",
        }
```

---

## 📊 Summary Table of Practice Questions

| # | Question Title | Exceptions Handled / Raised | Key Technique |
| :---: | :--- | :--- | :--- |
| **1** | Safe Division Calculator | `ZeroDivisionError`, `TypeError` | `try-except-else-finally` pattern |
| **2** | Safe String-to-Integer Converter | `(ValueError, TypeError)` | Tuple of exceptions & fallback default |
| **3** | Safe List Element Access | `IndexError`, `TypeError` | Sequence boundary protection |
| **4** | Safe Dictionary Lookup | `KeyError`, `TypeError` | Explicit key error interception |
| **5** | Safe File Reader with Cleanup | `FileNotFoundError`, `PermissionError` | Safe handle closure in `finally` |
| **6** | Constraint Enforcement | `TypeError`, `ValueError` | Explicit input validation via `raise` |
| **7** | Mixed Data Summation | `(ValueError, TypeError)` | Data cleaning & error filtering in loops |
| **8** | Square Root Calculator | `NegativeNumberError`, `TypeError` | Custom exception subclassing `Exception` |
| **9** | ATM Banking System | `InsufficientFundsError`, `ValueError`, `TypeError` | State mutation & audit logging |
| **10** | User Registration Pipeline | `KeyError`, `TypeError`, `ValueError` | Structured error reporting dictionary |

---

## 📁 Code Structure in this Repository

```
DAY-20-OF-PYTHON/
│
├── day20.py                 # Complete script containing all 10 solutions & test suites
├── README.md                # In-depth documentation, problem statements & code walkthroughs
└── .gitignore               # Standard Python gitignore rules
```

---

## 🛡️ Best Practices for Exception Handling

1. **Be Granular & Specific**: Never use a bare `except:` or catch base `Exception` without re-raising or logging. Narrow exceptions prevent masking unintended bugs.
2. **Clean Up Resources Responsibly**: Use `finally` blocks or context managers (`with` statements) to guarantee that file descriptors, sockets, and connections are released.
3. **Use `else` for Unambiguous Success**: Keep the `try` block as minimal as possible; place operations that should only run when no error occurred into the `else` block.
4. **Distinguish Business Logic Errors**: Subclass `Exception` to create domain-specific errors (e.g., `InsufficientFundsError`, `NegativeNumberError`) rather than overloading generic built-ins.
5. **Fail Fast with Meaningful Messages**: Validate function arguments at entry using `raise TypeError(...)` or `raise ValueError(...)` with descriptive messages.

---

## 🚀 How to Run the Code

Clone the repository and execute the script directly using Python 3:

```bash
# Clone the repository
git clone https://github.com/harish-0987/DAY-20-OF-PYTHON.git

# Navigate into the project directory
cd DAY-20-OF-PYTHON

# Run the comprehensive test suite
python day20.py
```

---

## 🌟 Key Takeaways

- Exception handling turns potential fatal crashes into controlled, manageable program events.
- Defensive programming prevents silent corruption and guarantees auditability.
- Mastering `try`, `except`, `else`, `finally`, and `raise` is essential for creating production-ready Python applications.

---
⭐ *Day 20 Complete! Keep building and pushing forward every single day.*
