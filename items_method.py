'''
dict.items() 
- a method of dictionary objects that returns a view object
    - a dynamic "view" of the dictionary's contents
    -  if the original dictionary is modified, the dict_items view object will automatically reflect those changes
- the view object displays a list of the dictionary's key-value tuple pairs
    - presents the dictionary's contents as a sequence of tuples
    - where each tuple contains a (key, value) pair from the dictionary
- commonly used in for loops to iterate over both the keys and values of a dictionary simultaneously
'''

# =============================================================================

print("\n================ dict.items() ================")
my_dict = {"name": "Rick", "age": 36, "city": "Las Vegas"}
student_grades = {"Lisa": 95, "James": 97, "Rick": 92}

# Get the items view object
items_view = my_dict.items()
print(items_view)# dict_items([('name', 'Rick'), ('age', 36), ('city', 'Las Vegas')])
print("------------------------------------------------------------")

# Tuple unpacking examples
    # Automatically unpacks: key = "value"

# Iterate through the items
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
'''
# Output:
Key: name, Value: Rick
Key: age, Value: 36
Key: city, Value: Las Vegas
'''
print("------------------------------------------------------------")

for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")
'''
# Output:
Student: Lisa, Grade: 95
Student: James, Grade: 97
Student: Rick, Grade: 92
'''
print("------------------------------------------------------------")

# Demonstrate the dynamic nature of the view
my_dict["occupation"] = "Developer"
print(items_view)# dict_items([('name', 'Rick'), ('age', 36), ('city', 'Las Vegas'), ('occupation', 'Developer')])
print("------------------------------------------------------------")