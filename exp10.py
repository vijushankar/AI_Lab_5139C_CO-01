"""
EXP 10
String - 3
CO1
M1.03
Implement programs using String

To print all vowels in a word
GPC VENNIKULAM
"""
"""
# C STYLE
# To print all vowels in a word
# To print all vowels in a word
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
  if letter in vowels:
    if letter not in found:
      found.append(letter)
for vowel in found:
  print(vowel)
"""

# To print all vowels in a word
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
word = input("Provide a word to search for vowels: ")
found = set()
found = {letter.lower() for letter in word if letter in vowels}

for vowel in found:
  print(vowel)


