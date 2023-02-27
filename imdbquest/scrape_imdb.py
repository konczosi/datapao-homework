import sys
import re
import requests
from bs4 import BeautifulSoup

def scrape_awards(movie_id: str) -> int:
    """Scrape number of oscars (if any) from movie's award page."""

    result = 0
    url = f"https://www.imdb.com/title{movie_id}"
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

def scrape_top_movies():
    """Scrape n movies from IMDB Top 250 webpage."""
