"""
EXP 13
Dictionary - 1
CO1
M1.05
Implement programs using Dictionary Manipulations
Problem : Do various operations on dictionary
Creating a dictionary:
Accessing and modifying elements:
Checking presence and length:
Iterating over key-value pairs:
Dictionary methods:
Merging dictionaries:
Handling missing keys:

GPCV
"""

"""

Implement programs using Dictionary Manipulations

Creating a dictionary:
Create an empty dictionary: my_dict = {} or my_dict = dict()
Create a dictionary with initial key-value pairs: my_dict = {"key1": value1, "key2": value2}

Accessing and modifying elements:
Retrieve a value by key: value = my_dict[key]
Add or update a key-value pair: my_dict[key] = value
Remove a key-value pair: del my_dict[key]

Checking presence and length:
Check if a key is present in the dictionary: key in my_dict
Get the number of key-value pairs: len(my_dict)

Iterating over key-value pairs:
Iterate over keys: for key in my_dict:
Iterate over values: for value in my_dict.values():
Iterate over key-value pairs: for key, value in my_dict.items():

Dictionary methods:
Get a list of all keys: keys = my_dict.keys()
Get a list of all values: values = my_dict.values()
Get a list of all key-value pairs: items = my_dict.items()
Copy a dictionary: new_dict = my_dict.copy()
Clear all key-value pairs: my_dict.clear()

Merging dictionaries:

Merge two dictionaries into a new dictionary: new_dict = {**dict1, **dict2} (Python 3.5+)
Update a dictionary with key-value pairs from another dictionary: my_dict.update(other_dict)

Handling missing keys:
Retrieve a value with a default if the key is missing: value = my_dict.get(key, default_value)
Set a default value if the key is missing: value = my_dict.setdefault(key, default_value)


"""
