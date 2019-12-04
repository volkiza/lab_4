#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import statcalc.stats.bootstrap.boot_func as st
import numpy as np


# In[2]:


class Boot_func_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass Boot_func_test')
    def setUp(self):
        #We need to setup arrays for every function because resampling is used
        self.p1=np.array([166, 201, 458, 190, 445,  87, 385, 427, 387, 166, 474,  49, 430,
       205,  54, 343, 413, 389,  20,  58, 191,  87, 463,  88, 389,  52,
       102,   1, 102,  20])
        self.p2=[1,2,3,4,5,6,7,8,9,10]
        self.p3=np.array([61, 26, 80, 82, 92, 21, 30, 68, 97, 42, 56,  8, 36, 35, 56,  9, 73,
       69, 87, 68,  7,  8, 84, 71, 99, 80, 67, 51, 15, 25])
        self.p4=np.array([314, 438, 478, 346, 213, 317, 456, 200,  20, 225, 253, 299, 171,
       307, 226, 469,  72, 139, 171, 345,   1, 469, 434, 334,  45,  16,
       415,  17, 421, 102, 112, 134, 295, 440, 394, 168, 355, 204, 122,
       488, 355, 317, 288,  23, 270,  64, 368, 367, 478, 406,  65,  39,
        46,  40, 147,  92,   6,  28, 484, 215])
        self.p5=[135,  61, 103,  73,  43,  11, 330, 294,  39,  65, 477, 130, 462,
       488, 438]
        print("The variables are initialized")
    def test_sample_stand_err(self):
        print("Test sample_stand_err")
        self.assertEqual(st.sample_stand_err(self.p1),30.4842)
        self.assertIsNotNone(st.sample_stand_err(self.p2))
        self.assertIsNotNone(st.sample_stand_err(self.p3))
        self.assertEqual(st.sample_stand_err(self.p4),20.2923)
        self.assertEqual(st.sample_stand_err(self.p5),47.1935)
    def test_stand_err(self):
        print("Test stand_err")
        self.assertIsNotNone(st.stand_err(self.p1))
        self.assertEqual(st.stand_err(self.p2),0.9083)
        self.assertEqual(st.stand_err(self.p3),5.2748)
        self.assertEqual(st.stand_err(self.p4),20.1225)
        self.assertIsNotNone(st.stand_err(self.p5))
    def test_sample_distr(self):
        print("Test sample_distr")
        self.assertEqual(len(st.sample_distr(self.p1)),10000)
        self.assertEqual(len(st.sample_distr(self.p2)),10000)
        self.assertIsNotNone(st.sample_distr(self.p3))
        self.assertIsNotNone(st.sample_distr(self.p4))
        self.assertIsNotNone(st.sample_distr(self.p5))
    def test_resample(self):
        print("Test resample")
        self.assertEqual(int(len(self.p1)/3), len(st.resample(self.p1)))
        self.assertEqual(int(len(self.p2)/3), len(st.resample(self.p2)))
        self.assertEqual(int(len(self.p3)/3), len(st.resample(self.p3)))
        self.assertIsNotNone(st.resample(self.p4))
        self.assertIsNotNone(st.resample(self.p5))
    def tearDown(self):
        print("The test is over")
    @classmethod
    def tearDownClass(cls):
        print('teardownClass Boot_func_test')
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




