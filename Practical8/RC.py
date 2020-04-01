# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:22:23 2020

@author: jacka
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
s = len(seq)
c = ''
#To reverse the sequence, add each string before c and use seq[i] to represent the each 'letter'.
for i in range(0,s):
    if seq[i] == 'A':
        c = 'T' +c
    elif seq[i] == 'T':
        c = 'A' +c
    elif seq[i] == 'G':
        c = 'C' +c
    elif seq[i] == 'C':
        c = 'G' +c
    else:
        print('it is not a DNA sequence')
#To make sure the correctness of the result, use len(c)==s to confirm the result
if len(c) == s:
    print(c)