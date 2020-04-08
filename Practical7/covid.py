# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:47:18 2020

@author: jacka
"""

import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
#Part1
os.chdir("D:\IBI1_2019-20\Practical7")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
covid_data.describe()
covid_data.iloc[0,1]
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
covid_data.iloc[0:3,[0,1,3]]
my_columns = [True, True, False, True, False, False] 
covid_data.iloc[0:3,my_columns]
covid_data.loc[2:4,"date"]
covid_data.loc[0:81,"total_cases"]
#Part2
print(covid_data.iloc[0:15:3,:])
#
i = 1 
X = 0
while X == 0 :
    if covid_data.iloc[i,1] == 'Afghanistan':
        print(covid_data.iloc[i,:])
    else:
        X = 1
    i = i + 1
#
world_new_cases=[]
world_dates=[]
world_death_cases=[]
n = 0
df = pd.DataFrame(covid_data)
for n in range(len(df)):
    if covid_data.iloc[n,1] == 'World':
        world_new_cases.append(covid_data.iloc[n,2])
        world_death_cases.append(covid_data.iloc[n,3])
        world_dates.append(covid_data.iloc[n,0])
#Part4
print('mean='+str(np.mean(world_new_cases,axis=0)))
print('median='+str(np.median(world_new_cases,axis=0)))
#Part5
plt.boxplot(world_new_cases,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.title('The boxplot of world new COVID - 19 cases')
plt.xlabel('')
plt.ylabel('World new cases')
plt.show()
#Part6
plt.plot(world_dates,world_new_cases,'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.title('The growth curve of world new COVID - 19 cases')
plt.xlabel('Date')
plt.ylabel('World new cases')
plt.show()
plt.plot(world_dates,world_death_cases,'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.title('The growth curve of world death COVID - 19 cases')
plt.xlabel('Date')
plt.ylabel('World death cases')
plt.show()
#Part3
t = 0
f = [0 for t in range(len(df))]
for t in range(len(df)):
    if covid_data.iloc[t,1] == 'Afghanistan':
        f[t] = True
    else:
        f[t] = False
print(f)
#Question
China_dates = []
China_new_cases = []
China_total_cases = []
for i in range(len(df)):
    if covid_data.iloc[i,1] == 'China':
        China_dates.append (covid_data.iloc[i,0])
        China_new_cases.append (covid_data.iloc[i,2])
        China_total_cases.append(covid_data.iloc[i,4])
plt.plot(China_dates,China_new_cases,'b+')
plt.title('The growth curve of new COVID - 19 cases in China')
plt.xlabel('Date')
plt.ylabel('China new cases')
plt.xticks(China_dates[0:len(China_dates):4],rotation=-90)
plt.show()
plt.plot(China_dates,China_total_cases,'b+')
plt.xticks(China_dates[0:len(China_dates):4],rotation=-90)
plt.title('The growth curve of all COVID - 19 cases in China')
plt.xlabel('Date')
plt.ylabel('China total cases')
plt.show()