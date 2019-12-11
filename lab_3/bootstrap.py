#!/usr/bin/env python
# coding: utf-8

# In[5]:


class LengthError(Exception):
    pass
class NonNumpy(Exception):
    pass

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
    def print_nums(self):
        try:
            if type(self.nums)!=np.ndarray:
                raise(NonNumpy)
            if self.nums.shape[0]<50:
                raise(LengthError)
            return print ("The original array is: {}".format(self.nums))
        except LengthError:
            print ("The array of size {} too short".format(self.nums.shape[0]))
        except NonNumpy:
            print("Inapropriate type, pass numpy array")
        except:
            print("Something wrong, try one more time")
        
    def mean(self):
        try:
            if type(self.nums)!=np.ndarray:
                raise(NonNumpy)
            if self.nums.shape[0]<50:
                raise(LengthError)
            return float('%.4f' % round(st.s_mean(self.nums),4))
        except LengthError:
            print ("The array of size {} too short".format(self.nums.shape[0]))
        except NonNumpy:
            print("Inapropriate type, pass numpy array")
        except:
            print("Something wrong, try one more time")
        
    def sd(self):
        try:
            if type(self.nums)!=np.ndarray:
                raise(NonNumpy)
            if self.nums.shape[0]<50:
                raise(LengthError)
            return float('%.4f' % round(st.s_std(self.nums),4))
        except LengthError:
            print ("The array of size {} too short".format(self.nums.shape[0]))
        except NonNumpy:
            print("Inapropriate type, pass numpy array")
        except:
            print("Something wrong, try one more time")
        
    def s_se(self):
        return float('%.4f' % round(bt.sample_stand_err(self.nums),4))
    def simulation(self):
        sample=bt.sample_distr(self.nums)
        print("Simulation results: ")
        print("Theoretical mean and simulated mean: {},{}\nTheoretical SE and simulated SE: {},{}".format(float('%.4f' % round(st.s_mean(self.nums),4)),float('%.4f' % round(st.s_mean(sample),4)),bt.sample_stand_err(self.nums),float('%.4f' % round(st.s_std(sample),4))))
        bt.b_plot(sample)
    


# In[ ]:




