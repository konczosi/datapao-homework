import argparse
import os
import csv
from imdbquest import adjust_ratings, scrape_imdb

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default = 20, help="How many movies to scrape.")
    args = parser.parse_args()
    return args

def main():
    """Main function for the IMDB Quest application"""
    args = parse_args()
    df = scrape_imdb.scrape_top_movies(args.n)
    # Adjust ratings by number of oscars
    df["adjusted_rating"] = df.apply(
        lambda x: x["rating"] + adjust_ratings.oscar_calculator(x["oscars_count"]),
        axis=1,
    )

    # Adjust ratings by number of reviews
    max_ratings = int(df["ratings_count"].max())
    df["adjusted_rating"] = df.apply(
        lambda x: x["adjusted_rating"]
        - adjust_ratings.review_penalizer(max_ratings, x["ratings_count"]),
        axis=1,
    )

    df = df.sort_values(by=['adjusted_rating'], ascending=False)

    # Check if 'data' directory exists, if not create it
    # Then write 'movies.csv' file
    dir_name = "./data/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        df.to_csv(f"{dir_name}movies.csv",sep=",", float_format = "%.1f",index=False, quoting=csv.QUOTE_ALL)
    else:
        df.to_csv(f"{dir_name}movies.csv",sep=",", float_format= "%.1f",index=False, quoting=csv.QUOTE_ALL)

if __name__ == "__main__":
    main()
