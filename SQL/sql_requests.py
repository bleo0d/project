SELECT_FILM_TITLE = """SELECT title FROM sakila.film"""

search_by_movie_title = """SELECT title FROM sakila.film
where title like %s"""