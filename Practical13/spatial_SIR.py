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
# repeat 100 times
for i in range(0,100):
    # find the infected points
    I=np.where(population==1)
    # loop through all infected points
    for j in range(len(I[0])):
        # get the coordinated of the infected points
        x=I[0][j]
        y=I[1][j]
        # find the points recovered from the disease with the probability gamma
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
        # infect neighbors of the infected points
        # find all the neighbor points
        for xn in range(x-1,x+2):
            for yn in range(y-1,y+2):
                # get rid of the infected points
                if (xn,yn)!=(x,y):
                    # make sure the neighbor points don't fall off the edge
                    if-1<xn<100 and -1<yn<100:
                        # infect the neighbor points which are susceptible
                        if population[xn,yn]==0:
                            # infect the neighbor with probability beta
                            population[xn,yn]=np.random.choice(range(0,2),
                                                           1,
                                                           p=[1-beta,beta])
plt.imshow(population,cmap='viridis',interpolation='nearest')
plt.savefig('spatial SIR',type='png')
