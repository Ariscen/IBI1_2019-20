# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:56:08 2020

@author: jacka
"""
import re
Genename = []
Gene = []
L=[]
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
fout = open('mito_gene.fa','w')
for i in range (length):
    if re.search('Mito',L[i]) :
       line1 = '>'+ Genename[i]+'  '+ str(len(Gene[i]))+'\n'
       line2 = Gene[i]+'\n'
       fout.write(line1)
       fout.write(line2)
try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()
