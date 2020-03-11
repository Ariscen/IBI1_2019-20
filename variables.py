# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:08:33 2020

@author: jacka
"""
# Here begins 4.1
a = int(input())
b = int(str(a)+str(a))
c = b/7
d = c/11
e = d/13
print ('a=',str(a),'e=',str(e))
if a == e :
    print ('a is equal to e')
elif a > e :
    print ('a is larger than e')
else:
    print ('a is smaller than e')
#Explanation: For any three-digit number, writing it twice equals to multiplying it by 1001
#             While 1001 = 7*11*13, a always equals to e

# Here begins 4.2
X = True
Y = False
Z = (X  and not Y) or (Y and not X)
W = X!=Y
print ('Z=',Z,'W=',W)
if Z == W :
    print ('Z equals to W')
#Explanation: If X =True, Y =False, then X and not Y = True, Y and not X = False, then Z = True
#             And as X is not equals to Y, W = True, then Z = W