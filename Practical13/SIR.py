# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:56:12 2020

@author: lenovo
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000
S=9999
I=1
R=0
Sn=[S]
In=[I]
Rn=[R]
time=[0]
C={'s':0,'i':1,'R':2}
beta=0.3
gamma=0.05
for i in range(0,1000):
    ni=np.random.choice(range(0,2),S,p=[1-beta*I/N,beta*I/N])
    nr=np.random.choice(range(1,3),I,p=[1-gamma,gamma])
    nin=sum(ni==1)
    nrn=sum(nr==2)
    S-=nin
    Sn.append(S)
    I=I+nin-nrn
    In.append(I)
    R+=nrn
    Rn.append(R)
    time.append(i+1)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(time,Sn,'b',marker = ',',label='Susceptible')
plt.plot(time,In,'r',marker=',',label='Infected')
plt.plot(time,Rn,'g',marker=',',label='Recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig('SIR model',type='png')