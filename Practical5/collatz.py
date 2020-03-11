# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:35:16 2020

@author: lenovo
"""
# set a value for n
n=100000
# when n is not equal to 1, 
while n!=1:
# when n is an even, n=n/2
    if n%2==0:
        n=n/2
        print(n)
#when n is odd, n=3*n+1
    elif n%2==1:
        n=3*n+1
        print(n)
