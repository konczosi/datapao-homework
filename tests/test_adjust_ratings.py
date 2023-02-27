import unittest
from imdbquest import adjust_ratings

class TestAdjustRatings(unittest.TestCase):

    def test_oscar_calculator(self):
        """Test oscar_calculator function"""
        self.assertEqual(adjust_ratings.oscar_calculator(0), 0)
        self.assertEqual(adjust_ratings.oscar_calculator(1), 0.3)
        self.assertEqual(adjust_ratings.oscar_calculator(2), 0.3)
        self.assertEqual(adjust_ratings.oscar_calculator(3), 0.5)
        self.assertEqual(adjust_ratings.oscar_calculator(4), 0.5)
        self.assertEqual(adjust_ratings.oscar_calculator(5), 0.5)
        self.assertEqual(adjust_ratings.oscar_calculator(6), 1.0)
        self.assertEqual(adjust_ratings.oscar_calculator(8), 1.0)
        self.assertEqual(adjust_ratings.oscar_calculator(10), 1.0)
        self.assertEqual(adjust_ratings.oscar_calculator(11), 1.5)


if __name__ == '__main__':
    unittest.main()
