#!/usr/bin/env python
# coding: utf-8

# In[1]:


class nonNegative(Exception):
    """Raised when the input value is a negative number"""
    pass
class nonText(Exception):
    """Raised when the input value is a string"""
    pass


# In[2]:


#z_score
import numpy as np
import statcalc.stats.stats as st

def p_obs(n,values):
    try:
        if values <= 0:
            raise(nonNegative)
        if n <= 0:
            raise(nonNegative)
        population = np.random.randint(0,values, size = n)
        return population
    except nonNegative:
        print ("Error: values and n should be greater than 0")

def p_zscore(x,n,values):
    try:
        if values <= 0:
            raise(nonNegative)
        if n <= 0:
            raise(nonNegative)
        if x == str(x):
            raise(nonText)
        z = (x - st.s_mean(p_obs(n,values))) / st.s_std(p_obs(n,values))
        return z
    except nonNegative:
        print ("Error: values and n should be greater than 0")
    except nonText:
        print("Error: not supporting string, please type a number")


def p_se(n,values):
    try:
        if values <= 0:
            raise(nonNegative)
        if n <= 0:
            raise(nonNegative)
        se = st.s_std(p_obs(n,values)) / (len(p_obs(n,values))**(1/2))
        return se
    except nonNegative:
        print ("Error: values and n should be greater than 0")
    except:
        print("Error: unknown")


# In[9]:


np.random.seed(12345)
print(p_zscore(6,3,7))
print(p_zscore(2,3,5))
print(p_zscore(3,3,5))
print(p_zscore(4,3,5))
print(p_zscore(5,3,5))


# In[10]:


np.random.seed(12345)
print(p_se(3,5))
print(p_se(4,10))
print(p_se(5,15))
print(p_se(6,20))
print(p_se(7,25))


# In[ ]:




