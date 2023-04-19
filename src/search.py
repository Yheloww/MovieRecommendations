from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 
import ast
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

merged = pd.read_csv('./cleaned_movies.csv')
vectorize = TfidfVectorizer(ngram_range=(1,2))
tfid = vectorize.fit_transform(merged['title'])


def search(title = input()):
    query_vec = vectorize.transform([title])
    similarity = cosine_similarity(query_vec, tfid).flatten()
    indices = np.argpartition(similarity,-5)[-5:]
    results = merged.iloc[indices][::-1]
    results[['title', 'overview', 'release_date','genres']]
    return results['movieId'].iloc[0]
