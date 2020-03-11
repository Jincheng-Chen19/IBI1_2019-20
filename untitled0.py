# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:02:50 2020

@author: lenovo
"""
x=1750
origin=x
A=str()
for n in range (0,13):
    if x%2==1:
        x=(x-1)/2
        A="2**"+str(n)+"+"+A
    else:
        x=x/2
B=str(origin)+"is" +A
print(B[:-1])