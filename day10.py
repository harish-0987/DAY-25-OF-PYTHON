# =============================================================================
# DAY 10: DICTIONARIES IN PYTHON (WHAT IS A DICT, METHODS & EXAMPLES)
# Author: Harish
# Repository: DAY-10-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

print("=" * 70)
print("     DAY 10: PYTHON DICTIONARIES - CONCEPTS, METHODS & CODE EXAMPLES")
print("=" * 70)


# =============================================================================
# PART 1: WHAT IS A DICTIONARY?
# =============================================================================
# Definition:
# A Dictionary in Python is a collection of key-value pairs.
# Each key is associated with a specific value: {key: value}.
#
# Key Features:
# 1. Key-Value Pairs : Every item is stored as 'key: value'.
# 2. Ordered         : Preserves insertion order (standard in Python 3.7+).
# 3. Mutable         : You can add, remove, and change values after creation.
# 4. Keys are Unique : Duplicate keys are NOT allowed. If repeated, the last
#                      assigned value overwrites the earlier one.
# 5. Keys are Hashable: Keys MUST be of an immutable type (str, int, float, tuple).
#                      Lists, sets, or dicts CANNOT be dictionary keys.
# 6. Values are Free : Values can be of ANY data type (numbers, strings, lists,
#                      other dicts, booleans) and can contain duplicates.
# 7. Fast Lookups    : Average time complexity for search/insert/delete is O(1).
# =============================================================================

print("\n--- PART 1: WHAT IS A DICTIONARY? ---\n")

# 1. Creating basic dictionaries
empty_dict_1 = {}
empty_dict_2 = dict()

user_profile = {
    "username": "harish_dev",
    "age": 21,
    "role": "Software Developer",
    "is_active": True,
    "skills": ["Python", "Git", "FastAPI"]
}

print("Empty dict 1      :", empty_dict_1)
print("User profile dict :", user_profile)
print("Data type         :", type(user_profile).__name__)
print("Length (keys count):", len(user_profile))

# 2. Duplicate keys gotcha: The last value wins
duplicates_demo = {"brand": "Apple", "brand": "Samsung", "year": 2024}
print("Duplicate key demo:", duplicates_demo)  # 'brand' will be 'Samsung'

# 3. Creating dictionaries with dict() constructor
person = dict(name="Harish", city="Bengaluru", experience=2)
print("Using dict()      :", person)

# 4. Creating from list of key-value tuples
tuple_pairs = [("id", 101), ("status", "success"), ("code", 200)]
from_tuples = dict(tuple_pairs)
print("From tuple pairs  :", from_tuples)


# =============================================================================
# PART 2: ACCESSING ELEMENTS
# =============================================================================
# 1. Square brackets: dict[key]
#    - Fast lookup.
#    - Raises KeyError if the key does not exist!
# 2. get() method: dict.get(key, default=None)
#    - Safe lookup.
#    - Returns None (or a custom default) if the key is missing. No crash!
# 3. Membership test: 'in' and 'not in'
#    - Checks if a KEY exists in the dictionary (checks keys, NOT values).
# =============================================================================

print("\n--- PART 2: ACCESSING ELEMENTS ---\n")

server_config = {
    "host": "127.0.0.1",
    "port": 8080,
    "ssl": True,
    "environment": "production"
}

# 1. Access using square brackets []
print("Host (via [])       :", server_config["host"])
print("Port (via [])       :", server_config["port"])

# 2. Access using .get() - safe access
print("Environment (get)   :", server_config.get("environment"))
print("Timeout (missing)   :", server_config.get("timeout"))                  # Returns None
print("Timeout with default:", server_config.get("timeout", 30))              # Returns 30

# 3. Membership test ('in' checks keys)
print("Is 'ssl' in config? :", "ssl" in server_config)
print("Is 'db_url' in config?:", "db_url" in server_config)
print("Is 8080 in config?  :", 8080 in server_config, "-> (False: 'in' checks keys, not values!)")


# =============================================================================
# PART 3: ADDING AND UPDATING ELEMENTS
# =============================================================================
# 1. Assignment: dict[key] = value
#    - If key exists: updates value.
#    - If key doesn't exist: adds new key-value pair.
# 2. update(): dict.update(other_dict_or_kwargs)
#    - Modifies the dictionary in-place with multiple key-value pairs.
# 3. Merge Operators (Python 3.9+):
#    - dict1 | dict2  : Returns a new merged dictionary.
#    - dict1 |= dict2 : In-place merge (updates dict1).
# =============================================================================

