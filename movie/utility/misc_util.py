import statistics

from movie.utility import constant


def result_message(result, message, payload):
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_average_rating(result):
    return statistics.mean(result)


def get_median_rating(result):
    return statistics.median(result)


def get_best_movie(result):
    max_rating = max(
        [float(value[constant.RATING_KEY]) for key, value in result.items()])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_worst_movie(result):
    max_rating = min(
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_stat_details(result):
    rating_for_all_movies = \
        [float(value[constant.RATING_KEY])
         for key, value in result[constant.PAYLOAD].items()]

    average_rating = get_average_rating(rating_for_all_movies)
    median_rating = get_median_rating(rating_for_all_movies)
    best_movie = get_best_movie(result[constant.PAYLOAD])
    worst_movie = get_worst_movie(result[constant.PAYLOAD])

    return average_rating, best_movie, median_rating, worst_movie
