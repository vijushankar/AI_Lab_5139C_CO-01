"""
Develop simple python programs using decision control structures

Problem : To determine if a year is a leap year or not
GPC VENNIKULAM
"""



#To determine if a year is a leap year or not
def IsLeap(year) :
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(year, "is a leap year.")
      else:
        print(year, "is not a leap year.")
    else:
      print(year, "is a leap year.")
  else:
    print(year, "is not a leap year.")

year = int(input("Enter a year: "))
IsLeap(year)
