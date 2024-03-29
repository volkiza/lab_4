import statcalc.stats.stats as st
import unittest


class TestStats(unittest.TestCase):
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [3, 4, 5, 6, 7]
    nums5 = [2, 4, 6, 7, 8]
    nums4 = [1, 3, 5, 7, 9]
    nums3 = [1, 4, 6, 2, 4]

    @classmethod
    def setUpClass(cls):
        print("Set Up Class")

    def setUp(self):
        print('Set Up')

    def tearDown(self):
        print('Tear Down')

    def test_mean(self):
        self.assertEqual(st.s_mean(self.nums1), 3)
        self.assertEqual(st.s_mean(self.nums2), 5)
        self.assertEqual(st.s_mean(self.nums3), 3.4)
        self.assertEqual(st.s_mean(self.nums4), 5.0)
        self.assertEqual(st.s_mean(self.nums5), 5.4)

    def test_median(self):
        self.assertEqual(st.s_median(self.nums1), 3)
        self.assertEqual(st.s_median(self.nums2), 5)
        self.assertEqual(st.s_median(self.nums3), 4)
        self.assertEqual(st.s_median(self.nums4), 5)
        self.assertEqual(st.s_median(self.nums5), 6)

    def test_var(self):
        self.assertEqual(st.s_var(self.nums1), 2)
        self.assertEqual(st.s_var(self.nums2), 2)
        self.assertEqual(st.s_var(self.nums3), 3.04)
        self.assertEqual(st.s_var(self.nums4), 8.0)
        self.assertEqual(st.s_var(self.nums5), 4.64)

    def test_sampleVar(self):
        self.assertEqual(st.sample_var(self.nums1), 2.5)
        self.assertEqual(st.sample_var(self.nums2), 2.5)
        self.assertEqual(st.sample_var(self.nums3), 3.8)
        self.assertEqual(st.sample_var(self.nums4), 10.0)
        self.assertEqual(st.sample_var(self.nums5), 5.8)

    def test_std(self):
        self.assertEqual(st.s_std(self.nums1), 1.4142135623730951)
        self.assertEqual(st.s_std(self.nums2), 1.4142135623730951)
        self.assertEqual(st.s_std(self.nums3), 1.7435595774162693)
        self.assertEqual(st.s_std(self.nums4), 2.8284271247461903)
        self.assertEqual(st.s_std(self.nums5), 2.1540659228538015)

    def test_sampleSd(self):
        self.assertEqual(st.sample_std(self.nums1), 1.5811388300841898)
        self.assertEqual(st.sample_std(self.nums2), 1.5811388300841898)
        self.assertEqual(st.sample_std(self.nums3), 1.9493588689617927)
        self.assertEqual(st.sample_std(self.nums4), 3.1622776601683795)
        self.assertEqual(st.sample_std(self.nums5), 2.4083189157584592)

    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")


unittest.main(argv=[''], verbosity=2, exit=False)