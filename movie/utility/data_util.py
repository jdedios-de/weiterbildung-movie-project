import json

from movie.utility import misc_util

cached_data = None

def load_data(file_path) -> misc_util.result_message:
    """
    Loads and returns the content of a JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    try:
        with open(file_path, "r") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return misc_util.result_message(False, "Error: The file was not found.", "")
    except IOError:
        return misc_util.result_message(False, "Error: Could not read the file.", "")
    except Exception as e:
        return misc_util.result_message(False, f"An unexpected error occurred: {e}", "")
    else:
        return misc_util.result_message(True, "File loaded successfully.", payload)


def write_data(details, file_path) -> misc_util.result_message:
    try:
        with open(file_path, 'w') as write_to_file:
            write_to_file.write(json.dumps(details))
    except FileNotFoundError:
        return misc_util.result_message(False, "Error: The file was not found.", "")
    except IOError:
        return misc_util.result_message(False, "Error: Could not write to the file.",
                              "")
    except Exception as e:
        return misc_util.result_message(False, f"An unexpected error occurred: {e}", "")
    else:
        return misc_util.result_message(True, "File written successfully.", "")


def build_dict(title, year, rating):
    return {title: {"rating": rating, "year": year}}


def build_to_add_dict(year, rating):
    return {"rating": rating, "year": year}


def fetch_data(file_path) -> dict:
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
