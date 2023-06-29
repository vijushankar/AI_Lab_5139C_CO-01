"""
EXP 09
String - 3
CO1
M1.03
Implement programs using String

to convert a string to uppercase
to count the occurrence of a character in a string
to split a string into a list of words
to replace a substring in a string
to check if a string starts with a specific prefix
to find the index of a substring in a string

GPC VENNIKULAM
"""

#  to convert a string to uppercase
string = "python"
uppercase_string = string.upper()
print("Uppercase string:", uppercase_string)


# to count the occurrence of a character in a string
string = "Hello, World!"
character = "l"
count = string.count(character)
print("Count:", count)


# to split a string into a list of words
string = "This is a sentence."
words = string.split()
print("List of words:", words)


# to replace a substring in a string
string = "Hello, World!"
new_string = string.replace("World", "Python")
print("New string:", new_string)


#  to check if a string starts with a specific prefix
string = "Hello, World!"
prefix = "Hello"
if string.startswith(prefix):
    print("String starts with the prefix")
else:
    print("String does not start with the prefix")


# to find the index of a substring in a string
string = "Hello, World!"
substring = "World"
index = string.index(substring)
print("Index of substring:", index)
