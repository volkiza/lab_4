#!/usr/bin/env python
# coding: utf-8

# In[1]:


#z_score
import numpy as np
import statcalc.stats.stats as st

def p_obs(n,values):
    population = np.random.randint(0,values, size = n)
    return population

def p_zscore(x,n,values):
    z = (x - st.s_mean(p_obs(n,values))) / st.s_std(p_obs(n,values))
    return z

def p_se(n,values):
    se = st.s_std(p_obs(n,values)) / (len(p_obs(n,values))**(1/2))
    return se


# In[ ]:





# In[ ]:




