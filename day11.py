# =============================================================================
# DAY 11: CONDITIONAL STATEMENTS IN PYTHON
# Author: Harish
# Repository: DAY-11-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("     DAY 11: PYTHON CONDITIONAL STATEMENTS - CONCEPTS & CODE EXAMPLES")
print("=" * 70)


# =============================================================================
# PART 1: WHAT IS A CONDITIONAL STATEMENT?
# =============================================================================
# Definition:
# A conditional statement (or decision-making statement) allows a program to
# execute different blocks of code based on whether a condition evaluates
# to True or False.
#
# Control Flow:
# In standard execution, Python executes code sequentially (line by line).
# Conditional statements introduce branching:
#                   [ Evaluate Condition ]
#                          /       \
#                    (True)         (False)
#                     /                 \
#        [ Execute True Block ]     [ Execute False Block / Skip ]
#                     \                 /
#                      [ Continue Code ]
#
# Python Truthy & Falsy Values:
# In Python, conditions evaluate to a boolean (True / False).
# Falsy values include: False, 0, 0.0, "", [], (), {}, set(), None.
# Everything else evaluates to Truthy!
# =============================================================================

print("\n--- PART 1: WHAT IS A CONDITIONAL STATEMENT? ---\n")

is_raining = True
if is_raining:
    print("Action: Take an umbrella! (Condition is True)")

# Truthy / Falsy demonstration
falsy_values = [0, "", [], None, False]
print("\nDemonstrating Falsy values:")
for val in falsy_values:
    if not val:
        print(f"Value {repr(val)} is evaluated as False in conditions.")


# =============================================================================
# PART 2: OPERATORS USED IN CONDITIONS
# =============================================================================
# 1. Comparison Operators:
#    == (Equal to)             != (Not equal to)
#    >  (Greater than)          <  (Less than)
#    >= (Greater than or equal) <= (Less than or equal)
#
# 2. Logical Operators:
#    and (True if both conditions are True)
#    or  (True if at least one condition is True)
#    not (Reverses the boolean value)
#
# 3. Membership & Identity Operators:
#    in / not in (Checks presence in a collection)
#    is / is not (Checks object identity / memory reference)
# =============================================================================

print("\n--- PART 2: OPERATORS IN CONDITIONS ---\n")

score = 85
attendance = 92

# Using comparison and logical operators
if score >= 80 and attendance >= 90:
    print(f"Eligible for Honors Diploma: Score={score}, Attendance={attendance}%")

# Using membership operator
allowed_roles = ["admin", "editor", "moderator"]
current_user_role = "editor"

if current_user_role in allowed_roles:
    print(f"Access granted for role: '{current_user_role}'")


# =============================================================================
# PART 3: THE 'if' STATEMENT (SINGLE DECISION)
# =============================================================================
# Syntax:
#   if condition:
#       # indented block executed ONLY if condition is True
# =============================================================================

print("\n--- PART 3: THE 'if' STATEMENT ---\n")

# Example 1: Check positive number
number = 15
if number > 0:
    print(f"{number} is a positive number.")

# Example 2: Voting eligibility check
age = 20
if age >= 18:
    print(f"Age {age}: You are eligible to vote!")


# =============================================================================
# PART 4: THE 'if...else' STATEMENT (TWO-WAY DECISION)
# =============================================================================
# Syntax:
#   if condition:
#       # runs when condition is True
#   else:
#       # runs when condition is False
# =============================================================================

print("\n--- PART 4: THE 'if...else' STATEMENT ---\n")

# Example 1: Even or Odd number checker
num_to_check = 27
if num_to_check % 2 == 0:
    print(f"{num_to_check} is an EVEN number.")
else:
    print(f"{num_to_check} is an ODD number.")

# Example 2: Pass or Fail exam result
marks = 64
passing_marks = 40

if marks >= passing_marks:
    print(f"Result: PASS (Scored {marks}/{100})")
else:
    print(f"Result: FAIL (Scored {marks}/{100})")

# Example 3: User authentication mock
input_password = "secure_password"
stored_password = "secure_password"

if input_password == stored_password:
    print("Authentication successful: Welcome back!")
else:
    print("Authentication failed: Incorrect password.")


# =============================================================================
# PART 5: THE 'if...elif...else' LADDER (MULTI-WAY DECISION)
# =============================================================================
# Syntax:
#   if condition1:
#       # runs if condition1 is True
#   elif condition2:
#       # runs if condition1 is False and condition2 is True
#   elif condition3:
#       # runs if previous conditions are False and condition3 is True
#   else:
#       # runs if none of the above conditions are True
# =============================================================================

