#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys
#sys.path.append("..")

import statcalc.stats.stats as st

def resample(nums):
    return np.random.choice(nums,size=int(len(nums)/3),replace=True)
def sample_stand_err(nums):
    return float('%.4f' % round((st.sample_std(nums)/len(nums)**0.5),4))
def stand_err(nums):
    return float('%.4f' % round((st.s_std(nums)/len(nums)**0.5),4))
def sample_distr(nums):
    sample_props=[]
    for _ in range(10000):
        sample=resample(nums)
        sample_props.append(st.s_mean(sample))
    sample_props=np.array(sample_props)
    return sample_props
def b_plot(nums):
    plt.hist(nums,color="pink",linewidth=2)
    plt.xlabel('Mean')
    plt.title('Simulated sampling distribution') 
    plt.show()

