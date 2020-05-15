# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:14:53 2020

@author: lenovo
"""
# input the numbers
n=input("Please input numbers to compute 24: (use ',' to divide them)")
cards=n.split(',')
for x in cards:
    if int(x) >=24 or int(x)<1:
        print('The input number must be integers from 1 to 23')
        break
number=[]
def countway(a):
    b=[]
    for i in range(0,a-1):
        for j in range(i+1,a):
            for k in range(6):
                b.append([i,j,k])
    return b
for z in cards:
    number.append(float(z))
cw=[[],[]]
for i in range(2,len(number)+1):
    cw.append(countway(i))
    
cws=[]
cwr=[]
for i in range(len(number)):
    cwr.append(cw[len(number)-i])
def t(l):
    l_copy=l[:]
    if len(l_copy)==len(cwr)-1:
        cws.append(l_copy)
    for y in cwr[len(l)]:
        l.append(y)
        t(l)
        l.pop()
t([])

def count(i,j,k,l):
    c=0
    if k==0:
        c=l[i]+l[j]
    elif k==1:
        c= l[i]-l[j]
    elif k==2:
        c=l[j]-l[i]
    elif k==3:
        c=l[i]*l[j]
    elif l[j]!=0 and l[i]!=0:
        if k==4:
            c=l[i]/l[j]
        else:
            c=l[j]/l[i]
    if c==24:
        return c
    else:
        l[i]=c
        l.pop(j)

a=False
t=0
for x in cards:
    if int(x) >=24 and int(x)<1:
        a=True
        break
for value in cws:
    number_copy=number[:]
    for m in value:
        if count(m[0],m[1],m[2],number_copy)==24 and a==False:
            print('Yes')
            t+=1
            print('Recursion Times:',t)
            a=True
        else:
            t+=1
if a==False:
    print('No')
    
    