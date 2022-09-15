

dict_query = {
    'get_select': """ SELECT title, country, release_year, listed_in, description
                                    FROM netflix
                                    WHERE title  = '{}'
                                    """
}


dict_query_years = {
    'get_select': """ SELECT title, release_year
                                    FROM netflix
                                    WHERE release_year  BETWEEN '{}' AND '{}'
                                    ORDER BY release_year
                                    """
}

dict_query_rating = {
    'get_select': """ SELECT title, rating, description
                                    FROM netflix
                                    WHERE rating IN {}
                                    ORDER BY rating
                                    
                                    """
}

dict_top_10_new_movies = {
    'get_select': """ SELECT title, description, listed_in, release_year
                                    FROM netflix
                                    WHERE listed_in LIKE '%{}%'
                                    ORDER BY release_year DESC 
                                    LIMIT  10

                                    """
}

