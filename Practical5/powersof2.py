# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:47:42 2020

@author: lenovo
"""
# set a value for x
x=1750
print (x,"is",end=" ")
# before we find all the 2**j, x should be larger than 0 
while x>0:
#find the proper 2**j for x
    for j in range(0,14):
        if x-2**j>0 and x-2**(j+1)<0:
            x=x-2**j
            print("2**",j,sep="",end=" ")
            print("+",end=" ")
        elif x-2**j==0:
            x=x-2**j
            print("2**",j,sep="")
