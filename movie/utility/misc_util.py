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
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]


def get_worst_movie(result):
    max_rating = min(
        [float(result[movie][constant.RATING_KEY]) for movie in result])

    return [movie for movie in result
            if max_rating == float(result[movie][constant.RATING_KEY])]
