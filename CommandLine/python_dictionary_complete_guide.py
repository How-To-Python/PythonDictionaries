"""
COMPLETE GUIDE TO PYTHON DICTIONARIES
=====================================

A comprehensive guide to working with Python dictionaries, covering everything from basic operations
to advanced techniques with interactive examples and demonstrations.

This guide is responsive and includes hands-on examples that you can run to see the output.
"""

import sys
import os

def print_section_header(title, char="=", width=80):
    """Print a formatted section header."""
    print("\n" + char * width)
    print(f" {title} ".center(width, char))
    print(char * width)

def print_subsection_header(title, char="-", width=60):
    """Print a formatted subsection header."""
    print("\n" + char * width)
    print(f" {title} ")
    print(char * width)

def run_example(example_func):
    """Run an example function and handle any errors."""
    try:
        example_func()
    except Exception as e:
        print(f"Error running example: {e}")

def pause_for_user():
    """Pause execution for user to review output."""
    input("\nPress Enter to continue to the next section...")

# =============================================================================
# TABLE OF CONTENTS
# =============================================================================

def show_table_of_contents():
    """Display the guide's table of contents."""
    print_section_header("PYTHON DICTIONARIES - COMPLETE GUIDE", "=")
    
    toc = """
TABLE OF CONTENTS:

1. Dictionary Basics - Creation, Access, and Properties
2. Basic Operations - Adding, Removing, and Modifying
3. Dictionary Methods - Essential built-in methods
4. Dictionary Comprehensions - Powerful one-liner creations
5. Iteration Techniques - Loops and advanced iteration
6. Dictionary Functions - Built-in functions and utilities
7. Advanced Techniques - Merging, unpacking, and more
8. Nested Dictionaries - Multi-level data structures
9. Performance Tips - Optimization and best practices
10. Real-World Examples - Practical applications
11. Interactive Demonstrations - Hands-on practice
12. Quick Reference - Cheat sheet

Each section includes:
✅ Clear explanations
✅ Interactive code examples
✅ Output demonstrations
✅ Best practices
✅ Common pitfalls to avoid
    """
    print(toc)

# =============================================================================
# 1. DICTIONARY BASICS
# =============================================================================

def dictionary_basics():
    """Demonstrate dictionary creation, access, and basic properties."""
    print_section_header("1. DICTIONARY BASICS")
    
    print_subsection_header("Creating Dictionaries")
    
    # Empty dictionary
    empty_dict = {}
    empty_dict2 = dict()
    print("Empty dictionary {}:", empty_dict)
    print("Empty dictionary dict():", empty_dict2)
    print("Type:", type(empty_dict))
    
    # Dictionary with initial data
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.85
    }
    print("Student dictionary:", student)
    
    # Mixed data types
    mixed_dict = {
        "string": "hello",
        "number": 42,
        "float": 3.14,
        "boolean": True,
        "list": [1, 2, 3],
        "nested": {"a": 1, "b": 2}
    }
    print("Mixed data types:", mixed_dict)
    
    print_subsection_header("Accessing Elements")
    
    # Direct access
    print("Student name:", student["name"])
    print("Student GPA:", student["gpa"])
    
    # Safe access with get()
    print("Grade (get):", student.get("grade", "Not assigned"))
    print("Major (get):", student.get("major"))
    
    # Checking existence
    print("'name' in student:", "name" in student)
    print("'grade' in student:", "grade" in student)
    
    print_subsection_header("Dictionary Properties")
    
    # Length
    print("Dictionary length:", len(student))
    
    # Keys, values, items
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    print("Items:", list(student.items()))

def dictionary_creation_methods():
    """Demonstrate various ways to create dictionaries."""
    print_subsection_header("Dictionary Creation Methods")
    
    # From lists using zip
    keys = ["apple", "banana", "cherry"]
    values = [1.20, 0.50, 2.30]
    fruit_prices = dict(zip(keys, values))
    print("From zip:", fruit_prices)
    
    # From list of tuples
    pairs = [("red", "#FF0000"), ("green", "#00FF00"), ("blue", "#0000FF")]
    colors = dict(pairs)
    print("From tuples:", colors)
    
    # Using keyword arguments
    person = dict(name="Bob", age=25, city="New York")
    print("From kwargs:", person)
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print("From comprehension:", squares)

# =============================================================================
# 2. BASIC OPERATIONS
# =============================================================================

