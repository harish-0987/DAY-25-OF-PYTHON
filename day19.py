# =============================================================================
# DAY 19: EXCEPTION HANDLING IN PYTHON (BASIC LEVEL)
# Author: Harish
# Repository: DAY-19-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# 1. WHAT IS AN ERROR VS. AN EXCEPTION?
# =============================================================================
# In Python, issues that stop code execution fall into two main categories:
#
# 1. SYNTAX ERRORS (Parsing Errors):
#    - Occur when the code violates the grammatical rules of Python.
#    - Detected *before* the script runs.
#    - Examples: Missing colons (:), unclosed parentheses, misspelled keywords.
#    - These CANNOT be handled using try/except blocks; they must be fixed in code.
#
# 2. EXCEPTIONS (Runtime Errors):
#    - The syntax is 100% valid, but an error occurs *during* program execution.
#    - Examples: Dividing a number by zero, accessing an invalid list index,
#      converting the string "apple" into an integer.
#    - If unhandled, exceptions cause Python to terminate abnormally (crash)
#      and print a "Traceback".
#
# =============================================================================
# 2. WHAT IS EXCEPTION HANDLING?
# =============================================================================
# Exception handling is a mechanism that allows a program to detect runtime
# errors, "catch" them gracefully, take corrective action, and keep running
# without crashing.
#
# The Core Architecture:
# - try      : Code block that might produce an exception.
# - except   : Code block that executes IF an exception occurs.
# - else     : Code block that executes IF NO exception occurs in the try block.
# - finally  : Code block that ALWAYS executes, regardless of errors.
# - raise    : Keyword used to trigger an exception intentionally.
# =============================================================================


def print_section(title: str):
    """Utility function to print visually formatted section headers."""
    print("\n" + "=" * 75)
    print(f"  {title}")
    print("=" * 75)


