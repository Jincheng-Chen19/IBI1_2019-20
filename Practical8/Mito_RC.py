# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:33:52 2020

@author: lenovo
"""
# import necessary libraries
import re
# read the content
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
x=[]
y=str()
gene=[]
cgene=[]
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
# let users input a name for the file
name=input('Please input a filename for a faste file you want(including".fa"): ')
yfile=open(name,'w')
# change all the genes to complementary sequence
for a in range(count):
    gene[a]=re.sub('G','c',gene[a])
    gene[a]=re.sub('C','g',gene[a])
    gene[a]=re.sub('A','t',gene[a])
    gene[a]=re.sub('T','a',gene[a])
    gene[a]=gene[a].upper()
    # reverse the sequence to make it from 5' to 3'
    gene[a]=gene[a][::-1]
# find the genes on mitochondria chromosome
for i in range(count):
    if ':Mito:' in x[i]:
        # write the genes name, length and complementary sequence to the fasta file named by users
        line1='>'+genename[i]+'      '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        yfile.write(line1)
        yfile.write(line2)
yfile.close()
# read the fasta file named by users
zfile=open(name,'r')
for line in zfile:
    print(line)