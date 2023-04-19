import pandas as pd

ratings = pd.read_csv('../datas/ratings.csv')
movies = pd.read_csv('cleaned_movies.csv')
movies = movies.set_index('movieId')



def find_similar_movie(movie_id, num_of_movie):
    # find users similar to us
    similar_users = ratings[(ratings["movieId"] == movie_id) & (
        ratings['rating'] > 4)]['userId'].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(
        similar_users)) & (ratings['rating'] > 4)]["movieId"]
    # adjusting recommendations ( more than 10% recommended the movie)
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .1]
    # find how common the recommendation where over all users
    all_user = ratings[(ratings['movieId'].isin(
        similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_users_recs = all_user["movieId"].value_counts(
    ) / len(all_user["userId"].unique())
    # creation of a score for recommendation
    rec_percentages = pd.concat([similar_user_recs, all_users_recs], axis=1)
    rec_percentages.columns = ['similar', 'all']
    rec_percentages["score"] = rec_percentages['similar'] / \
        rec_percentages["all"]
    # sorting the score to have the more logical on top
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(num_of_movie).merge(movies, left_index=True, right_on='movieId')[['score', 'title','vote_average']]
