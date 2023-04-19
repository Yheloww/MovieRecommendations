import pandas as pd 

movies = pd.read_csv('cleaned_movies.csv')
movies = movies.set_index('movieId')

def best_movie_year(year, number):
    movies_test = movies.loc[movies['year'] == year]
    best = movies_test.nlargest(number ,['vote_average'])
    return best[['title','release_date']]