def basic_operations():
    """Demonstrate basic dictionary operations."""
    print_section_header("2. BASIC OPERATIONS")
    
    # Starting dictionary
    inventory = {"apples": 50, "bananas": 30}
    print("Starting inventory:", inventory)
    
    print_subsection_header("Adding Elements")
    
    # Direct assignment
    inventory["oranges"] = 25
    print("After adding oranges:", inventory)
    
    # Update with another dictionary
    new_items = {"grapes": 15, "strawberries": 8}
    inventory.update(new_items)
    print("After update:", inventory)
    
    # Update with keyword arguments
    inventory.update(pineapples=5, mangoes=12)
    print("After kwargs update:", inventory)
    
    print_subsection_header("Removing Elements")
    
    # Using del
    del inventory["strawberries"]
    print("After del strawberries:", inventory)
    
    # Using pop()
    apple_count = inventory.pop("apples")
    print(f"Popped apples: {apple_count}")
    print("After pop:", inventory)
    
    # Using pop() with default
    grape_count = inventory.pop("grapes", 0)
    print(f"Grapes count: {grape_count}")
    
    # Using popitem() - removes last item (Python 3.7+)
    last_item = inventory.popitem()
    print(f"Last item removed: {last_item}")
    print("After popitem:", inventory)
    
    # Clear all items
    temp_dict = {"a": 1, "b": 2}
    print("Before clear:", temp_dict)
    temp_dict.clear()
    print("After clear:", temp_dict)
    
    print_subsection_header("Modifying Elements")
    
    # Direct modification
    inventory["bananas"] = 45
    print("Modified bananas:", inventory)
    
    # Conditional modification
    if "pineapples" in inventory:
        inventory["pineapples"] += 3
        print("Increased pineapples:", inventory)

# =============================================================================
# 3. DICTIONARY METHODS
# =============================================================================

def dictionary_methods():
    """Demonstrate essential dictionary methods."""
    print_section_header("3. DICTIONARY METHODS")
    
    student_grades = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 92,
        "Diana": 88
    }
    
    print("Student grades:", student_grades)
    
    print_subsection_header("View Methods")
    
    # Keys, values, items
    keys = student_grades.keys()
    values = student_grades.values()
    items = student_grades.items()
    
    print("Keys type:", type(keys))
    print("Keys:", list(keys))
    print("Values:", list(values))
    print("Items:", list(items))
    
    print_subsection_header("Safe Access Methods")
    
    # get() method
    print("Alice's grade:", student_grades.get("Alice"))
    print("Eve's grade:", student_grades.get("Eve", "Not found"))
    
    # setdefault() method
    grade = student_grades.setdefault("Eve", 85)
    print(f"Eve's grade (setdefault): {grade}")
    print("Updated grades:", student_grades)
    
    # setdefault() with existing key
    existing_grade = student_grades.setdefault("Alice", 100)
    print(f"Alice's grade (existing): {existing_grade}")
    
    print_subsection_header("Copying Dictionaries")
    
    # Shallow copy
    grades_copy = student_grades.copy()
    print("Original:", student_grades)
    print("Copy:", grades_copy)
    
    # Demonstrate shallow copy behavior
    nested_dict = {"a": {"x": 1}, "b": {"y": 2}}
    shallow_copy = nested_dict.copy()
    
    nested_dict["a"]["x"] = 99
    print("Original after modification:", nested_dict)
    print("Shallow copy:", shallow_copy)  # Also affected!

# =============================================================================
# 4. DICTIONARY COMPREHENSIONS
# =============================================================================

