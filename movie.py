import sql.sql_requests as req
from mongo.mongo_requests import *
import sql.sql_connect
import logging
import time


logger = logging.getLogger(__name__)



class Movie:
    def __init__(self, cursor, mongo_db):
        self.cursor = cursor
        self.mongo_db = mongo_db

    def search_by_movie_title(self,title_input):
        limit = 10
        page = 0

        while True:
            offset = page * limit

            self.cursor.execute(req.search_by_movie_title, (title_input + "%", limit, offset))

            movies = self.cursor.fetchall()

            if not movies:
                print("\nФильмы закончились, вас перекинет в главное меню")
                time.sleep(3)
                return None


            for movie in movies:
                print(movie[0])

            user_input = input("\nПоказать ещё фильмы? y/n:")
            if user_input.lower() != "y":
                break

            page += 1

    def search_by_movie_year(self):
        start_year = int(input("введите с какого года вы хотите найти фильм: "))
        end_year = int(input("введите до какого года вы хотите найти фильм: "))
        if start_year > end_year:
            start_year, end_year = end_year, start_year

        search_by_year = {
            "release_year":
                {"$gte": start_year,
                 "$lte": end_year
                 }
        }

        movie_year = self.mongo_db['sakila_film'].find(search_by_year)

        for movie in movie_year:
            print(movie)
















