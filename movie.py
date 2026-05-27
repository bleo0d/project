import SQL.sql_requests as req
import SQL.sql_connect
import logging

logger = logging.getLogger(__name__)



class Movie:
    def __init__(self, cursor):
        self.cursor = cursor

    def search_by_movie_title(self):
        user_input = input("введите название фильма на англ")
        if user_input.isdigit():
            logger.warning("ошибка: введите название на англ")
            print("ошибка: введите название на англ")

        try:
            self.cursor.execute(req.search_by_movie_title, (user_input + "%",))

            for name in self.cursor.fetchall():
                print(name[0])
        except Exception as e:
            logger.exception("Ошибка поиска фильма")
            print(e)



