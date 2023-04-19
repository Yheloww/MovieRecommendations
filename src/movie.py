import pandas as pd
from recommendations import *
from year import *

df = pd.read_csv('cleaned_movies.csv')
df = df.set_index('movieId')

class Movie():
    def __init__(self,movieId):
        self.movieId = df.loc[movieId]
        # infos
        self.title = self.movieId['title']
        self.overview = self.movieId['overview']
        self.original_language = self.movieId['original_language']
        self.runtime = self.movieId['runtime']
        self.budget = self.movieId['budget']
        self.tagline = self.movieId['tagline']
        self.genres = self.movieId['genres']
        # date
        self.release_date = self.movieId['release_date']
        self.year = self.movieId['year']
        # vote
        self.vote_average = self.movieId['vote_average']
        self.popularity = self.movieId['popularity']
        self.vote_count = self.movieId['vote_count']
        # images
        self.poster = self.movieId['poster_path']
        self.video = self.movieId['video']
        # reco 
        self.recommendations = find_similar_movie(movieId,5)
        self.year_films = best_movie_year(self.year,5)


    def show_infos(self):
        print(self.title, self.vote_average, self.popularity)

    
