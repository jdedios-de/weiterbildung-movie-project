from movie.utility import constant
from movie.utility.print_util import print_menu

"""
Enter new movie name: test
Enter new movie year: 2024
Enter new movie rating: 9.9
"""


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
