# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:48:03 2020

@author: jacka
"""

seq1 = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2 = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq3 = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
edit_distance1 = 0
for i in range(len(seq1)):
    if seq1[i]!=seq2[i]:
        edit_distance1 += 1
print(100-edit_distance1/len(seq1)*100,'%')
edit_distance2 = 0
for i in range(len(seq2)):
    if seq2[i]!=seq3[i]:
        edit_distance2 += 1
print(100-edit_distance2/len(seq2)*100,'%')
edit_distance3 = 0
for i in range(len(seq3)):
    if seq1[i]!=seq3[i]:
        edit_distance3 += 1
print(100-edit_distance3/len(seq3)*100,'%')