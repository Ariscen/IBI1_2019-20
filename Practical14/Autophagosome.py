# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:21:43 2020

@author: lenovo
"""
# import necessary libraries
import xml.dom.minidom
import pandas as pd
# parse go_obo.xml into a DOM document object
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# find root element
ele=DOMTree.documentElement
# a list of 'term' elements
terms=ele.getElementsByTagName('term')
# list all the arrays
defs=[]
is_a=[]
dic={}
for term in terms:
    Defs=term.getElementsByTagName('def')
    Ids=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    for m in is_as:
        is_a.append(m.childNodes[0].data)
    dic[Ids.childNodes[0].data]=is_a[:]
    is_a.clear()
    for Def in Defs:
        defstr=Def.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)  
# select the arrays we need
array=[]
for m in range(len(defs)):
    if 'autophagosome' in defs[m]:
        array.append(m)
ids=[]
names=[]
definitions=[]
for i in array:
    Ids=terms.item(i).getElementsByTagName('id')[0]
    ids.append(Ids.childNodes[0].data)
    Names=terms.item(i).getElementsByTagName('name')[0]
    names.append(Names.childNodes[0].data)
    definitions.append(defs[i])

# count the chilnode number
childnode = []
for i in ids:
    x = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1
            x.append (j)
    y = x[:]
    inc = count
    while inc != 0 :
        x = []
        inc = 0
        for k in y:
            for j in dic:
                if k in dic[j]:
                    inc += 1
                    count += 1
                    x.append (j)
        y = x[:]
    childnode.append (count)
# put the data into excel
xfile=pd.DataFrame({'id':ids,'name':names,'definition':definition,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'])
