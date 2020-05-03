# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:16:14 2020

@author: jacka
"""

s = input(r"Please input numbers to compute 24 (use ',' to divide them): ")
number = []
# Use flag = False or True to control the programme to return the result only when the numbers entered are between 1 and 23 in integer.
for value in s.split(","):
   number.append(float(value))
   flag = False
while flag == False:
    flag = True  
    for value in number:
       if value > 23 or value < 1:
         flag = False
# Print tips when the numbers entered do not fit the requirement.
         print("Invalid number " + str(value) + ". The numbers you enter should be between 1 to 23 in integer.")
         s = input(r"Please input numbers to compute 24: (use ',' to divide them): ")
         number = []
         for value in s.split(","):
            number.append(float(value))
         break

# Function to list out combinations
def f(l: int):
   b = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             b.append([i, j, k])
   return (b)
   
# Select out one combination
s_cal = [[], []]
for i in range(2, len(number) + 1):
   s_cal.append(f(i))
   
s_select = []
s_rel = []
for i in range(len(number)):
   s_rel.append(s_cal[len(number) - i])
   
def t(l: list):
   l_copy = l.copy()
   if len(l_copy) == len(s_rel) - 1:
      s_select.append(l_copy)
   for value in s_rel[len(l)]:
      l.append(value)
      t(l)
      l.pop()
t([])

# Select one equation from the combination 
def y(i:int, j:int, k:int, l:list):
    op = 0 
    if k == 0:
        op = l[i] + l[j]
    elif k == 1:
        op = l[i] - l[j]
    elif k == 2:
        op = l[j] - l[i]
    elif k == 3:
        op = l[i] * l[j]
    elif l[j] != 0 and l[i] != 0 :
        if k == 4:
            op = l[i] / l[j]
        else:
            op = l[j] / l[i]
    if op == 24:
        return (0)
    else:
        l[i] = op
        l.pop(j)       
 
# Prepare for the output
q = 0   
n = 1
for value in s_select:
     number_copy=number.copy()
     for m in value:
         if y(m[0], m[1], m[2], number_copy) ==0 and q == 0:
            print("Yes")
            print("Recursion Times: " + str(n))
            q = 1
         else:
            n = n + 1
if q == 0:
    print("No")