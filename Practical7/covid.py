# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:23:57 2020

@author: lenovo
"""
# import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# change working directory (this directory is for my computer. I submit the file folder IBI1_2019-20. Therefore, the first three part of this directory may be different. Please change to your directory)
os.chdir('F:/university course/IBI/IBI1_2019-20/Practical7')
# read the content
covid_data = pd.read_csv("full_data.csv")
# showing all columns and every third row between (and including) 0 and 15
print(covid_data.iloc[0:16:3,:],'\n')
z=[]
c=[]
# read the location
x= covid_data.iloc[:,1]
# find the row corresponding to Afghanistan
for y in range (0,7996):
    # use Boolean to show "total_cases" for rows corresponding to Afghanistan
    if x[y]== 'Afghanistan':
        z.append(True)
    else:
        z.append(False)
print(covid_data.loc[z,'total_cases'],'\n')
# read the location
a= covid_data.iloc[:,1]
# find the row corresponding to World
for b in range (0,7996):
    if a[b]=='World':
        c.append(b)
print(covid_data.iloc[c,[0,2]],'\n')
# find "date","new_cases", and "new_deaths" for rows corresponding to World
world_date=covid_data.loc[c,'date']
world_new_cases=covid_data.loc[c,'new_cases']
world_new_deaths=covid_data.loc[c,'new_deaths']
# use numpy to count the mean and median of new cases for the entire world.
print(np.mean(world_new_cases,axis=0))
print(np.median(world_new_cases,axis=0),'\n')
# make boxplot for world_new_cases
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
# plot both world new cases and world new deaths.
plt.plot(world_date,world_new_cases,'bo',label='world new cases')
plt.plot(world_date,world_new_deaths,'ro',label='world new deaths')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.legend()
plt.title('world new cases')
plt.show()

# read the date and total_cases
x=covid_data.loc[:,'date']
n=covid_data.loc[:,'total_cases']
z=[]
# find the location whose total_cases lower than 10 
for y in range(0,7996):
    if x[y]=='2020-03-31':
        if n[y]<=10:
            z.append(y)
a=covid_data.loc[z,'total_cases']
print(covid_data.loc[z,'location'])
# print the number of locations whose total_cases lower than 10 
print(len(z))