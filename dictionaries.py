from termcolor import colored

from shannon_utils import color_256, rgb_color

print(color_256("\n============================== Dictionary Basics ==============================",fg=51, bg=46, bold=True, underline=True))


'''
using empty curly braces {} you can
    - create an empty dictionary
    - wipe an existing dictionary by reassigning it to an empty dictionary
'''
# =============================================================================
# 1. Create Empty Dictionary
# =============================================================================
emp_phone_numbers = {}
print(colored(
            "================================================================" \
            "\n1. Create Empty Dictionary" \
            "\n================================================================",
            'yellow'
            ))
print(colored(f'Empty Dictionary: {emp_phone_numbers}', 'magenta'))# {}
print("------------------------------------------------------------")

# =============================================================================
# 2. Wipe Entire Dictionary
# =============================================================================
student_age = {'Tatum': 23, 'Clayton': 31, 'Reed': 28, 'James': 34}
print(colored(
            "================================================================" \
            "\n2. Wipe Entire Dictionary" \
            "\n================================================================",
            'yellow'
            ))
print(color_256(f'Original Dictionary: {student_age}', fg=46))
print("********************************************")
student_age = {}  # Wiping the dictionary
print(colored(f'Wiped Dictionary: {student_age}', 'magenta'))# {}
print("------------------------------------------------------------")



# =============================================================================
# 3. Create a dictionary with content
# =============================================================================
print(colored(
            "================================================================" \
            "\n3. Create a dictionary with content" \
            "\n================================================================",
            'yellow'
            ))
emp_phone_numbers = {"Lisa": 1234567890, "James": 9876540321, "Kim": 5673456288}
print(colored(f'Employee Phone Numbers: {emp_phone_numbers}', 'magenta'))# {'Lisa': 1234567890, 'James': 9876540321, 'Kim': 5673456288}
print("------------------------------------------------------------")

'''
using square brackets [] with a key you can
    - add a new key-value pair to an existing dictionary
        - if there is no such key, it will create a new entry with the new key and value
    - edit the value associated with an existing key in the dictionary
        - if the key already exists in the dictionary, it will change the value to the new value
'''
# =============================================================================
# 4. Editing Items in an existing dictionary
# =============================================================================
print(colored(
            "================================================================" \
            "\n4. Editing Items in an existing dictionary" \
            "\n================================================================",
            'yellow'
            ))
print(color_256(f'Original Employee Phone Numbers: {emp_phone_numbers}', fg=46))
print("********************************************")
emp_phone_numbers["James"] = 5432345678  # Editing James's phone number
print(colored(f'Updated Employee Phone Numbers: {emp_phone_numbers}', 'magenta'))# {'Lisa': 1234567890, 'James': 5432345678, 'Kim': 5673456288}
print("------------------------------------------------------------")


# =============================================================================
# 5. Adding Items to an existing dictionary
# =============================================================================
print(colored(
            "================================================================" \
            "\n5. Adding Items to an existing dictionary" \
            "\n================================================================",
            'yellow'
            ))
print(color_256(f'Original Employee Phone Numbers: {emp_phone_numbers}', fg=46))
print("********************************************")
emp_phone_numbers["Mary"] = 5432345678  # Adding Mary to the dictionary
print(colored(f'Updated Employee Phone Numbers: {emp_phone_numbers}', 'magenta'))# {'Lisa': 1234567890, 'James': 5432345678, 'Kim': 5673456288, 'Mary': 5432345678}
print("------------------------------------------------------------")


'''
using the pop() method you can
    - remove a key-value pair from the dictionary based on the specified key(index)
        - if the key exists, it will remove the key and its associated value
        - if the key does not exist, it will raise a KeyError unless a default value is provided
            - emp_phone_numbers.pop("Kate"")# will raise a KeyError
            - emp_phone_numbers.pop("Kate", "There is no Kate")# will return There is no Kate
    - returns the value associated with the removed key
'''
# =============================================================================
# 6. Removing Items by Index from an existing dictionary
# =============================================================================
print(colored(
            "================================================================" \
            "\n6. Removing Items by Index from an existing dictionary" \
            "\n================================================================",
            'yellow'
            ))
print(color_256(f'Original Employee Phone Numbers: {emp_phone_numbers}', fg=46))
print("********************************************")
emp_phone_numbers.pop("James")  # Removing James from the dictionary
print(colored(f'Updated Employee Phone Numbers: {emp_phone_numbers}', 'magenta'))# {'Lisa': 1234567890, 'Kim': 5673456288, 'Mary': 5432345678}
print("------------------------------------------------------------")


# #*************************************************ACCESSING VALUES******************************************************************


'''
you can access values in a dictionary using several methods:
    - Square Brackets(Bracket Notation) dict['key'], using the key
        - if the key does not exist, this method will raise a KeyError
        - use the the get() Method to avoid the KeyError, if the key does not exist
    - dict.get('key', default_value) Method, using the key
        - you can specify a default value to return if the key is not found
        - if the key does not exist, it returns None or the specified default value
    - dict.values() method
        - returns a view object containing all the values in the dictionary
    - dict.items() method
        - returns a view object containing all the key-value pairs in the dictionary
        - view object: dict_items([(key1, value1), (key2, value2), ...])
        - the view object can be iterated over to access each key-value pair
        - the view object can be converted to a list of tuples using list(dict.items())
'''
my_dict = {'name': 'Shannon', 'age': 37}
# =============================================================================
# 7. Accessing values
# =============================================================================
print(colored(
            "================================================================" \
            "\n7. Accessing Values" \
            "\n================================================================",
            'yellow'
            ))
print(color_256(f'Dictionary: {my_dict}', fg=46))
print("********************************************")
print(colored(f"Bracket Notation: my_dict['name'] =  {my_dict['name']}", 'magenta'))# Shannon
print(color_256(f"Bracket Notation with key that does not exist: my_dict['race'] =  KeyError: 'race'", fg=208))# KeyError
print(colored(f"Get Method: my_dict.get('age') =  {my_dict.get('age')}", 'magenta'))# 37
print(color_256(f"Get Method with Default: my_dict.get('race', 'Not Found') =  {my_dict.get('race', 'Not Found')}", fg=208))# Not Found
print(colored(f"Values Method: my_dict.values() =  {my_dict.values()}", 'magenta'))# dict_values(['Shannon', 37])
print(color_256(f"Items Method: my_dict.items() =  {my_dict.items()}", fg=208))#dict_items([('name', 'Shannon'), ('age', 37)])
print(colored(f"Items as List: list(my_dict.items()) =  {list(my_dict.items())}", 'magenta'))#list of tuples: [('name', 'Shannon'), ('age', 37)]
print("------------------------------------------------------------")


# =============================================================================
# 8.Get Key with the highest Value: max()
# =============================================================================
bids = {
    "Shannon": 215.0,
    "lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}
print(colored(
            "================================================================" \
            "\n8. Get Key with the highest Value: max()" \
            "\n================================================================",
            'yellow'
            ))

print(color_256(f'Dictionary: {bids}', fg=46))
print(colored(f"max(): {max(bids, key=bids.get)}", 'magenta'))#returns Molly
