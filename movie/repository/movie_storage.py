from pathlib import WindowsPath

from movie.utility import data_util
from movie.utility import constant
from movie.utility import misc_util

"""
This module provides functions for managing movie data stored in a JSON file.
It allows listing, adding, deleting, updating, and retrieving movie information.
All interactions with the movie database are handled by reading and writing to the JSON file.

Functions:
    list_movies(file_path: WindowsPath) -> misc_util.result_message:
        Retrieves the list of movies from the database and returns it as a dictionary.

    add_movie(title: str, year: str, rating: str, file_path: WindowsPath) -> misc_util.result_message:
        Adds a new movie to the movie database and saves the updated list to the JSON file.

    delete_movie(title: str, file_path: WindowsPath) -> misc_util.result_message:
        Deletes a movie from the database and saves the updated list to the JSON file.

    search_movies(file_path: WindowsPath) -> misc_util.result_message:
        Returns the entire list of movies in the database without any filtering or searching.

    stats_movies(file_path: WindowsPath) -> misc_util.result_message:
        Retrieves the entire movie database to calculate and display statistics.

    update_movie(title: str, rating: str, file_path: WindowsPath) -> misc_util.result_message:
        Updates the rating of an existing movie in the database and saves the updated list to the JSON file.
"""


def list_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieve the list of movies from storage.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message containing a success flag,
                                  a message string, and a selected
                                  movies from the storage.
    """
    return data_util.fetch_data(file_path)


def add_movie(title: str, year: str, rating: str,
              file_path: WindowsPath) -> misc_util.result_message:
    """
    Add a new movie to the storage.

    This function retrieves the existing movie data from the specified
    file path, adds a new movie with the given title, year, and rating, and
    then writes the updated movie data back to the file.

    Parameters:
        title (str): The title of the movie to be added.
        year (str): The release year of the movie.
        rating (str): The rating of the movie.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message containing a success flag,
                                  a message string, and a payload
    """
    details: misc_util.result_message = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title] = data_util.build_to_add_dict(year,
                                                                   rating)

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Delete a movie from the storage.

    This function removes a movie with the specified title from the storage.
    It first retrieves the current movie data from the given file path,
    deletes the entry matching the specified title, and then writes the
    updated data back to the file.

    Parameters:
        title (str): The title of the movie to be deleted.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message containing a success flag,
                                  a message string, and a payload
    """
    details: misc_util.result_message = data_util.fetch_data(file_path)

    del details[constant.PAYLOAD][title]

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def search_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieve all movies from storage.

    This function fetches the complete movie data from the specified file path
    to facilitate movie searching.

    Args:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message containing a success flag,
                                  a message string, and a selected
                                  movies from the storage.
    """
    return data_util.fetch_data(file_path)


def stats_movies(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieve movie statistics

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message containing a success flag,
                                  a message string, and a payload of movies
                                  statistics.
    """
    return data_util.fetch_data(file_path)


def update_movie(title: str, rating: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    """
    Update the rating of an existing movie.

    This function updates the rating of a specified movie title in the storage.
    It retrieves the current movie data, modifies the rating for the specified
    title, and writes the updated data back to the file.

    Parameters:
        title (str): The title of the movie to be updated.
        rating (str): The new rating of the movie.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message indicating the success or
                                  failure of the operation, including
                                  the new rating.
    """
    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = float(rating)

    result = data_util.write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result
