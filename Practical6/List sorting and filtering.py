# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:32:01 2020

@author: jacka
"""

import matplotlib.pyplot as plt
gene_lengths = [9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
n = len(gene_lengths)
# Sort the sequence to show the smallest number and the largest number.
gene_lengths.sort()
del(gene_lengths[0])
# Delete the [n-2] instead of [n-1] because we have deleted the smallest number, so the length has already become n-1.
del(gene_lengths[n-2])
print(gene_lengths)
# To ensure that it can output the boxplot, we set some parameters.
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()