def dictionary_comprehensions():
    """Demonstrate dictionary comprehensions."""
    print_section_header("4. DICTIONARY COMPREHENSIONS")
    
    print_subsection_header("Basic Dictionary Comprehensions")
    
    # Basic syntax: {key_expr: value_expr for item in iterable}
    squares = {x: x**2 for x in range(1, 6)}
    print("Squares:", squares)
    
    # String processing
    words = ["apple", "banana", "cherry"]
    word_lengths = {word: len(word) for word in words}
    print("Word lengths:", word_lengths)
    
    print_subsection_header("Conditional Dictionary Comprehensions")
    
    # With condition
    numbers = range(1, 11)
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print("Even squares:", even_squares)
    
    # Transform existing dictionary
    prices = {"laptop": 1000, "mouse": 30, "keyboard": 80}
    discounted = {item: price * 0.9 for item, price in prices.items()}
    print("Original prices:", prices)
    print("Discounted prices:", discounted)
    
    # Conditional expressions
    grade_letters = {
        name: ("A" if grade >= 90 else "B" if grade >= 80 else "C")
        for name, grade in {"Alice": 95, "Bob": 87, "Charlie": 76}.items()
    }
    print("Grade letters:", grade_letters)
    
    print_subsection_header("Advanced Comprehensions")
    
    # Working with multiple iterables
    fruits = ["apple", "banana", "cherry"]
    colors = ["red", "yellow", "red"]
    fruit_colors = {fruit: color for fruit, color in zip(fruits, colors)}
    print("Fruit colors:", fruit_colors)
    
    # Filtering and transforming
    inventory = {
        "laptop": {"price": 999, "stock": 5},
        "mouse": {"price": 25, "stock": 0},
        "keyboard": {"price": 75, "stock": 10}
    }
    
    in_stock = {
        item: details["price"]
        for item, details in inventory.items()
        if details["stock"] > 0
    }
    print("Items in stock:", in_stock)

# =============================================================================
# 5. ITERATION TECHNIQUES
# =============================================================================

def iteration_techniques():
    """Demonstrate various ways to iterate over dictionaries."""
    print_section_header("5. ITERATION TECHNIQUES")
    
    book_info = {
        "title": "Python Programming",
        "author": "John Doe",
        "year": 2024,
        "pages": 350,
        "price": 29.99
    }
    
    print("Book information:", book_info)
    
    print_subsection_header("Basic Iteration")
    
    # Iterate over keys (default)
    print("Keys only:")
    for key in book_info:
        print(f"  {key}")
    
    # Explicit keys iteration
    print("Keys (explicit):")
    for key in book_info.keys():
        print(f"  {key}")
    
    # Iterate over values
    print("Values only:")
    for value in book_info.values():
        print(f"  {value}")
    
    print_subsection_header("Key-Value Iteration")
    
    # Iterate over items
    print("Key-value pairs:")
    for key, value in book_info.items():
        print(f"  {key}: {value}")
    
    # Formatted output
    print("Formatted book info:")
    for key, value in book_info.items():
        print(f"  {key.title()}: {value}")
    
    print_subsection_header("Advanced Iteration")
    
    # Enumerate with items
    print("Enumerated items:")
    for i, (key, value) in enumerate(book_info.items(), 1):
        print(f"  {i}. {key}: {value}")
    
    # Conditional iteration
    print("Numeric values only:")
    for key, value in book_info.items():
        if isinstance(value, (int, float)):
            print(f"  {key}: {value}")
    
    # Multiple dictionaries
    prices = {"apple": 1.20, "banana": 0.50}
    stock = {"apple": 50, "banana": 30}
    
    print("Price and stock info:")
    for fruit in prices:
        if fruit in stock:
            print(f"  {fruit}: ${prices[fruit]:.2f}, Stock: {stock[fruit]}")

# =============================================================================
# 6. ADVANCED TECHNIQUES
# =============================================================================

def advanced_techniques():
    """Demonstrate advanced dictionary techniques."""
    print_section_header("6. ADVANCED TECHNIQUES")
    
    print_subsection_header("Dictionary Merging")
    
    # Using ** operator (Python 3.5+)
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"e": 5}
    
    merged = {**dict1, **dict2, **dict3}
    print("Merged dictionaries:", merged)
    
    # Handling conflicts
    config_default = {"theme": "light", "font_size": 12, "auto_save": True}
    config_user = {"theme": "dark", "font_size": 14}
    
    final_config = {**config_default, **config_user}
    print("Default config:", config_default)
    print("User config:", config_user)
    print("Final config:", final_config)
    
    print_subsection_header("Dictionary Unpacking")
    
    # Function parameters
    def create_user(**kwargs):
        defaults = {"active": True, "role": "user"}
        user_data = {**defaults, **kwargs}
        return user_data
    
    user1 = create_user(name="Alice", email="alice@example.com")
    user2 = create_user(name="Bob", role="admin", active=False)
    
    print("User 1:", user1)
    print("User 2:", user2)
    
    print_subsection_header("defaultdict Usage")
    
    from collections import defaultdict
    
    # Group words by first letter
    words = ["apple", "banana", "cherry", "apricot", "blueberry"]
    grouped = defaultdict(list)
    
    for word in words:
        grouped[word[0]].append(word)
    
    print("Grouped words:", dict(grouped))
    
    # Count items
    text = "hello world hello python world"
    word_count = defaultdict(int)
    
    for word in text.split():
        word_count[word] += 1
    
    print("Word count:", dict(word_count))

