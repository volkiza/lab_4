#!/usr/bin/env python
# coding: utf-8

# In[12]:


import unittest
import statcalc.stats.bootstrap.boot_func as st
import numpy as np
from unittest import mock
import matplotlib.pyplot as plt


# In[16]:


class Boot_func_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass Boot_func_test')
    def setUp(self):
        #We need to setup arrays for every function because resampling is used
        self.p1=np.array([47, 51, 21, 32,  9, 40, 20, 17, 31, 13, 56, 53, 55,  9, 26, 45, 17,
       53, 11, 29, 29, 11, 33,  0, 47, 59, 40, 53, 42,  3, 21, 27, 30, 55,
        1, 14, 56, 56, 49, 31,  1, 30, 26, 13, 54, 46, 11, 32, 53, 42, 16,
       20, 18, 35, 44, 12, 22, 12,  4, 34, 22, 35, 34, 53, 15, 15, 25, 19,
       34,  9, 15, 33, 16, 44, 23, 12, 44, 41, 57, 56, 52,  7, 26, 22, 40,
       26, 44, 35, 12, 28, 15,  8,  5, 31, 12, 48, 38, 59, 44, 57,  0, 57,
       51, 58, 44, 13, 54, 24, 42,  6, 27, 24, 44, 47, 14,  4, 49,  3, 24,
        3, 34, 19, 18, 38, 28, 57, 30, 46, 19, 26, 57, 27, 46,  0, 15,  6,
       52, 19, 12, 41, 24, 53, 40,  6, 30, 34, 13, 10, 37,  7, 33,  5, 59,
        8, 42, 50, 43, 30, 47, 16, 42, 59, 17, 43, 38, 47, 34, 12,  1, 46,
       44, 13, 14, 18, 39,  2, 44, 25, 51, 28, 40, 24, 21, 49, 14, 26, 23,
       56, 23, 11, 55,  2, 17, 19, 43, 12, 38,  5, 38, 47, 55, 43, 26, 36,
       30, 48, 49, 57, 17, 30, 33, 12, 59, 50, 34, 49, 40, 49,  2, 54, 24,
       44,  5, 34, 45, 23, 56, 19, 31, 14, 50, 26, 17, 21, 46, 50, 42, 24,
       14, 13, 44, 56, 30, 28, 30,  0, 54, 26, 23, 44])

        self.p4=[314, 438, 478, 346, 213, 317, 456, 200,  20, 225, 253, 299, 171,
       307, 226, 469,  72, 139, 171, 345,   1, 469, 434, 334,  45,  16,
       415,  17, 421, 102, 112, 134, 295, 440, 394, 168, 355, 204, 122,
       488, 355, 317, 288,  23, 270,  64, 368, 367, 478, 406,  65,  39,
        46,  40, 147,  92,   6,  28, 484, 215]
        self.p6=np.array([1])
        print("The variables are initialized")
    def test_sample_stand_err(self):
        print("Test sample_stand_err")
        self.assertEqual(st.sample_stand_err(self.p1),1.0645)

    def test_stand_err(self):
        print("Test stand_err")
        self.assertIsNotNone(st.stand_err(self.p1))

    def test_sample_distr(self):
        print("Test sample_distr")
        self.assertEqual(len(st.sample_distr(self.p1)),10000)

    def test_resample(self):
        print("Test resample")
        self.assertEqual(int(len(self.p1)/3), len(st.resample(self.p1)))

        self.assertFalse(st.resample(self.p6))
        self.assertFalse(st.resample(self.p4))

    @mock.patch("%s.st.plt" % __name__)
    def test_module(self,mock_plt):
        st.b_plot(self.p1)
        assert mock_plt.title.call_args_list[0][0][0] == 'Simulated sampling distribution'
        assert mock_plt.hist.called
       
    def tearDown(self):
        print("The test is over")
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass Boot_func_test')
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




