from pathlib import WindowsPath
import random

from movie.repository import movie_storage
from movie.utility import misc_util
from movie.utility import constant

from movie.utility.misc_util import result_message

"""
This module provides service functions to handle various operations
related to movies. It interacts with the movie storage and utility
functions to retrieve, manipulate, and return movie data in
a structured format.

Functions:
    service_list_movies(option: str, file_path: WindowsPath)
    -> result_message:
    Lists movies from the storage. Optionally sorts them by rating or year.

    service_filter_movies(minimum_rating,
    start_year, end_year, file_path: WindowsPath) -> result_message:
        Filters movies based on minimum rating and a year range.

    service_search_movies(file_path: WindowsPath) -> result_message:
        Searches for movies in the storage without any filters.

    service_find_movie(is_exact: bool, title: str,
    file_path: WindowsPath) -> result_message:
        Finds a movie by its title. Can search foran exact match
        or a partial match.

    service_stat_movies(file_path: WindowsPath) -> result_message:
        Retrieves movie statistics, including average rating,
        median rating, best and worst movie.

    service_random_movie(file_path: WindowsPath) -> result_message:
        Returns a randomly selected movie from the list.

    service_add_movie(title: str, year: str, rating: str,
    file_path: WindowsPath):
        Adds a new movie to the movie list with a title, year, and rating.

    service_delete_movie(title: str, file_path: WindowsPath):
        Deletes a movie from the list based on its title.

    service_update_movie(title: str, rating: str, file_path: WindowsPath):
        Updates the rating of an existing movie by its title.
"""


def service_list_movies(option: str,
                        file_path: WindowsPath) -> result_message:
    """
    Retrieve and optionally sort a list of movies by rating or year.

    Parameters:
        option (str): The sort option, which can be either
                      constant.RATING_KEY`to sort by rating or
                      constant.YEAR_KEY`to sort by year.

        file_path (WindowsPath): The path to the file containing movie data.
                                 DI for Testing and Production

    Returns:
        result_message: A result message containing a success flag,
                        a message string, and the sorted or unsorted list
                        of movies in a dictionary format.
    """
    if option == constant.RATING_KEY:
        result = movie_storage.list_movies(file_path)

        return misc_util.result_message(True,
                                        "Movies sorted by rating",
                                        dict(sorted(
                                            result[constant.PAYLOAD].items(),
                                            key=lambda x: x[1][
                                                constant.RATING_KEY],
                                            reverse=True)
                                        ))

    elif option == constant.YEAR_KEY:
        result = movie_storage.list_movies(file_path)

        return misc_util.result_message(True,
                                        "Movies sorted by year",
                                        dict(sorted(
                                            result[constant.PAYLOAD].items(),
                                            key=lambda x: x[1][
                                                constant.YEAR_KEY],
                                            reverse=True)
                                        ))

    else:
        return movie_storage.list_movies(file_path)


def service_filter_movies(minimum_rating: float,
                          start_year: int,
                          end_year: int,
                          file_path: WindowsPath) -> result_message:
    """
    Filter movies based on rating and year range.

    Parameters:
        minimum_rating (float): The minimum rating a movie must have to be
                                included in the results.
        start_year (int): The starting year of the range to filter movies.
        end_year (int): The ending year of the range to filter movies.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message containing a success flag, a
                        message string, and a list of movies that meet the
                        filtering criteria.
    """
    result = movie_storage.list_movies(file_path)

    return misc_util.result_message(True,
                                    "Movies sorted by year",
                                    [{key: value}
                                     for key, value in
                                     result[constant.PAYLOAD].items()
                                     if (value[constant.RATING_KEY]
                                         >= minimum_rating)
                                     and
                                     (start_year <= value[
                                         constant.YEAR_KEY] <= end_year)]
                                    )


def service_search_movies(file_path: WindowsPath) -> result_message:
    """
    Search for movies in the storage.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    result_message: A result message containing a success flag, a
                    message string, and a list of movies that meet the
                    filtering criteria.
    """
    return movie_storage.search_movies(file_path)


def service_find_movie(is_exact: bool, title: str,
                       file_path: WindowsPath) -> result_message:
    """
    Find a movie by title in the storage.

    This function searches for a movie in the storage by title.
    It can perform an exact match search or a partial match based on the
    `is_exact` flag.

    Parameters:
        is_exact (bool): If True, performs an exact title search;
                         if False, allows for partial title matches.

        title (str): The title of the movie to search for.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message containing a success flag, a
                message string, and a list of movies that meet the
                filtering criteria or None.
    """
    result = movie_storage.search_movies(file_path)

    if is_exact:

        has_movie = result[constant.PAYLOAD][title]

        if not bool(has_movie):
            return misc_util.result_message(False,
                                            "Searching for "
                                            "the movie returned no results.",
                                            "")
        else:
            return misc_util.result_message(True,
                                            f"Searching for "
                                            f"the movie {title} "
                                            f"returned results.",
                                            "")
    else:
        return misc_util.result_message(True,
                                        "The search for "
                                        "movies was successful.",
                                        [{key: value} for key, value in
                                         result[constant.PAYLOAD].items()
                                         if title.lower() in key.lower()])


def service_stat_movies(file_path: WindowsPath) -> result_message:
    """
    Generate and retrieve movie statistics.

    This function calculates various statistics about the movies in storage,
    including the average rating, median rating, best movie, and worst movie.
    It retrieves the necessary data from the movie_storage and formats the
    statistics into a result message.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message containing a success flag, a message
                        string, and a list of statistics including average
                        rating, median rating, best movie, worst movie,
                        and the original data payload.
    """
    result = movie_storage.stats_movies(file_path)

    (average_rating,
     best_movie,
     median_rating,
     worst_movie) = misc_util.get_stat_details(result)

    return misc_util.result_message(True,
                                    "Movie statistics "
                                    "have been generated.",
                                    [average_rating, median_rating,
                                     best_movie, worst_movie,
                                     result[constant.PAYLOAD]])


def service_random_movie(file_path: WindowsPath):
    """
    Retrieve a random movie from the storage.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message containing a success flag,
                        a message string, and a randomly selected movie
                        from the storage.
    """
    generate_random_movie = movie_storage.list_movies(file_path)[
        constant.PAYLOAD]

    return misc_util.result_message(True,
                                    "A random movie has "
                                    "been generated.",
                                    random.choice(
                                        list(generate_random_movie.items())))


def service_add_movie(title: str, year: str, rating: str,
                      file_path: WindowsPath):
    """
    Add a new movie to the storage. It calls the appropriate method
    from the movie_storage module to perform the addition.

    Parameters:
        title (str): The title of the movie to be added.
        year (str): The release year of the movie.
        rating (str): The rating of the movie.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message indicating the success or
                        failure of the operation.
    """
    return movie_storage.add_movie(title, year, rating, file_path)


def service_delete_movie(title: str, file_path: WindowsPath):
    """
    Delete a movie from the storage.

    Parameter:
        title (str): The title of the movie to be deleted.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message indicating the success
                        or failure of the operation.
    """
    return movie_storage.delete_movie(title, file_path)


def service_update_movie(title: str, rating: str, file_path: WindowsPath):
    """
    Update the rating of an existing movie.

    Parameters:
        title (str): The title of the movie to be updated.
        rating (str): The new rating of the movie.
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        result_message: A result message indicating the success
                        or failure of the operation.
    """
    return movie_storage.update_movie(title, rating, file_path)
