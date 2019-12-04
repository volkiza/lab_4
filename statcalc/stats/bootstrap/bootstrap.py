#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys

import statcalc.stats.stats as st

from statcalc.stats.bootstrap import boot_func as bt

# In[3]:


class Bootstrap:
    def __init__(self,nums):
        self.nums=nums
        if isinstance(nums,np.ndarray):
            pass
        else:
            nums=np.array(nums)
            print("Transfered the list to numpy array")
    def print_nums(self):
        return print ("The original array is: {}".format(self.nums))
    def mean(self):
        return float('%.4f' % round(st.s_mean(self.nums),4))
    def sd(self):
        return float('%.4f' % round(st.s_std(self.nums),4))
    def s_se(self):
        return float('%.4f' % round(bt.sample_stand_err(self.nums),4))
    def simulation(self):
        sample=bt.sample_distr(self.nums)
        print("Simulation results: ")
        print("Theoretical mean and simulated mean: {},{}\nTheoretical SE and simulated SE: {},{}".format(float('%.4f' % round(st.s_mean(self.nums),4)),float('%.4f' % round(st.s_mean(sample),4)),bt.sample_stand_err(self.nums),float('%.4f' % round(st.s_std(sample),4))))
        bt.b_plot(sample)
    

