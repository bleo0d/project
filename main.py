from mongo.mongo_connect import MONGO_DB_CONNECT
from sql.sql_connect import SQL_DB_CONNECT
from ui import *
from movie import *
import logger_config

def main():
    with SQL_DB_CONNECT() as sql_db:
        with MONGO_DB_CONNECT() as mongo_db:
            menu = Menu(["Поиск по названию фильма",
                     "Поиск по году выпуска",
                     "Посмотреть популярные запросы",
                     "выход"
            ])
            movie = Movie(sql_db, mongo_db)

            while True:
                choise = menu.show()

                match choise:
                    case 1:
                        title_input = input("Введите название фильма: ")
                        movie.search_by_movie_title(title_input)
                    case 2:
                        movie.search_by_movie_year()






                    case 4:
                        break


if __name__ == '__main__':
    main()