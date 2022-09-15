
import json
import sqlite3


def get_actors(name_one, name_two):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f'SELECT "cast" ' \
                f'FROM netflix ' \
                f'WHERE "cast" LIKE "%{name_one}%" ' \
                f'AND "cast" LIKE "%{name_two}%"'
        cursor.execute(query)
        result = cursor.fetchall()

        list_actors = []
        for i in result:
            for x in i[0].split(', '):
                list_actors.append(x)
        actors_string = ','.join(list_actors)
        actors = actors_string.split(',')
        s= set()
        for i in actors:
            if actors.count(i) > 2 and i not in (name_one, name_two):
                s.add(i)
    return list(s)


def get_movies(type_movie, year_movie, genre_movie):

    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f'SELECT "title", "description" ' \
                f'FROM netflix ' \
                f'WHERE "type" = "{type_movie}" ' \
                f'AND "release_year" = "{year_movie}"' \
                f'AND "listed_in" = "{genre_movie}"'
        cursor.execute(query)
        result = cursor.fetchall()
        list_data = []
        for i in result:
            data_movies = {}
            data_movies[i[0]] = i[1]
            list_data.append(data_movies)

        result_json = json.dumps(list_data, indent=4)
    return result_json

print(get_movies("Movie", 2003, "Action & Adventure"))