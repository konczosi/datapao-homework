### test movei with oscars, movie with only nominations, movie with no awards at all, and a non existent movie.
import unittest
from imdbquest import scrape_imdb

class TestScrapeIMDB(unittest.TestCase):

    def test_scrape_has_oscar(self):
        """Test movie with oscars"""
        oscar_movie_id = "/tt0068646/awards/" # The Godfather 3 Oscars
        self.assertEqual(scrape_imdb.scrape_awards(oscar_movie_id), 3)

    def test_scrape_no_oscar(self):
        """Test movie with no oscars"""
        no_oscar_movie_id = "/tt0111161/awards/" # The Shawshank Redemption 0 Oscars
        self.assertEqual(scrape_imdb.scrape_awards(no_oscar_movie_id), 0)

    def test_scrape_sys_exit(self):
        """Test broken link"""
        wrong_movie_id = "/tt0/awards/"
        with self.assertRaises(SystemExit) as cm:
            scrape_imdb.scrape_awards(wrong_movie_id)
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
