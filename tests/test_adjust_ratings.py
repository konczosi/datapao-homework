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

    def test_review_penalizer(self):
        """Test review_penalizer function"""
        self.assertEqual(adjust_ratings.review_penalizer(100_000, 0), 0.1)
        self.assertEqual(adjust_ratings.review_penalizer(99_999, 0), 0)
        self.assertEqual(adjust_ratings.review_penalizer(1000_001,1), 1.0)


if __name__ == '__main__':
    unittest.main()
