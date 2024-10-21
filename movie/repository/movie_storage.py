from movie.utility.data_util import load_data
from movie.utility.data_util import write_data
from movie.utility.data_util import build_to_add_dict


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
    return load_data(file_path)


def add_movie(title, year, rating, file_path):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    details = load_data(file_path)

    details[title] = build_to_add_dict(year, rating)

    return write_data(details, file_path)


def delete_movie(title, file_path):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    details = load_data(file_path)

    del details[title]

    return write_data(details, file_path)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass

  