from movie.utility import data_util

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
    return data_util.fetch_data(file_path)


def add_movie(title, year, rating, file_path):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title] = data_util.build_to_add_dict(year,
                                                                   rating)

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title, file_path):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = data_util.fetch_data(file_path)

    del details[constant.PAYLOAD][title]

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def search_movies(title, file_path):
    details = data_util.fetch_data(file_path)

    return details[constant.PAYLOAD]


def stats_movies(file_path):
    return data_util.fetch_data(file_path)


def update_movie(title, rating, file_path):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = rating

    result = data_util.write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result

