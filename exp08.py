"""
exp 08
String - 2
CO1
M1.03
Implement programs using String

To check if a string is a palindrome
GPC VENNIKULAM
"""

def isPalindrom(string):
  reversed_string = string[::-1]
  if string == reversed_string:
    #print("Palindrome")
    return True
  else:
    #print("Not a palindrome")
    return False

if isPalindrom(input("Enter a string: ")):
  print ("The given string is a palindrom")
else:
  print ("The given string is not a palindrom")

