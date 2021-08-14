# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 01:20:46 2021

@author: whiter9
"""

import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns

fold = '4H'
_4H = pd.read_csv('4H_NGS_filtered.csv', header=0)
print(_4H)

with open('4H_sequences.txt', 'w') as save_file:  
    for i in range(len(_4H['seq'])):
        save_file.write('>{}.{}\n{}\n'.format(fold,i,_4H['seq'][i]))
