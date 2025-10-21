import random
import re
from termcolor import colored
'''
re module
- used for working with regular expressions, which allow for advanced string searching and manipulation
- provides functions to search, match, and manipulate strings based on specific patterns
- commonly used for tasks such as:
    - validating input formats (e.g., email addresses, phone numbers)
    - searching for specific patterns within text
    - replacing substrings based on patterns
    - splitting strings using complex delimiters
- key functions:
    - re.match(): checks for a match only at the beginning of the string
    - re.search(): searches the entire string for a match
    - re.findall(): finds all occurrences of a pattern in a string and returns them as a list
    - re.sub(): replaces occurrences of a pattern with a specified replacement string

'''

print(colored("\n" + "="*30 + " Dictionary Comprehension " + "="*30, 'yellow', "on_blue", attrs=['bold']))

# =============================================================================
# 1. Create a new dictionary from an iterable
# =============================================================================
'''
Keyword Method: {new_key: new_value for item in list}
'''
names_list = ["Tatum", "Clayton", "Reed", "James", "Shannon", "Ace", "Mike", "Jane", "Will", "Lisa"]
score_dict = {name: random.randint(75, 100) for name in names_list}# this will create a dictionary with names as keys and random scores between 75 and 100 as values
print(colored(
            "\n" + "="*63 + \
            "\n1. From the names list create a dictionary with names as" \
            "\nkeys and random scores between 75 and 100 as values"
            "\n" + "="*63, 
            'yellow'
            ))
print(colored(f'Names List: {names_list}', 'cyan'))
print(colored(f'Scores Dictionary: {score_dict}', 'magenta'))# returns something like {'Tatum': 89, 'Clayton': 86, 'Reed': 98, 'James': 84, 'Shannon': 94, 'Ace': 98, 'Mike': 80, 'Jane': 83, 'Will': 75, 'Lisa': 86}
print(colored("-"*100, 'yellow'))
# ====================================================================================================


# ======================================================================================================================================
# 2. Create a dictionary that takes each word in the given sentence and calculates the number of letters in each word
# ======================================================================================================================================
'''
Keyword Method: {item: value for item in list}
'''
sentence = "Do you want to learn python?"
word_dict = {item: len(item) for item in sentence.split(" ")}
print(colored(
            "\n" + "="*63 + \
            "\n2. Count the number of letters in each word"
            "\n" + "="*63, 
            'yellow'
            ))
print(colored(f'Sentence: "{sentence}"', 'cyan'))
print(colored(f'Word Count Dictionary: {word_dict}', 'magenta'))# returns {'Do': 2, 'you': 3, 'want': 4, 'to': 2, 'learn': 5, 'python?': 7}
print(colored("-"*100, 'yellow'))
# =======================================================================================================================================


# ==================================================================================================================================================
# 3. Create a dictionary that takes each word in the given sentence and calculates the number of letters in each word(ignoring punctuation marks)
# ==================================================================================================================================================
'''
re module: used to split the sentence using regex to keep only words

Keyword Method: {item: value for item in list}
'''
word_dict2 = {item: len(item) for item in re.findall(r'\b\w+\b', sentence)}
print(colored(
            "\n" + "="*75 + \
            "\n3. Count the number of letters in each word(ignoring punctuation marks)"
            "\n" + "="*75, 
            'yellow'
            ))
print(colored(f'Sentence: "{sentence}"', 'cyan'))
print(colored(f'Word Count Dictionary: {word_dict2}', 'magenta'))# returns {'Do': 2, 'you': 3, 'want': 4, 'to': 2, 'learn': 5, 'python': 6}
print(colored("-"*100, 'yellow'))
# ===================================================================================================================================================


# =============================================================================
# 4. Create a new dictionary based on values in an existing dictionary
# =============================================================================
'''
Keyword Method: {key: value_expression for (key, value) in existing_dict.items()}
'''
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {weekday: (c_degree * 9/5) + 32 for (weekday, c_degree) in weather_c.items()}
print(colored(
            "\n" + "="*68 + \
            "\n4. Use the celsius values to create a new dictionary (Fahrenheit)"
            "\n" + "="*68, 
            'yellow'
            ))
print(colored(f'Existing dictionary (Celsius): {weather_c}', 'cyan'))
print(colored(f'New dictionary: {weather_f}', 'magenta'))# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
print(colored("-"*100, 'yellow'))
# ====================================================================================================


# ====================================================================================================
# 5. Create a new dictionary with the key and value of each student that has a score of 90 or above
# ====================================================================================================
'''
Keyword Method: new_dict = {key_expression: value_expression for item in iterable if condition}
'''
score_dict = {'Tatum': 75, 'Clayton': 83, 'Reed': 75, 'James': 92, 'Shannon': 78, 'Ace': 100, 'Mike': 90, 'Jane': 92, 'Will': 84, 'Lisa': 79}
a_students = {name: score for (name, score) in score_dict.items() if score >= 90}
print(colored(
            "\n" + "="*123 + \
            "\n5. FILTERING WITH IF CLAUSE: Create a new dictionary with the key and value of each student that has a scored above 90" \
            "\n" + "="*123,
            'yellow'
            ))
print(colored(f'Existing Dictionary: {score_dict}', 'cyan'))
print(colored(f'New Dictionary: {a_students}', 'magenta'))# returns {'James': 92, 'Ace': 100, 'Mike': 90, 'Jane': 92}
print(colored("-"*100, 'yellow'))
# ====================================================================================================


# =============================================================================
# 6. Create a new dictionary based on values in an existing dictionary
# =============================================================================
'''
Keyword Method: {key: (value_if_true if condition else value_if_false) for item in iterable}
'''
pass_failed = {name: ("Pass" if score >= 90 else "Failed") for (name, score) in score_dict.items()}
print(colored(
            "\n" + "="*113 + \
            "\n6. CONDITIONAL VALUE ASSIGNMENT: Create a new dictionary that assigns 'Pass' or 'Failed' based on scores" \
            "\n" + "="*113,
            'yellow'
            ))
print(colored(f'Existing Dictionary: {score_dict}', 'cyan'))
print(colored(f'New Dictionary: {pass_failed}', 'magenta'))# returns something like {'Tatum': 'Failed', 'Clayton': 'Failed', 'Reed': 'Failed', 'James': 'Pass', 'Shannon': 'Failed', 'Ace': 'Pass', 'Mike': 'Pass', 'Jane': 'Pass', 'Will': 'Failed', 'Lisa': 'Failed'}
print(colored("-"*100, 'yellow'))
# ====================================================================================================