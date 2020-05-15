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
# loop through all the 'term'
for term in terms:
    # get a list of 'def' elements, a list of 'is_a' elements. a nodelist of 'id' elements
    DEFs=term.getElementsByTagName('def')
    IDs=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    # add them to a list,is_a as string
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    # make a dictionary, keys are the 'id' as string, values are the 'is_a' of this 'id'
    dic[IDs.childNodes[0].data]=is_a[:]
    # clear the 'is_a' list
    is_a.clear()
    for DEF in DEFs:
        # get the 'defstr', add them to 'defs' list as string
        defstr=DEF.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
a=[]
# find all the terms which have 'autophagosome' in their 'defstr'
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
ids=[]
names=[]
d=[]
# make a list for the ids, and a list for the names which have autophagosome in 'defstr'
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])
sys.setrecursionlimit(10000)
# make a recursion function to find the number of childnodes
def F(count=int,n=int,l=list,c=list):
    # start with get the id from the list'ids'
    if count==0 and n<len(ids):
        x=ids[n]
        y=False
        for i in dic:
            # if have childnodes, count the number, and add the name of first level of childnodes to 'l'
            if x in dic[i]:
                y=True
                count+=1
                l.append(i)
        # if no childnodes,go to next one in 'ids', add count to c list
        if y==False:
            n=n+1
            c.append(count)
            count=0
        return F(count,n,l,c)
    # if we have find the first childnodes, find next level of childnodes
    if count!=0 and n<len(ids):
        l_copy=l[:]
        l.clear()
        for x in l_copy:
            for i in dic:
                # count the number of childnodes of this level
                if x in dic[i]:
                    count+=1
                    l.append(i)
        # if no more of childnodes, go to next 'id' in ids list, and add count to c list
        if l_copy==[]:
            c.append(count)
            count=0
            n+=1
        return F(count,n,l,c)
    # after finish the searching, return c
    if count==0 and n==len(ids):
        return c
childnode=F(0,0,[],[])
# write into the excel
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'],
               index=False)
