# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
# Input the DNA sequence
L = "ATGCTTCAGAAAGGTCTTACG"
n = len(L)
A=0
T=0
G=0
C=0
# Using loops to count the quantity of each nucleotide (Using for i in range (0,n) t = L[i-1])
for i in range (0,n):
    t = L[i-1]
    if t == 'A':
        A = A + 1
    elif t == 'T':
        T = T + 1
    elif t == 'G':
        G = G + 1
    elif t == 'C':
        C = C + 1
    else:
        print('It is not a right DNA sequence')
print(' A =',A,' T =',T,' G =',G,' C =',C)
# To set the parameters of the pie plot, remember that labels are strings.
labels = ['A','T','G','C']
sizes = [A,T,G,C]
explode = [0,0,0,0]
# Specify the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title('pie of the four DNA nucleotides')
# Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
