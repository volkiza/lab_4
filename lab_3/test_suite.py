#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from testDistance import TestDistance
from testStats import TestStats
from bootstrap_test import TestBoot
from boot_func_test import Boot_func_test


# In[2]:


def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestDistance))
    suite.addTest(unittest.makeSuite(TestStats))
    suite.addTest(unittest.makeSuite(Boot_func_test))
    suite.addTest(unittest.makeSuite(TestBoot))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[ ]:




