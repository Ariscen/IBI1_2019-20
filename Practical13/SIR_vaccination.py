# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:03:40 2020

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
p =[0]
# susceptible number
sus = [9999]
# infected number
inf = [1]
# recovered number
rec = [0]
# The infected and recovery numbers after every operation
result1 = []
result2 = []
# Vaccination rate
r = [0,10,20,30,40,50,60,70,80,90,100]
# Simulate the process, don't forget to turn the variables into initial value after each i-loop.
for v in range(0,11):
    p = [0]
    inf = [1]
    sus=[9999-r[v]*100]
# Consider that sus may be smaller than zero when r=100
    if sus[0] < 0:
        sus = [0]
        inf = [0]
    s = str(r[v])+'%'
    for i in range(0,t):
        result1 = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/N),β*(inf[i]/N)])
        n1 = np.sum(result1 == 1)
        result2 = np.random.choice(range(2),inf[i],p=[1-γ,γ])
        n2 = np.sum(result2 == 1)
        sus.append(sus[i]-n1)
        inf.append(inf[i]+n1-n2)
        rec.append(rec[i]+n2)
        p.append(i)
# make the figure
    plt.plot(p, inf, label=s)
    plt.legend(loc = 'upper right')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.show()