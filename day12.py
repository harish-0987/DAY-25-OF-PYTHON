# =============================================================================
# DAY 12: LOOPS AND JUMP STATEMENTS IN PYTHON
# Author: Harish
# Repository: DAY-12-OF-PYTHON-
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# 1. FOR LOOP (BASIC LEVEL)
# =============================================================================
# A for loop is used to repeat a block of code a specific number of times
# or iterate over a sequence (such as a range, list, or string).

print("--- 1. FOR LOOP EXAMPLES ---")

# Example 1: Using range() to print numbers from 1 to 5
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Example 2: Looping through a list
fruits = ["apple", "banana", "mango"]
print("\nFruits list:")
for fruit in fruits:
    print(fruit)

# Example 3: Looping through a string
print("\nCharacters in 'Python':")
for char in "Python":
    print(char)


# =============================================================================
# 2. WHILE LOOP (BASIC LEVEL)
# =============================================================================
# A while loop repeats a block of code as long as a condition is True.

print("\n--- 2. WHILE LOOP EXAMPLES ---")

# Example 1: Basic counter (1 to 5)
count = 1
print("\nCounting using while loop:")
while count <= 5:
    print("Count:", count)
    count += 1  # Increment to avoid infinite loop

# Example 2: Countdown
timer = 3
print("\nCountdown:")
while timer > 0:
    print(timer)
    timer -= 1
print("Time's up!")


# =============================================================================
# 3. JUMP STATEMENTS (BASIC LEVEL)
# =============================================================================
# Jump statements alter the regular flow of a loop:
# - break: Terminates the loop completely.
# - continue: Skips the current iteration and jumps to the next.
# - pass: Acts as a placeholder (does nothing).

print("\n--- 3. JUMP STATEMENTS ---")

# A. break statement: Stop when number is 3
print("\nUsing break (stops when i == 3):")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# B. continue statement: Skip number 3
print("\nUsing continue (skips when i == 3):")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# C. pass statement: Placeholder for future code
print("\nUsing pass (does nothing):")
for i in range(1, 4):
    if i == 2:
        pass  # TODO: add logic later
    print(i)
