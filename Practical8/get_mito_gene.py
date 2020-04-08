# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:56:15 2020

@author: lenovo
"""
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
x=[]
z=str()
gene=[]
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
yfile=open('mito_gene.fa','w')

for i in range(count):
    if ':Mito:' in x[i]:
        line1='>'+genename[i]+'     '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        yfile.write(line1)
        yfile.write(line2)
yfile.close()
zfile=open('mito_gene.fa','r')
for line in zfile:
    print(line)
