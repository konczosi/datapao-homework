# The Big IMDB quest
## Description
This Python application is designed to scrape the *[top 250 IMDb movies](https://www.imdb.com/chart/top/)* website
and extract data such as movie title, rating, number of ratings and number of Oscars.
The web scraper uses BeautifulSoup (bs4) to extract this information about movies.
Based on a given logic, the number of ratings and number of Oscar awards, the movies get an adjusted rating.
Finally, the data is saved with the adjusted ratings in a movies.csv file.
## Installation
1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/konczosi/datapao-homework.git
    ```
2. Create a virtual Python environment (e.g. with venv):
    ```bash
    python3 -m venv venv
    ```
3. Install the required packages with pip:
   ```bash
   python -m pip install -r requirements.txt
   ```
## Usage
- Simply run the `app.py` python file. The default number of movies to scrape is 20, but can be changed with the `-n` option.
    ```bash
    python app.py
    ```
- or
    ```bash
    python app.py -n 30
    ```
## Roadmap
- Use Docker to containerize the application.
- Benchmark and speed up the function that scrapes the number of Oscar awards.
## License 
- [MIT](LICENSE.md)