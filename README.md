# Day 17: Recursion in Python (Basic Level) 🔄⚡

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-17-OF-PYTHON](https://github.com/harish-0987/DAY-17-OF-PYTHON)

Welcome to **Day 17 of Python**! Today we dive into **Recursion**—one of the foundational programming concepts where a function solves complex problems by breaking them down into smaller instances of themselves.

---

## 📌 Table of Contents
1. [What is Recursion?](#1-what-is-recursion)
2. [The Anatomy of a Recursive Function](#2-the-anatomy-of-a-recursive-function)
3. [Understanding the Call Stack & Unwinding](#3-understanding-the-call-stack--unwinding)
4. [Code Examples & Walkthrough](#4-code-examples--walkthrough)
   - [Example 1: Countdown & Stack Order](#example-1-countdown--stack-order)
   - [Example 2: Factorial of a Number (n!)](#example-2-factorial-of-a-number-n)
   - [Example 3: Sum of First N Natural Numbers](#example-3-sum-of-first-n-natural-numbers)
   - [Example 4: Fibonacci Sequence](#example-4-fibonacci-sequence)
   - [Example 5: Sum of Digits](#example-5-sum-of-digits)
   - [Example 6: Power Function (x^n)](#example-6-power-function-xn)
   - [Example 7: String Reversal & Palindrome Check](#example-7-string-reversal--palindrome-check)
   - [Example 8: Recursion Limit & Handling RecursionError](#example-8-recursion-limit--handling-recursionerror)
5. [Recursion vs Iteration (Loops)](#5-recursion-vs-iteration-loops)
6. [Best Practices for Writing Recursive Functions](#6-best-practices-for-writing-recursive-functions)
7. [How to Run](#7-how-to-run)
8. [Summary & Key Takeaways](#8-summary--key-takeaways)

---

## 1. What is Recursion?

**Recursion** is a technique in programming where a function calls itself to solve a smaller instance of the same problem until it reaches a designated stopping point.

Instead of writing repetitive loops, recursion allows us to express mathematical equations and structural data patterns directly in code.

---

## 2. The Anatomy of a Recursive Function

Every valid recursive function consists of two crucial parts:

1. **Base Case (Stopping Condition)**:
   - The condition under which the function terminates and returns a direct answer without calling itself again.
   - *Without a base case, recursion runs infinitely until memory is exhausted.*
2. **Recursive Case**:
   - The block of code where the function breaks the input down and calls itself with a simpler or smaller argument, moving closer to the base case.

```python
def recursive_pattern(n):
    # 1. Base Case
    if n <= 0:
        return 0

    # 2. Recursive Case
    return n + recursive_pattern(n - 1)
```

---

## 3. Understanding the Call Stack & Unwinding

When a function calls itself, Python places a new **stack frame** onto the Call Stack in memory.

### Visualizing `factorial(4)`:

```
[Phase 1: Winding / Pushing onto Call Stack]
factorial(4) calls 4 * factorial(3)
    factorial(3) calls 3 * factorial(2)
        factorial(2) calls 2 * factorial(1)
            factorial(1) -> BASE CASE REACHED (returns 1)

[Phase 2: Unwinding / Popping off Call Stack]
            factorial(1) returns 1
        factorial(2) returns 2 * 1 = 2
    factorial(3) returns 3 * 2 = 6
factorial(4) returns 4 * 6 = 24
```

---

## 4. Code Examples & Walkthrough

### Example 1: Countdown & Stack Order
Demonstrates how code executes before the recursive call (winding) versus after it returns (unwinding).

```python
def countdown(n):
    if n <= 0:
        print("  [Base Case] Blast off!")
        return
    print(f"  Entering countdown({n})")
    countdown(n - 1)
    print(f"  Unwinding frame for n = {n}")
```

---

### Example 2: Factorial of a Number ($n!$)
Mathematical definition: $n! = n \times (n-1)!$ with $0! = 1$ and $1! = 1$.

```python
def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
```

---

### Example 3: Sum of First N Natural Numbers
Sum of numbers from $1$ to $N$: $\text{sum}(N) = N + \text{sum}(N - 1)$.

```python
def sum_natural(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + sum_natural(n - 1)
```

---

### Example 4: Fibonacci Sequence
$F(0) = 0$, $F(1) = 1$, $F(n) = F(n-1) + F(n-2)$. Demonstrates branching (multiple) recursion.

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

### Example 5: Sum of Digits
Extracts the last digit using `% 10` and recursively sums the quotient `// 10`.

```python
def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)
```

---

### Example 6: Power Function ($x^n$)
Calculates $base^{exponent}$ recursively, supporting negative powers as well.

```python
def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)
```

---

### Example 7: String Reversal & Palindrome Check
Reverses characters by placing the first character at the end of the reversed substring. Checks palindromes by matching outer characters.

```python
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

---

### Example 8: Recursion Limit & Handling `RecursionError`
Python prevents stack overflow crashes by capping the maximum recursion depth (default is typically 1000).

```python
import sys

print("Recursion limit:", sys.getrecursionlimit())

try:
    def infinite(n=1):
        return infinite(n + 1)
    infinite()
except RecursionError as err:
    print("Caught expected recursion error:", err)
```

---

## 5. Recursion vs Iteration (Loops)

| Feature | Recursion | Iteration (Loops) |
| :--- | :--- | :--- |
| **Mechanism** | Function calls itself repeatedly | Repeated block execution (`for`/`while`) |
| **Termination** | When Base Case is satisfied | When loop condition becomes `False` |
| **Memory Usage** | High overhead ($O(N)$ stack frames) | Low overhead ($O(1)$ auxiliary memory) |
| **Execution Speed** | Slower (function call overhead) | Faster |
| **Best Used For** | Trees, graphs, divide-and-conquer, backtracking | Simple sequences, arrays, counters |
| **Failure Mode** | `RecursionError` (Stack overflow) | Infinite loop (CPU hang) |

---

## 6. Best Practices for Writing Recursive Functions

1. **Always Define the Base Case First**: Before writing any logic, define when the function must stop.
2. **Ensure Convergence**: Ensure each recursive step strictly moves the parameter closer to the base case (e.g., `n - 1`, `s[1:]`, `n // 10`).
3. **Guard Against Invalid Inputs**: Handle negative numbers or unexpected types with sanity checks.
4. **Be Mindful of Call Stack Depth**: For iterations exceeding 1,000 steps, consider an iterative approach or dynamic programming / memoization.

---

## 7. How to Run

Clone the repository and run the script:

```bash
# Clone the repository
git clone https://github.com/harish-0987/DAY-17-OF-PYTHON.git

# Navigate into the project directory
cd DAY-17-OF-PYTHON

# Run the script
python day17.py
```

---

## 8. Summary & Key Takeaways

- **Recursion** breaks problems into identical smaller subproblems.
- A **Base Case** is non-negotiable to prevent infinite recursion.
- Each call consumes memory on the **Call Stack** until the base case begins unwinding.
- Recursion offers clean, elegant code for naturally hierarchical problems like tree traversals, parsing, and divide-and-conquer algorithms.

---

⭐ **Star this repository** if you find this helpful on your Python learning journey!
