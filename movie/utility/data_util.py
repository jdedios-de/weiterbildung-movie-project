import json
from pathlib import WindowsPath

from movie.utility import misc_util

"""
This module provides utility functions for loading, writing, and managing movie data stored in JSON format.
It includes functions to load data from a file, write data to a file, and build dictionaries for movie entries.
The module also implements a caching mechanism to optimize data fetching.

Functions:
    load_data(file_path: WindowsPath) -> misc_util.result_message:
        Loads and returns the content of a JSON file. Handles errors related to file access.

    write_data(details: dict, file_path: WindowsPath) -> misc_util.result_message:
        Writes the provided data to a JSON file. Handles errors related to file writing.

    build_dict(title: str, year: str, rating: str) -> dict:
        Creates a dictionary representation of a movie with its title, year, and rating.

    build_to_add_dict(year: str, rating: str) -> dict:
        Constructs a dictionary to represent a movie's rating and year for addition to the database.

    fetch_data(file_path: WindowsPath) -> misc_util.result_message:
        Fetches the data from the JSON file, caching the result after the first load.
        This implements a singleton pattern to minimize repeated file access.
"""

cached_data = None

def load_data(file_path: WindowsPath) -> misc_util.result_message:
    """
    Loads and returns the content of a JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    try:
        with open(file_path, "r") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return (misc_util.result_message
                (False,
                 "Error: The file was not found.", ""))
    except IOError:
        return (misc_util.result_message
                (False,
                 "Error: Could not read the file.", ""))
    except Exception as e:
        return (misc_util.result_message
                (False,
                 f"An unexpected error occurred: {e}",
                 ""))
    else:
        return (misc_util.result_message
                (True, "File loaded successfully.",
                 payload))


def write_data(details: dict,
               file_path: WindowsPath) -> misc_util.result_message:
    try:
        with open(file_path, 'w') as write_to_file:
            write_to_file.write(json.dumps(details))
    except FileNotFoundError:
        return (misc_util.result_message
                (False,
                 "Error: The file was not found.", ""))
    except IOError:
        return (misc_util.result_message
                (False,
                 "Error: Could not write to the file.",
                 ""))
    except Exception as e:
        return (misc_util.result_message
                (False,
                 f"An unexpected error occurred: {e}",
                 ""))
    else:
        return (misc_util.result_message
                (True, "File written successfully.",
                 ""))


def build_dict(title: str, year: str, rating: str) -> dict:
    return {title: {"rating": float(rating), "year": int(year)}}


def build_to_add_dict(year: str, rating: str) -> dict:
    return {"rating": float(rating), "year": int(year)}


def fetch_data(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches the data and caches it after the first load,
    demonstrating the [SINGLETON PATTERN] and
    following the standard for API invocation

    Returns:
        dict: The cached or freshly loaded data from the JSON file.
    """
    global cached_data

    if cached_data is None:
        cached_data = load_data(file_path)
    return cached_data
