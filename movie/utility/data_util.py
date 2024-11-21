import csv
import json
from pathlib import WindowsPath

from movie.utility import misc_util, constant

cached_data = None
cached_data_html = None


def load_data(file_path: WindowsPath) -> misc_util.result_message:
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
    return {
        title: {constant.RATING_KEY: float(rating),
                constant.YEAR_KEY: int(year),
                constant.POSTER_KEY: poster, constant.IMDBID_KEY: imdbid}}


def build_dict(title: str, year: str, rating: str, poster: str) -> dict:
    return {
        title: {constant.RATING_KEY: float(rating),
                constant.YEAR_KEY: int(year),
                constant.POSTER_KEY: poster}}


def build_to_add_dict(year: str, rating: str, poster: str, notes: str,
                      imdbid: str) -> dict:
    return {constant.RATING_KEY: float(rating), constant.YEAR_KEY: int(year),
            constant.POSTER_KEY: poster, constant.NOTES_KEY: notes,
            constant.IMDBID_KEY: imdbid}


def fetch_data(file_path: WindowsPath) -> misc_util.result_message:
    global cached_data

    if cached_data is None:
        cached_data = load_data(file_path)
    return cached_data


def load_data_html(file_path: WindowsPath) -> misc_util.result_message:
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
    global cached_data_html
    if cached_data_html is None:
        cached_data_html = load_data_html(file_path)
    return cached_data_html
