# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:21:49 2020

@author: jacka
"""

# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt
# Define several nescessary variables.
# The population number
N = 10000
# infection constant
β = 0.3
# recovered constant
γ = 0.05
# The total time required and the time of operation
t = 1000
p = [0]
# susceptible number
sus = [9999]
# infected number
inf = [1]
# recovered number
rec = [0]
# The infected and recovery numbers after every operation
result1 = []
result2 = []
# Simulate the process
for i in range(0,t):
    result1 = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/N),β*(inf[i]/N)])
    n1 = np.sum(result1 == 1)
    result2 = np.random.choice(range(2),inf[i],p=[1-γ,γ])
    n2 = np.sum(result2 == 1)
# Add the change to three groups after every operation
    sus.append(sus[i]-n1)
    inf.append(inf[i]+n1-n2)
    rec.append(rec[i]+n2)
    p.append(i)
# make the figure
y1=sus
y2=inf
y3=rec
plt.plot(p, y1, label='susceptible number')
plt.plot(p, y2, label='infected number')
plt.plot(p, y3, label='recovered number')
plt.xlabel('Time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend(loc = 'upper right')
plt.show