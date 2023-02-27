import pandas as pd
from imdbquest import adjust_ratings, scrape_imdb


def main():
    """Main function for the IMDB Quest application"""
    df = scrape_imdb.scrape_top_movies(movies_count=2)
    
    # Adjusting ratings by number of oscars
    df["adjusted_rating"] = df.apply(
        lambda x: x["rating"] + adjust_ratings.oscar_calculator(x["oscars_count"]),
        axis=1,
    )
    print(df)
    # Adjusting ratings by number of reviews


if __name__ == "__main__":
    main()
