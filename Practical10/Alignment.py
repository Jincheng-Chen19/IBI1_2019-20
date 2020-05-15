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
    # get the sequence and remove the'\n', human
    if '>' not in x:
        h=x
        h=h.rstrip()
    # get the name of the protein, human
    else:
        hname=x.lstrip('>')
for y in yfile:
    # get sequence, remove'\n', mouse
    if '>' not in y:
        m=y
        m=m.rstrip()
    #get name, mouse
    else:
        mname=y.lstrip('>')
for z in zfile:
    # get sequence, remove '\n', random
    if '>' not in z:
        r=z
        r=r.rstrip()
        # get name, random
    else:
        rname=z.lstrip('>')

line=matrix.iloc[:,0]
# for next three parts, compare each amino acid and find the number of different amino acids
# take one protein sequence as column index, another protein sequence as row index.
# compare each amino acid of two sequences, get the corresponding score, and count the total scores
# for bonus project, find the place that BLOSUM>=0, add a '+' ; the place that BLOSUM<0, add a ' '
score1=0
s1=''
edit_distance1=0
for i in range(len(h)):
    if h[i]!=m[i]:
        edit_distance1+=1
    for k in range(0,24):
        if m[i]==line[k]:
            score1+=int(matrix.loc[k,h[i]])
            if int(matrix.loc[k,h[i]])>=0:
                s1+='+'
            else:
                s1+=' '
e1=edit_distance1/len(h)
score2=0
s2=''
edit_distance2=0
for i in range(len(h)):
    if h[i]!=r[i]:
        edit_distance2+=1
    for k in range(0,24):
        if r[i]==line[k]:
            score2+=int(matrix.loc[k,h[i]])
            if int(matrix.loc[k,h[i]])>=0:
                s2+='+'
            else:
                s2+=' '
e2=edit_distance2/len(h)
score3=0
s3=''
edit_distance3=0
for i in range(len(m)):
    if m[i]!=r[i]:
        edit_distance3+=1
    for k in range(0,24):
        if r[i]==line[k]:
            score3+=int(matrix.loc[k,m[i]])
            if int(matrix.loc[k,m[i]])>=0:
                s3+='+'
            else:
                s3+=' '
e3=edit_distance3/len(m)
# print the result with bonus project
print(hname+h+'\n'+s1+'\n'+mname+m+'\n'+'human-mouse score is: '+str(score1)+'  percentage is: '+str(100-e1*100)+'%'+'\n')
print(hname+h+'\n'+s2+'\n'+rname+r+'\n'+'human-random score is: '+str(score2)+'  percentage is: '+str(100-e2*100)+'%'+'\n')
print(mname+m+'\n'+s3+'\n'+rname+r+'\n'+'mouse-random score is: '+str(score3)+'  percentage is: '+str(100-e3*100)+'%')