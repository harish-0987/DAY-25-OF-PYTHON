# =============================================================================
# DAY 18: MODULES AND THEIR TYPES IN PYTHON (BASIC LEVEL)
# Author: Harish
# Repository: DAY-18-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# 1. WHAT IS A MODULE?
# =============================================================================
# In Python, a MODULE is simply a file containing Python definitions, functions,
# classes, and runnable code with a `.py` extension.
#
# Think of a module like a toolbox: instead of building all your tools from
# scratch every time you write a script, you can organize related tools into a
# module and "import" them whenever and wherever you need them.
#
# Key Benefits of Modules:
# 1. Code Reusability: Write code once in a module and use it across multiple projects.
# 2. Maintainability: Breaking large codebases into smaller files makes code easier to read and debug.
# 3. Namespace Management: Prevents naming conflicts between different functions and variables.
# =============================================================================

# =============================================================================
# 2. TYPES OF MODULES IN PYTHON
# =============================================================================
# Python modules are categorized into THREE primary types:
#
# 1. BUILT-IN MODULES:
#    - Pre-installed with Python out-of-the-box (Python Standard Library).
#    - Do NOT require installation via pip.
#    - Examples: `math`, `random`, `datetime`, `sys`, `os`, `platform`, `json`.
#
# 2. USER-DEFINED MODULES:
#    - Custom `.py` files created by developers to organize their own code.
#    - You create a file (e.g., `my_custom_module.py`) and import it into another file.
#
# 3. THIRD-PARTY / EXTERNAL MODULES:
#    - Created by the open-source community and hosted on PyPI (Python Package Index).
#    - Installed using Python's package installer: `pip install <package_name>`.
#    - Examples: `requests` (HTTP requests), `numpy` (math/arrays), `pandas` (data analysis).
# =============================================================================

# =============================================================================
# 3. DIFFERENT WAYS TO IMPORT MODULES
# =============================================================================
# A. Standard Import:
#    import math
#    -> Accessed via module name: math.sqrt(25)
#
# B. Import with an Alias (Renaming using 'as'):
#    import datetime as dt
#    -> Accessed using shorter alias: dt.datetime.now()
#
# C. Import Specific Attributes / Functions:
#    from math import pi, pow
#    -> Directly used without module prefix: pow(2, 3)
#
# D. Import Everything (Wildcard import - NOT RECOMMENDED):
#    from random import *
#    -> Pollutes current namespace and can cause accidental name collisions.
# =============================================================================

# Standard library imports (PEP 8 recommends placing imports at top)
import math
import random
import datetime as dt
import sys
import platform

# User-defined module import (created in our workspace)
import my_custom_module as custom


def print_section(title: str):
    """Utility function to print visually formatted section headers."""
    print("\n" + "=" * 75)
    print(f"  {title}")
    print("=" * 75)


