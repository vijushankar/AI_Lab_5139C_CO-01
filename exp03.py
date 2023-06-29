"""
3
control structure - 3
CO1
M1.01
Develop simple python programs using decision control structures

Problem : To determine if the current minute is odd or even


Develop simple python programs using decision control structures

Problem : To determine if the current minute is odd or even
Ref : Head Firs Java, Paul Barry

GPC VENNIKULAM
EXP 03
"""

from datetime import datetime

odds = list (range(1,60))
right_this_minute = datetime.today().minute
if right_this_minute in odds :
  print("This minute seems a little odd.")
else:
  print("Not an odd minute.")
