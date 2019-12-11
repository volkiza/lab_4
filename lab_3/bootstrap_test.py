#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import numpy as np
import matplotlib.pyplot as plt

from unittest import mock

from statcalc.stats.bootstrap import bootstrap as bs


# In[4]:


class TestBoot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupclass TestBoot')
    def setUp(self):
        #We need to setup arrays for every function because resampling is used
        self.p1=np.array([166, 201, 458, 190, 445,  87, 385, 427, 387, 166, 474,  49, 430,
       205,  54, 343, 413, 389,  20,  58, 191,  87, 463,  88, 389,  52,
       102,   1, 102,  20])
        self.p2=np.array([1,2,3,4,5,6,7,8,9,10])
        self.p3=np.array([61, 26, 80, 82, 92, 21, 30, 68, 97, 42, 56,  8, 36, 35, 56,  9, 73,
       69, 87, 68,  7,  8, 84, 71, 99, 80, 67, 51, 15, 25])
        self.p4=np.array([314, 438, 478, 346, 213, 317, 456, 200,  20, 225, 253, 299, 171,
       307, 226, 469,  72, 139, 171, 345,   1, 469, 434, 334,  45,  16,
       415,  17, 421, 102, 112, 134, 295, 440, 394, 168, 355, 204, 122,
       488, 355, 317, 288,  23, 270,  64, 368, 367, 478, 406,  65,  39,
        46,  40, 147,  92,   6,  28, 484, 215])
        self.p5=np.array([135,  61, 103,  73,  43,  11, 330, 294,  39,  65, 477, 130, 462,
       488, 438])
        self.b1=bs.Bootstrap(self.p1)
        self.b2=bs.Bootstrap(self.p2)
        self.b3=bs.Bootstrap(self.p3)
        self.b4=bs.Bootstrap(self.p4)
        self.b5=bs.Bootstrap(self.p5)
        print("The variables are initialized")
    def test_mean(self):
        print("Test mean")
        self.assertEqual(self.b1.mean(),228.0667)
        self.assertEqual(self.b2.mean(),5.5000)
        self.assertEqual(self.b3.mean(),53.4333)
        self.assertEqual(self.b4.mean(),242.05)
        self.assertEqual(self.b5.mean(),209.9333)
    def test_sd(self):
        print("Test sd")
        self.assertEqual(self.b1.sd(),164.1625)
        self.assertEqual(self.b2.sd(),2.8723)
        self.assertEqual(self.b3.sd(),28.8914)
        self.assertEqual(self.b4.sd(),155.8683)
        self.assertEqual(self.b5.sd(),176.5818)
    def test_se(self):
        print("Test stand_err")
        self.assertEqual(self.b1.s_se(),30.4842)
        self.assertEqual(self.b2.s_se(),0.9574)
        self.assertEqual(self.b3.s_se(),5.3650)
        self.assertEqual(self.b4.s_se(),20.2923)
        self.assertEqual(self.b5.s_se(),47.1935)
    def test_is_instance(self):
        print("Check if the part of instance class")
        self.assertIsInstance(self.b1,bs.Bootstrap)
        self.assertIsInstance(self.b2,bs.Bootstrap)
        self.assertIsInstance(self.b3,bs.Bootstrap)
        self.assertIsInstance(self.b4,bs.Bootstrap)
        self.assertIsInstance(self.b5,bs.Bootstrap)
        self.assertNotIsInstance(self.p5,bs.Bootstrap)
    def test_print(self):
        self.assertFalse(self.b1.print_nums())
    def test_simulation(self):
        self.assertFalse(self.b1.simulation())
    def tearDown(self):
        print("The test is over")
    @classmethod
    def tearDownClass(cls):
        print('teardownClass TestBoot')
        
unittest.main(argv=[''], verbosity=2, exit=False)

# In[ ]:




