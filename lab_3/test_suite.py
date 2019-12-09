#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from testDistance import TestDistance
from testStats import TestStats
from bootstrap_test import TestBoot
from boot_func_test import Boot_func_test
from z_score_test import TestZ_score
from knn_test import TestKnn


# In[2]:


def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestDistance))
    suite.addTest(unittest.makeSuite(TestStats))
    #suite.addTest(unittest.makeSuite(Boot_func_test))
    #suite.addTest(unittest.makeSuite(TestBoot))
    suite.addTest(unittest.makeSuite(TestZ_score))
    suite.addTest(unittest.makeSuite(TestKnn))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[ ]:





# In[ ]:




