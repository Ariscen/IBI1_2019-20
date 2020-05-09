# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:06:16 2020

@author: jacka
"""

# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt
# make array of all susceptible population and infected population
population = np. zeros ( (100 , 100) )
outbreak = np.random. choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# make the figure
plt.figure ( figsize =(6 ,4) , dpi=150) 
plt.imshow( population , cmap='viridis', interpolation='nearest' )
# Define β and γ
β = 0.3
γ = 0.05
# find infected points
for i in range (0,100):
    infected = np.where(population==1)
# loop through all infected points
    for i in range(len(infected[0])):
# get x, y coordinates for each point
        x = infected[0][i]
        y = infected[1][i]
# For eight neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
# make sure that only neighbours instead of including itself.
                if (xNeighbour,yNeighbour) != (x,y):
# Consider about edges of the figure
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
# only infect uninfected neighbours 
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
    infected = np.where(population==1)
# find recovered points
    for i in range(len(infected[0])):
        x = infected[0][i]
        y = infected[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-γ,γ])[0] + 1   
    plt.figure ( figsize =(6 ,4) , dpi=150) 
    plt.imshow( population , cmap='viridis', interpolation='nearest')