def nested_dictionaries():
    """Demonstrate working with nested dictionaries."""
    print_subsection_header("Nested Dictionaries")
    
    # Complex data structure
    company = {
        "name": "TechCorp",
        "founded": 2010,
        "employees": {
            "engineering": {
                "alice": {"position": "Senior Developer", "salary": 95000},
                "bob": {"position": "DevOps Engineer", "salary": 85000}
            },
            "marketing": {
                "charlie": {"position": "Marketing Manager", "salary": 75000},
                "diana": {"position": "Content Creator", "salary": 55000}
            }
        }
    }
    
    print("Company structure:")
    print(f"Name: {company['name']}")
    print(f"Founded: {company['founded']}")
    
    # Access nested data
    alice_info = company["employees"]["engineering"]["alice"]
    print(f"Alice: {alice_info['position']}, ${alice_info['salary']:,}")
    
    # Iterate through nested structure
    print("\nAll employees:")
    for dept_name, dept_info in company["employees"].items():
        print(f"  {dept_name.title()} Department:")
        for emp_name, emp_info in dept_info.items():
            print(f"    {emp_name.title()}: {emp_info['position']}")
    
    # Safe nested access
    def safe_get(d, *keys, default=None):
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return default
        return d
    
    # Test safe access
    result1 = safe_get(company, "employees", "engineering", "alice", "salary")
    result2 = safe_get(company, "employees", "finance", "eve", "salary", default="N/A")
    
    print(f"\nSafe access - Alice salary: {result1}")
    print(f"Safe access - Eve salary: {result2}")

# =============================================================================
# 7. REAL-WORLD EXAMPLES
# =============================================================================

def real_world_examples():
    """Demonstrate practical real-world applications."""
    print_section_header("7. REAL-WORLD EXAMPLES")
    
    print_subsection_header("Example 1: Configuration Management")
    
    # Application configuration
    default_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp"
        },
        "cache": {
            "type": "redis",
            "ttl": 3600
        },
        "logging": {
            "level": "INFO",
            "file": "app.log"
        }
    }
    
    user_config = {
        "database": {
            "host": "prod-server.com",
            "port": 5433
        },
        "logging": {
            "level": "DEBUG"
        }
    }
    
    def merge_config(default, user):
        """Recursively merge configuration dictionaries."""
        result = default.copy()
        for key, value in user.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    final_config = merge_config(default_config, user_config)
    
    print("Default config:")
    for section, settings in default_config.items():
        print(f"  {section}: {settings}")
    
    print("\nFinal merged config:")
    for section, settings in final_config.items():
        print(f"  {section}: {settings}")
    
    print_subsection_header("Example 2: Data Processing Pipeline")
    
    # Student records processing
    raw_records = [
        "Alice,20,Computer Science,3.85",
        "Bob,22,Mathematics,3.70",
        "Charlie,19,Physics,3.92"
    ]
    
    students = {}
    for record in raw_records:
        name, age, major, gpa = record.split(",")
        students[name] = {
            "age": int(age),
            "major": major,
            "gpa": float(gpa),
            "honors": float(gpa) >= 3.8
        }
    
    print("Processed student records:")
    for name, info in students.items():
        honors_status = "Yes" if info["honors"] else "No"
        print(f"  {name}: {info['major']}, GPA: {info['gpa']}, Honors: {honors_status}")
    
    # Statistical analysis
    total_gpa = sum(student["gpa"] for student in students.values())
    avg_gpa = total_gpa / len(students)
    honors_count = sum(1 for student in students.values() if student["honors"])
    
    print(f"\nStatistics:")
    print(f"  Average GPA: {avg_gpa:.2f}")
    print(f"  Honors students: {honors_count}/{len(students)}")
    
    print_subsection_header("Example 3: Inventory Management System")
    
    inventory = {
        "electronics": {
            "laptop": {"price": 999.99, "stock": 5, "supplier": "TechCorp"},
            "mouse": {"price": 29.99, "stock": 25, "supplier": "AccessoryCo"}
        },
        "books": {
            "python_guide": {"price": 39.99, "stock": 15, "supplier": "BookHouse"},
            "data_science": {"price": 49.99, "stock": 8, "supplier": "EduPress"}
        }
    }
    
    def get_low_stock_items(inventory, threshold=10):
        """Find items with stock below threshold."""
        low_stock = {}
        for category, items in inventory.items():
            for item, details in items.items():
                if details["stock"] < threshold:
                    low_stock[f"{category}/{item}"] = details["stock"]
        return low_stock
    
    def calculate_inventory_value(inventory):
        """Calculate total inventory value."""
        total_value = 0
        for category, items in inventory.items():
            for item, details in items.items():
                total_value += details["price"] * details["stock"]
        return total_value
    
    low_stock = get_low_stock_items(inventory)
    total_value = calculate_inventory_value(inventory)
    
    print("Low stock items:")
    for item, stock in low_stock.items():
        print(f"  {item}: {stock} units")
    
    print(f"\nTotal inventory value: ${total_value:,.2f}")

