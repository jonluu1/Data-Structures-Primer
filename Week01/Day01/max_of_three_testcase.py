import unittest
from max_of_three import max_of_three

class TestCases(unittest.TestCase):
    def test_max_of_three_all_positions(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(1, 3, 2), 3)
        self.assertEqual(max_of_three(3, 2, 1), 3)
    def test_max_of_three_floats(self):
        self.assertAlmostEqual(max_of_three(1.1, 1.2, 1.3), 1.3)
        self.assertAlmostEqual(max_of_three(1.1, 1.3, 1.2), 1.3)
        self.assertAlmostEqual(max_of_three(1.3, 1.2, 1.1), 1.3)
    def test_max_of_three_two_same(self):
        self.assertEqual(max_of_three(1, 1, 3), 3)
        self.assertEqual(max_of_three(1, 3, 1), 3)
        self.assertEqual(max_of_three(3, 1, 1), 3)
        self.assertEqual(max_of_three(1, 3, 3), 3)
        self.assertEqual(max_of_three(3, 3, 1), 3)
        self.assertEqual(max_of_three(3, 1, 3), 3)
    def test_max_of_three_all_same(self):
        self.assertEqual(max_of_three(3, 3, 3), 3)

if __name__ == '__main__':
    unittest.main()
