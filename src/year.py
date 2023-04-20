import pandas as pd 
import json

movies = pd.read_csv('cleaned_movies.csv')
movies = movies.set_index('movieId')

def best_movie_year(year, number):
    movies_test = movies.loc[movies['year'] == year]
    best = movies_test.nlargest(number ,['vote_average'])
    return print(best[['title','release_date']])




def movies_all():
    years = movies.year.drop_duplicates().to_list()
    file_save = []
    for year in years:
        movies_test = movies.loc[movies['year'] == year]
        best = movies_test.nlargest(1,['vote_average'])
        best = best[['title','release_date','year']]
        result = best.to_json(orient='records')
        with open("year.json") as fp:
            listObj = json.load(fp)
            listObj.append(result)
        with open("test.json", 'w') as json_file:
            json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))

        
    with open("year_all.json", "w") as outfile:
        outfile.write(str(file_save))

        


movies_all()