print("\n--- PART 3: ADDING AND UPDATING ELEMENTS ---\n")

device = {"name": "Laptop", "price": 1200}
print("Initial device      :", device)

# 1. Adding a new key
device["brand"] = "Dell"
print("After adding 'brand':", device)

# 2. Updating an existing key
device["price"] = 1100
print("After updating price:", device)

# 3. Using .update() with multiple items
device.update({"color": "Space Gray", "warranty_years": 2, "price": 1050})
print("After .update()     :", device)

# 4. Dictionary Merge Operators (Python 3.9+)
extra_specs = {"ram": "16GB", "storage": "512GB SSD"}
merged_device = device | extra_specs
print("Merged via |        :", merged_device)

device |= {"os": "Ubuntu Linux"}
print("In-place merged via |= :", device)


# =============================================================================
# PART 4: REMOVING ELEMENTS
# =============================================================================
# 1. pop(key, [default]) : Removes key and returns its value.
#                          Raises KeyError if key not found and no default set.
# 2. popitem()           : Removes and returns the LAST inserted (key, value) tuple.
#                          Raises KeyError if dictionary is empty.
# 3. del dict[key]       : Deletes key-value pair permanently.
# 4. clear()             : Empties the dictionary completely (leaves {}).
# =============================================================================

print("\n--- PART 4: REMOVING ELEMENTS ---\n")

inventory = {
    "item_01": "Mechanical Keyboard",
    "item_02": "Wireless Mouse",
    "item_03": "USB-C Hub",
    "item_04": "Webcam 1080p",
    "item_05": "Monitor 27 inch"
}
print("Initial inventory:", inventory)

# 1. pop() - removes specific key and returns value
removed_item = inventory.pop("item_03")
print(f"Popped item_03   : '{removed_item}'")
print("After pop()      :", inventory)

# pop() with default prevents KeyError
safe_pop = inventory.pop("item_99", "Not Available")
print(f"Safe pop missing : '{safe_pop}'")

# 2. popitem() - removes last inserted item (LIFO order)
last_key, last_val = inventory.popitem()
print(f"Popped last item : ('{last_key}': '{last_val}')")
print("After popitem()  :", inventory)

# 3. del statement
del inventory["item_01"]
print("After del item_01:", inventory)

# 4. clear() - wipes all entries
temp_cart = {"apple": 3, "bread": 1}
temp_cart.clear()
print("After clear()    :", temp_cart)


# =============================================================================
# PART 5: DICTIONARY VIEWS & ITERATION
# =============================================================================
# 1. keys()   : Returns dynamic view of all keys.
# 2. values() : Returns dynamic view of all values.
# 3. items()  : Returns dynamic view of all (key, value) pairs as tuples.
#
# These views update automatically when the dictionary changes!
# =============================================================================

print("\n--- PART 5: DICTIONARY VIEWS & ITERATION ---\n")

student_scores = {
    "Harish": 95,
    "Ananya": 88,
    "Rahul": 76,
    "Priya": 92
}

print("Keys view  :", student_scores.keys())
print("Values view:", student_scores.values())
print("Items view :", student_scores.items())

# 1. Iterating through keys (default behavior)
print("\nIterating through keys:")
for name in student_scores:  # or student_scores.keys()
    print(f" - Student: {name}")

# 2. Iterating through values
print("\nIterating through values:")
for score in student_scores.values():
    print(f" - Score: {score}")

# 3. Iterating through key-value pairs with .items() (Most common & useful!)
print("\nIterating through key-value pairs:")
for name, score in student_scores.items():
    status = "Distinction" if score >= 90 else "Passed"
    print(f" - {name:8}: {score} ({status})")


# =============================================================================
# PART 6: OTHER USEFUL DICTIONARY METHODS
# =============================================================================
# 1. setdefault(key, default) :
#    - If key exists: returns its current value (does NOT change it).
#    - If key does NOT exist: inserts key with default value and returns it.
# 2. fromkeys(iterable, value=None) :
#    - Creates a new dictionary with keys from sequence and all values set to value.
# 3. copy() :
#    - Creates a shallow copy of the dictionary.
# =============================================================================

