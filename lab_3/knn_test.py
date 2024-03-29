#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import knn as k
import numpy as np


# In[3]:


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
        self.assertIsNone(k.knn(dataset, dataset[5], 0))
        self.assertIsNone(k.knn(dataset, 0, 4))
        
        dataset1 = np.random.choice(range(1,200),200)
        self.assertEqual(k.knn(dataset1, dataset1[5], 4), 118.75)
        self.assertIsNone(k.knn(dataset1, dataset1[5], 0))
        self.assertIsNone(k.knn(dataset1, 0, 4))
        
        dataset2 = np.random.choice(range(1,300),300)
        self.assertEqual(k.knn(dataset2, dataset2[5], 4), 212.25)
        self.assertIsNone(k.knn(dataset2, dataset2[5], 0))
        self.assertIsNone(k.knn(dataset2, 0, 4))
        
        dataset3 = np.random.choice(range(1,400),400)
        self.assertEqual(k.knn(dataset3, dataset3[5], 4), 44.0)
        self.assertIsNone(k.knn(dataset3, dataset3[5], 0))
        self.assertIsNone(k.knn(dataset3, 0, 4))
        
        dataset4 = np.random.choice(range(1,500),500)
        self.assertEqual(k.knn(dataset4, dataset4[5], 4), 149.5)
        self.assertIsNone(k.knn(dataset4, dataset4[5], 0))
        self.assertIsNone(k.knn(dataset4, 0, 4))

    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




