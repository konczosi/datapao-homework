import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from imdbquest import scrape_imdb

class TestScrapeIMDB(unittest.TestCase):

    def test_scrape_awards_has_oscar(self):
        """Test movie with oscars"""
        oscar_movie_id = "/title/tt0068646/" # The Godfather 3 Oscars
        self.assertEqual(scrape_imdb.scrape_awards(oscar_movie_id), 3)

    def test_scrape_awards_no_oscar(self):
        """Test movie with no oscars"""
        no_oscar_movie_id = "/title/tt0111161/" # The Shawshank Redemption 0 Oscars
        self.assertEqual(scrape_imdb.scrape_awards(no_oscar_movie_id), 0)

    def test_scrape_awards_sys_exit(self):
        """Test broken link"""
        wrong_movie_id = "/title/tt0/"
        with self.assertRaises(SystemExit) as cm:
            scrape_imdb.scrape_awards(wrong_movie_id)
        self.assertEqual(cm.exception.code, 1)

    def test_cast_df(self):
        """Test cast_df function"""
        df_before = pd.DataFrame({'title': "test", 'rating': "9.2",'ratings_count': 2707286.0, "oscars_count": "0"}, index=[0])
        df_after = pd.DataFrame({'title': "test", 'rating': 9.2,'ratings_count': 2707286, "oscars_count": 0}, index=[0])
        df_real = scrape_imdb.cast_df(df_before)
        assert_frame_equal(df_after, df_real)

    def test_scrape_top_movies_sys_exit(self):
        """Test whether the final DataFrame correct"""
        df_expected = pd.DataFrame({'title': "The Shawshank Redemption", 'rating': 9.2,'ratings_count': 2707286, "oscars_count": 0}, index=[0])
        df_real = scrape_imdb.scrape_top_movies(movies_count = 1)
        # 10 percent relative tolerance - number of votes updates frequently
        assert_frame_equal(df_expected, df_real,rtol=0.1)

if __name__ == '__main__':
    unittest.main()
