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
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_average_rating(result: list) -> float:
    return statistics.mean(result)


def get_median_rating(result: list) -> float:
    return statistics.median(result)


def get_best_movie(result: dict):
    max_rating = max(
        [float(value[constant.RATING_KEY]) for key, value in result.items()])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_worst_movie(result: dict):
    max_rating = min(
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_stat_details(result: dict) -> tuple:
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
    if minimum_rating == "":
        minimum_rating = 0
    if start_year == "":
        start_year = 1
    if end_year == "":
        from datetime import datetime
        end_year = datetime.now().year

    return float(minimum_rating), int(start_year), int(end_year)
