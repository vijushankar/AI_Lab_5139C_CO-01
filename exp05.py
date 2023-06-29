"""
exp 05
While loop - 2
CO1
M1.02
Implement python Programs using loop control structures

Problem : To find factorial of a given number using “while” loop ( C style loop)

Implement python Programs using loop control structures
Problem : To find factorial of a given number using while loop ( C style loop)
gpc vennikulam
"""
def myFactorialFun(num):
  factorial = 1
  i = 1
  
  while i <= num:
    factorial *= i
    i += 1

  return factorial
 
print("Factorial of the number is",myFactorialFun(int(input("Enter a number: "))))
