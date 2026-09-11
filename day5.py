# =============================================================================
# DAY 5: STRINGS IN PYTHON (WHAT IS STRING, METHODS & OPERATIONS)
# Author: Harish
# Repository: Day-5-of-python
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 75)
print("       DAY 5: STRINGS IN PYTHON - BASICS, OPERATIONS & METHODS")
print("=" * 75)


# =============================================================================
# PART 1: WHAT IS A STRING?
# =============================================================================
# Definition:
# A string is a sequence of characters enclosed inside quotes.
# Characters can be letters, numbers, spaces, symbols, or punctuation.
# In Python, strings have the data type 'str'.
#
# Ways to create strings:
# 1. Single quotes   : 'Hello'
# 2. Double quotes   : "Hello"
# 3. Triple quotes   : '''Hello''' or """Hello""" (used for multi-line strings)
# =============================================================================

print("\n--- PART 1: WHAT IS A STRING? ---\n")

str1 = 'Hello, Python!'          # Single quotes
str2 = "Python is awesome!"      # Double quotes
str3 = """This is a              
multi-line string."""            # Triple quotes (preserves newlines)

print("Single quote string :", str1)
print("Double quote string :", str2)
print("Multi-line string   :\n", str3)

# Checking data type and length
sample_text = "Python Programming"
print("\nSample text        :", sample_text)
print("Data type          :", type(sample_text).__name__)
print("Length (len)       :", len(sample_text), "characters")


# =============================================================================
# PART 2: STRING IMMUTABILITY (IMPORTANT CONCEPT)
# =============================================================================
# In Python, strings are IMMUTABLE.
# "Immutable" means once a string is created, its characters CANNOT be changed
# or modified in-place.
#
# If you modify a string (e.g. using .upper() or replace()), Python creates
# a BRAND NEW string in memory instead of changing the original string.
# =============================================================================

print("\n--- PART 2: STRING IMMUTABILITY ---\n")

greeting = "Hello"
print("Original greeting:", greeting)

# Attempting greeting[0] = "J" would raise:
# TypeError: 'str' object does not support item assignment

# Creating a new string from the old one:
new_greeting = "J" + greeting[1:]
print("Modified greeting (new string):", new_greeting)
print("Original remains unchanged   :", greeting)


# =============================================================================
# PART 3: BASIC STRING OPERATIONS
# =============================================================================
# 1. Concatenation (+) : Joining two or more strings together.
# 2. Repetition    (*) : Repeating a string multiple times.
# 3. Indexing      []  : Accessing an individual character by position.
#    - Positive Indexing : starts from 0 (left to right)
#    - Negative Indexing : starts from -1 (right to left)
# 4. Slicing   [start:stop:step] : Extracting a portion/substring.
# 5. Membership (in / not in)    : Checking if substring exists in string.
# 6. Comparison (==, !=, <, >)   : Comparing strings alphabetically.
# =============================================================================

print("\n--- PART 3: BASIC STRING OPERATIONS ---\n")

# 1. Concatenation (+)
first_name = "Harish"
last_name = "Dev"
full_name = first_name + " " + last_name
print("1. Concatenation (+):")
print("   first_name + ' ' + last_name =", full_name)

# 2. Repetition (*)
line_divider = "-" * 30
echo = "Python! " * 3
print("\n2. Repetition (*):")
print("   'Python! ' * 3 =", echo)
print("   Divider line   =", line_divider)

# 3. Indexing (Positive & Negative)
# Word:   P   y   t   h   o   n
# Index:  0   1   2   3   4   5
# -Index:-6  -5  -4  -3  -2  -1
word = "Python"
print("\n3. Indexing in 'Python':")
print("   word[0]  (First character) :", word[0])
print("   word[2]  (Third character) :", word[2])
print("   word[-1] (Last character)  :", word[-1])
print("   word[-2] (Second last)     :", word[-2])

# 4. Slicing [start : stop : step]
# Note: 'stop' index is EXCLUDED (up to, but not including stop)
topic = "PythonProgramming"
print("\n4. Slicing in 'PythonProgramming':")
print("   topic[0:6]   (from 0 to 5)       :", topic[0:6])
print("   topic[6:]    (from 6 to end)     :", topic[6:])
print("   topic[:6]    (from start to 5)   :", topic[:6])
print("   topic[::2]   (every 2nd character):", topic[::2])
print("   topic[::-1]  (reverse string)    :", topic[::-1])

# 5. Membership Operators ('in' and 'not in')
sentence = "Learning Python step by step"
print("\n5. Membership Operators:")
print("   'Python' in sentence     :", "Python" in sentence)
print("   'Java' in sentence       :", "Java" in sentence)
print("   'Easy' not in sentence   :", "Easy" not in sentence)

# 6. String Comparisons
print("\n6. String Comparisons:")
print("   'apple' == 'apple' :", "apple" == "apple")
print("   'apple' < 'banana' :", "apple" < "banana", "(Alphabetical order)")


# =============================================================================
# PART 4: COMMON & ESSENTIAL STRING METHODS
# =============================================================================
# Methods are built-in functions that belong to string objects.
# They are called using dot notation: string.method()
#
# Categories covered:
# A. Case Conversion Methods
# B. Whitespace & Trimming Methods
# C. Searching & Counting Methods
# D. Replacement, Splitting & Joining Methods
# E. Character Inspection / Validation Methods
# =============================================================================

print("\n--- PART 4: ESSENTIAL STRING METHODS ---\n")

