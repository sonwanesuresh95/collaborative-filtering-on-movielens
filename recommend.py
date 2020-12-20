import pandas as pd
import numpy as np


class Lens:
    def __init__(self):
        self.ui = self.build_dataset()
        self.mapping = {'1': 'Star Wars (1977)',
                        '2': 'Contact (1997)',
                        '3': 'Fargo (1996)',
                        '4': 'Return of the Jedi (1983)',
                        '5': 'English Patient, The (1996)',
                        '6': 'Scream (1996)',
                        '7': 'Toy Story (1995)',
                        '8': 'Air Force One (1997)'}

    # build dataset and generate pivot table for User-Item matrix
    def build_dataset(self):
        u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
        users = pd.read_csv('dataset/ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings = pd.read_csv('dataset/ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')
        m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
        movies = pd.read_csv('dataset/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')
        movie_ratings = pd.merge(movies, ratings)
        lens = pd.merge(movie_ratings, users)
        sub = lens[['user_id', 'title', 'rating']]
        ui = sub.pivot_table(index='user_id', columns='title', values='rating', fill_value=0)
        return ui

    # Recommend top 20 similar content using correlation
    def recommend_similar(self, title):
        rec = self.ui.corrwith(self.ui[self.mapping[title]])
        return list(rec.sort_values(ascending=False).to_dict().keys())[1:20]
