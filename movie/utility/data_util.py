import csv
import json
from pathlib import WindowsPath

from movie.utility import misc_util, constant

cached_data = None
cached_data_html = None


def load_data(file_path: WindowsPath) -> misc_util.result_message:
    """
    Loads data from a file (JSON or CSV) into a dictionary.

    Parameter:
        file_path (WindowsPath): Path to the file.

    Returns:
        misc_util.result_message: A dictionary containing:
            - result (bool): Status of the operation.
            - message (str): Success or error message.
            - payload (dict): Parsed file data or an empty string on failure.
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
                                              row[constant.RATING_KEY],
                                              row[constant.POSTER_KEY]))
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
    Writes data to a file in JSON, CSV, or HTML format.

    Parameter:
        details (dict): The data to write.
        file_path (WindowsPath): Path to the file.

    Returns:
        misc_util.result_message: A dictionary containing:
            - result (bool): Status of the operation.
            - message (str): Success or error message.
    """
    try:
        if "json" in file_path.name:
            with open(file_path, 'w') as handle:
                handle.write(json.dumps(details))
        elif "csv" in file_path.name:
            with open(file_path, mode='w', newline='') as handle:
                csv_writer = csv.writer(handle)
                csv_writer.writerow([constant.TITLE_KEY, constant.RATING_KEY,
                                     constant.YEAR_KEY, constant.POSTER_KEY,
                                     constant.NOTES_KEY, constant.IMDBID_KEY])
                for key, value in details.items():
                    csv_writer.writerow([key,
                                         value[constant.RATING_KEY],
                                         value[constant.YEAR_KEY],
                                         value[constant.POSTER_KEY],
                                         value[constant.NOTES_KEY],
                                         value[constant.IMDBID_KEY]])
        elif "html" in file_path.name:
            with open(file_path, 'w') as handle:
                handle.write(details)
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
                      imdbid: str, poster: str) -> dict:
    """
    Creates a dictionary with movie details, including a poster and IMDb ID.

    Parameters:
        title (str): Movie title.
        year (str): Release year.
        rating (str): Movie rating.
        imdbid (str): IMDb ID of the movie.
        poster (str): URL to the movie poster.

    Returns:
        dict: A dictionary containing the movie details.
    """
    return {
        title: {constant.RATING_KEY: float(rating),
                constant.YEAR_KEY: int(year),
                constant.POSTER_KEY: poster, constant.IMDBID_KEY: imdbid}}


def build_dict(title: str, year: str, rating: str, poster: str) -> dict:
    """
    Creates a dictionary with movie details, excluding IMDb ID and notes.

    Parameters:
        title (str): Movie title.
        year (str): Release year.
        rating (str): Movie rating.
        poster (str): URL to the movie poster.

    Returns:
        dict: A dictionary containing the movie details.
    """
    return {
        title: {constant.RATING_KEY: float(rating),
                constant.YEAR_KEY: int(year),
                constant.POSTER_KEY: poster}}


def build_to_add_dict(year: str, rating: str, poster: str, notes: str,
                      imdbid: str) -> dict:
    """
    Creates a dictionary for adding a new movie, including all details.

    Parameters:
        year (str): Release year.
        rating (str): Movie rating.
        poster (str): URL to the movie poster.
        notes (str): User notes for the movie.
        imdbid (str): IMDb ID of the movie.

    Returns:
        dict: A dictionary with full movie details for adding to storage.
    """
    return {constant.RATING_KEY: float(rating), constant.YEAR_KEY: int(year),
            constant.POSTER_KEY: poster, constant.NOTES_KEY: notes,
            constant.IMDBID_KEY: imdbid}


def fetch_data(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieves data from a file, utilizing a cached version if available.

    Parameter:
        file_path (WindowsPath): Path to the file.

    Returns:
        misc_util.result_message: Cached or newly loaded file data.
    """
    global cached_data

    if cached_data is None:
        cached_data = load_data(file_path)
    return cached_data


def load_data_html(file_path: WindowsPath) -> misc_util.result_message:
    """
    Loads HTML data from a file into a list of lines.

    Parameter:
        file_path (WindowsPath): Path to the HTML file.

    Returns:
        misc_util.result_message: A dictionary containing:
            - result (bool): Status of the operation.
            - message (str): Success or error message.
            - payload (list): HTML lines or an empty string on failure.
    """
    try:
        with open(file_path, "r") as handle:
            payload = handle.readlines()
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


def fetch_data_html(file_path: WindowsPath) -> misc_util.result_message:
    """
    Retrieves HTML data from a file, utilizing a cached version if available.

    Parameter:
        file_path (WindowsPath): Path to the HTML file.

    Returns:
        misc_util.result_message: Cached or newly loaded HTML data.
    """
    global cached_data_html
    if cached_data_html is None:
        cached_data_html = load_data_html(file_path)
    return cached_data_html
