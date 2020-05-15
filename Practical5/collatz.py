# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:35:16 2020

@author: lenovo
"""
# set a value for n
n=100000
# when n is not equal to 1, 
while n!=1:
# when the remainder of N divided by 2 is 0, n is even
    if n%2==0:
        #when n is even, n=n/2
        n=n/2
        print(n)
# when the remainder of N divided by 2 is 1, n is odd
    elif n%2==1:
        # when n is odd, n=3*n+1
        n=3*n+1
        print(n)
