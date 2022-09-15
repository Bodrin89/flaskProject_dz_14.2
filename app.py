
from flask import Flask, jsonify
from db import get_by_data
from query import*

app = Flask(__name__)

@app.route('/movie/<title>')
def search_move(title):
    list_select = ("title", "country", "release_year", "listed_in", "description")
    movie_title = get_by_data(dict_query['get_select'], list_select, title)

    return jsonify(movie_title)

@app.route('/movie/<int:year_one>/to/<int:year_two>')
def search_years_move(year_one, year_two):
    list_select = ("title", "release_year")
    movie_title = get_by_data(dict_query_years['get_select'], list_select, year_one, year_two)
    return jsonify(movie_title)


@app.route('/rating/family')
def search_rating_family():
    list_select = ("title", "rating", "description")
    family = ("G", "PG", "PG-13")
    movie_title = get_by_data(dict_query_rating['get_select'], list_select, family)
    return jsonify(movie_title)


@app.route('/rating/children')
def search_rating_children():
    list_select = ("title", "rating", "description")
    children = ("G", "G")
    movie_title = get_by_data(dict_query_rating['get_select'], list_select, children)
    return jsonify(movie_title)


@app.route('/rating/adult')
def search_rating_adult():
    list_select = ("title", "rating", "description")
    adult = ("R", "NC-17")
    movie_title = get_by_data(dict_query_rating['get_select'], list_select, adult)
    return jsonify(movie_title)

@app.route('/genre/<genre>')
def get_top_10_new_movies(genre):
    list_select = ("title", "description")
    movie_title = get_by_data(dict_top_10_new_movies['get_select'], list_select, genre)
    return jsonify(movie_title)

if __name__ == '__main__':
    app.run()
