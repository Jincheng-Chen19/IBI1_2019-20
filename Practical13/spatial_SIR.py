# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:58:07 2020

@author: lenovo
"""
# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
# make array of all susceptible population 
population=np.zeros((100 , 100))
outbreak=np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]]=1
beta=0.3
gamma=0.05
plt.figure(figsize=(6,4),dpi=150)

for i in range(0,100):
    I=np.where(population==1)
    for j in range(len(I[0])):
        x=I[0][j]
        y=I[1][j]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
        for xn in range(x-1,x+2):
            for yn in range(y-1,y+2):
                if (xn,yn)!=(x,y):
                    if-1<xn<100 and -1<yn<100:
                        if population[xn,yn]==0:
                            population[xn,yn]=np.random.choice(range(0,2),
                                                           1,
                                                           p=[1-beta,beta])
    plt.imshow(population,cmap='viridis',interpolation='nearest')
