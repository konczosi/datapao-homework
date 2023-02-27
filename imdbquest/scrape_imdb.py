import sys
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_awards(movie_id: str) -> int:
    """Scrape number of oscars (if any) from movie's award page."""
    result = 0
    url = f"https://www.imdb.com{movie_id}awards/"
    response = requests.get(url, headers={"Accept-Language":"en"}, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        awards = soup.find_all('td',class_='title_award_outcome')
        for award in awards:
            if award.text == "\nWinner\nOscar\n":
                result = award.get('rowspan')
    else:
        print(f"Cannot access movie's award webpage. Url: {url}")
        sys.exit(1)

    return int(result)

def cast_df(df: pd.DataFrame) -> pd.DataFrame:
    """ Casting the pandas dataframe to the appropriate datatypes"""
    df['title'] = df['title'].astype(str)
    df['rating'] = df['rating'].astype(float)
    df['ratings_count'] = df['ratings_count'].astype(int)
    df['oscars_count'] = df['oscars_count'].astype(int)

    return df

def scrape_top_movies(movies_count : int =20) -> pd.DataFrame:
    """Scrape n movies from IMDB Top 250 webpage."""
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url, headers={"Accept-Language":"en"}, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        raw_movies = soup.find('tbody',class_='lister-list').find_all('tr',limit=movies_count)
        movies = []

        for raw_movie in raw_movies:
            title = raw_movie.find('td',class_='titleColumn').a.text
            rating = raw_movie.find('td',class_='ratingColumn imdbRating').strong.text
            ratings_count = raw_movie.find('span', attrs={'name': 'nv'}).get('data-value')
            movie_id = raw_movie.find('td',class_='titleColumn').a.get('href')
            oscars_count = scrape_awards(movie_id)

            data = {'title': title,
                    'rating': rating,
                    'ratings_count': ratings_count,
                    'oscars_count': oscars_count}
            movies.append(data)
    else:
        print(f"Cannot access IMDB webpage. Url: {url}")
        sys.exit(1)

    df_movies = cast_df(pd.DataFrame(movies))
    return df_movies
