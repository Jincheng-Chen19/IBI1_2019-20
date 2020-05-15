# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:56:15 2020

@author: lenovo
"""
# read the content
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
x=[]
y=str()
gene=[]
genename=[]
count=0
# get all the genes in xfile
for line in xfile:
    # find the line containing the gene information
    if line.startswith('>'):
        # add the sequence of the previous gene to 'gene' list
        if y!='':
            gene.append(y)
        # add the gene name to 'genename' list
        genename.append(line[1:6])
        # add all the gene information to 'x' list
        x.append(line)
        # count the total number of gene
        count+=1
        y=''
    else:
        # if the line don't have '>', this line containing the sequence.
        # remove the '\n' and add them to a string.
        line=line.rstrip()
        y+=line
gene.append(y)
yfile=open('mito_gene.fa','w')
# find the genes on mitochondria chromosome
for i in range(count):
    if ':Mito:' in x[i]:
        # write the proper genes into the mito_gene.fa
        line1='>'+genename[i]+'     '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        yfile.write(line1)
        yfile.write(line2)
yfile.close()
# read mito_gene.fa
zfile=open('mito_gene.fa','r')
for line in zfile:
    print(line)
