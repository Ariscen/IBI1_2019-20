# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:56:08 2020

@author: jacka
"""
import re
Genename = []
Gene = []
L=[]
res=[]
i = 0
s = ''
length = 0
c=''
l=''
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    if line.startswith('>'):
        if s != '':
            Gene.append(s)
        s = line[1:6] 
        l = line[1:100]
        L.append(l)
        Genename.append(s)
        length = length + 1
        s = ''
    else:
        s = s + line
Gene.append(s) 
for j in range(length):
    seq = Gene[j]
    c = ''
    for i in range(len(seq)):
       if seq[i] == 'A':
          c = 'T' +c
       elif seq[i] == 'T':
          c = 'A' +c
       elif seq[i] == 'G':
          c = 'C' +c
       elif seq[i] == 'C':
          c = 'G' +c
    res.append(c)
Name=input('please enter your filename: ')
fout = open(Name,'w')
for i in range (length):
    if re.search('Mito',L[i]) :
       line1 = '>'+ Genename[i]+'  '+ str(len(Gene[i]))+'\n'
       line2 = res[i]+'\n'
       fout.write(line1)
       fout.write(line2)
try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()
