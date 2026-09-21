# =============================================================================
# DAY 15: GENERATORS IN PYTHON
# Author: Harish
# Repository: DAY-15-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

import sys

# =============================================================================
# 1. WHAT IS A GENERATOR? (BASIC CONCEPT)
# =============================================================================
# A generator is a special type of function in Python that produces a sequence
# of values on-the-fly instead of computing them all at once and storing them in
# memory.
#
# Key difference:
# - A normal function uses 'return' to send back a single value and terminates.
# - A generator function uses 'yield' to produce a value, pauses execution,
#   saves its state, and resumes from that point when the next value is requested.

print("--- 1. BASIC GENERATOR FUNCTION ---")

# Defining a simple generator function
def simple_generator():
    yield "First item"
    yield "Second item"
    yield "Third item"

# Calling the function returns a generator object, it doesn't run the body yet!
gen = simple_generator()
print("Generator object:", gen)

# Iterating over generator using a standard for-loop
print("\nIterating with a for loop:")
for item in simple_generator():
    print("Received:", item)


# =============================================================================
# 2. HOW GENERATORS WORK: 'yield' VS 'return' & 'next()'
# =============================================================================
# You can retrieve items one by one using the built-in next() function.
# When all values have been yielded, Python raises a StopIteration exception.

print("\n--- 2. STEP-BY-STEP RETRIEVAL WITH next() ---")

def count_up_to_three():
    print("-> Generator started")
    yield 1
    print("-> Resumed after 1st yield")
    yield 2
    print("-> Resumed after 2nd yield")
    yield 3
    print("-> Generator finished")

counter = count_up_to_three()

# Fetch items manually with next()
print("Step 1:", next(counter))
print("Step 2:", next(counter))
print("Step 3:", next(counter))

# Calling next() again when exhausted raises StopIteration:
try:
    print(next(counter))
except StopIteration:
    print("Generator exhausted: StopIteration caught safely!")


# =============================================================================
# 3. ADVANTAGES OF GENERATORS
# =============================================================================
# Why should we use generators?
#
# Advantage 1: MEMORY EFFICIENCY (Lazy Evaluation)
# - Regular lists store all items in memory simultaneously.
# - Generators produce items one at a time on demand ("lazy evaluation"),
#   saving massive amounts of RAM.

print("\n--- 3. ADVANTAGES OF GENERATORS ---")
print("[Advantage 1: Memory Efficiency]")

# Compare memory consumption using sys.getsizeof()
N = 100_000

# List approach: stores all 100,000 numbers in memory
numbers_list = [i for i in range(N)]
list_size = sys.getsizeof(numbers_list)

# Generator approach: stores only the generator state
numbers_gen = (i for i in range(N))
gen_size = sys.getsizeof(numbers_gen)

print(f"Memory used by List (100,000 items)     : {list_size:,} bytes")
print(f"Memory used by Generator (100,000 items): {gen_size:,} bytes")
print(f"-> Generator uses only {gen_size} bytes regardless of how many items it produces!")

# Advantage 2: FASTER STARTUP & HIGH PERFORMANCE
# - No need to wait for the entire dataset to be generated before processing starts.

print("\n[Advantage 2: Lazy Execution]")
print("Values are computed on-demand, enabling immediate processing without upfront computation delay.")

# Advantage 3: REPRESENTING INFINITE SEQUENCES
# - Because generators are lazy, they can generate an infinite stream of data
#   without running out of memory.

print("\n[Advantage 3: Infinite Sequences]")

def infinite_counter(start=1):
    current = start
    while True:
        yield current
        current += 1

inf_gen = infinite_counter(start=100)
print("Taking first 5 values from an infinite sequence:")
for _ in range(5):
    print(next(inf_gen), end=" ")
print()

# Advantage 4: SIMPLER IMPLEMENTATION THAN CUSTOM ITERATORS
# - Creating an iterator class requires __iter__() and __next__() boilerplate.
# - A generator handles the iterator protocol automatically!


# =============================================================================
# 4. GENERATOR EXPRESSIONS (CONCISE SYNTAX)
# =============================================================================
# Just like list comprehensions, Python supports generator expressions.
# Syntax: use round parentheses () instead of square brackets []

print("\n--- 4. GENERATOR EXPRESSIONS ---")

# List comprehension: builds list immediately in memory
squares_list = [x ** 2 for x in range(1, 6)]
print("List comprehension     :", squares_list)

# Generator expression: creates lazy generator object
squares_gen = (x ** 2 for x in range(1, 6))
print("Generator expression   :", squares_gen)
print("Items from generator   :", list(squares_gen))


# =============================================================================
# 5. PRACTICAL BASIC EXAMPLES
# =============================================================================

print("\n--- 5. PRACTICAL BASIC EXAMPLES ---")

# Example A: Generating Even Numbers up to a limit
def even_numbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            yield num

print("Even numbers up to 10:", list(even_numbers(10)))

# Example B: Simple Countdown Generator
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print("Countdown from 5:")
for count in countdown(5):
    print(count, end=" ")
print("-> Blast off!")


# =============================================================================
# 6. SUMMARY & KEY TAKEAWAYS
# =============================================================================
# 1. Generators are defined using regular function syntax with 'yield'.
# 2. 'yield' pauses the function and returns a value; next() resumes it.
# 3. Memory efficient: items are produced on-demand (lazy evaluation).
# 4. Ideal for large datasets, file processing, and infinite streams.
# 5. Generator expressions: (expr for item in iterable) provides a clean 1-liner.
