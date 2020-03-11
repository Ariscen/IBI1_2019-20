# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:33:00 2020

@author: jacka
"""
# Using a =[ , , , ] can help me make the code clearer
# Remember to define all the variables (except those defined within the 'for loop")
# for i in range (1,j)
#     t = j-1
#     if a[t] > 0:
#         s=s+" 2**'+str(t)
# Let the first variable seperated from others
# so s=s+"2**'+str(j-1) if j=j+1 after the first calculation
# From a[0], n=(n-a[0])/2, then it goes similarly in the "while for" structure
# Remember to add print(s) and things like "space"
n=int(input())
j=0
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
s=str(n)+' is '
while n>0:
   a[j] = n % 2
   n = (n-a[j]) / 2
   j=j+1
s=s+'2**'+str(j-1)
for i in range (2,j+1):
    t = j-i
    if a[t] > 0:
        s=s+' + 2**'+str(t)
print(s)

    


