"""
exp 07
String - 1
CO1
M1.03
Implement programs using String

Do the following:
Read two strings str1 and str2
Find their length
Concatenate ( merge ) them
Repeat str1 n times
Print a slice of str1
Check a particular letter is in str1
Check a particular letter is not in str1
Iterate over the elements of the strings
Print letters starting from index 4, ending at index 11, with step 3
Print the alternate letters from index 0
Print the string in reverse order

gpc vennikulam
"""


str1 = input("Enter your first string ")
str2 = input("Enter your second string ")

print("Your first string is ", str1)
print("Your second string is ", str2)

print("length of the first string is ", len(str1))
print("length of the second string is ", len(str2))

print("concatenation of the two strings is ", str1+str2)

print("Three times of the first string is ", 3*str1)

print("Fifth character of the first string is ", str1[5])
print("A slice of the first string from index 3 to 6 is ", str1[3:6])

ch = input("Enter a character ")
if ch in str1:
  print(ch, "is in", str1)
else:
  print(ch, "is not in", str1)

ch = input("Enter a character ")
if ch not in str1:
  print(ch, "is not in", str1)
else:
  print(ch, "is in", str1)

for c in str1:
  print(c)

for c1, c2 in zip(str1, str2):
  print(c1, c2)

#Print letters starting from index 4, ending at index 11, with step 3
str1[4:11:3]

# string[start:stop:step]
#Print the alternate letters from index 0
str1[::2]

#Print the string in reverse order
str1[::-1]




