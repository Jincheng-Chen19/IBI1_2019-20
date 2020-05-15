# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:56:12 2020

@author: lenovo
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# set varibles for susceptible, infected, recovered
N=10000
S=9999
I=1
R=0
Sn=[S]
In=[I]
Rn=[R]
time=[0]
beta=0.3
gamma=0.05
# repeat 1000 times
for i in range(0,1000):
    # randomly find the newly infected people with the probability beta*I/N, 1 means infected, 0 means susceptible
    ni=np.random.choice(range(0,2),S,p=[1-beta*I/N,beta*I/N])
    # randomly find the newly recovered people with the probability gamma, 2 means recovered
    nr=np.random.choice(range(1,3),I,p=[1-gamma,gamma])
    # count the number of newly infected people
    nin=sum(ni==1)
    # count the number of newly recovered people
    nrn=sum(nr==2)
    # the number of susceptible people change to the original number minus the number of newly infected people
    S-=nin
    Sn.append(S)
    # the number of infected people change to the original number plus the number of newly infected people and minus the number of newly recovered people
    I=I+nin-nrn
    In.append(I)
    # the numeber of recovered people change to the original number plus the numebr of newly recovered people
    R+=nrn
    Rn.append(R)
    # record the time
    time.append(i+1)
# make a plot for the number of susceptible, infected, and recovered people
plt.figure(figsize=(6,4),dpi=150)
plt.plot(time,Sn,'b',marker = ',',label='Susceptible')
plt.plot(time,In,'r',marker=',',label='Infected')
plt.plot(time,Rn,'g',marker=',',label='Recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig('SIR model',type='png')