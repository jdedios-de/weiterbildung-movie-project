
def input_add_movie():
    movie_name = input("Enter new movie name: ")
    movie_year = input("Enter new movie year: ")
    movie_rating = input("Enter new movie rating: ")

    return movie_name, movie_year, movie_rating


def input_update_movie():
    movie_name = input("Enter movie name: ")
    movie_rating = input("Enter new movie rating: ")

    return movie_name, movie_rating


def input_delete_movie():
    return input("Enter movie name: ")


def input_search_movie():
    return input("Enter part of movie name: ")
