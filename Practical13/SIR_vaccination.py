# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:19:25 2020

@author: lenovo
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N=10000
S=9999
V=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
I=1
In=[]
time=[]
dic={}
C={'s':0,'i':1,'R':2}
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
    if S>0:
        for j in range(0,1000):
            ni=np.random.choice(range(0,2),S,p=[1-beta*I/N,beta*I/N])
            nr=np.random.choice(range(1,3),I,p=[1-gamma,gamma])
            nin=sum(ni==1)
            nrn=sum(nr==2)
            S-=nin
            I=I+nin-nrn
            In.append(I)
            time.append(j+1)
        In_copy=In[:]
        dic[i]=In_copy
    if S<0:
        for j in range(0,1000):
            nr=np.random.choice(range(1,3),I,p=[1-gamma,gamma])
            nrn=sum(nr==2)
            I=I-nrn
            In.append(I)
            time.append(j+1)
        In_copy=In[:]
        dic[i]=In
plt.figure(figsize=(6,4),dpi=150)
n=1
for x in dic:
    plt.plot(time,dic[x],color=cm.viridis(n),label=str(int(x*100))+'%')
    n+=25
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig('SIR model with different vaccination rates',type='png')