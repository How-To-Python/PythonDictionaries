#**************************Create Empty/Wipe Entire Dictionary*********************************************
# You create an empty dictionary and wipe an exsiting dictionary using the same syntax
emp_phone_numbers = {}

#**************************Create Dictionary with content**************************************
emp_phone_numbers = {"Lisa": 1234567890, "James": 9876540321, "Kim": 5673456288}

#**************Editing Items and Adding new items to an existing dictionary********************
emp_phone_numbers["Mary"] = 5432345678
#Adding New item: if there is no key "Mary" then it's going to create a new entry with the new key and value
#Editing item:  if there is a key "Mary" already in the dictionary then it will change the value to the new value


#********************************Removing Items by index:pop()**********************
# removes the key-value pair associated with the specified key from the dictionary
emp_phone_numbers.pop("James")#returns 9876540321(value of James), returns the value associated with the removed key
# if the key is not found it will cause a KeyError, use default value to avoid KeyError
emp_phone_numbers.pop("Kate", "There is no Kate")# will return There is no Kate
#*************************************************ACCESSING VALUES******************************************************************

my_dict = {'name': 'Shannon', 'age': 37}

#*********************************Accessing values: Square Brackets []***************************************************************
# if the key does not exist, this method will raise a KeyError
print(f"square brackets:  {my_dict['name']}")# Shannon
#my_dict['number']# will raise a KeyError

#*********************************Accessing values: get() Method*********************************************************************
# use the the get() Method to avoid the KeyError, if the key does not exist
# you can specify a default value to return if the key is not found
print(f".get(), no default:  {my_dict.get("number")}")# Returns None if the number key is not found
print(f".get(), with default:  {my_dict.get("number", "Unknown")}")#Returns "Unknown" if "number" key is not found

#*********************************Accessing values: values() method******************************************************************

print(f".values():  {my_dict.values()}")# dict_values(['Shannon', 37])
#*********************************Accessing values: .items()*************************************************************************
print(f".items():  {my_dict.items()}")#dict_items([('name', 'Shannon'), ('age', 37)])




#***********************************Get Key with the highest Value: max()*******************************************
bids = {
    "Shannon": 215.0,
    "lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}

print(f"max(): {max(bids, key=bids.get)}")#returns Molly