print("\n--- PART 6: OTHER USEFUL METHODS ---\n")

# 1. setdefault()
app_settings = {"theme": "dark", "fontSize": 14}

# 'theme' already exists -> returns current value "dark", does not overwrite
current_theme = app_settings.setdefault("theme", "light")
print("setdefault existing key :", current_theme)

# 'autoSave' does not exist -> inserts "autoSave": True and returns True
autosave_val = app_settings.setdefault("autoSave", True)
print("setdefault new key      :", autosave_val)
print("Settings dictionary     :", app_settings)

# 2. fromkeys()
features = ["audio", "video", "chat", "screen_share"]
permissions = dict.fromkeys(features, "disabled")
print("\nfromkeys() default      :", permissions)

# 3. copy() vs reference
original_dict = {"a": 1, "b": 2}
reference_dict = original_dict        # Points to the same memory!
shallow_copied = original_dict.copy() # New separate dictionary!

shallow_copied["c"] = 99
print("Original after copy edit:", original_dict)   # Unchanged: {'a': 1, 'b': 2}
print("Copied dict             :", shallow_copied) # {'a': 1, 'b': 2, 'c': 99}


# =============================================================================
# PART 7: NESTED DICTIONARIES
# =============================================================================
# A dictionary can contain other dictionaries as values.
# Common for representing hierarchical, JSON-like data (APIs, databases).
# =============================================================================

print("\n--- PART 7: NESTED DICTIONARIES ---\n")

company = {
    "emp_001": {
        "name": "Harish",
        "dept": "Engineering",
        "skills": ["Python", "FastAPI", "SQL"],
        "salary": 85000
    },
    "emp_002": {
        "name": "Kavya",
        "dept": "Data Science",
        "skills": ["Python", "Pandas", "PyTorch"],
        "salary": 92000
    },
    "emp_003": {
        "name": "Arun",
        "dept": "DevOps",
        "skills": ["Docker", "Kubernetes", "AWS"],
        "salary": 88000
    }
}

# Accessing nested values
print("Emp 001 Name  :", company["emp_001"]["name"])
print("Emp 002 Skills:", company["emp_002"]["skills"])
print("Emp 003 Salary:", company["emp_003"]["salary"])

# Modifying nested dictionary
company["emp_001"]["salary"] = 90000
company["emp_001"]["skills"].append("Docker")
print("\nUpdated Emp 001 details:", company["emp_001"])

# Iterating through nested dictionaries
print("\nCompany Directory:")
for emp_id, info in company.items():
    print(f"[{emp_id}] {info['name']} - {info['dept']} (Salary: ${info['salary']:,})")


# =============================================================================
# PART 8: DICTIONARY COMPREHENSIONS
# =============================================================================
# Syntax: {key_expr: value_expr for item in iterable if condition}
# Elegant, pythonic way to build transformed dictionaries in a single line.
# =============================================================================

print("\n--- PART 8: DICTIONARY COMPREHENSIONS ---\n")

# 1. Squares of numbers 1 to 6
squares = {num: num ** 2 for num in range(1, 7)}
print("Squares 1 to 6        :", squares)

# 2. Filtering with condition: only even numbers squared
even_squares = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print("Even squares          :", even_squares)

# 3. Transforming values (e.g. converting Celsius to Fahrenheit)
celsius_temps = {"city_a": 0, "city_b": 25, "city_c": 37, "city_d": 100}
fahrenheit_temps = {city: round((temp * 9/5) + 32, 1) for city, temp in celsius_temps.items()}
print("Celsius temps         :", celsius_temps)
print("Fahrenheit temps      :", fahrenheit_temps)

# 4. Inverting a dictionary (swapping keys and values)
original_roles = {"alice": "admin", "bob": "editor", "charlie": "viewer"}
inverted_roles = {role: user for user, role in original_roles.items()}
print("Original roles        :", original_roles)
print("Inverted roles (V->K) :", inverted_roles)


# =============================================================================
# PART 9: REAL-WORLD PRACTICAL EXAMPLES
# =============================================================================
# Real-world problem solving with dictionaries:
# 1. Word Frequency Counter (classic NLP & text processing task).
# 2. Student Gradebook Analyzer (computes average, highest, lowest, grade).
# 3. E-Commerce Shopping Cart & Invoice Generator.
# =============================================================================

