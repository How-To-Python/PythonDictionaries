print("\n================ Dictionary Processing Patterns ================")

student_grades = {
    "Lisa": 95,
    "James": 97,
    "Rick": 92
}

print("\nPattern 1: Keys Only:")
# Pattern 1: Keys only
for student in student_grades.keys():
    print(student)
print("------------------------------------------------------------")

print("\nPattern 2: Values Only:") 
for grade in student_grades.values():
    print(grade)
print("------------------------------------------------------------")



# dict.items() creates tuples of key-value pairs: ("Lisa", 95), ("James", 97), ("Rick", 92)

print("\nPattern 3: Key-value pairs WITHOUT tuple unpacking:")#verbose
for item in student_grades.items():
    # item = ("Lisa", 95)  # First iteration
    # Must use indexing:
    print(f"Student: {item[0]}, Grade: {item[1]}")

print("\nPattern 4: Key-value pairs WITH tuple unpacking:")# (preferred)
for student, grade in student_grades.items():  # Tuple unpacking!
    # Automatically unpacks: student = "Lisa", grade = 95
    # Direct variable access - no indexing needed
    print(f"Student: {student}, Grade: {grade}")