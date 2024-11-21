import statistics

from movie.utility import constant


def result_message(result: bool, message: str, payload) -> dict:
    """
    Constructs a standardized result message.

    Parameters:
        result (bool): The success status of the operation.
        message (str): A descriptive message related to the operation.
        payload: The data or content associated with the result.

    Returns:
        dict: A dictionary containing the result, message, and payload.
    """
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_average_rating(result: list) -> float:
    """
    Calculates the average rating from a list of ratings.

    Parameter:
        result (list): A list of numerical ratings.

    Returns:
        float: The average rating.
    """
    return statistics.mean(result)


def get_median_rating(result: list) -> float:
    """
    Calculates the median rating from a list of ratings.

    Parameter:
        result (list): A list of numerical ratings.

    Returns:
        float: The median rating.
    """
    return statistics.median(result)


def get_best_movie(result: dict) -> list:
    """
    Identifies the movie(s) with the highest rating.

    Parameter:
        result (dict): A dictionary where keys are movie names and values
                       are details including ratings.

    Returns:
        list: A list of movie names with the highest rating.
    """
    max_rating = max(
        [float(value[constant.RATING_KEY]) for key, value in result.items()])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_worst_movie(result: dict) -> list:
    """
    Identifies the movie(s) with the lowest rating.

    Parameter:
        result (dict): A dictionary where keys are movie names and values
                       are details including ratings.

    Returns:
        list: A list of movie names with the lowest rating.
    """
    min_rating = min(
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if min_rating == float(result[movie][constant.RATING_KEY])]


def get_stat_details(result: dict) -> tuple:
    """
    Computes statistical details about movie ratings.

    Parameter:
        result (dict): A dictionary containing movie details with ratings.

    Returns:
        tuple: A tuple containing:
            - Average rating (float)
            - List of the best movie(s) (list)
            - Median rating (float)
            - List of worst movie(s) (list)
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
    Validates and converts filter inputs for movie search.

    Parameter:
        end_year (str): The end year as a string input by the user.
        minimum_rating (str): The minimum rating as a string input by the user.
        start_year (str): The start year as a string input by the user.

    Returns:
        tuple: A tuple containing:
            - minimum_rating (float): The validated minimum rating.
            - start_year (int): The validated start year.
            - end_year (int): The validated end year.
    """
    if minimum_rating == constant.EMPTY:
        minimum_rating = 0
    if start_year == constant.EMPTY:
        start_year = 1
    if end_year == constant.EMPTY:
        from datetime import datetime
        end_year = datetime.now().year

    return float(minimum_rating), int(start_year), int(end_year)
