# =============================================================================
# DAY 20: PRACTICE QUESTIONS ON EXCEPTION HANDLING (BASIC LEVEL)
# Author: Harish
# Repository: DAY-20-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# INTRODUCTION:
# Exception handling is an indispensable skill in Python programming. It enables
# programs to anticipate potential failure points, intercept runtime errors,
# safeguard critical data, and ensure seamless user experiences.
#
# This file contains 10 carefully designed, basic-level practice questions
# covering the most common real-world scenarios:
#   1. Safe Division Calculator (ZeroDivisionError, TypeError)
#   2. Safe String-to-Integer Converter (ValueError, TypeError)
#   3. Safe List Element Access (IndexError, TypeError)
#   4. Safe Dictionary Lookup (KeyError, TypeError)
#   5. Safe File Reader with Cleanup (FileNotFoundError, finally)
#   6. Enforcing Constraints with 'raise' (ValueError, TypeError)
#   7. Mixed Data Summation with Error Filtering (ValueError, TypeError)
#   8. Custom Exception - Negative Number Handling (NegativeNumberError)
#   9. Banking System with Custom Exception & Full Architecture (try-except-else-finally)
#  10. User Registration Validator Pipeline (KeyError, ValueError, TypeError)
# =============================================================================

import math
from typing import Any, Dict, List, Optional, Tuple, Union


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 78)
    print(f"  {title}")
    print("=" * 78)


# =============================================================================
# CUSTOM EXCEPTION CLASSES
# =============================================================================
class NegativeNumberError(Exception):
    """Raised when an operation requires a non-negative number but receives negative."""

    def __init__(self, value: Union[int, float], message: str = "Negative numbers are not allowed!"):
        self.value = value
        self.message = f"{message} (Received: {value})"
        super().__init__(self.message)


class InsufficientFundsError(Exception):
    """Raised when a withdrawal attempt exceeds the available account balance."""

    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Withdrawal failed: Requested ${amount:.2f}, but current balance is ${balance:.2f}."
        )


# =============================================================================
# PRACTICE QUESTION 1: SAFE DIVISION CALCULATOR
# =============================================================================
# Problem: Write a function `safe_divide(a, b)` that performs division of `a`
# by `b`. Catch division by zero (`ZeroDivisionError`) and invalid types (`TypeError`).
# Use `else` to return the quotient and `finally` to log completion.
# =============================================================================
def safe_divide(a: Any, b: Any) -> Optional[float]:
    """Divides `a` by `b` safely, handling ZeroDivisionError and TypeError."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"   [Error] Cannot divide {a} by zero!")
        return None
    except TypeError:
        print(f"   [Error] Unsupported operand types for division: {type(a).__name__} and {type(b).__name__}!")
        return None
    else:
        print(f"   [Success] Division successful: {a} / {b} = {result:.4f}")
        return result
    finally:
        print("   [Log] Division operation finalized.")


# =============================================================================
# PRACTICE QUESTION 2: SAFE STRING-TO-INTEGER CONVERTER
# =============================================================================
# Problem: Write a function `safe_str_to_int(value, default=0)` that safely
# converts a string to an integer. If the conversion fails due to invalid characters
# (ValueError) or incorrect type (TypeError), catch it and return `default`.
# =============================================================================
def safe_str_to_int(value: Any, default: int = 0) -> int:
    """Safely converts `value` to int; returns `default` if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError) as err:
        print(f"   [Handled {type(err).__name__}] Could not convert {repr(value)} to int. Falling back to default: {default}")
        return default


# =============================================================================
# PRACTICE QUESTION 3: SAFE LIST ELEMENT ACCESS
# =============================================================================
# Problem: Write a function `get_list_element(items, index, default=None)` that
# accesses an element at `index`. Catch `IndexError` when index is out of bounds
# and `TypeError` if `items` is not subscriptable or `index` is not an integer.
# =============================================================================
def get_list_element(items: Any, index: Any, default: Any = None) -> Any:
    """Safely accesses element at `index` from `items`, returning `default` on error."""
    try:
        return items[index]
    except IndexError:
        print(f"   [IndexError] Index {index} is out of bounds for sequence of length {len(items) if hasattr(items, '__len__') else 'unknown'}!")
        return default
    except TypeError as err:
        print(f"   [TypeError] Invalid access operation: {err}")
        return default


