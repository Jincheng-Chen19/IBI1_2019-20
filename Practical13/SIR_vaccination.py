# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:19:25 2020

@author: lenovo
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# set varibles for susceptible, infected, recovered, and a list for vaccinatied
N=10000
S=9999
V=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
I=1
R=0
In=[]
time=[]
dic={}
beta=0.3
gamma=0.05
for i in V:
    In.clear()
    I=1
    In.append(I)
    S=9999
    S=int(S-N*i)
    time.clear()
    time=[0]
    # make sure the 
    if S>0:
        # repeat 1000 times
        for j in range(0,1000):
            # randomly find newly infected people with the probability beta*I/N, 1 means infected, 0 means susceptible
            ni=np.random.choice(range(0,2),S,p=[1-beta*I/N,beta*I/N])
            # randomly find newly recovered people with the probability gamma, 2 means recovered
            nr=np.random.choice(range(1,3),I,p=[1-gamma,gamma])
            # count the number of newly infected people
            nin=sum(ni==1)
            # count the number of newly recovered people
            nrn=sum(nr==2)
            # the number of isusceptible people change to the original number minus the number of newly infected people
            S-=nin
            # the number of infected people change to the original number plus the number of newly infected people and minus the number of newly recovered people
            I=I+nin-nrn
            In.append(I)
        In_copy=In[:]
        # set a dictionary to record the infected number for each vaccination
        dic[i]=In_copy
    if S<0:
        for j in range(0,1000):
            # all the population are vaccination, so, no one can be infected
            I=0
            In.append(I)
            # record the time
            time.append(j+1)
        In_copy=In[:]
        # set a dictionary to record the infected for each vaccination
        dic[i]=In
# make a plot for all the proportion of vaccinatied people
plt.figure(figsize=(6,4),dpi=150)
n=1
# choose color for each curve
for x in dic:
    plt.plot(time,dic[x],color=cm.viridis(n),label=str(int(x*100))+'%')
    n+=25
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig('SIR model with different vaccination rates',type='png')