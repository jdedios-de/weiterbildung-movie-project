import json

from dotenv import load_dotenv

import requests
import os

from movie.utility import misc_util
from movie.utility.constant import MOVIE_API_URL
from movie.utility.data_util import build_dict_poster


def get_key() -> str:
    load_dotenv()

    return os.getenv('key')


def get_parameters(movie_title: str) -> str:
    return f"?t={movie_title}&apikey="


def get_movie_data_from_api(movie_title: str) -> json:
    try:
        response = requests.get(
            MOVIE_API_URL + get_parameters(movie_title) + get_key(),
            verify=True,  # verify SSL Certificates
            timeout=5)  # 5 seconds timeout

        response.raise_for_status()  # Raises HTTPError for bad responses

        if response.status_code == 200:
            if response.json()["Response"] == 'True':
                return (misc_util.result_message
                        (True,
                         "Movie information has been fetched"
                         "successfully.",
                         build_dict_poster(response.json()["Title"],
                                           response.json()["Year"],
                                           response.json()["imdbRating"],
                                           response.json()["Poster"])))
            else:
                return (misc_util.result_message
                        (False,
                         f"{response.json()}",
                         response.json()))
        else:
            return (misc_util.result_message
                    (False,
                     f"{response.json()}",
                     response.json()))

    except requests.exceptions.RequestException:
        return (misc_util.result_message
                (False,
                 f"{response.json()}",
                 f": {response.json()}"))
    except ValueError:
        return (misc_util.result_message
                (False,
                 f"{response.json()}",
                 f": {response.json()}"))
