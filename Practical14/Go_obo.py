# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:21:43 2020

@author: lenovo
"""
# import necessary libraries
import pandas as pd
import xml.dom.minidom
import sys
# prase go_obo.xml into a DOM document object
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# find root element
obo=DOMTree.documentElement
# a list of 'terms' elements
terms=obo.getElementsByTagName('term')
defs=[]
is_a=[]
dic={}

for term in terms:
    DEFs=term.getElementsByTagName('def')
    IDs=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    dic[IDs.childNodes[0].data]=is_a[:]
    is_a.clear()
    for DEF in DEFs:
        defstr=DEF.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
a=[]
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
ids=[]
names=[]
d=[]
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])
sys.setrecursionlimit(10000)
def F(count=int,n=int,l=list,c=list):
    if count==0 and n<len(ids):
        x=ids[n]
        y=False
        for i in dic:
            if x in dic[i]:
                y=True
                count+=1
                l.append(i)
        if y ==False:
            n=n+1
            c.append(count)
            count=0
        return F(count,n,l,c)
    if count!=0 and n<len(ids):
        l_copy=l[:]
        l.clear()
        for x in l_copy:
            for i in dic:
                if x in dic[i]:
                    count+=1
                    l.append(i)
        if l_copy==[]:
            c.append(count)
            count=0
            n+=1
        return F(count,n,l,c)
    if count==0 and n==len(ids):
        return c
childnode=F(0,0,[],[])
# write into the excel
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'],
               index=False)
