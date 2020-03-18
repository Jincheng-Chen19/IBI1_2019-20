# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:55:23 2020

@author: lenovo
"""
import matplotlib.pyplot as plt
# count the number of these four nucleotides
L=['A','T','G','C','T','T','C','A','G','A','A','A','G','G','T','C','T','T','A','C','G']
a=L.count('A')
g=L.count('G')
c=L.count('C')
t=L.count('T')
print(a,g,c,t)
x=a+g+c+t
# make the frequency dictionary 
nucleotides={'A':a/x,'G':g/x,'C':c/x,'T':t/x}
print(nucleotides)
# make the pie chart
labels='A','G','C','T'
sizes=[a/x,g/x,c/x,t/x]
explode=(0,0,0,0.08)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False, startangle=90)
plt.axis('equal')
plt.show()
