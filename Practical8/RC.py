# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:58:28 2020

@author: lenovo
"""
# import necessary libraries
import re
L=[]
# input the sequence
seq='ATGCGACTACGATCGAGGGCCAT'
# find the complementary bases
seq1=re.sub('G','c',seq)
seq1=re.sub('C','g',seq1)
seq1=re.sub('A','t',seq1)
seq1=re.sub('T','a',seq1)
seq1=seq1.upper()
#  reverse the sequence, let the cDNA sequence from 5' to 3'
cseq=seq1[::-1]
print(seq)
print(seq1)
print(cseq)