# =============================================================================
# 8. QUICK REFERENCE
# =============================================================================

def quick_reference():
    """Provide a comprehensive quick reference guide."""
    print_section_header("8. QUICK REFERENCE GUIDE")
    
    reference_sections = {
        "Dictionary Creation": [
            "{}                          # Empty dictionary",
            "{'a': 1, 'b': 2}           # With initial data",
            "dict()                      # Empty using constructor",
            "dict(a=1, b=2)             # Using keyword args",
            "dict([('a', 1), ('b', 2)]) # From list of tuples",
            "dict(zip(keys, values))    # From two lists",
            "{k: v for k, v in items}   # Dictionary comprehension"
        ],
        
        "Accessing Elements": [
            "d['key']                    # Direct access (KeyError if missing)",
            "d.get('key')               # Safe access (None if missing)",
            "d.get('key', default)      # Safe access with default",
            "'key' in d                 # Check if key exists",
            "d.keys()                   # Get all keys",
            "d.values()                 # Get all values",
            "d.items()                  # Get key-value pairs"
        ],
        
        "Adding/Updating Elements": [
            "d['key'] = value           # Add or update single item",
            "d.update(other_dict)       # Update with another dictionary",
            "d.update(key=value)        # Update with keyword args",
            "d.setdefault('key', value) # Add only if key doesn't exist",
            "d1.update(d2)              # Merge d2 into d1",
            "new_d = {**d1, **d2}       # Merge creating new dictionary"
        ],
        
        "Removing Elements": [
            "del d['key']               # Remove key (KeyError if missing)",
            "d.pop('key')               # Remove and return value",
            "d.pop('key', default)      # Remove with default if missing",
            "d.popitem()                # Remove and return last item",
            "d.clear()                  # Remove all items"
        ],
        
        "Iteration": [
            "for key in d:              # Iterate over keys",
            "for key in d.keys():       # Explicit key iteration",
            "for value in d.values():   # Iterate over values",
            "for k, v in d.items():     # Iterate over key-value pairs",
            "for i, (k, v) in enumerate(d.items()): # With index"
        ],
        
        "Dictionary Comprehensions": [
            "{k: v for k, v in items}   # Basic comprehension",
            "{k: v for k, v in items if condition} # With filter",
            "{k: f(v) for k, v in d.items()} # Transform values",
            "{f(k): v for k, v in d.items()} # Transform keys",
            "{k: ('A' if v > 90 else 'B') for k, v in d.items()} # Conditional"
        ],
        
        "Common Patterns": [
            "d.copy()                   # Shallow copy",
            "dict(d)                    # Also creates copy",
            "len(d)                     # Number of items",
            "bool(d)                    # False if empty, True otherwise",
            "sorted(d.items())          # Sort by keys",
            "max(d, key=d.get)          # Key with maximum value",
            "min(d, key=d.get)          # Key with minimum value"
        ]
    }
    
    for section_title, items in reference_sections.items():
        print_subsection_header(section_title)
        for item in items:
            print(f"  {item}")
        print()

