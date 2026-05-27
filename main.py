from SQL.sql_connect import SQL_DB_CONNECT
from UI import *
from movie import *
import logger_config

def main():
    with SQL_DB_CONNECT() as sql_db:
        menu = Menu(["Поиск по названию фильма",
                     "Поиск по году выпуска",
                     "Посмотреть популярные запросы",
                     "выход"
        ])
        movie = Movie(sql_db)

        while True:
            choise = menu.show()

            match choise:
                case 1:
                    movie.search_by_movie_title()


                case 4:
                    break


if __name__ == '__main__':
    main()