def main():
    print("=" * 75)
    print(" DAY 18: MODULES AND THEIR TYPES IN PYTHON (BASIC LEVEL)")
    print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
    print("=" * 75)

    # -------------------------------------------------------------------------
    # PART 1: BUILT-IN MODULES DEMONSTRATION
    # -------------------------------------------------------------------------
    print_section("TYPE 1: BUILT-IN MODULES (PYTHON STANDARD LIBRARY)")

    # 1.1 The 'math' Module
    print("[1.1] Using the 'math' Built-in Module:")
    number = 64
    print(f"  - math.sqrt({number})      : {math.sqrt(number)}")
    print(f"  - math.pow(2, 5)          : {math.pow(2, 5)}")
    print(f"  - math.pi                 : {math.pi}")
    print(f"  - math.ceil(7.2)          : {math.ceil(7.2)} (rounds UP)")
    print(f"  - math.floor(7.8)         : {math.floor(7.8)} (rounds DOWN)")
    print(f"  - math.factorial(5)       : {math.factorial(5)} (5 * 4 * 3 * 2 * 1)")

    # 1.2 The 'random' Module
    print("\n[1.2] Using the 'random' Built-in Module:")
    random_int = random.randint(1, 100)
    print(f"  - random.randint(1, 100)  : {random_int}")

    fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
    selected_fruit = random.choice(fruits)
    print(f"  - random.choice({fruits}) : {selected_fruit}")

    random_float = round(random.random(), 4)
    print(f"  - random.random() [0.0-1.0): {random_float}")

    sample_cards = ["Ace", "King", "Queen", "Jack"]
    random.shuffle(sample_cards)
    print(f"  - random.shuffle(cards)   : {sample_cards}")

    # 1.3 The 'datetime' Module (imported as 'dt')
    print("\n[1.3] Using the 'datetime' Built-in Module (with alias 'dt'):")
    current_timestamp = dt.datetime.now()
    formatted_date = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    today_date = dt.date.today()
    print(f"  - dt.date.today()         : {today_date}")
    print(f"  - dt.datetime.now() raw   : {current_timestamp}")
    print(f"  - Formatted Timestamp     : {formatted_date}")

    # 1.4 The 'platform' and 'sys' Modules
    print("\n[1.4] System Introspection with 'platform' and 'sys':")
    print(f"  - Operating System        : {platform.system()} ({platform.release()})")
    print(f"  - Python Version          : {platform.python_version()}")
    print(f"  - Python Executable Path  : {sys.executable}")

    # -------------------------------------------------------------------------
    # PART 2: USER-DEFINED MODULES DEMONSTRATION
    # -------------------------------------------------------------------------
    print_section("TYPE 2: USER-DEFINED MODULES (CUSTOM FILES)")

    print("[2.1] What is a User-Defined Module?")
    print("  Any Python file created by you (e.g., 'my_custom_module.py') can be")
    print("  imported into another script using standard import syntax.")

    print("\n[2.2] Accessing Variables and Functions from 'my_custom_module':")
    print(f"  - Module Name Variable    : {custom.MODULE_NAME}")
    print(f"  - Module Version Variable : {custom.VERSION}")
    print(f"  - custom.greet_user('Harish') : {custom.greet_user('Harish')}")
    print(f"  - custom.add_numbers(15, 27)  : {custom.add_numbers(15, 27)}")
    print(f"  - custom.multiply_numbers(6, 8): {custom.multiply_numbers(6, 8)}")
    print(f"  - custom.get_circle_area(7)   : {custom.get_circle_area(7):.2f}")

    print("\n[2.3] Understanding `__name__` and `if __name__ == '__main__':`:")
    print("  - When a file is run directly: `__name__` is set to '__main__'.")
    print("  - When imported as a module:   `__name__` is set to the module's file name.")
    print(f"  - Current script's __name__   : '{__name__}' (running directly)")
    print(f"  - Imported custom module's __name__ : '{custom.__name__}'")

    # -------------------------------------------------------------------------
    # PART 3: THIRD-PARTY / EXTERNAL MODULES DEMONSTRATION
    # -------------------------------------------------------------------------
    print_section("TYPE 3: THIRD-PARTY / EXTERNAL MODULES (PyPI & pip)")

    print("[3.1] What are Third-Party Modules?")
    print("  Modules developed by the Python community that do not ship with Python.")
    print("  They are installed into your Python environment using the 'pip' command:")
    print("    > pip install requests")
    print("    > pip install numpy")
    print("    > pip install colorama")

    print("\n[3.2] Safe Import Handling (Graceful Fallback):")
    try:
        # Attempt to import an external module if installed
        import requests  # type: ignore
        print("  [SUCCESS] 'requests' module is installed and available!")
        print(f"  - Requests version: {requests.__version__}")
    except ImportError:
        print("  [INFO] Third-party module 'requests' is not installed in this environment.")
        print("  To install it, open terminal and run:")
        print("      pip install requests")
        print("  Here is how you would use it once installed:")
        print("      import requests")
        print("      response = requests.get('https://api.github.com')")
        print("      print(response.status_code) # 200")

    # -------------------------------------------------------------------------
    # PART 4: INTROSPECTION & MODULE UTILITIES
    # -------------------------------------------------------------------------
    print_section("USEFUL BUILT-IN FUNCTIONS FOR MODULES")

    # 4.1 dir() function
    print("[4.1] The `dir()` Function:")
    print("  Returns a list of all valid attributes and functions in a module.")
    math_attrs = [attr for attr in dir(math) if not attr.startswith("__")][:8]
    print(f"  - First 8 attributes in math module: {math_attrs}")

    custom_attrs = [attr for attr in dir(custom) if not attr.startswith("__")]
    print(f"  - Attributes in my_custom_module   : {custom_attrs}")

    # 4.2 Module search path (sys.path)
    print("\n[4.2] Where does Python look for modules? (`sys.path`):")
    print("  When you type 'import <name>', Python searches these locations in order:")
    print("  1. The current working directory (where the script was launched).")
    print("  2. Standard library directories.")
    print("  3. Site-packages directory (where third-party pip packages are installed).")
    print(f"  - First search directory in sys.path: {sys.path[0]}")

    # -------------------------------------------------------------------------
    # SUMMARY & BEST PRACTICES
    # -------------------------------------------------------------------------
    print_section("KEY TAKEAWAYS & BEST PRACTICES (PEP 8)")
    print("1. Structure: Place all imports at the very top of your file.")
    print("2. Grouping: Follow PEP 8 import grouping order:")
    print("      Group 1: Standard library imports (e.g., math, sys)")
    print("      Group 2: Related third-party imports (e.g., requests, numpy)")
    print("      Group 3: Local application / custom imports (e.g., my_custom_module)")
    print("3. Readability: Avoid `from module import *`. Be explicit about what you import.")
    print("4. File Naming: Always use lowercase letters with underscores for module names.")
    print("   Never name your file after a built-in module (e.g., don't name your file `math.py`!).")
    print("=" * 75)
    print(" DAY 18 COMPLETE: MODULES MASTERED!")
    print("=" * 75)


if __name__ == "__main__":
    main()
