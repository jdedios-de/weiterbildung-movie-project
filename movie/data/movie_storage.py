from pathlib import WindowsPath

from movie.utility import data_util
from movie.utility import constant
from movie.utility import misc_util


def list_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches and lists all movies from the storage file.

    Parameter:
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object
    """
    return data_util.fetch_data(file_path)


def add_movie(title: str, year: str, rating: str, poster: str,
              notes: str, imdbid: str,
              file_path: WindowsPath) -> misc_util.result_message:
    """
    Adds a new movie to the storage.

    Parameters:
        title: Title of the movie.
        year: Release year of the movie.
        rating: Rating of the movie.
        poster: URL to the movie poster.
        notes: Additional notes about the movie.
        imdbid: IMDb ID of the movie.
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object
    """
    details: misc_util.result_message = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title] = data_util.build_to_add_dict(year,
                                                                   rating,
                                                                   poster,
                                                                   notes,
                                                                   imdbid)

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Deletes a movie from the storage by title.

    Parameter:
        title: Title of the movie to delete.
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object
    """
    details: misc_util.result_message = data_util.fetch_data(file_path)
    del details[constant.PAYLOAD][title.title()]

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def search_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches all movies from the storage for searching.

    Parameter:
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object
    """
    return data_util.fetch_data(file_path)


def stats_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches and generates movie statistics from the storage.

    Parameter:
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object
    """
    return data_util.fetch_data(file_path)


def update_movie(title: str, rating: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Updates the rating of an existing movie in the storage.

    Parameters:
        title: Title of the movie to update.
        rating: New rating for the movie.
        file_path: Path to the storage file where movie data is stored.

    Return: A result_message object indicating success or failure after the update,
             including the updated rating.
    """
    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = float(rating)

    result = data_util.write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result
