from pathlib import WindowsPath
import random

from movie.data import movie_storage
from movie.utility import misc_util
from movie.utility import constant

from movie.utility.misc_util import result_message


def service_list_movies(option: str,
                        file_path: WindowsPath) -> result_message:
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
    return movie_storage.search_movies(file_path)


def service_find_movie(is_exact: bool, title: str,
                       file_path: WindowsPath) -> result_message:
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
    generate_random_movie = movie_storage.list_movies(file_path)[
        constant.PAYLOAD]

    return misc_util.result_message(True,
                                    "A random movie has "
                                    "been generated.",
                                    random.choice(
                                        list(generate_random_movie.items())))


def service_add_movie(title: str, year: str, rating: str, poster: str,
                      notes: str, imdbid: str, file_path: WindowsPath):
    return movie_storage.add_movie(title, year, rating, poster, notes, imdbid,
                                   file_path)


def service_delete_movie(title: str, file_path: WindowsPath):
    return movie_storage.delete_movie(title, file_path)


def service_update_movie(title: str, rating: str, file_path: WindowsPath):
    return movie_storage.update_movie(title, rating, file_path)
