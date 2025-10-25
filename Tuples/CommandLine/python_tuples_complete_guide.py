"""
COMPLETE GUIDE TO PYTHON TUPLES
===============================

A comprehensive guide to working with Python tuples, covering everything from basic operations
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
    print_section_header("PYTHON TUPLES - COMPLETE GUIDE", "=")
    
    toc = """
TABLE OF CONTENTS:

1. Tuple Basics - Creation, Access, and Properties
2. Tuple Operations - Indexing, Slicing, and Concatenation
3. Tuple Methods - Essential built-in methods
4. Tuple Unpacking - Extracting values efficiently
5. Tuple Iteration - Various ways to loop through tuples
6. Named Tuples - Creating structured data
7. Tuple Comprehensions - Using generator expressions
8. Nested Tuples - Working with complex structures
9. Tuple vs List - Performance comparisons
10. Advanced Techniques - Sorting, searching, and more
11. Real-world Applications - Practical examples
12. Common Pitfalls - What to avoid and best practices
    """
    
    print(toc)
    print("\n" + "=" * 80)
    print("Choose a section number (1-12) or 'all' to run everything:")

# =============================================================================
# 1. TUPLE BASICS - CREATION, ACCESS, AND PROPERTIES
# =============================================================================

def tuple_creation_examples():
    """Demonstrate different ways to create tuples."""
    print_section_header("1. TUPLE CREATION EXAMPLES")
    
    print(">>> Creating Empty Tuples:")
    empty_tuple1 = ()
    empty_tuple2 = tuple()
    print(f"empty_tuple1 = (): {empty_tuple1}")
    print(f"empty_tuple2 = tuple(): {empty_tuple2}")
    print(f"Type: {type(empty_tuple1)}")
    
    print("\n>>> Creating Tuples with Values:")
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    mixed = (1, "hello", 3.14, True)
    print(f"coordinates: {coordinates}")
    print(f"colors: {colors}")
    print(f"mixed: {mixed}")
    
    print("\n>>> Single Element Tuples (Note the comma!):")
    single = (42,)  # Comma is required!
    not_tuple = (42)  # This is just a number in parentheses
    print(f"single = (42,): {single}, type: {type(single)}")
    print(f"not_tuple = (42): {not_tuple}, type: {type(not_tuple)}")
    
    print("\n>>> Creating Tuples without Parentheses:")
    point = 3, 4, 5
    name_age = "Alice", 25
    print(f"point = 3, 4, 5: {point}")
    print(f"name_age = 'Alice', 25: {name_age}")
    
    print("\n>>> Using tuple() Constructor:")
    from_list = tuple([1, 2, 3, 4])
    from_string = tuple("hello")
    from_range = tuple(range(5))
    print(f"from_list: {from_list}")
    print(f"from_string: {from_string}")
    print(f"from_range: {from_range}")

def tuple_properties():
    """Demonstrate tuple properties and characteristics."""
    print_section_header("TUPLE PROPERTIES AND CHARACTERISTICS")
    
    sample_tuple = (1, 2, 3, 2, 4, 2)
    
    print(">>> Immutability:")
    print(f"Original tuple: {sample_tuple}")
    try:
        sample_tuple[0] = 10  # This will raise an error
    except TypeError as e:
        print(f"Trying to modify: TypeError - {e}")
    
    print("\n>>> Ordered Collection:")
    print(f"First element (index 0): {sample_tuple[0]}")
    print(f"Last element (index -1): {sample_tuple[-1]}")
    print(f"Elements maintain order: {sample_tuple}")
    
    print("\n>>> Allow Duplicates:")
    print(f"Count of '2': {sample_tuple.count(2)}")
    print(f"All elements: {sample_tuple}")
    
    print("\n>>> Length and Membership:")
    print(f"Length: {len(sample_tuple)}")
    print(f"Is 3 in tuple? {3 in sample_tuple}")
    print(f"Is 10 in tuple? {10 in sample_tuple}")

def tuple_indexing_slicing():
    """Demonstrate tuple indexing and slicing."""
    print_section_header("TUPLE INDEXING AND SLICING")
    
    fruits = ("apple", "banana", "cherry", "date", "elderberry")
    print(f"Fruits tuple: {fruits}")
    
    print("\n>>> Positive Indexing:")
    for i in range(len(fruits)):
        print(f"Index {i}: {fruits[i]}")
    
    print("\n>>> Negative Indexing:")
    for i in range(-1, -len(fruits)-1, -1):
        print(f"Index {i}: {fruits[i]}")
    
    print("\n>>> Slicing Examples:")
    print(f"fruits[1:4]: {fruits[1:4]}")
    print(f"fruits[:3]: {fruits[:3]}")
    print(f"fruits[2:]: {fruits[2:]}")
    print(f"fruits[::2]: {fruits[::2]}")
    print(f"fruits[::-1]: {fruits[::-1]}")

# =============================================================================
# 2. TUPLE OPERATIONS
# =============================================================================

def tuple_operations():
    """Demonstrate tuple operations."""
    print_section_header("2. TUPLE OPERATIONS")
    
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    print(">>> Concatenation:")
    concatenated = tuple1 + tuple2
    print(f"tuple1: {tuple1}")
    print(f"tuple2: {tuple2}")
    print(f"tuple1 + tuple2: {concatenated}")
    
    print("\n>>> Repetition:")
    repeated = tuple1 * 3
    print(f"tuple1 * 3: {repeated}")
    
    print("\n>>> Comparison:")
    print(f"tuple1 == (1, 2, 3): {tuple1 == (1, 2, 3)}")
    print(f"tuple1 < (1, 2, 4): {tuple1 < (1, 2, 4)}")
    print(f"tuple1 > (0, 9, 9): {tuple1 > (0, 9, 9)}")
    
    print("\n>>> Membership Testing:")
    print(f"2 in tuple1: {2 in tuple1}")
    print(f"7 not in tuple1: {7 not in tuple1}")

# =============================================================================
# 3. TUPLE METHODS
# =============================================================================

def tuple_methods():
    """Demonstrate tuple methods."""
    print_section_header("3. TUPLE METHODS")
    
    sample = (1, 2, 3, 2, 4, 2, 5)
    print(f"Sample tuple: {sample}")
    
    print("\n>>> count() method:")
    print(f"sample.count(2): {sample.count(2)}")
    print(f"sample.count(10): {sample.count(10)}")
    
    print("\n>>> index() method:")
    print(f"sample.index(3): {sample.index(3)}")
    print(f"sample.index(2): {sample.index(2)}")  # Returns first occurrence
    
    try:
        print(f"sample.index(10): {sample.index(10)}")
    except ValueError as e:
        print(f"sample.index(10): ValueError - {e}")
    
    print("\n>>> index() with start parameter:")
    print(f"sample.index(2, 2): {sample.index(2, 2)}")  # Start search from index 2

# =============================================================================
# 4. TUPLE UNPACKING
# =============================================================================

def tuple_unpacking():
    """Demonstrate tuple unpacking techniques."""
    print_section_header("4. TUPLE UNPACKING")
    
    print(">>> Basic Unpacking:")
    point = (10, 20)
    x, y = point
    print(f"point = {point}")
    print(f"x, y = point")
    print(f"x = {x}, y = {y}")
    
    print("\n>>> Multiple Assignment:")
    name, age, city = ("Alice", 30, "New York")
    print(f"name, age, city = ('Alice', 30, 'New York')")
    print(f"name = {name}, age = {age}, city = {city}")
    
    print("\n>>> Swapping Variables:")
    a, b = 10, 20
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
    
    print("\n>>> Extended Unpacking (Python 3+):")
    numbers = (1, 2, 3, 4, 5, 6)
    first, second, *rest, last = numbers
    print(f"numbers = {numbers}")
    print(f"first = {first}")
    print(f"second = {second}")
    print(f"rest = {rest}")
    print(f"last = {last}")
    
    print("\n>>> Unpacking in Function Arguments:")
    def greet(name, age, city):
        return f"Hello {name}, age {age}, from {city}"
    
    person = ("Bob", 25, "Boston")
    greeting = greet(*person)
    print(f"person = {person}")
    print(f"greet(*person): {greeting}")

def tuple_unpacking_advanced():
    """Advanced tuple unpacking examples."""
    print_section_header("ADVANCED TUPLE UNPACKING")
    
    print(">>> Nested Tuple Unpacking:")
    nested = ((1, 2), (3, 4), (5, 6))
    (a, b), (c, d), (e, f) = nested
    print(f"nested = {nested}")
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
    
    print("\n>>> Ignoring Values with Underscore:")
    data = ("John", 30, "Engineer", "New York")
    name, age, _, city = data
    print(f"data = {data}")
    print(f"name = {name}, age = {age}, city = {city}")
    print("(profession ignored with _)")
    
    print("\n>>> Unpacking in Loops:")
    coordinates = [(1, 2), (3, 4), (5, 6)]
    print("coordinates =", coordinates)
    print("Unpacking in for loop:")
    for x, y in coordinates:
        print(f"  Point: x={x}, y={y}")

# =============================================================================
# 5. TUPLE ITERATION
# =============================================================================

def tuple_iteration():
    """Demonstrate various ways to iterate through tuples."""
    print_section_header("5. TUPLE ITERATION TECHNIQUES")
    
    colors = ("red", "green", "blue", "yellow")
    print(f"colors = {colors}")
    
    print("\n>>> Basic Iteration:")
    for color in colors:
        print(f"  Color: {color}")
    
    print("\n>>> Iteration with Index:")
    for i, color in enumerate(colors):
        print(f"  Index {i}: {color}")
    
    print("\n>>> Iteration with Index (manual):")
    for i in range(len(colors)):
        print(f"  Index {i}: {colors[i]}")
    
    print("\n>>> Reverse Iteration:")
    for color in reversed(colors):
        print(f"  Color: {color}")
    
    print("\n>>> Iterating Multiple Tuples:")
    sizes = ("small", "medium", "large", "extra-large")
    print(f"sizes = {sizes}")
    print("Zipped iteration:")
    for color, size in zip(colors, sizes):
        print(f"  {size} {color}")

# =============================================================================
# 6. NAMED TUPLES
# =============================================================================

def named_tuples():
    """Demonstrate named tuples."""
    print_section_header("6. NAMED TUPLES")
    
    from collections import namedtuple
    
    print(">>> Creating Named Tuple Class:")
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', 'name age city')
    
    print("Point = namedtuple('Point', ['x', 'y'])")
    print("Person = namedtuple('Person', 'name age city')")
    
    print("\n>>> Creating Named Tuple Instances:")
    p1 = Point(10, 20)
    p2 = Point(x=30, y=40)
    person1 = Person("Alice", 30, "New York")
    
    print(f"p1 = Point(10, 20): {p1}")
    print(f"p2 = Point(x=30, y=40): {p2}")
    print(f"person1 = Person('Alice', 30, 'New York'): {person1}")
    
    print("\n>>> Accessing Named Tuple Fields:")
    print(f"p1.x: {p1.x}")
    print(f"p1.y: {p1.y}")
    print(f"person1.name: {person1.name}")
    print(f"person1.age: {person1.age}")
    
    print("\n>>> Named Tuple Methods:")
    print(f"p1._asdict(): {p1._asdict()}")
    print(f"person1._replace(age=31): {person1._replace(age=31)}")
    print(f"Point._fields: {Point._fields}")
    
    print("\n>>> Named Tuples are Still Tuples:")
    print(f"isinstance(p1, tuple): {isinstance(p1, tuple)}")
    print(f"p1[0]: {p1[0]}")  # Access by index
    print(f"len(person1): {len(person1)}")

# =============================================================================
# 7. TUPLE COMPREHENSIONS (Generator Expressions)
# =============================================================================

def tuple_comprehensions():
    """Demonstrate tuple comprehensions using generator expressions."""
    print_section_header("7. TUPLE COMPREHENSIONS")
    
    print(">>> Generator Expression to Tuple:")
    squares = tuple(x**2 for x in range(1, 6))
    print(f"squares = tuple(x**2 for x in range(1, 6))")
    print(f"squares: {squares}")
    
    print("\n>>> Filtering with Conditions:")
    even_squares = tuple(x**2 for x in range(1, 11) if x % 2 == 0)
    print(f"even_squares = tuple(x**2 for x in range(1, 11) if x % 2 == 0)")
    print(f"even_squares: {even_squares}")
    
    print("\n>>> String Operations:")
    words = ["hello", "world", "python", "tuples"]
    upper_words = tuple(word.upper() for word in words)
    print(f"words: {words}")
    print(f"upper_words = tuple(word.upper() for word in words)")
    print(f"upper_words: {upper_words}")
    
    print("\n>>> Nested Generator Expressions:")
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    flattened = tuple(num for row in matrix for num in row)
    print(f"matrix: {matrix}")
    print(f"flattened = tuple(num for row in matrix for num in row)")
    print(f"flattened: {flattened}")
    
    print("\n>>> Complex Transformations:")
    coordinates = ((1, 2), (3, 4), (5, 6))
    distances = tuple((x**2 + y**2)**0.5 for x, y in coordinates)
    print(f"coordinates: {coordinates}")
    print(f"distances = tuple((x**2 + y**2)**0.5 for x, y in coordinates)")
    print(f"distances: {distances}")

# =============================================================================
# 8. NESTED TUPLES
# =============================================================================

def nested_tuples():
    """Demonstrate working with nested tuples."""
    print_section_header("8. NESTED TUPLES")
    
    print(">>> Creating Nested Tuples:")
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    contacts = (("Alice", "123-456"), ("Bob", "789-012"), ("Carol", "345-678"))
    print(f"matrix: {matrix}")
    print(f"contacts: {contacts}")
    
    print("\n>>> Accessing Nested Elements:")
    print(f"matrix[1]: {matrix[1]}")
    print(f"matrix[1][2]: {matrix[1][2]}")
    print(f"contacts[0][0]: {contacts[0][0]}")
    
    print("\n>>> Iterating Through Nested Tuples:")
    print("Matrix elements:")
    for row in matrix:
        for element in row:
            print(f"  {element}", end=" ")
        print()
    
    print("\nContacts:")
    for name, phone in contacts:
        print(f"  {name}: {phone}")
    
    print("\n>>> Nested Tuple Operations:")
    # Finding maximum in each row
    row_maxes = tuple(max(row) for row in matrix)
    print(f"row_maxes = tuple(max(row) for row in matrix)")
    print(f"row_maxes: {row_maxes}")
    
    # Transpose matrix
    transposed = tuple(zip(*matrix))
    print(f"transposed = tuple(zip(*matrix))")
    print(f"transposed: {transposed}")

# =============================================================================
# 9. TUPLE VS LIST COMPARISON
# =============================================================================

def tuple_vs_list():
    """Compare tuples with lists."""
    print_section_header("9. TUPLE VS LIST COMPARISON")
    
    import sys
    import time
    
    # Create test data
    tuple_data = tuple(range(1000))
    list_data = list(range(1000))
    
    print(">>> Memory Usage:")
    print(f"Tuple size: {sys.getsizeof(tuple_data)} bytes")
    print(f"List size: {sys.getsizeof(list_data)} bytes")
    print(f"Tuple is {(sys.getsizeof(list_data) / sys.getsizeof(tuple_data)):.1f}x smaller")
    
    print("\n>>> Access Speed (1M operations):")
    
    # Tuple access
    start = time.time()
    for _ in range(1000000):
        _ = tuple_data[500]
    tuple_time = time.time() - start
    
    # List access
    start = time.time()
    for _ in range(1000000):
        _ = list_data[500]
    list_time = time.time() - start
    
    print(f"Tuple access time: {tuple_time:.4f} seconds")
    print(f"List access time: {list_time:.4f} seconds")
    
    print("\n>>> Mutability Difference:")
    sample_list = [1, 2, 3]
    sample_tuple = (1, 2, 3)
    
    print(f"Original list: {sample_list}")
    sample_list[0] = 99
    print(f"Modified list: {sample_list}")
    
    print(f"Original tuple: {sample_tuple}")
    try:
        sample_tuple[0] = 99
    except TypeError as e:
        print(f"Trying to modify tuple: {e}")

# =============================================================================
# 10. ADVANCED TECHNIQUES
# =============================================================================

def advanced_techniques():
    """Demonstrate advanced tuple techniques."""
    print_section_header("10. ADVANCED TECHNIQUES")
    
    print(">>> Sorting Tuples:")
    points = [(3, 2), (1, 4), (5, 1), (2, 3)]
    print(f"Original points: {points}")
    
    # Sort by first element
    sorted_by_x = sorted(points)
    print(f"Sorted by x: {sorted_by_x}")
    
    # Sort by second element
    sorted_by_y = sorted(points, key=lambda p: p[1])
    print(f"Sorted by y: {sorted_by_y}")
    
    # Sort by distance from origin
    sorted_by_distance = sorted(points, key=lambda p: (p[0]**2 + p[1]**2)**0.5)
    print(f"Sorted by distance: {sorted_by_distance}")
    
    print("\n>>> Using Tuples as Dictionary Keys:")
    grid = {}
    grid[(0, 0)] = "origin"
    grid[(1, 0)] = "right"
    grid[(0, 1)] = "up"
    grid[(1, 1)] = "diagonal"
    
    print("Grid dictionary with tuple keys:")
    for position, description in grid.items():
        print(f"  {position}: {description}")
    
    print("\n>>> Tuple Return Values:")
    def get_name_age():
        return "Alice", 30
    
    def get_coordinates():
        return 10, 20, 30
    
    name, age = get_name_age()
    x, y, z = get_coordinates()
    print(f"get_name_age() returned: name='{name}', age={age}")
    print(f"get_coordinates() returned: x={x}, y={y}, z={z}")

# =============================================================================
# 11. REAL-WORLD APPLICATIONS
# =============================================================================

def real_world_applications():
    """Demonstrate real-world tuple applications."""
    print_section_header("11. REAL-WORLD APPLICATIONS")
    
    print(">>> Configuration Settings (Immutable):")
    DATABASE_CONFIG = ("localhost", 5432, "mydb", "user", "password")
    API_ENDPOINTS = (
        ("users", "/api/users"),
        ("posts", "/api/posts"),
        ("comments", "/api/comments")
    )
    
    host, port, db_name, user, password = DATABASE_CONFIG
    print(f"Database: {db_name} at {host}:{port}")
    
    print("\nAPI Endpoints:")
    for name, endpoint in API_ENDPOINTS:
        print(f"  {name}: {endpoint}")
    
    print("\n>>> Coordinate Systems:")
    class Point3D:
        def __init__(self, x, y, z):
            self.coordinates = (x, y, z)
        
        def __str__(self):
            return f"Point3D{self.coordinates}"
        
        def distance_from_origin(self):
            x, y, z = self.coordinates
            return (x**2 + y**2 + z**2)**0.5
    
    point = Point3D(3, 4, 5)
    print(f"3D Point: {point}")
    print(f"Distance from origin: {point.distance_from_origin():.2f}")
    
    print("\n>>> RGB Color Representation:")
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0)
    }
    
    print("Color palette:")
    for color_name, rgb in colors.items():
        r, g, b = rgb
        print(f"  {color_name}: RGB({r}, {g}, {b})")
    
    print("\n>>> Function Return Multiple Values:")
    def analyze_numbers(numbers):
        if not numbers:
            return 0, 0, 0, 0
        return min(numbers), max(numbers), sum(numbers), len(numbers)
    
    data = [10, 5, 8, 3, 15, 12]
    minimum, maximum, total, count = analyze_numbers(data)
    average = total / count if count > 0 else 0
    
    print(f"Numbers: {data}")
    print(f"Analysis: min={minimum}, max={maximum}, sum={total}, count={count}, avg={average:.2f}")

# =============================================================================
# 12. COMMON PITFALLS AND BEST PRACTICES
# =============================================================================

def common_pitfalls():
    """Demonstrate common pitfalls and best practices."""
    print_section_header("12. COMMON PITFALLS AND BEST PRACTICES")
    
    print(">>> Single Element Tuple Pitfall:")
    print("WRONG: single_element = (42)")
    single_element = (42)
    print(f"Result: {single_element}, type: {type(single_element)}")
    
    print("CORRECT: single_element = (42,)")
    single_element = (42,)
    print(f"Result: {single_element}, type: {type(single_element)}")
    
    print("\n>>> Tuple Concatenation vs List Append:")
    print("Inefficient for multiple additions:")
    numbers = (1, 2, 3)
    print(f"Original: {numbers}")
    numbers = numbers + (4,)  # Creates new tuple
    numbers = numbers + (5,)  # Creates another new tuple
    print(f"After additions: {numbers}")
    
    print("\nBetter approach for multiple additions:")
    temp_list = list(numbers)
    temp_list.extend([6, 7, 8])
    numbers = tuple(temp_list)
    print(f"Final result: {numbers}")
    
    print("\n>>> Mutable Objects in Tuples:")
    mutable_tuple = ([1, 2], [3, 4])
    print(f"Original: {mutable_tuple}")
    mutable_tuple[0].append(3)  # This works!
    print(f"After modifying list inside: {mutable_tuple}")
    print("Note: The tuple structure is immutable, but contents can be mutable")
    
    print("\n>>> Best Practices:")
    practices = [
        "Use tuples for heterogeneous data (name, age, city)",
        "Use tuples for coordinates and points",
        "Use tuples as dictionary keys when you need composite keys",
        "Use named tuples for better code readability",
        "Don't forget the comma for single-element tuples",
        "Use tuple unpacking for multiple return values",
        "Consider tuples for configuration that shouldn't change"
    ]
    
    for i, practice in enumerate(practices, 1):
        print(f"{i}. {practice}")

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main program to run the tuple guide."""
    
    # Dictionary mapping section numbers to functions
    sections = {
        1: tuple_creation_examples,
        2: tuple_operations,
        3: tuple_methods,
        4: tuple_unpacking,
        5: tuple_iteration,
        6: named_tuples,
        7: tuple_comprehensions,
        8: nested_tuples,
        9: tuple_vs_list,
        10: advanced_techniques,
        11: real_world_applications,
        12: common_pitfalls
    }
    
    # Additional demonstrations
    additional_demos = {
        'properties': tuple_properties,
        'indexing': tuple_indexing_slicing,
        'unpacking_advanced': tuple_unpacking_advanced
    }
    
    show_table_of_contents()
    
    while True:
        try:
            choice = input().strip().lower()
            
            if choice == 'quit' or choice == 'exit':
                print("Thanks for learning about Python tuples!")
                break
            elif choice == 'all':
                print("Running all sections...")
                for section_num in sorted(sections.keys()):
                    run_example(sections[section_num])
                    if section_num < max(sections.keys()):
                        pause_for_user()
                break
            elif choice.isdigit():
                section_num = int(choice)
                if section_num in sections:
                    run_example(sections[section_num])
                    
                    # Run additional demos for certain sections
                    if section_num == 1:
                        run_example(tuple_properties)
                        run_example(tuple_indexing_slicing)
                    elif section_num == 4:
                        run_example(tuple_unpacking_advanced)
                    
                    print(f"\nSection {section_num} completed!")
                    print("Enter another section number, 'all' for everything, or 'quit' to exit:")
                else:
                    print(f"Invalid section number. Please choose 1-{max(sections.keys())}")
            elif choice == 'toc':
                show_table_of_contents()
            else:
                print("Invalid choice. Enter a section number (1-12), 'all', 'toc', or 'quit'")
                
        except KeyboardInterrupt:
            print("\n\nThanks for learning about Python tuples!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()