"""
Exp. 01
control structure - 1
CO1
M1.01
Develop simple python programs using decision control structures

Problem : To determine if a number is positive, negative, or zero.

"""

def myfun(num):
  if num > 0:
    print("The number is positive.")
  elif num < 0:
    print("The number is negative.")
  else:
    print("The number is zero.")

myfun(int(input("Enter an integer number: ")))