# =============================================================================
# CUSTOM EXCEPTION CLASS (Inherits from Python's built-in Exception)
# =============================================================================
class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds available balance."""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}! Available balance is only ${balance:.2f}."
        )


class InvalidAgeError(Exception):
    """Custom exception raised when an age value is outside a realistic range."""
    pass


def main():
    print("=" * 75)
    print(" DAY 19: EXCEPTION HANDLING IN PYTHON (BASIC LEVEL)")
    print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
    print("=" * 75)

    # -------------------------------------------------------------------------
    # PART 1: COMMON BUILT-IN PYTHON EXCEPTIONS
    # -------------------------------------------------------------------------
    print_section("PART 1: COMMON BUILT-IN EXCEPTIONS IN PYTHON")
    print("Python provides built-in exception classes for specific runtime errors:\n")

    # 1.1 ZeroDivisionError
    print("[1.1] ZeroDivisionError:")
    try:
        _ = 100 / 0
    except ZeroDivisionError as e:
        print(f"  - Caught ZeroDivisionError: {e}")

    # 1.2 ValueError
    print("\n[1.2] ValueError:")
    try:
        _ = int("PythonIsAwesome")
    except ValueError as e:
        print(f"  - Caught ValueError: {e}")

    # 1.3 TypeError
    print("\n[1.3] TypeError:")
    try:
        _ = 10 + "20"
    except TypeError as e:
        print(f"  - Caught TypeError: {e}")

    # 1.4 IndexError
    print("\n[1.4] IndexError:")
    try:
        sample_list = [10, 20, 30]
        _ = sample_list[5]
    except IndexError as e:
        print(f"  - Caught IndexError: {e}")

    # 1.5 KeyError
    print("\n[1.5] KeyError:")
    try:
        user_info = {"name": "Harish", "role": "Developer"}
        _ = user_info["salary"]
    except KeyError as e:
        print(f"  - Caught KeyError (missing key): {e}")

    # 1.6 FileNotFoundError
    print("\n[1.6] FileNotFoundError:")
    try:
        with open("non_existent_file.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print(f"  - Caught FileNotFoundError: {e}")

    # -------------------------------------------------------------------------
    # PART 2: CATCHING SPECIFIC & MULTIPLE EXCEPTIONS
    # -------------------------------------------------------------------------
    print_section("PART 2: HANDLING SPECIFIC & MULTIPLE EXCEPTIONS")

    # 2.1 Multiple Separate 'except' Blocks
    print("[2.1] Using Multiple 'except' Blocks for Granular Handling:")

    def parse_and_divide(val_a: str, val_b: str):
        try:
            num_a = float(val_a)
            num_b = float(val_b)
            result = num_a / num_b
            print(f"  - Success: {val_a} / {val_b} = {result:.2f}")
        except ValueError as err:
            print(f"  - [Input Error] Non-numeric input received: '{err}'")
        except ZeroDivisionError:
            print(f"  - [Math Error] Division by zero is mathematically undefined!")

    parse_and_divide("50", "5")    # Valid
    parse_and_divide("50", "0")    # Triggers ZeroDivisionError
    parse_and_divide("50", "abc")  # Triggers ValueError

    # 2.2 Catching Multiple Exceptions in One 'except' Block using a Tuple
    print("\n[2.2] Catching Multiple Exceptions in a Single Tuple:")
    test_cases = [(100, 0), (100, "invalid"), (50, 2)]

    for a, b in test_cases:
        try:
            res = a / b
            print(f"  - Success: {a} / {b} = {res}")
        except (ZeroDivisionError, TypeError) as err:
            print(f"  - Caught expected error for inputs ({a}, {b}) -> {type(err).__name__}: {err}")

    # -------------------------------------------------------------------------
    # PART 3: THE COMPLETE FLOW: try - except - else - finally
    # -------------------------------------------------------------------------
    print_section("PART 3: THE COMPLETE FLOW (try - except - else - finally)")
    print("Flow rules:")
    print("  - 'try'     : Runs first.")
    print("  - 'except'  : Runs ONLY if an error occurs inside 'try'.")
    print("  - 'else'    : Runs ONLY if NO error occurred in 'try'.")
    print("  - 'finally' : ALWAYS runs, guaranteeing cleanup (closing files, DBs, sockets).\n")

    def demonstrate_full_flow(dividend: float, divisor: float):
        print(f"-> Calling demonstrate_full_flow({dividend}, {divisor}):")
        try:
            print("   [1] Entering 'try' block...")
            quotient = dividend / divisor
        except ZeroDivisionError as err:
            print(f"   [2] In 'except' block: Handled {err}")
        else:
            print(f"   [2] In 'else' block: Division succeeded! Result = {quotient:.2f}")
        finally:
            print("   [3] In 'finally' block: Cleanup and reset completed (Always executes!).\n")

    demonstrate_full_flow(40, 4)   # Scenario A: Success
    demonstrate_full_flow(40, 0)   # Scenario B: Exception occurred

    # -------------------------------------------------------------------------
    # PART 4: RAISING EXCEPTIONS MANUALLY ('raise')
    # -------------------------------------------------------------------------
    print_section("PART 4: RAISING EXCEPTIONS MANUALLY WITH 'raise'")
    print("Use the 'raise' keyword to enforce business constraints and sanity checks.\n")

    def register_voter(name: str, age: int):
        if not isinstance(age, int):
            raise TypeError(f"Age must be an integer, got {type(age).__name__}")
        if age < 0:
            raise ValueError(f"Age cannot be negative: {age}")
        if age < 18:
            raise ValueError(f"Voter '{name}' must be at least 18 years old to register (given: {age})")
        return f"Registration successful for {name} (Age: {age})!"

    voters = [
        ("Alice", 21),
        ("Bob", -5),
        ("Charlie", 15),
        ("David", "twenty"),
    ]

    for name, age in voters:
        try:
            status = register_voter(name, age)
            print(f"  - {status}")
        except (ValueError, TypeError) as err:
            print(f"  - Validation failed for '{name}': {err}")

    # -------------------------------------------------------------------------
    # PART 5: CUSTOM (USER-DEFINED) EXCEPTIONS
    # -------------------------------------------------------------------------
    print_section("PART 5: CUSTOM / USER-DEFINED EXCEPTIONS")
    print("Create domain-specific exceptions by subclassing Python's 'Exception'.\n")

    class BankAccount:
        def __init__(self, owner: str, balance: float):
            self.owner = owner
            self.balance = balance

        def withdraw(self, amount: float):
            if amount <= 0:
                raise ValueError("Withdrawal amount must be strictly greater than $0.00!")
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            print(f"  - [Success] Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    account = BankAccount(owner="Harish", balance=500.00)
    print(f"Created account for '{account.owner}' with initial balance: ${account.balance:.2f}\n")

    withdrawal_attempts = [150.00, -20.00, 600.00, 200.00]

    for amt in withdrawal_attempts:
        print(f"Attempting to withdraw ${amt:.2f}:")
        try:
            account.withdraw(amt)
        except InsufficientFundsError as ife:
            print(f"    Caught Custom Exception: {ife}")
        except ValueError as ve:
            print(f"    Caught Validation Error: {ve}")

    # -------------------------------------------------------------------------
    # PART 6: PRACTICAL UTILITY - SAFE NUMBER PARSER
    # -------------------------------------------------------------------------
    print_section("PART 6: REAL-WORLD PATTERN - ROBUST INPUT PARSER")
    print("A reusable utility function that parses strings to numbers safely without crashing.\n")

    def safe_convert_to_int(value: str, default: int = 0) -> int:
        """Safely parses string to int; returns default value on failure."""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    test_inputs = ["42", "hello", "100", None, "99.9", "777"]
    print("Parsing various inputs safely:")
    for item in test_inputs:
        parsed = safe_convert_to_int(item, default=-1)
        print(f"  - Input: {repr(item):<12} -> Parsed Integer: {parsed}")

    # -------------------------------------------------------------------------
    # SUMMARY & BEST PRACTICES
    # -------------------------------------------------------------------------
    print_section("KEY TAKEAWAYS & BEST PRACTICES (PEP 8)")
    print("1. Be Specific: Never use bare 'except:' without an exception class.")
    print("   Catch specific exceptions (e.g. ValueError, ZeroDivisionError).")
    print("2. Keep 'try' Minimal: Wrap ONLY the lines of code likely to fail, not whole scripts.")
    print("3. Use 'else' Wisely: Place code that should only run if the 'try' succeeded in 'else'.")
    print("4. Use 'finally' for Cleanup: Always clean up file handles, network calls, or locks.")
    print("5. Don't Suppress Errors Silently: Never use 'except Exception: pass' without logging.")
    print("=" * 75)
    print(" DAY 19 COMPLETE: EXCEPTION HANDLING MASTERED!")
    print("=" * 75)


if __name__ == "__main__":
    main()