def common_pitfalls():
    """Show common pitfalls and how to avoid them."""
    print_subsection_header("Common Pitfalls")
    
    pitfalls = [
        {
            "title": "Mutable Default Arguments",
            "wrong": "def add_item(item, d={}):  # DON'T DO THIS",
            "right": "def add_item(item, d=None):\n    if d is None:\n        d = {}",
            "explanation": "Default mutable arguments are shared between function calls"
        },
        {
            "title": "KeyError vs get() Method",
            "wrong": "value = d['key']  # Raises KeyError if key missing",
            "right": "value = d.get('key', default_value)",
            "explanation": "Use get() for safe access or check with 'in' operator first"
        },
        {
            "title": "Modifying Dictionary During Iteration",
            "wrong": "for key in d:\n    if condition:\n        del d[key]  # RuntimeError!",
            "right": "keys_to_remove = [k for k, v in d.items() if condition]\nfor k in keys_to_remove:\n    del d[k]",
            "explanation": "Collect keys to modify first, then modify dictionary"
        },
        {
            "title": "Dictionary vs List for Lookups",
            "wrong": "items = [('a', 1), ('b', 2)]  # Slow O(n) lookups",
            "right": "items = {'a': 1, 'b': 2}  # Fast O(1) lookups",
            "explanation": "Use dictionaries for fast key-based lookups"
        }
    ]
    
    for i, pitfall in enumerate(pitfalls, 1):
        print(f"{i}. {pitfall['title']}")
        print(f"   Wrong: {pitfall['wrong']}")
        print(f"   Right: {pitfall['right']}")
        print(f"   Why: {pitfall['explanation']}")
        print()

# =============================================================================
# MAIN EXECUTION AND MENU SYSTEM
# =============================================================================

def show_menu():
    """Display the main menu."""
    menu_items = [
        ("1", "Dictionary Basics", dictionary_basics),
        ("2", "Creation Methods", dictionary_creation_methods),
        ("3", "Basic Operations", basic_operations),
        ("4", "Dictionary Methods", dictionary_methods),
        ("5", "Dictionary Comprehensions", dictionary_comprehensions),
        ("6", "Iteration Techniques", iteration_techniques),
        ("7", "Advanced Techniques", advanced_techniques),
        ("8", "Nested Dictionaries", nested_dictionaries),
        ("9", "Real-World Examples", real_world_examples),
        ("10", "Quick Reference", quick_reference),
        ("11", "Common Pitfalls", common_pitfalls),
        ("A", "All Sections", run_all_sections),
        ("T", "Table of Contents", show_table_of_contents),
        ("Q", "Quit", None)
    ]
    
    print("\n" + "=" * 60)
    print(" PYTHON DICTIONARIES GUIDE - MAIN MENU ".center(60, "="))
    print("=" * 60)
    
    for key, title, _ in menu_items:
        print(f"  {key}. {title}")
    
    print("=" * 60)
    return menu_items

def run_all_sections():
    """Run all sections in sequence."""
    sections = [
        ("Dictionary Basics", dictionary_basics),
        ("Creation Methods", dictionary_creation_methods),
        ("Basic Operations", basic_operations),
        ("Dictionary Methods", dictionary_methods),
        ("Dictionary Comprehensions", dictionary_comprehensions),
        ("Iteration Techniques", iteration_techniques),
        ("Advanced Techniques", advanced_techniques),
        ("Nested Dictionaries", nested_dictionaries),
        ("Real-World Examples", real_world_examples),
        ("Quick Reference", quick_reference),
        ("Common Pitfalls", common_pitfalls)
    ]
    
    print_section_header("RUNNING ALL SECTIONS")
    print("This will run through all sections of the dictionary guide.")
    print("Each section includes examples and demonstrations.")
    
    for i, (title, func) in enumerate(sections, 1):
        print(f"\nRunning Section {i}/{len(sections)}: {title}")
        run_example(func)
        
        if i < len(sections):
            pause_for_user()

def main():
    """Main function to run the guide."""
    print("Welcome to the Complete Python Dictionaries Guide!")
    print("This interactive guide will teach you everything about Python dictionaries.")
    
    # Show table of contents first
    show_table_of_contents()
    
    while True:
        menu_items = show_menu()
        choice = input("\nEnter your choice: ").strip().upper()
        
        # Find the selected menu item
        selected_item = None
        for key, title, func in menu_items:
            if key.upper() == choice:
                selected_item = (key, title, func)
                break
        
        if not selected_item:
            print("Invalid choice. Please try again.")
            continue
        
        key, title, func = selected_item
        
        if key.upper() == "Q":
            print("\nThank you for using the Python Dictionaries Guide!")
            print("Happy coding with Python dictionaries!")
            break
        
        if func:
            print(f"\nRunning: {title}")
            run_example(func)
            
            # Ask if user wants to continue
            continue_choice = input("\nPress Enter to return to menu (or 'q' to quit): ").strip().lower()
            if continue_choice == 'q':
                print("\nThank you for using the Python Dictionaries Guide!")
                break

if __name__ == "__main__":
    main()