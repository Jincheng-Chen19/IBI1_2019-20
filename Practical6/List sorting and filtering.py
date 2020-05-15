# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:24:05 2020

@author: lenovo
"""
# import necessary libraries
import matplotlib.pyplot as plt
# sort the gene_lengths
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()
# remove the longest and shortest genes
del gene_lengths[0]
gene_lengths.pop()
print(gene_lengths)
# make a box plots for gene length
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.title('gene length')
plt.show()