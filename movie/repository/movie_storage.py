from pathlib import WindowsPath

from movie.utility import data_util
from movie.utility import constant
from movie.utility import misc_util


def list_movies(file_path: WindowsPath) -> misc_util.result_message:
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
    return data_util.fetch_data(file_path)


def add_movie(title: str, year: str, rating: str,
              file_path: WindowsPath) -> misc_util.result_message:
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    details: misc_util.result_message = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title] = data_util.build_to_add_dict(year,
                                                                   rating)

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details: misc_util.result_message = data_util.fetch_data(file_path)

    del details[constant.PAYLOAD][title]

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def search_movies(file_path: WindowsPath) -> misc_util.result_message:
    return data_util.fetch_data(file_path)


def stats_movies(file_path: WindowsPath) -> misc_util.result_message:
    return data_util.fetch_data(file_path)


def update_movie(title: str, rating: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = float(rating)

    result = data_util.write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result
