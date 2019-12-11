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
        self.p2=np.array([37, 189,  83, 351, 339,  67, 212, 493, 423, 280, 430, 100, 178,
               391, 133, 204, 305, 120, 494, 183,  15, 175, 216, 183,  93,  64,
                85, 286, 211, 356, 118, 476,  19, 105, 253, 112, 478, 229, 178,
               385, 329, 148, 107, 353, 371, 115, 467, 451, 313, 444,  73, 293,
               329, 190,  99, 334, 316, 123, 269, 239, 153,  80, 147, 301, 386,
               392, 315, 266, 161, 372,  26, 128,  70,  44, 102, 100, 328, 414,
               258, 183, 177, 349, 435, 210, 497, 222, 420, 311, 339, 298, 299,
               298, 227, 324, 120, 132, 250, 328, 384, 426, 465,  84, 151, 489,
               149, 327, 245, 148,  42, 298, 453,  27, 435, 400, 154, 170,  46,
                21, 109,  82, 152,   6, 291,  29, 232, 253,  68, 328, 336, 399,
               247, 172, 250, 106, 288, 135, 317,  85, 427, 114, 341, 286, 284,
               291, 417,  11, 407,  27, 112, 315,  32, 158, 439, 472, 112, 472,
                 1, 202, 245, 398,  52, 482, 102, 402,  87, 115, 157, 278, 149,
                89, 383, 297,  79, 349, 445, 182, 496,  30, 255, 474,  60, 173,
               127, 197, 171, 295, 398, 180, 410,  68, 422, 263, 396, 469, 482,
               393,  53, 188,  43,   8, 469, 386,  55, 227, 485, 319, 307, 488,
                17,  80,  49, 234, 224, 105, 266, 486, 217,  48, 410, 245, 123,
                71, 403, 166, 417, 218, 427, 224, 490, 321, 318,  15, 395, 396,
               459, 407, 167, 180, 146, 137, 444, 214, 282,  70, 302, 492, 476,
               414, 375, 169])
        self.p3=np.array([3571,  800,  988, 1914,  663, 3732,  498, 2041, 3381, 2763,   49,
       2871, 1205, 3001, 3342, 1240, 2737, 3074, 2695,  394,  271, 3322,
       1818, 2622, 1404, 1233, 3792, 1359,  399, 3045, 2614, 1842, 1347,
       2701,  195, 1889,  715, 3434, 3068,  337, 2978,  133, 1573,   40,
       3543, 2081, 1527, 1452, 2480,  853,  943])
        self.p4=np.array([314, 438, 478, 346, 213, 317, 456, 200,  20, 225, 253, 299, 171,
       307, 226, 469,  72, 139, 171, 345,   1, 469, 434, 334,  45,  16,
       415,  17, 421, 102, 112, 134, 295, 440, 394, 168, 355, 204, 122,
       488, 355, 317, 288,  23, 270,  64, 368, 367, 478, 406,  65,  39,
        46,  40, 147,  92,   6,  28, 484, 215])
        self.p5=np.array([3014, 3244,  469, 1335, 2175, 2710, 1085, 2332,  934, 3713, 3782,
        523, 1370, 2437,  438, 2889, 3485, 1940, 3532, 2782,  907,  405,
        170, 3662, 2278, 3814, 2656, 3375, 1627, 1392, 1034,  196, 2146,
       3750,  662, 2785, 3121, 1119,  720,  108, 1807, 1550, 3126, 3351,
        294, 3356, 1258, 3685, 2052, 1032,  362,  802, 1050, 3835, 3696,
       3024, 3277,  117, 3458,  869, 3142,  796, 2530, 1044, 1688, 3095,
       3009, 2108,  943, 1361, 2247, 1733, 1341, 1258, 3484, 3610,  821,
       1046])
        self.b1=bs.Bootstrap(self.p1)
        self.b2=bs.Bootstrap(self.p2)
        self.b3=bs.Bootstrap(self.p3)
        self.b4=bs.Bootstrap(self.p4)
        self.b5=bs.Bootstrap(self.p5)
        print("The variables are initialized")
    def test_mean(self):
        print("Test mean")
        self.assertEqual(self.b1.mean(),30.716)
        self.assertEqual(self.b2.mean(),247.08)
        self.assertEqual(self.b3.mean(),1881.7451)
        self.assertEqual(self.b4.mean(),242.05)
        self.assertEqual(self.b5.mean(),2017.6026)
    def test_sd(self):
        print("Test sd")
        self.assertEqual(self.b1.sd(),16.798)
        self.assertEqual(self.b2.sd(),143.0241)
        self.assertEqual(self.b3.sd(),1143.7814)
        self.assertEqual(self.b4.sd(),155.8683)
        self.assertEqual(self.b5.sd(),1174.1176)
    def test_se(self):
        print("Test stand_err")
        self.assertEqual(self.b1.s_se(),1.0645)
        self.assertEqual(self.b2.s_se(),9.0638)
        self.assertEqual(self.b3.s_se(),161.7551)
        self.assertEqual(self.b4.s_se(),20.2923)
        self.assertEqual(self.b5.s_se(),133.8031)
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




