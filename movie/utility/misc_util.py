import statistics

from movie.utility import constant

"""
This module contains utility functions for handling results,
calculating statistics on movie ratings, and validating input.

Functions:
    result_message(result: bool, message: str, payload) -> dict:
        Constructs a standardized result message dictionary with
        the given result status, message, and payload.

    get_average_rating(result: list) -> float:
        Calculates and returns the average rating from a list of ratings.

    get_median_rating(result: list) -> float:
        Calculates and returns the median rating from a list of ratings.

    get_best_movie(result: dict):
        Identifies and returns the movie(s) with the highest rating
        from the provided movie data dictionary.

    get_worst_movie(result: dict):
        Identifies and returns the movie(s) with the lowest rating
        from the provided movie data dictionary.

    get_stat_details(result: dict) -> tuple:
        Extracts rating information from the movie data dictionary,
        calculates the average rating, median rating, best movie,
        and worst movie, and returns these values as a tuple.

    validate_input_filter_movie(end_year: str, minimum_rating: str,
                                start_year: str) -> tuple:
        Validates and converts user input for filtering movies based on
        rating and year. If input is empty, default values are assigned.
        Returns a tuple containing the validated minimum rating,
        start year, and end year.
"""


def result_message(result: bool, message: str, payload) -> dict:
    """
    Construct a standardized result message with a result status, message,
    and payload.

      Parameters:
          result (bool): The success status of the operation.
          message (str): A descriptive message related to the operation.
          payload: Data or information associated with the result.

      Returns:
          dict: A dictionary containing the result status, message,
                and payload.
      """
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_average_rating(result: list) -> float:
    """
    Calculate the average rating from a list of ratings.

    Parameter:
        result (list): List of movie ratings.

    Returns:
        float: The average rating.
    """
    return statistics.mean(result)


def get_median_rating(result: list) -> float:
    """
    Calculate the median rating from a list of ratings.

    Parameter:
        result (list): List of movie ratings.

    Returns:
        float: The median rating.
    """
    return statistics.median(result)


def get_best_movie(result: dict) -> list:
    """
    Identify the movie(s) with the highest rating.

    Parameter:
        result (dict): Dictionary of movies with their corresponding ratings.

    Returns:
        list: A list of movie titles with the highest rating.
    """
    max_rating = max(
        [float(value[constant.RATING_KEY]) for key, value in result.items()])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_worst_movie(result: dict) -> list:
    """
    Identify the movie(s) with the lowest rating.

    Parameter:
        result (dict): Dictionary of movies with their corresponding ratings.

    Returns:
        list: A list of movie titles with the lowest rating.
    """
    min_rating = min(
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if min_rating == float(result[movie][constant.RATING_KEY])]


def get_stat_details(result: dict) -> tuple:
    """
    Extract and calculate statistical details of movies, including
    average, median, highest, and lowest ratings.

    Parameter:
        result (dict): Dictionary containing movie data with ratings.

    Returns:
        tuple: A tuple containing average rating, best movies, median rating,
               and worst movies.
    """
    rating_for_all_movies = \
        [float(value[constant.RATING_KEY])
         for key, value in result[constant.PAYLOAD].items()]

    average_rating = get_average_rating(rating_for_all_movies)
    median_rating = get_median_rating(rating_for_all_movies)
    best_movie = get_best_movie(result[constant.PAYLOAD])
    worst_movie = get_worst_movie(result[constant.PAYLOAD])

    return average_rating, best_movie, median_rating, worst_movie


def validate_input_filter_movie(end_year: str, minimum_rating: str,
                                start_year: str) -> tuple:
    """
    Validate and set default values for filtering movies by rating and
    year range.

    Parameters:
        end_year (str): The end year for the filter range, defaulting
                        to the current year.
        minimum_rating (str): The minimum rating for filtering,
                              defaulting to 0 if empty.
        start_year (str): The start year for the filter range,
                          defaulting to 1 if empty.

    Returns:
        tuple: A tuple containing validated minimum rating, start year,
               and end year.
    """
    if minimum_rating == constant.EMPTY:
        minimum_rating = 0
    if start_year == constant.EMPTY:
        start_year = 1
    if end_year == constant.EMPTY:
        from datetime import datetime
        end_year = datetime.now().year

    return float(minimum_rating), int(start_year), int(end_year)