# =============================================================================
# PRACTICE QUESTION 4: SAFE DICTIONARY LOOKUP
# =============================================================================
# Problem: Write a function `safe_dict_lookup(data, key, default=None)` that
# retrieves a value for `key` without using `.get()`. Catch `KeyError` if key is
# absent and `TypeError` if `data` is not a mapping/dictionary.
# =============================================================================
def safe_dict_lookup(data: Any, key: Any, default: Any = None) -> Any:
    """Safely retrieves `key` from dictionary `data` using explicit KeyError handling."""
    try:
        return data[key]
    except KeyError:
        print(f"   [KeyError] Key {repr(key)} does not exist in dictionary. Returning default: {repr(default)}")
        return default
    except TypeError as err:
        print(f"   [TypeError] Provided object is not a subscriptable dictionary: {err}")
        return default


# =============================================================================
# PRACTICE QUESTION 5: SAFE FILE READER WITH CLEANUP
# =============================================================================
# Problem: Write a function `read_file_safely(filepath)` that attempts to open
# and read a file's content. Catch `FileNotFoundError` and `PermissionError`.
# Use a `finally` block to verify file handle closure.
# =============================================================================
def read_file_safely(filepath: str) -> Optional[str]:
    """Attempts to read a file safely with proper exception catching and cleanup."""
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
        else:
            print("   [Cleanup] No open file handle required closure.")


# =============================================================================
# PRACTICE QUESTION 6: ENFORCING CONSTRAINTS WITH 'raise'
# =============================================================================
# Problem: Write a function `validate_voting_age(name, age)` that verifies if a
# citizen is eligible to vote.
#   - Raise `TypeError` if `age` is not an int or float.
#   - Raise `ValueError` if `age < 0` or `age > 125` (unrealistic age).
#   - Return True if `age >= 18`, otherwise False.
# =============================================================================
def validate_voting_age(name: str, age: Any) -> bool:
    """Validates voter eligibility; raises appropriate built-in exceptions for invalid input."""
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be a numeric integer or float, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 125:
        raise ValueError(f"Age {age} exceeds maximum realistic human lifespan (125)")

    if age >= 18:
        print(f"   [Eligible] '{name}' (age {age}) is eligible to vote.")
        return True
    else:
        print(f"   [Underage] '{name}' (age {age}) is not eligible to vote (must be 18+).")
        return False


# =============================================================================
# PRACTICE QUESTION 7: MIXED DATA SUMMATION WITH ERROR FILTERING
# =============================================================================
# Problem: Write a function `sum_valid_numbers(elements)` that takes a list of
# mixed elements (ints, floats, numeric strings, invalid strings, None, lists).
# Try converting each element to float and summing them up. Catch `ValueError`
# and `TypeError` to skip invalid elements, counting skipped items.
# =============================================================================
def sum_valid_numbers(elements: List[Any]) -> Tuple[float, int, int]:
    """Sums valid numbers from a mixed collection while skipping unparseable elements.
    
    Returns:
        (total_sum, valid_count, skipped_count)
    """
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


# =============================================================================
# PRACTICE QUESTION 8: CUSTOM EXCEPTION - NEGATIVE NUMBER HANDLING
# =============================================================================
# Problem: Define a custom exception `NegativeNumberError`. Write a function
# `calculate_square_root(value)` that computes the square root. If `value < 0`,
# raise `NegativeNumberError`. If `value` is not numeric, raise `TypeError`.
# =============================================================================
def calculate_square_root(value: Any) -> float:
    """Calculates square root; raises NegativeNumberError for negative input."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    if value < 0:
        raise NegativeNumberError(value, "Cannot compute real square root of a negative number")
    return math.sqrt(value)


# =============================================================================
# PRACTICE QUESTION 9: BANK ACCOUNT TRANSACTION SYSTEM
# =============================================================================
# Problem: Build a `BankAccount` class with a `withdraw(amount)` method.
#   - Raise `TypeError` if amount is not numeric.
#   - Raise `ValueError` if amount <= 0.
#   - Raise custom `InsufficientFundsError` if amount > balance.
#   - Demonstrate full `try-except-else-finally` architecture.
# =============================================================================
class BankAccount:
    """Represents a simple bank account with strict transaction validation."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def withdraw(self, amount: Any) -> float:
        """Executes withdrawal with rigorous input and balance validation."""
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Withdrawal amount must be numeric, got {type(amount).__name__}")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be strictly positive (got: {amount})")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        return self.balance


def execute_atm_withdrawal(account: BankAccount, amount: Any) -> None:
    """Driver function wrapping account withdrawal in full try-except-else-finally."""
    print(f"-> Initiating ATM withdrawal of ${amount} for '{account.account_holder}'...")
    try:
        new_balance = account.withdraw(amount)
    except InsufficientFundsError as ife:
        print(f"   [Declined - Custom Exception] {ife}")
    except (ValueError, TypeError) as err:
        print(f"   [Declined - Validation Error] {type(err).__name__}: {err}")
    else:
        print(f"   [Approved] Withdrawal complete! Remaining balance: ${new_balance:.2f}")
    finally:
        print(f"   [Receipt] Session finished. Current Balance: ${account.balance:.2f}\n")


