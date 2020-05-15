# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""
# import necessary libraries
import sys
c=float()
result=[]
recursion_time=0
cards=[]
# let the user input the integers
n= input("Please input numbers to compute 24:(use ',' to divide them)")
# turn the string to list, split by ','
N=n.split(',')
# change all the string in list to float
for i in N:
   cards.append(float(i))
# check whether all the number between 1 to 23
for x in cards:
    if int(x) >=24 or int(x)<1:
        print('The input number must be integers from 1 to 23')
        break
    else:
        # define the way to compute 24 points
        def Function(a,b,f):
            global c,recursion_time
            if f==0:
                c=a+b
            if f==1:
                c=a*b
            if f==2:
                c=a-b
            if f==3:
                if b==0.0:
                    c='stop'
                else:
                    c=a/b
            if f==4:
                if a==0.0:
                    c='stop'
                else:
                    c=b/a
            # if any intermediate precess equals to 24, the funtion will break
            if c==24.0:
                recursion_time+=1
                print('Yes')
                print('Recursion times:',recursion_time)
                # this code is got from the internet, https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
                sys.exit()
            else:
                return c
        # define another function to do the recursive merging and calculating 
        def R(L):
            global c,recursion_time
            #  if the length of list L is 1, 
            if len(L)==1:
                result.append(L[0])
            else:
                # take every possible two numbers into account, but may lead to repetition
                for i in range(0,len(L)-1):
                    for j in range(i+1,len(L)):
                        L_copy1=L[:]
                        x=L[i]
                        y=L[j]
                        L_copy1.remove(x)
                        L_copy1.remove(y)
                        for f in range(0,5):
                            L_copy2=L_copy1[:]
                            Result=Function(x,y,f)
                            recursion_time+=1
                            if c=='stop':
                                c=float()
                            else:
                                L_copy2.append(Result)
                                R(L_copy2)
                            

        R(cards)
        # if these number can calculate 24, print 'yes'
        x=False
        for i in range(len(result)):
            if result[i]==24:
                x=True
                print('Yes')
                break
        # if cannot, print 'no'
        if x==False:
            print('No')
            break
# the complexity of this function: O(n**2).this complexity may be a little high.
    
