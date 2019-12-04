import statcalc.stats.distance as dt
import unittest


class TestDistance(unittest.TestCase):
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [3, 4, 5, 6, 7]
    nums3 = [1, 4, 6, 2, 4]

    @classmethod
    def setUpClass(cls):
        print("Set Up Class")

    def setUp(self):
        print('Set Up')

    def tearDown(self):
        print('Tear Down')

    def test_eDist(self):
        self.assertEqual(dt.e_distance(self.nums1, self.nums2), 4.47213595499958)
        self.assertEqual(dt.e_distance(self.nums1, self.nums3), 4.242640687119285)
        self.assertEqual(dt.e_distance(self.nums1, self.nums1), 0.0)
        self.assertEqual(dt.e_distance(self.nums2, self.nums3), 5.477225575051661)
        self.assertEqual(dt.e_distance(self.nums2, self.nums2), 0.0)

    def test_dotProd(self):
        self.assertEqual(dt.dotProduct(self.nums1, self.nums2), 85)
        self.assertEqual(dt.dotProduct(self.nums1, self.nums3), 55)
        self.assertEqual(dt.dotProduct(self.nums1, self.nums1), 55)
        self.assertEqual(dt.dotProduct(self.nums2, self.nums3), 89)
        self.assertEqual(dt.dotProduct(self.nums2, self.nums2), 135)


    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")


unittest.main(argv=[''], verbosity=2, exit=False)
