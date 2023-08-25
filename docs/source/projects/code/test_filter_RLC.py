import unittest
from filter_RLC import RLC_BP3_Filter

class TestRLC_BP3_Filter(unittest.TestCase):

    def setUp(self):
        self.L = 10**-3
        self.Tm_ref, self.w0_ref, self.m_ref = 0.5, 10*3, 0.2
        self.my_filter = RLC_BP3_Filter(10**3, 10**3, 10**-9, self.L)

    def test_set_and_get_params(self):
        self.my_filter.set_components(self.Tm_ref, self.w0_ref, self.m_ref)
        _, Tm, w0, m = self.my_filter.get_params()

        self.assertAlmostEqual(Tm, self.Tm_ref, places=20)
        self.assertAlmostEqual(w0, self.w0_ref, places=20)
        self.assertAlmostEqual(m, self.m_ref, places=20)


if __name__ == "__main__":
    unittest.main()