print("\n--- PART 5: THE 'if...elif...else' LADDER ---\n")

# Example 1: Student Grade System
student_score = 88

if student_score >= 90:
    grade = "A+ (Outstanding)"
elif student_score >= 80:
    grade = "A (Excellent)"
elif student_score >= 70:
    grade = "B (Very Good)"
elif student_score >= 60:
    grade = "C (Good)"
elif student_score >= 50:
    grade = "D (Satisfactory)"
else:
    grade = "F (Fail)"

print(f"Score: {student_score} -> Grade: {grade}")

# Example 2: Traffic Light Simulator
signal_color = "yellow"

if signal_color == "red":
    action = "STOP! Do not cross."
elif signal_color == "yellow":
    action = "SLOW DOWN and prepare to stop."
elif signal_color == "green":
    action = "GO! Road is clear."
else:
    action = "Invalid signal color."

print(f"Traffic Signal [{signal_color.upper()}]: {action}")

# Example 3: Categorizing Age Groups
person_age = 22

if person_age < 0:
    category = "Invalid age"
elif person_age <= 12:
    category = "Child"
elif person_age <= 19:
    category = "Teenager"
elif person_age <= 59:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Age {person_age} is categorized as: {category}")


# =============================================================================
# PART 6: NESTED 'if' STATEMENTS
# =============================================================================
# Definition:
# A conditional statement placed inside the body of another conditional statement.
#
# Syntax:
#   if condition1:
#       if condition2:
#           # runs if both condition1 and condition2 are True
#       else:
#           # runs if condition1 is True but condition2 is False
#   else:
#       # runs if condition1 is False
# =============================================================================

print("\n--- PART 6: NESTED 'if' STATEMENTS ---\n")

# Example 1: ATM Withdrawal validation
account_balance = 5000
withdrawal_amount = 2000
pin_entered = 1234
correct_pin = 1234

if pin_entered == correct_pin:
    print("PIN Verified successfully.")
    if withdrawal_amount <= account_balance:
        account_balance -= withdrawal_amount
        print(f"Withdrawal of Rs.{withdrawal_amount} successful!")
        print(f"Remaining balance: Rs.{account_balance}")
    else:
        print(f"Error: Insufficient balance. Available: Rs.{account_balance}")
else:
    print("Error: Incorrect PIN. Transaction cancelled.")

# Example 2: Blood Donation Eligibility
# Requirements: Age >= 18, Weight >= 50kg
donor_age = 21
donor_weight = 55

if donor_age >= 18:
    if donor_weight >= 50:
        print("Eligible to donate blood! Thank you for saving lives.")
    else:
        print("Not eligible: Weight must be at least 50 kg.")
else:
    print("Not eligible: Donor must be at least 18 years old.")


# =============================================================================
# PART 7: SHORT-HAND IF & TERNARY OPERATOR
# =============================================================================
# 1. Short-hand if:
#    if condition: statement
#
# 2. Ternary Operator (Conditional Expression):
#    value_if_true if condition else value_if_false
# =============================================================================

print("\n--- PART 7: SHORT-HAND & TERNARY OPERATOR ---\n")

# 1. One-line if
temperature = 32
if temperature > 30: print("It's a hot day! (Short-hand if)")

# 2. Ternary Operator
a, b = 25, 40
larger = a if a > b else b
print(f"Larger between {a} and {b} is: {larger}")

# 3. Inline status assignment
status_code = 200
status_message = "OK / Success" if status_code == 200 else "Error or Other"
print(f"Status {status_code}: {status_message}")


# =============================================================================
# PART 8: MATCH...CASE STATEMENT (PYTHON 3.10+ PATTERN MATCHING)
# =============================================================================
# Python 3.10 introduced structural pattern matching via 'match...case'.
# It is a clean, modern alternative to long if-elif-else chains.
#
# Syntax:
#   match variable:
#       case pattern1:
#           # code
#       case pattern2:
#           # code
#       case _:
#           # default fallback (wildcard)
# =============================================================================

print("\n--- PART 8: MATCH...CASE STATEMENT ---\n")

def get_http_status_message(status_code: int) -> str:
    match status_code:
        case 200:
            return "200 OK: Request succeeded."
        case 201:
            return "201 Created: Resource successfully created."
        case 400:
            return "400 Bad Request: Invalid client syntax."
        case 401:
            return "401 Unauthorized: Authentication required."
        case 404:
            return "404 Not Found: Resource not found."
        case 500:
            return "500 Internal Server Error: Server encountered an error."
        case _:
            return f"{status_code} Unknown Status Code."

