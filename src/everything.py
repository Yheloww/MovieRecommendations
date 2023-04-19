from search import *
from movie import * 
from recommendations import * 

movie = search()
infos = Movie(movie)
print(infos.show_infos())
# print(f"recommended movie for {infos.title} : {infos.recommendations}")
# print(f"best movies of the year {infos.year} : {infos.year_films}")