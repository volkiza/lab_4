#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest
import z_score as z
import numpy as np


# In[4]:


class TestZ_score(unittest.TestCase):
    
    np.random.seed(12345)
    
    @classmethod
    def setUpClass(cls):
        print("Set Up Class")

    def setUp(self):
        print('Set Up')
    
    def test_p_zscore(self):
        np.random.seed(12345)
        self.assertEqual(z.p_zscore(6,3,7), 1.414213562373095)
        self.assertIsNone(z.p_zscore(6,3,0))
        self.assertIsNone(z.p_zscore('test',3,0))
        self.assertEqual(z.p_zscore(2,3,5), 0.7071067811865476)
        self.assertIsNone(z.p_zscore(2,0,6))
        self.assertIsNone(z.p_zscore('test',3,5))
        self.assertEqual(z.p_zscore(3,3,5), 2.449489742783178)
        self.assertIsNone(z.p_zscore(3,3,-1))
        self.assertIsNone(z.p_zscore('test',3,5))
        self.assertEqual(z.p_zscore(4,3,5), 1.8708286933869707)
        self.assertIsNone(z.p_zscore(4,0,5))
        self.assertIsNone(z.p_zscore('test',3,5))
        self.assertEqual(z.p_zscore(5,3,5), 5.65685424949238)
        self.assertIsNone(z.p_zscore(5,3,-1))
        self.assertIsNone(z.p_zscore('test',3,5))
    
    def test_p_se(self):
        np.random.seed(12345)
        self.assertEqual(z.p_se(3,5), 0.7200822998230956)
        self.assertIsNone(z.p_se(3,0))
        
        self.assertEqual(z.p_se(4,10), 1.4737282653189494)
        self.assertIsNone(z.p_se(0,10))
        
        self.assertEqual(z.p_se(5,15), 2.2018174311236614)
        self.assertIsNone(z.p_se(5,0))
        
        self.assertEqual(z.p_se(6,20), 2.0092379244472363)
        self.assertIsNone(z.p_se(0,20))
        
        self.assertEqual(z.p_se(7,25), 2.7658896891587617)
        self.assertIsNone(z.p_se(7,0))
        
    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




