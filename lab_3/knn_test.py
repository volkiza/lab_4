#!/usr/bin/env python
# coding: utf-8

# In[23]:


import unittest
import knn as k
import numpy as np


# In[24]:


class TestKnn(unittest.TestCase):
    
    np.random.seed(12345)
    
    @classmethod
    def setUpClass(cls):
        print("Set Up Class")

    def setUp(self):
        print('Set Up')
    
    def test_knn(self):
        np.random.seed(12345)
        dataset = np.random.choice(range(1,100),100)
        self.assertEqual(k.knn(dataset, dataset[5], 4), 36.0)
        dataset1 = np.random.choice(range(1,200),200)
        self.assertEqual(k.knn(dataset1, dataset1[5], 4), 118.75)
        dataset2 = np.random.choice(range(1,300),300)
        self.assertEqual(k.knn(dataset2, dataset2[5], 4), 212.25)
        dataset3 = np.random.choice(range(1,400),400)
        self.assertEqual(k.knn(dataset3, dataset3[5], 4), 44.0)
        dataset4 = np.random.choice(range(1,500),500)
        self.assertEqual(k.knn(dataset4, dataset4[5], 4), 149.5)

    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




