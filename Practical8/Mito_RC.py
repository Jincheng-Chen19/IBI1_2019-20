# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:33:52 2020

@author: lenovo
"""
import re
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
x=[]
z=str()
gene=[]
cgene=[]
genename=[]
y=[]
count=0
for line in xfile:
    if line.startswith('>'):
        if z!='':
            gene.append(z)
        genename.append(line[1:6])
        z=''
        x.append(line)
        count+=1
    else:
        line=line.rstrip()
        z=z+str(line)
gene.append(z)
yfile=open('Please input a filename.fa','w')
for a in range(count):
    gene[a]=re.sub('G+?','c',gene[a])
    gene[a]=re.sub('C+?','G',gene[a])
    gene[a]=re.sub('c+?','C',gene[a])
    gene[a]=re.sub('A+?','t',gene[a])
    gene[a]=re.sub('T+?','A',gene[a])
    gene[a]=re.sub('t+?','T',gene[a])
    gene[a]=gene[a][::-1]
for i in range(count):
    if ':Mito:' in x[i]:
        line1='>'+genename[i]+'      '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        yfile.write(line1)
        yfile.write(line2)
yfile.close()
zfile=open('Please input a filename.fa','r')
for line in zfile:
    print(line)