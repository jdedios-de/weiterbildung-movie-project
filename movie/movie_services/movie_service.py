from movie.repository import movie_storage

from movie.utility import misc_util

from movie.utility import constant

import random

from movie.utility.misc_util import result_message


def service_list_movies(option: str, file_path) -> result_message:
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


def service_search_movies(to_search: str, file_path) -> result_message:
    return movie_storage.search_movies(to_search, file_path)


def service_find_movie(is_exact, title, file_path):
    result: dict = movie_storage.search_movies(title, file_path)

    if is_exact:

        has_movie = result[title]

        if not bool(has_movie):
            return misc_util.result_message(False,
                                            "Searching for the movie returned no results.",
                                            "")
        else:
            return misc_util.result_message(True,
                                            f"Searching for the movie {title} returned results.",
                                            "")
    else:
        return misc_util.result_message(True,
                                        "The search for movies was successful.",
                                        [{key: value} for key, value in
                                         result.items()
                                         if title.lower() in key.lower()])


def service_stat_movies(file_path):
    result = movie_storage.stats_movies(file_path)

    (average_rating,
     best_movie,
     median_rating,
     worst_movie) = misc_util.get_stat_details(result)

    return misc_util.result_message(True, "Movie statistics have been generated.",
                                    [average_rating, median_rating,
                                     best_movie, worst_movie,
                                     result[constant.PAYLOAD]])


def service_random_movie(file_path):
    generate_random_movie = movie_storage.list_movies(file_path)[
        constant.PAYLOAD]

    return misc_util.result_message(True, "A random movie has been generated.",
                                    random.choice(
                                        list(generate_random_movie.items())))


def service_add_movie(title, year, rating, file_path):
    return movie_storage.add_movie(title, year, rating, file_path)


def service_delete_movie(title, file_path):
    return movie_storage.delete_movie(title, file_path)


def service_update_movie(title, rating, file_path):
    return movie_storage.update_movie(title, rating, file_path)
