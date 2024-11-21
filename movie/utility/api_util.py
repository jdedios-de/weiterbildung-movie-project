import json

from dotenv import load_dotenv

import requests
import os

from movie.utility import misc_util
from movie.utility.constant import MOVIE_API_URL
from movie.utility.data_util import build_dict_poster


def get_key() -> str:
    """
    Retrieves the API key from the `.env` file.

    Returns:
        str: The API key as a string.
    """
    load_dotenv()

    return os.getenv('key')


def get_parameters(movie_title: str) -> str:
    """
    Constructs query parameters for the API request.

    Parameter:
        movie_title (str): The title of the movie to fetch.

    Returns:
        str: A query string containing the movie title and `apikey` placeholder.
    """
    return f"?t={movie_title}&apikey="


def get_movie_data_from_api(movie_title: str) -> json:
    """
    Fetches movie data from an external API using the title.

    Parameter:
        movie_title (str): Title of the movie to search.

    Returns:
        json: A `result_message` JSON object indicating success or failure,
              along with movie data or error details.
    """
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
                                           response.json()["imdbID"],
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
    except Exception:
        raise Exception(
            "Please check if the .env file exists or if the key exists.")
