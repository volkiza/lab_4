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
    except:
        print("Something wrong, try one more time")
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
    except:
        print("Something wrong, try one more time")
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
    except:
        print("Something wrong, try one more time")
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



# In[63]:


p1=np.arange(0,100)
p1


# In[64]:


resample(p1)


# In[65]:


p2=[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


# In[66]:


type(p2)


# In[67]:


resample(p2)


# In[68]:


p3=np.arange(0,40)
p3


# In[51]:


resample(p3)


# In[ ]:




