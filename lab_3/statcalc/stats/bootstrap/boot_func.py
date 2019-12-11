#!/usr/bin/env python
# coding: utf-8

# In[57]:


class LengthError(Exception):
    pass
class NonNumpy(Exception):
    pass


# In[ ]:





# In[62]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys
#sys.path.append("..")

import statcalc.stats.stats as st

def resample(nums):
    try:
        if type(nums)!=np.ndarray:
            raise(NonNumpy)
        ran=np.random.choice(nums,size=int(len(nums)/3),replace=True)
        if nums.shape[0]<50:
            raise(LengthError)
        return ran
    except LengthError:
        print ("The array of size {} too short".format(nums.shape[0]))
    except NonNumpy:
        print("Inapropriate type, pass numpy array")

def sample_stand_err(nums):
    try:
        if type(nums)!=np.ndarray:
            raise(NonNumpy)
        if nums.shape[0]<50:
            raise(LengthError)
        return float('%.4f' % round((st.sample_std(nums)/len(nums)**0.5),4))
    except LengthError:
        print ("The array of size {} too short".format(nums.shape[0]))
    except NonNumpy:
        print("Inapropriate type, pass numpy array")

def stand_err(nums):
    try:
        if type(nums)!=np.ndarray:
            raise(NonNumpy)
        if nums.shape[0]<50:
            raise(LengthError)
        return float('%.4f' % round((st.s_std(nums)/len(nums)**0.5),4))
    except LengthError:
        print ("The array of size {} too short".format(nums.shape[0])) 
    except NonNumpy:
        print("Inapropriate type, pass numpy array")

def sample_distr(nums):
    try:
        if type(nums)!=np.ndarray:
            raise(NonNumpy)
        if nums.shape[0]<50:
            raise(LengthError)
        sample_props=[]
        for _ in range(10000):
            sample=resample(nums)
            sample_props.append(st.s_mean(sample))
        sample_props=np.array(sample_props)
        return sample_props
    except LengthError:
        print ("The array of size {} too short".format(nums.shape[0])) 
    except NonNumpy:
        print("Inapropriate type, pass numpy array")

def b_plot(nums):
    plt.hist(nums,color="pink",linewidth=2)
    plt.xlabel('Mean')
    plt.title('Simulated sampling distribution') 
    plt.show()



# In[63]:

