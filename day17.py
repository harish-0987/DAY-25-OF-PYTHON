# =============================================================================
# DAY 17: RECURSION IN PYTHON (BASIC LEVEL)
# Author: Harish
# Repository: DAY-17-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

import sys

# =============================================================================
# 1. WHAT IS RECURSION?
# =============================================================================
# Recursion is a programming technique where a function calls itself directly
# or indirectly to solve a smaller instance of the same problem.
#
# Every recursive function MUST have two essential components:
# 1. Base Case:
#    The termination condition that stops recursion. Without a base case,
#    the function would call itself indefinitely, leading to a stack overflow
#    (in Python, a RecursionError).
#
# 2. Recursive Case:
#    The part of the function where it reduces the problem into smaller subproblems
#    and calls itself with modified input, moving closer to the base case.
#
# Memory Note (The Call Stack):
# Each recursive call creates a new "stack frame" in memory to store local variables
# and return addresses. When the base case is reached, the stack "unwinds" and
# returns values back up the chain of calls.
# =============================================================================

print("=" * 70)
print(" DAY 17: RECURSION IN PYTHON (BASIC LEVEL)")
print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
print("=" * 70)


# =============================================================================
# 2. EXAMPLE 1: SIMPLE COUNTDOWN (UNDERSTANDING CALL FLOW)
# =============================================================================
print("\n--- 1. SIMPLE COUNTDOWN & CALL STACK UNWINDING ---")

def countdown(n):
    """
    Demonstrates basic recursion and execution order (winding vs unwinding).
    """
    # 1. Base Case
    if n <= 0:
        print("  [Base Case Reached!] Blast off! ***")
        return

    # 2. Work done before recursive call (Going Down the Stack / Winding)
    print(f"  Counting down: {n} (Entering countdown({n}))")

    # 3. Recursive Case
    countdown(n - 1)

    # 4. Work done after recursive call returns (Coming Up / Unwinding Stack)
    print(f"  Unwinding frame for n = {n}")

print("Calling countdown(3):")
countdown(3)


# =============================================================================
# 3. EXAMPLE 2: FACTORIAL OF A NUMBER (n!)
# =============================================================================
# Mathematical Definition:
# n! = n * (n - 1) * (n - 2) * ... * 1
# 0! = 1, 1! = 1
# Recursive formula: factorial(n) = n * factorial(n - 1)
# =============================================================================
print("\n--- 2. FACTORIAL OF A NUMBER ---")

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base Case: 0! = 1 and 1! = 1
    if n in (0, 1):
        return 1
    # Recursive Case: n * (n - 1)!
    return n * factorial(n - 1)

def factorial_with_trace(n, depth=0):
    """
    Calculates factorial while printing a visual trace of the call stack.
    """
    indent = "    " * depth
    print(f"{indent}-> factorial({n}) called")
    if n in (0, 1):
        print(f"{indent}<- factorial({n}) returns 1 (Base Case)")
        return 1
    
    result = n * factorial_with_trace(n - 1, depth + 1)
    print(f"{indent}<- factorial({n}) returns {n} * factorial({n-1}) = {result}")
    return result

test_n = 5
print(f"Calculating {test_n}! using basic factorial: {factorial(test_n)}")
print("\nVisual Call Stack Trace for factorial(4):")
fact_trace_result = factorial_with_trace(4)
print(f"Final Result: {fact_trace_result}")


# =============================================================================
# 4. EXAMPLE 3: SUM OF FIRST N NATURAL NUMBERS
# =============================================================================
# Formula: Sum(N) = 1 + 2 + 3 + ... + N
# Recursive formula: sum_natural(n) = n + sum_natural(n - 1)
# Base Case: sum_natural(1) = 1 or sum_natural(0) = 0
# =============================================================================
print("\n--- 3. SUM OF FIRST N NATURAL NUMBERS ---")

def sum_natural(n):
    """
    Returns the sum of natural numbers from 1 up to n.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

num = 10
print(f"Sum of first {num} natural numbers: {sum_natural(num)}")
# Formula verification: n * (n + 1) // 2
print(f"Formula check [n*(n+1)//2]: {num * (num + 1) // 2}")


# =============================================================================
# 5. EXAMPLE 4: FIBONACCI SEQUENCE (Nth FIBONACCI NUMBER)
# =============================================================================
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Definition:
# F(0) = 0
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2) for n >= 2
# =============================================================================
print("\n--- 4. FIBONACCI SEQUENCE ---")

def fibonacci(n):
    """
    Computes the n-th Fibonacci number recursively (0-indexed).
    """
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative.")
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case (multiple recursion: calls itself twice)
    return fibonacci(n - 1) + fibonacci(n - 2)

fib_count = 8
print(f"First {fib_count} Fibonacci numbers:")
fib_series = [fibonacci(i) for i in range(fib_count)]
print("Series:", fib_series)
print(f"The 7th Fibonacci number is: {fibonacci(7)}")


# =============================================================================
# 6. EXAMPLE 5: SUM OF DIGITS OF A NUMBER
# =============================================================================
# Problem: Given integer 1234, return 1 + 2 + 3 + 4 = 10.
# Logic:
# - Last digit is n % 10.
# - Remaining digits are n // 10.
# - Base Case: When n < 10, return n.
# =============================================================================
print("\n--- 5. SUM OF DIGITS ---")

def sum_of_digits(n):
    """
    Recursively sums all digits of a positive integer.
    """
    n = abs(n)  # handle negative inputs safely
    # Base Case: Single digit number
    if n < 10:
        return n
    # Recursive Case: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n // 10)

sample_number = 9876
print(f"Sum of digits of {sample_number}: {sum_of_digits(sample_number)} (9+8+7+6 = 30)")


# =============================================================================
# 7. EXAMPLE 6: POWER FUNCTION (x^n)
# =============================================================================
# Problem: Calculate base^exp recursively.
# Logic:
# - x^0 = 1 (Base Case)
# - x^n = x * x^(n - 1) (Recursive Case)
# =============================================================================
print("\n--- 6. RECURSIVE POWER FUNCTION (x^n) ---")

def power(base, exponent):
    """
    Calculates base raised to the power of exponent (non-negative exponent).
    """
    if exponent == 0:
        return 1
    if exponent < 0:
        # Negative exponent support: x^(-n) = 1 / (x^n)
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)

print(f"2^5 = {power(2, 5)}")
print(f"3^4 = {power(3, 4)}")
print(f"5^0 = {power(5, 0)}")
print(f"2^(-3) = {power(2, -3)}")


# =============================================================================
# 8. EXAMPLE 7: STRING REVERSAL & PALINDROME CHECK
# =============================================================================
# Reversing string "hello":
# - Take first char 'h' and place at the end of reverse("ello")
# - reverse("ello") + 'h'
# =============================================================================
print("\n--- 7. STRING REVERSAL & PALINDROME CHECK ---")

def reverse_string(s):
    """
    Reverses a string recursively.
    """
    # Base Case: empty string or single character string
    if len(s) <= 1:
        return s
    # Recursive Case: reverse(rest_of_string) + first_character
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    """
    Checks if a string is a palindrome using recursion.
    """
    # Clean string: lowercase and remove non-alphanumeric characters
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    
    # Base Case: empty string or 1 character is always palindrome
    if len(s) <= 1:
        return True
    
    # Check outermost characters
    if s[0] != s[-1]:
        return False
    
    # Recurse on the substring between the outer characters
    return is_palindrome(s[1:-1])

text = "Python"
print(f"Original text: '{text}' -> Reversed: '{reverse_string(text)}'")

test_words = ["racecar", "madam", "recursion", "A man a plan a canal Panama"]
for word in test_words:
    print(f"Is '{word}' a palindrome? -> {is_palindrome(word)}")


# =============================================================================
# 9. EXAMPLE 8: PYTHON'S RECURSION LIMIT & HANDLING RecursionError
# =============================================================================
# Python maintains a maximum recursion depth limit to protect memory from
# stack overflow caused by runaway or infinite recursion.
# You can check it via `sys.getrecursionlimit()`.
# =============================================================================
print("\n--- 8. RECURSION DEPTH LIMIT & SAFETY ---")

current_limit = sys.getrecursionlimit()
print(f"Current Python Recursion Limit: {current_limit} calls")

def infinite_recursion(counter=1):
    """
    A function without a base case to demonstrate RecursionError.
    """
    return infinite_recursion(counter + 1)

print("Demonstrating safe handling of infinite recursion:")
try:
    infinite_recursion()
except RecursionError as err:
    print(f"  [CAUGHT EXPECTED ERROR]: {err}")
    print("  -> Always make sure every recursive function has a reachable BASE CASE!")


# =============================================================================
# 10. RECURSION VS ITERATION (LOOPS) SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print(" RECURSION VS ITERATION (QUICK COMPARISON)")
print("=" * 70)
comparison_table = """
+--------------------+----------------------------+----------------------------+
| Feature            | Recursion                  | Iteration (Loops)          |
+--------------------+----------------------------+----------------------------+
| Definition         | Function calls itself      | Code repeats in a loop     |
| Termination        | Reaches Base Case          | Loop condition becomes False|
| Memory (Overhead)  | Uses Call Stack (O(N) aux) | Fixed memory (O(1) aux)    |
| Code Readability   | Elegant for trees/graphs   | Simpler for linear tasks   |
| Risk               | RecursionError (Stack)     | Infinite Loop (CPU hang)   |
+--------------------+----------------------------+----------------------------+
"""
print(comparison_table)

print("Day 17 - Recursion completed successfully!")
