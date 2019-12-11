#!/usr/bin/env python
# coding: utf-8

# In[4]:


class nonNegative(Exception):
    """Raised when the input value is a negative number"""
    pass
class nonText(Exception):
    """Raised when the input value is a string"""
    pass

import random
import numpy as np
import statcalc.stats.distance as ds
import statcalc.stats.stats as st

def knn(tr, te_row, n_neighbors):
    try:
        if n_neighbors <= 0:
            raise(nonNegative)
        if n_neighbors == str(n_neighbors):
            raise(nonText)
        distances = list()
        for tr_row in tr:
            d = ds.e_distance(te_row, tr_row)
            distances.append((tr_row, d))
        distances.sort(key=lambda tup: tup[1])
        neighbors = list()
        for i in range(n_neighbors):
            neighbors.append(distances[i][0])
        return st.s_mean(neighbors)
    except nonNegative:
        print ("Error: n_neighbors should be greater than 0")
    except nonText:
        print("Error: not supporting string, please type a number")


# In[5]:


np.random.seed(12345)
dataset = np.random.choice(range(1,100),100)
print(knn(dataset, dataset[5], 4))
dataset1 = np.random.choice(range(1,200),200)
print(knn(dataset1, dataset1[5], 4))
dataset2 = np.random.choice(range(1,300),300)
print(knn(dataset2, dataset2[5], 4))
dataset3 = np.random.choice(range(1,400),400)
print(knn(dataset3, dataset3[5], 4))
dataset4 = np.random.choice(range(1,500),500)
print(knn(dataset4, dataset4[5], 4))


# In[ ]:




