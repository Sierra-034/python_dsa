import unittest
from src.comparison import SavingsAccount

class ComparisonTest(unittest.TestCase):
    def test_comparison_lt(self):
        s1 = SavingsAccount('Ken', '1000', 0)
        s2 = SavingsAccount('Bill', '1001', 30)
        self.assertFalse(s1 < s2)
        self.assertTrue(s2 < s1)

    def test_comparison_gt(self):
        s1 = SavingsAccount('Ken', '1000', 0)
        s2 = SavingsAccount('Bill', '1001', 30)
        self.assertTrue(s1 > s2)
        self.assertFalse(s2 > s1)

    def test_comparison_eq(self):
        s1 = SavingsAccount('Ken', '1000', 0)
        s2 = SavingsAccount('Bill', '1001', 30)
        self.assertFalse(s1 == s2)
        self.assertTrue(s1 != s2)


if __name__ == '__main__':
    unittest.main()
