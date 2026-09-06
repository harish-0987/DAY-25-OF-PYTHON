"""
=============================================================================
DAY 1: WHAT IS PYTHON?
Author: Harish (github.com/harish-0987)
Repository: DAY-1-OF-PYTHON-
=============================================================================

Motto:
    "Not here to be known, here to build."
"""

import sys
import platform


def banner():
    print("=" * 65)
    print("           DAY 1: WHAT IS PYTHON? - INTRODUCTION            ")
    print("=" * 65)
    message1 = "Not here to be known"
    message2 = "Here to build"
    print(f"Motto: '{message1}, {message2}'\n")


def what_is_python():
    """Explains what Python is, its history, and core characteristics."""
    print("-------------------------------------------------------------")
    print("1. WHAT IS PYTHON?")
    print("-------------------------------------------------------------")
    definition = """
    Python is a popular, high-level, interpreted, and general-purpose
    programming language created by Guido van Rossum and first released
    in 1991.

    It is designed with an emphasis on code readability, allowing
    programmers to express concepts in fewer lines of code compared
    to languages like C++ or Java.
    """
    print(definition.strip())
    print("\nCurrent Environment Details:")
    print(f"  - Python Version : {platform.python_version()}")
    print(f"  - Implementation  : {platform.python_implementation()}")
    print(f"  - OS Platform     : {platform.system()} {platform.release()}\n")


def key_features():
    """Details key features of Python with code examples."""
    print("-------------------------------------------------------------")
    print("2. KEY FEATURES OF PYTHON")
    print("-------------------------------------------------------------")
    features = [
        ("1. Simple & Readable", "Clean syntax that reads like natural English."),
        ("2. Interpreted Language", "Executed line-by-line; no explicit compilation step needed."),
        ("3. Dynamically Typed", "No need to declare variable types explicitly."),
        ("4. High-Level Language", "Automatic memory management and garbage collection."),
        ("5. Multi-Paradigm", "Supports Object-Oriented, Functional, and Procedural programming."),
        ("6. Cross-Platform", "Runs seamlessly on Windows, macOS, Linux, etc."),
        ("7. Vast Standard Library", "Batteries-included philosophy for math, web, data, and AI.")
    ]
    for title, desc in features:
        print(f"  * {title:<25} : {desc}")
    print()


def how_python_works():
    """Explains Python's execution model (Source Code -> Bytecode -> PVM)."""
    print("-------------------------------------------------------------")
    print("3. HOW DOES PYTHON WORK?")
    print("-------------------------------------------------------------")
    flow = """
    [Source Code: .py]
           |
           v  (Python Compiler parses syntax)
    [Bytecode: .pyc]
           |
           v  (Python Virtual Machine executes instructions)
    [Machine Code / Output]
    """
    print(flow)
    print("Python compiles source code to intermediate bytecode, which")
    print("is then executed by the Python Virtual Machine (PVM).\n")


def live_demo():
    """Demonstrates dynamic typing, clean syntax, and operations."""
    print("-------------------------------------------------------------")
    print("4. PYTHON IN ACTION (LIVE DEMONSTRATIONS)")
    print("-------------------------------------------------------------")

    # 1. Simple Hello World
    print(">> Simple Output:")
    greeting = "Hello, World! Welcome to Python Day 1."
    print(f"   {greeting}")

    # 2. Dynamic Typing Demo
    print("\n>> Dynamic Typing in Python:")
    variable = 100
    print(f"   variable = {variable} (Type: {type(variable).__name__})")
    variable = "Now I am a string!"
    print(f"   variable = '{variable}' (Type: {type(variable).__name__})")
    variable = [1, 2, 3]
    print(f"   variable = {variable} (Type: {type(variable).__name__})")

    # 3. Simple Math & Clean Syntax
    print("\n>> Elegant Math Operations:")
    a, b = 25, 4
    print(f"   {a} + {b} = {a + b}")
    print(f"   {a} * {b} = {a * b}")
    print(f"   {a} / {b} = {a / b}")
    print(f"   {a} ** {b} = {a ** b} (Power: {a} raised to {b})")

    # 4. Multi-assignment
    name, role, day = "Harish", "Python Learner & Developer", 1
    print("\n>> Multiple Assignments in One Line:")
    print(f"   Student : {name}")
    print(f"   Role    : {role}")
    print(f"   Day     : {day}\n")


def applications_of_python():
    """Overview of major application domains of Python."""
    print("-------------------------------------------------------------")
    print("5. WHERE IS PYTHON USED?")
    print("-------------------------------------------------------------")
    domains = {
        "Web Development": "Django, Flask, FastAPI",
        "Data Science & AI": "Pandas, NumPy, TensorFlow, PyTorch",
        "Automation & Scripting": "Automating repetitive daily tasks and workflows",
        "Software Development": "Desktop GUIs, CLI applications, utilities",
        "Cloud & DevOps": "AWS, Docker automation, Infrastructure tooling"
    }
    for field, tech in domains.items():
        print(f"  - {field:<24} : {tech}")
    print()


def main():
    banner()
    what_is_python()
    key_features()
    how_python_works()
    live_demo()
    applications_of_python()
    print("=" * 65)
    print("             DAY 1: WHAT IS PYTHON COMPLETE!                 ")
    print("=" * 65)


if __name__ == "__main__":
    main()