# =============================================================================
# PRACTICE QUESTION 10: USER REGISTRATION VALIDATOR PIPELINE
# =============================================================================
# Problem: Write a function `validate_user_registration(user_data)` that validates
# a user registration dictionary.
# Required keys: "username" (str, non-empty), "email" (str, containing '@'),
# "age" (int, between 13 and 120).
# Catch `KeyError`, `TypeError`, and `ValueError`, returning a structured status dict.
# =============================================================================
def validate_user_registration(user_data: Any) -> Dict[str, Any]:
    """Validates user payload through an exception-handled pipeline."""
    try:
        # Check dictionary type
        if not isinstance(user_data, dict):
            raise TypeError(f"Payload must be a dictionary, got {type(user_data).__name__}")

        # Required key checking (raises KeyError if missing)
        username = user_data["username"]
        email = user_data["email"]
        age_raw = user_data["age"]

        # Validate types and values
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


# =============================================================================
# MAIN EXECUTION ROUTINE
# =============================================================================
def main():
    print("=" * 78)
    print(" DAY 20: PRACTICE QUESTIONS ON EXCEPTION HANDLING (BASIC LEVEL)")
    print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
    print(" Repository: DAY-20-OF-PYTHON")
    print("=" * 78)

    # -------------------------------------------------------------------------
    # TEST 1: SAFE DIVISION CALCULATOR
    # -------------------------------------------------------------------------
    print_section("QUESTION 1: SAFE DIVISION CALCULATOR")
    test_divisions = [
        (100, 5),     # Valid division
        (45, 0),      # Division by zero
        ("80", 4),    # TypeError: string dividend
        (12.5, 2.5),  # Float division
    ]
    for num, denom in test_divisions:
        print(f"Testing safe_divide({repr(num)}, {repr(denom)}):")
        safe_divide(num, denom)
        print()

    # -------------------------------------------------------------------------
    # TEST 2: SAFE STRING-TO-INTEGER CONVERTER
    # -------------------------------------------------------------------------
    print_section("QUESTION 2: SAFE STRING-TO-INTEGER CONVERTER")
    test_strings = ["42", "-15", "python", "3.1415", None, "1000"]
    for s in test_strings:
        res = safe_str_to_int(s, default=-1)
        print(f"-> Parsed {repr(s):<12} => Result: {res}")

    # -------------------------------------------------------------------------
    # TEST 3: SAFE LIST ELEMENT ACCESS
    # -------------------------------------------------------------------------
    print_section("QUESTION 3: SAFE LIST ELEMENT ACCESS")
    languages = ["Python", "Rust", "Go", "TypeScript"]
    test_indices = [0, 2, 10, -1, "first"]
    print(f"Target sequence: {languages}\n")
    for idx in test_indices:
        item = get_list_element(languages, idx, default="<OUT_OF_RANGE>")
        print(f"-> Element at index {repr(idx):<8} => {repr(item)}")

    # -------------------------------------------------------------------------
    # TEST 4: SAFE DICTIONARY LOOKUP
    # -------------------------------------------------------------------------
    print_section("QUESTION 4: SAFE DICTIONARY LOOKUP")
    developer = {"name": "Harish", "role": "Software Developer", "days_coded": 20}
    test_keys = ["name", "role", "salary", "motto"]
    print(f"Target dictionary: {developer}\n")
    for k in test_keys:
        val = safe_dict_lookup(developer, k, default="[NOT SPECIFIED]")
        print(f"-> Key {repr(k):<12} => Value: {repr(val)}")

    # -------------------------------------------------------------------------
    # TEST 5: SAFE FILE READER WITH CLEANUP
    # -------------------------------------------------------------------------
    print_section("QUESTION 5: SAFE FILE READER WITH CLEANUP")
    print("Scenario A: Attempting to read a non-existent file:")
    read_file_safely("imaginary_file_that_does_not_exist.txt")

    print("\nScenario B: Reading this current script file (day20.py):")
    script_snippet = read_file_safely(__file__)
    if script_snippet:
        first_line = script_snippet.splitlines()[0]
        print(f"   First line preview: {first_line}")

    # -------------------------------------------------------------------------
    # TEST 6: ENFORCING CONSTRAINTS WITH 'raise'
    # -------------------------------------------------------------------------
    print_section("QUESTION 6: ENFORCING CONSTRAINTS WITH 'raise'")
    candidates = [
        ("Alice", 24),
        ("Bob", 16),
        ("Charlie", -3),
        ("Diana", 150),
        ("Eve", "twenty"),
    ]
    for name, age in candidates:
        print(f"Testing voter verification for '{name}' with age={repr(age)}:")
        try:
            validate_voting_age(name, age)
        except (ValueError, TypeError) as exc:
            print(f"   [Validation Exception] {type(exc).__name__}: {exc}")
        print()

    # -------------------------------------------------------------------------
    # TEST 7: MIXED DATA SUMMATION WITH ERROR FILTERING
    # -------------------------------------------------------------------------
    print_section("QUESTION 7: MIXED DATA SUMMATION WITH ERROR FILTERING")
    mixed_dataset = [10, "20.5", "invalid", None, 35, [1, 2], "-5.5", "100"]
    print(f"Input dataset: {mixed_dataset}")
    total, valid, skipped = sum_valid_numbers(mixed_dataset)
    print(f"-> Total sum of valid numbers : {total}")
    print(f"-> Valid items converted      : {valid}")
    print(f"-> Invalid items skipped      : {skipped}")

    # -------------------------------------------------------------------------
    # TEST 8: CUSTOM EXCEPTION - NEGATIVE NUMBER HANDLING
    # -------------------------------------------------------------------------
    print_section("QUESTION 8: CUSTOM EXCEPTION (NegativeNumberError)")
    math_test_inputs = [25, 0, -9, "nine", 144]
    for val in math_test_inputs:
        print(f"Calculating square root of {repr(val)}:")
        try:
            sq_root = calculate_square_root(val)
            print(f"   [Result] sqrt({val}) = {sq_root:.2f}")
        except NegativeNumberError as nne:
            print(f"   [Custom Error] {nne}")
        except TypeError as te:
            print(f"   [Type Error] {te}")
        print()

    # -------------------------------------------------------------------------
    # TEST 9: BANK ACCOUNT TRANSACTION SYSTEM
    # -------------------------------------------------------------------------
    print_section("QUESTION 9: BANK ACCOUNT TRANSACTION SYSTEM")
    my_account = BankAccount(account_holder="Harish", initial_balance=500.0)
    print(f"Created account for '{my_account.account_holder}' with initial balance: ${my_account.balance:.2f}\n")

    execute_atm_withdrawal(my_account, 150.0)   # Valid withdrawal
    execute_atm_withdrawal(my_account, -50.0)   # Negative amount -> ValueError
    execute_atm_withdrawal(my_account, "100")   # Wrong type -> TypeError
    execute_atm_withdrawal(my_account, 800.0)   # Exceeds balance -> InsufficientFundsError
    execute_atm_withdrawal(my_account, 200.0)   # Valid withdrawal

    # -------------------------------------------------------------------------
    # TEST 10: USER REGISTRATION VALIDATOR PIPELINE
    # -------------------------------------------------------------------------
    print_section("QUESTION 10: USER REGISTRATION VALIDATOR PIPELINE")
    profiles = [
        {"username": "harish_dev", "email": "harish@example.com", "age": 22},  # Valid
        {"username": "", "email": "empty_user@example.com", "age": 25},        # Invalid username
        {"username": "johndoe", "email": "invalid_email_format", "age": 30},   # Invalid email
        {"username": "timmy", "email": "timmy@example.com", "age": 10},         # Underage (< 13)
        {"username": "sarah", "email": "sarah@example.com"},                    # Missing 'age' key
        "not_even_a_dictionary",                                                # Invalid payload type
    ]

    for idx, p in enumerate(profiles, start=1):
        print(f"Profile {idx}: {repr(p)}")
        validation_report = validate_user_registration(p)
        status_tag = "VALID" if validation_report["is_valid"] else "INVALID"
        print(f"   Status: [{status_tag}] | Error: {validation_report['error_type']} | Message: {validation_report['message']}\n")

    # -------------------------------------------------------------------------
    # SUMMARY & BEST PRACTICES
    # -------------------------------------------------------------------------
    print_section("SUMMARY & BEST PRACTICES FOR EXCEPTION HANDLING")
    print("1. Precision: Catch narrow, specific exceptions rather than bare 'except:'.")
    print("2. Graceful Degradation: Provide sane fallbacks or defaults when errors occur.")
    print("3. Guaranteed Cleanup: Utilize 'finally' to release resources regardless of errors.")
    print("4. Custom Domain Exceptions: Subclass 'Exception' to express business logic failures.")
    print("5. Clarity: Never swallow exceptions blindly with 'except Exception: pass'.")
    print("=" * 78)
    print(" DAY 20 PRACTICE COMPLETE: EXCEPTION HANDLING CONFIDENTLY MASTERED!")
    print("=" * 78)


if __name__ == "__main__":
    main()
