# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:28:20 2020

@author: lenovo
"""
# import necessary libraries
import pandas as pd
# read the file
xfile=open('SOD2_human.fa','r')
yfile=open('SOD2_mouse.fa','r')
zfile=open('RandomSeq.fa','r')
# read BLOSUM62
matrix=pd.read_csv('BLOSUM62.csv')
# get the amino acid sequences and the name of the protein
for x in xfile:
    if '>' not in x:
        h=x
        h=h.rstrip()
    else:
        hname=x.lstrip('>')
for y in yfile:
    if '>' not in y:
        m=y
        m=m.rstrip()
    else:
        mname=y.lstrip('>')
for z in zfile:
    if '>' not in z:
        r=z
        r=r.rstrip()
    else:
        rname=z.lstrip('>')

line=matrix.iloc[:,0]
edit_distance1=0
for i in range(len(h)):
    for k in range(0,24):
        if m[i]==line[k]:
            edit_distance1+=int(matrix.loc[k,h[i]])
edit_distance2=0
for i in range(len(h)):
    for k in range(0,24):
        if r[i]==line[k]:
            edit_distance2+=int(matrix.loc[k,h[i]])
edit_distance3=0
for i in range(len(m)):
    for k in range(0,24):
        if r[i]==line[k]:
            edit_distance3+=int(matrix.loc[k,m[i]])
print(hname+h+'\n'+mname+m+'\n'+'human-mouse is:'+str(edit_distance1)+'\n')
print(hname+h+'\n'+rname+r+'\n'+'human-random is:'+str(edit_distance2)+'\n')
print(mname+m+'\n'+rname+r+'\n'+'mouse-random is:'+str(edit_distance3)+'\n')