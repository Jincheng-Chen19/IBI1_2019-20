# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:58:28 2020

@author: lenovo
"""
L=[]
import re
seq='ATGCGACTACGATCGAGGGCCAT'
seq1=re.sub('G+?','c',seq)
seq1=re.sub('C+?','G',seq1)
seq1=re.sub('c+?','C',seq1)
seq1=re.sub('A+?','t',seq1)
seq1=re.sub('T+?','A',seq1)
seq1=re.sub('t+?','T',seq1)
L=list(seq1)
L.reverse()
cseq=''.join([str(a)for a in L])
print(seq)
print(seq1)
print(cseq)