print(get_http_status_message(200))
print(get_http_status_message(404))
print(get_http_status_message(500))

# Day of Week using match...case with OR patterns (|)
day_number = 6
match day_number:
    case 1 | 2 | 3 | 4 | 5:
        day_type = "Weekday (Time to code and build!)"
    case 6 | 7:
        day_type = "Weekend (Time to learn and recharge!)"
    case _:
        day_type = "Invalid day number."

print(f"Day {day_number} is: {day_type}")


# =============================================================================
# PART 9: HANDS-ON PRACTICAL MINI-PROJECTS
# =============================================================================

print("\n--- PART 9: HANDS-ON MINI-PROJECTS ---\n")

# Mini-Project 1: Leap Year Checker
# Rules: Divisible by 4, but NOT 100 unless also divisible by 400
print("[Mini-Project 1: Leap Year Checker]")
test_years = [2000, 2024, 2025, 1900]

for year in test_years:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"  -> Year {year}: LEAP YEAR (366 days)")
    else:
        print(f"  -> Year {year}: COMMON YEAR (365 days)")

print()

# Mini-Project 2: Simple Arithmetic Calculator
print("[Mini-Project 2: Simple Calculator]")
def calculate(num1: float, num2: float, op: str):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2 if num2 != 0 else "Error: Division by zero!"
    elif op == "%":
        return num1 % num2 if num2 != 0 else "Error: Modulo by zero!"
    elif op == "**":
        return num1 ** num2
    else:
        return "Error: Unsupported operator."

print("  10 + 5  =", calculate(10, 5, "+"))
print("  20 / 4  =", calculate(20, 4, "/"))
print("  15 / 0  =", calculate(15, 0, "/"))
print("  2 ** 5  =", calculate(2, 5, "**"))

print()

# Mini-Project 3: Movie Ticket Pricing with Discounts
print("[Mini-Project 3: Movie Ticket Pricing]")
def calculate_ticket_price(customer_age: int, is_student: bool, is_weekend: bool) -> float:
    # Base price
    if customer_age < 5:
        base_price = 0.0      # Free for toddlers
    elif customer_age <= 12:
        base_price = 100.0    # Child fare
    elif customer_age >= 60:
        base_price = 120.0    # Senior citizen fare
    else:
        base_price = 200.0    # Standard adult fare

    # Weekend surcharge
    if is_weekend and base_price > 0:
        base_price += 50.0

    # Student discount (20% off)
    if is_student and base_price > 0:
        discount = base_price * 0.20
        base_price -= discount

    return base_price

price1 = calculate_ticket_price(customer_age=21, is_student=True, is_weekend=False)
price2 = calculate_ticket_price(customer_age=70, is_student=False, is_weekend=True)
price3 = calculate_ticket_price(customer_age=4, is_student=False, is_weekend=True)

print(f"  Student (Age 21, Weekday): Rs.{price1:.2f}")
print(f"  Senior (Age 70, Weekend): Rs.{price2:.2f}")
print(f"  Toddler (Age 4, Weekend) : Rs.{price3:.2f}")


# =============================================================================
# PART 10: BEST PRACTICES & COMMON GOTCHAS
# =============================================================================
print("\n--- PART 10: BEST PRACTICES & COMMON GOTCHAS ---\n")

# 1. Never compare booleans explicitly to True/False
is_ready = True
# Suboptimal: if is_ready == True:
# Pythonic:
if is_ready:
    print("Good Practice: Used 'if is_ready:' instead of 'if is_ready == True:'")

# 2. Chained comparisons (Pythonic superpower)
val = 15
if 10 <= val <= 20:
    print(f"Good Practice: Chained comparison '10 <= {val} <= 20' is clean and readable.")

# 3. Using .get() or 'in' before accessing dictionary keys to prevent KeyError
data = {"language": "Python"}
if "framework" in data:
    print(data["framework"])
else:
    print("Good Practice: Checked key existence with 'in' before access.")

# 4. Use 'is' for None checks, not '=='
result = None
if result is None:
    print("Good Practice: Checked 'result is None' instead of 'result == None'.")

print("\n" + "=" * 70)
print("     DAY 11 COMPLETED SUCCESSFULLY: CONDITIONAL STATEMENTS MASTERED!")
print("=" * 70)