print("\n--- PART 9: REAL-WORLD PRACTICAL EXAMPLES ---\n")

# --- Example 1: Word Frequency Counter ---
text = "python is amazing and python is versatile and python is fast"
words = text.lower().split()
word_frequency = {}

for word in words:
    # get(word, 0) + 1 handles both new words and increments existing counts cleanly
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("1. Word Frequency Counter:")
print("Text:", text)
for word, count in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True):
    print(f" - '{word}': {count} time(s)")

# --- Example 2: Gradebook Analyzer ---
grades = {
    "Math": 94,
    "Science": 89,
    "Computer Science": 98,
    "English": 85,
    "History": 79
}

total_marks = sum(grades.values())
subject_count = len(grades)
average_marks = total_marks / subject_count
highest_subject = max(grades, key=grades.get)
lowest_subject = min(grades, key=grades.get)

print("\n2. Student Gradebook Report:")
print(f"Total Subjects : {subject_count}")
print(f"Total Marks    : {total_marks} / {subject_count * 100}")
print(f"Average Marks  : {average_marks:.2f}%")
print(f"Best Subject   : {highest_subject} ({grades[highest_subject]}%)")
print(f"Lowest Subject : {lowest_subject} ({grades[lowest_subject]}%)")

# --- Example 3: Shopping Cart Bill Generator ---
catalog = {
    "notebook": 45,
    "gel_pen": 15,
    "backpack": 650,
    "water_bottle": 180,
    "desk_lamp": 420
}

cart = {
    "notebook": 3,
    "gel_pen": 5,
    "backpack": 1,
    "water_bottle": 2
}

print("\n3. Shopping Cart Invoice:")
print("-" * 50)
print(f"{'Item':<15} {'Price':>8} {'Qty':>6} {'Total':>12}")
print("-" * 50)

grand_total = 0
for item, quantity in cart.items():
    price = catalog.get(item, 0)
    item_total = price * quantity
    grand_total += item_total
    print(f"{item.replace('_', ' ').title():<15} Rs.{price:>7.2f} {quantity:>6} Rs.{item_total:>11.2f}")

print("-" * 50)
discount = 0.10 * grand_total if grand_total >= 1000 else 0.0
final_amount = grand_total - discount
print(f"{'Subtotal':<31} Rs.{grand_total:>11.2f}")
if discount > 0:
    print(f"{'10% Festive Discount':<31} -Rs.{discount:>10.2f}")
print(f"{'Final Payable':<31} Rs.{final_amount:>11.2f}")
print("-" * 50)


# =============================================================================
# PART 10: COMMON PITFALLS & BEST PRACTICES
# =============================================================================
# 1. Unhashable Keys:
#    - Using a list as a key raises TypeError: unhashable type: 'list'.
#    - Use a tuple instead if you need a sequence as a key!
#
# 2. Modifying a Dictionary While Iterating Over It:
#    - Raises RuntimeError: dictionary changed size during iteration.
#    - Solution: Iterate over list(my_dict.keys()) instead of my_dict.
#
# 3. KeyError vs .get():
#    - Prefer .get(key, default) whenever you're unsure if the key exists.
# =============================================================================

print("\n--- PART 10: PITFALLS & BEST PRACTICES ---\n")

# Pitfall 1: Tuple as key (valid) vs List as key (invalid)
coordinate_map = {
    (12.9716, 77.5946): "Bengaluru",
    (19.0760, 72.8777): "Mumbai",
    (28.7041, 77.1025): "New Delhi"
}
print("Tuple key lookup (Bengaluru coordinates):", coordinate_map[(12.9716, 77.5946)])

# Pitfall 2: Safely deleting items while iterating
tasks = {
    "task_1": "completed",
    "task_2": "pending",
    "task_3": "completed",
    "task_4": "in_progress"
}

# Iterate over a snapshot list of keys:
for task_id in list(tasks.keys()):
    if tasks[task_id] == "completed":
        del tasks[task_id]

print("Remaining active tasks after cleanup   :", tasks)


print("\n" + "=" * 70)
print("            DAY 10 COMPLETED SUCCESSFULLY! KEEP BUILDING!             ")
print("=" * 70)