# A. Case Conversion
text = "hello World of PYTHON"
print("A. Case Conversion Methods:")
print("   Original text :", text)
print("   .upper()      :", text.upper())
print("   .lower()      :", text.lower())
print("   .title()      :", text.title())
print("   .capitalize() :", text.capitalize())
print("   .swapcase()   :", text.swapcase())

# B. Whitespace & Trimming
padded = "   Python Developer   "
print("\nB. Trimming / Stripping Methods:")
print(f"   Original padded : '{padded}'")
print(f"   .strip()        : '{padded.strip()}' (removes both sides)")
print(f"   .lstrip()       : '{padded.lstrip()}' (removes left side)")
print(f"   .rstrip()       : '{padded.rstrip()}' (removes right side)")

# C. Searching & Counting
phrase = "Keep coding, keep building, keep learning"
print("\nC. Searching and Counting:")
print("   Phrase            :", phrase)
print("   .count('keep')    :", phrase.count("keep"), "(Case sensitive)")
print("   .count('Keep')    :", phrase.count("Keep"))
print("   .find('coding')   : Index", phrase.find("coding"))
print("   .find('Java')     : Index", phrase.find("Java"), "(-1 means not found)")
print("   .startswith('Keep'):", phrase.startswith("Keep"))
print("   .endswith('learning'):", phrase.endswith("learning"))

# D. Replacing, Splitting, and Joining
languages_csv = "Python,JavaScript,C++,Go,Rust"
print("\nD. Replacing, Splitting & Joining:")

# Replace
messy_note = "I like apples and apples"
fixed_note = messy_note.replace("apples", "oranges")
print("   .replace()  :", fixed_note)

# Split (converts string to a list of items)
lang_list = languages_csv.split(",")
print("   .split(',') :", lang_list)

# Join (joins list items into a single string)
joined_with_hyphen = " - ".join(lang_list)
print("   ' - '.join():", joined_with_hyphen)

# E. Inspection & Validation Methods (returns True/False)
val1 = "Python"
val2 = "12345"
val3 = "Python3"
val4 = "   "

print("\nE. String Validation / Inspection Methods:")
print(f"   '{val1}'.isalpha() : {val1.isalpha()} (Only letters)")
print(f"   '{val2}'.isdigit() : {val2.isdigit()} (Only numbers)")
print(f"   '{val3}'.isalnum() : {val3.isalnum()} (Letters and numbers)")
print(f"   '{val4}'.isspace() : {val4.isspace()} (Only whitespace)")


# =============================================================================
# PART 5: STRING FORMATTING (HOW TO INSERT VARIABLES INTO STRINGS)
# =============================================================================
# 1. f-strings (Formatted String Literals) - Recommended & Modern (Python 3.6+)
# 2. str.format() method
# 3. % operator (Old school style)
# =============================================================================

print("\n--- PART 5: STRING FORMATTING ---\n")

user_name = "Harish"
current_day = 5
topic_name = "Strings"
score_percentage = 98.756

# 1. f-strings (Fast, clean, most readable)
msg_fstring = f"Hello {user_name}! Welcome to Day {current_day}: {topic_name}. Score: {score_percentage:.2f}%"
print("1. f-string format :", msg_fstring)

# 2. .format() method
msg_format = "Hello {}! Welcome to Day {}: {}.".format(user_name, current_day, topic_name)
print("2. .format() method:", msg_format)

# 3. Escape Sequences
# \n = new line, \t = tab space, \\ = backslash, \' or \" = quotes
print("\n3. Escape Sequences Demo:")
print("   Line 1\n   Line 2 (after \\n)")
print("   Item 1\tItem 2\tItem 3 (using \\t)")
print("   He said, \"Python is great!\" (escaped quotes)")


# =============================================================================
# PART 6: PRACTICAL BEGINNER EXERCISES
# =============================================================================
# Mini-Exercise 1: Username & Domain Extractor from Email
# Mini-Exercise 2: Palindrome Checker (reads same forwards and backwards)
# Mini-Exercise 3: Clean & Capitalize User Input
# =============================================================================

print("\n--- PART 6: PRACTICAL MINI-EXERCISES ---\n")

# Exercise 1: Extract username and domain
email = "harish.developer@example.com"
username, domain = email.split("@")
print("Exercise 1: Email Breakdown")
print(f"   Full Email : {email}")
print(f"   Username   : {username}")
print(f"   Domain     : {domain}")

# Exercise 2: Palindrome Checker
test_word = "radar"
clean_word = test_word.lower()
is_palindrome = clean_word == clean_word[::-1]
print(f"\nExercise 2: Palindrome Check for '{test_word}'")
print(f"   Reversed   : '{clean_word[::-1]}'")
print(f"   Palindrome : {is_palindrome}")

# Exercise 3: User Input Cleaner
raw_input_name = "   hArIsH   "
cleaned_name = raw_input_name.strip().capitalize()
print("\nExercise 3: Clean User Input")
print(f"   Raw Input     : '{raw_input_name}'")
print(f"   Cleaned Name  : '{cleaned_name}'")

# =============================================================================
# SUMMARY & WRAP-UP
# =============================================================================
print("\n" + "=" * 75)
print("DAY 5 COMPLETED SUCCESSFULLY!")
print("Key Takeaways:")
print("1. Strings are sequences of characters enclosed in quotes (str).")
print("2. Strings are immutable - operations return new strings.")
print("3. Operations: Concatenation (+), Repetition (*), Indexing [i], Slicing [::].")
print("4. Methods: .upper(), .lower(), .strip(), .replace(), .split(), .join(), etc.")
print("5. Formatting: Use modern f-strings for clean variable embedding.")
print("=" * 75)
