from pathlib import WindowsPath

from movie.utility import data_util
from movie.utility import constant
from movie.utility import misc_util


def list_movies(file_path: WindowsPath) -> misc_util.result_message:
    return data_util.fetch_data(file_path)


def add_movie(title: str, year: str, rating: str, poster: str,
              notes: str, imdbid: str,
              file_path: WindowsPath) -> misc_util.result_message:
    details: misc_util.result_message = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title] = data_util.build_to_add_dict(year,
                                                                   rating,
                                                                   poster,
                                                                   notes,
                                                                   imdbid)

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def delete_movie(title: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    details: misc_util.result_message = data_util.fetch_data(file_path)
    del details[constant.PAYLOAD][title.title()]

    return data_util.write_data(details[constant.PAYLOAD], file_path)


def search_movies(file_path: WindowsPath) -> misc_util.result_message:
    return data_util.fetch_data(file_path)


def stats_movies(file_path: WindowsPath) -> misc_util.result_message:
    return data_util.fetch_data(file_path)


def update_movie(title: str, rating: str,
                 file_path: WindowsPath) -> misc_util.result_message:
    details = data_util.fetch_data(file_path)

    details[constant.PAYLOAD][title][constant.RATING_KEY] = float(rating)

    result = data_util.write_data(details[constant.PAYLOAD], file_path)

    result["rating"] = rating

    return result
