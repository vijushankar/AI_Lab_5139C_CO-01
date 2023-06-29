"""
EXP 04
While loop - 1
CO1
M1.02
Implement python Programs using loop control structures

Problem : To find sum of elements in a list using “while” loop ( C style loop)


Implement python Programs using loop control structures
Problem : To find sum of elements in a list using while loop ( C style loop)

EXP 04
GPC VENNIKULAM
"""
"""
def findSum(mylist):
  s = 0;
  for no in mylist:
    s = s + no
  return s
  
print("The sum is",findSum([1, 2, 4]))
"""
# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize variables for sum and index
total_sum = 0
index = 0

# Calculate the sum using a while loop
while index < len(numbers):
    total_sum += numbers[index]
    index += 1

# Print the sum
print("The list is:", numbers)

# Print the sum
print("Sum of elements:", total_sum)
