# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:10:02 2020

@author: jacka
"""
#if n%2==0:
#   n=(n-n%2)/2
#else:
#    n=3*n+1
n = int(input())
print(n)
while n>1:
    if n % 2 == 0 :
        n = (n - n % 2) / 2
    else:
        n = 3 * n + 1
    print('n →', n)
#Comment: Using “→” can help to make the result clearer.
#         These codes realize the goal of building collatz sequences when giving the first numbers.