# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:23:57 2020

@author: lenovo
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('F:/university course/IBI/Week7. Public Health Informatics/Practical 7 guide')
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:16:3,:])
z=[]
c=[]
x= covid_data.iloc[:,1]
for y in range (0,7996):
    x[y]=='Afghanistan'
    if x[y]== True:
        z.append(y)
print(covid_data.loc[z,'total_cases'])
a= covid_data.iloc[:,1]
for b in range (0,7996):
    if a[b]=='World':
        c.append(b)
print(covid_data.iloc[c,[0,2]])
world_date=covid_data.loc[c,'date']
world_new_cases=covid_data.loc[c,'new_cases']
print(np.mean(world_new_cases,axis=0))
print(np.median(world_new_cases,axis=0))
plt.boxplot(world_new_cases,
            vert= True,
            whis= 1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch= False,)
plt.show()
plt.plot(world_date,world_new_cases,'bo')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('world new cases')
x=covid_data.loc[:,'date']
n=covid_data.loc[:,'total_cases']
z=[]
for y in range(0,7996):
    if x[y]=='2020-03-31':
        if n[y]<=10:
            z.append(y)
a=covid_data.loc[z,'total_cases']
print(covid_data.loc[z,'location'])
print(len(z))