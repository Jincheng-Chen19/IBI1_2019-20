# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:24:05 2020

@author: lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
# sort the gene_lengths
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()
# remove the two most extreme genes
del gene_lengths[0]
gene_lengths.pop()
print(gene_lengths)
# set an interval
n=10000
gene_length=np.random.uniform(0,140000,n)
# make a box plots
plt.boxplot(gene_length,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()