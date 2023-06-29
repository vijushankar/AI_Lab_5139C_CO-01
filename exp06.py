"""
exp 06
for loop - 1
CO1
M1.02
Implement python Programs using loop control structures

Problem : To print even numbers from 1 to 10 using a "for" loop


Implement python Programs using loop control structures
Problem : To print even numbers from 1 to 10 using a "for" loop
"""
"""

#C Style
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
"""
#Pythonic Style
mylist = [i for i in range(1, 11) if i%2 == 0 ]
print (mylist)
