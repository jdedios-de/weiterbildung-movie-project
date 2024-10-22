from movie.utility.data_util import fetch_data
from movie.utility.data_util import write_data
from movie.utility.data_util import build_to_add_dict

from movie.utility import constant

def list_movies(file_path):
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    return fetch_data(file_path)


def stats_movies(file_path):
    return fetch_data(file_path)


def add_movie(title, year, rating, file_path):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    details = fetch_data(file_path)

    details[constant.PAYLOAD][title] = build_to_add_dict(year, rating)

    return write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title, file_path):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = fetch_data(file_path)

    del details[constant.PAYLOAD][title]

    return write_data(details[constant.PAYLOAD], file_path)


def find_movie(title, file_path):
    details = fetch_data(file_path)

    return details[constant.PAYLOAD][title]

def update_movie(title, rating, file_path):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = rating

    result = write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result
