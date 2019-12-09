#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import numpy as np
import statcalc.stats.distance as ds
import statcalc.stats.stats as st

def knn(tr, te_row, n_neighbors):
    distances = list()
    for tr_row in tr:
        d = ds.e_distance(te_row, tr_row)
        distances.append((tr_row, d))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(n_neighbors):
        neighbors.append(distances[i][0])
    return st.s_mean(neighbors)


# In[ ]:




