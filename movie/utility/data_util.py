import csv
import json
from pathlib import WindowsPath

from movie.utility import misc_util, constant

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
    Load movie data from a specified file path.

    This function attempts to open and read movie data from a JSON file at
    the specified file path. It handles potential errors during the file
    operation, such as file not found, read errors, and unexpected exceptions.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: A result message indicating the success
                                  or failure of the file loading operation,
                                  along with the payload data if successful.
    """
    payload = {}

    try:
        if "json" in file_path.name:
            with open(file_path, "r") as handle:
                payload = json.load(handle)
        elif "csv" in file_path.name:
            with open(file_path, mode='r') as handle:
                csv_reader = csv.DictReader(handle)
                for row in list(csv_reader):
                    payload.update(build_dict(row[constant.TITLE_KEY],
                                              row[constant.YEAR_KEY],
                                              row[constant.RATING_KEY]))
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
    """
    Write movie data to a JSON file.

    Attempts to write movie data to the specified file path in JSON format.
    Handles errors related to file access and other unexpected exceptions.

    Parameters:
        details (dict): The movie data to be written to the file.
        file_path (WindowsPath): The path to the JSON file where data is
                                 to be written.

    Returns:
        misc_util.result_message: A result message indicating the success or
                                  failure of the file write operation.
    """
    try:
        if "json" in file_path.name:
            with open(file_path, 'w') as handle:
                handle.write(json.dumps(details))
        elif "csv" in file_path.name:
            with open(file_path, mode='w', newline='') as handle:
                csv_writer = csv.writer(handle)
                csv_writer.writerow(['title', 'rating', 'year'])
                for key, value in details.items():
                    csv_writer.writerow([key,
                                         value[constant.RATING_KEY],
                                         value[constant.YEAR_KEY]])

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


def build_dict_poster(title: str, year: str, rating: str,
                      poster: str) -> dict:
    return {title:{"rating": float(rating), "year": int(year), "poster": poster}}


def build_dict(title: str, year: str, rating: str) -> dict:
    """
    Construct a dictionary for a movie entry.

    This function creates a dictionary representing a movie with its title,
    release year, and rating.

    Parameters:
        title (str): The title of the movie.
        year (str): The release year of the movie as a string.
        rating (str): The rating of the movie as a string.

    Returns:
        dict: A dictionary structured as
              {title: {"rating": float, "year": int}}.
    """
    return {title: {"rating": float(rating), "year": int(year)}}


def build_to_add_dict(year: str, rating: str) -> dict:
    """
    Construct a dictionary for adding a movie entry.

    This function creates a dictionary containing the release year and rating
    for a movie entry.

    Parameters:
        year (str): The release year of the movie as a string.
        rating (str): The rating of the movie as a string.

    Returns:
        dict: A dictionary structured as {"rating": float, "year": int}.
    """
    return {"rating": float(rating), "year": int(year)}


def fetch_data(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieve movie data, using a cached version if available.

    This function retrieves movie data from the specified file path, utilizing
    a cached version if available to minimize file I/O operations.

    Parameter:
        file_path (WindowsPath): The path to the file containing movie data.

    Returns:
        misc_util.result_message: The loaded or cached movie data.
    """
    global cached_data

    if cached_data is None:
        cached_data = load_data(file_path)
    return cached_data
