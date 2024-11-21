from movie.utility import constant
from movie.utility.data_util import write_data, fetch_data_html
from movie.utility.misc_util import result_message


def get_api_movies_format_html(result: dict) -> result_message:
    """
    Formats movie data fetched from storage into HTML structure.

    Parameter:
        result (dict): The dictionary containing movie data and result status.

    Returns:
        result_message: A dictionary containing:
            - result (bool): Status of the operation.
            - message (str): Success or failure message.
            - payload (str): HTML formatted string of movies or a "No movies"
                             message.
    """
    output = ''
    if result[constant.RESULT]:
        for key, value in result[constant.PAYLOAD].items():
            try:
                output += '<li>'
                output += (
                    f"<div class='movie' title='{value[constant.NOTES_KEY]}' "
                    f'onclick="window.location.href=\'https://www.imdb.com/title/{value[constant.IMDBID_KEY]}/\'"'
                    f" style='cursor: pointer;'>")
                output += f"<img class='movie-poster' src={value[constant.POSTER_KEY]}>"
                output += f"<div class='movie-title'>{key}</div>"
                output += f"<div class='movie-year'>Released: {value[constant.YEAR_KEY]}</div>"
                output += f"<div class='movie-year'>Rating: {value[constant.RATING_KEY]}</div>"
                output += "</div>"
                output += "</li>"
            except KeyError:
                continue

        return result_message(True,
                              "Movies information has been fetched successfully.",
                              output)
    else:
        output += '<li class="cards__item">'
        output += (" <h2 style='color: red;"
                   "width: 80%;font-weight: bold;background-color: yellow;"
                   "padding: 10px;border: 3px solid red;"
                   "border-radius: 5px;text-transform: uppercase;'>"
                   "No movies.</h2>")
        output += "</li'>"

        return result_message(False,
                              "No movies",
                              output)


def replace_html_from_storage_items(html_result) -> dict:
    """
    Replaces placeholders in the HTML template with actual movie data.

    Parameter:
        html_result (dict): Dictionary containing movie data.

    Returns:
        dict: Updated HTML content with movie data or placeholders.
    """
    return_value = fetch_data_html(constant.TEMPLATE_HTML_FILE_PATH)

    return_value_from_storage = get_api_movies_format_html(html_result)

    updated_title = ''.join(return_value[constant.PAYLOAD]).replace(
        "__TEMPLATE_TITLE__",
        "MOVIE LIBRARIES")

    return result_message(return_value_from_storage[constant.RESULT],
                          return_value_from_storage[constant.MESSAGE],
                          ''.join(updated_title).replace(
                              "__TEMPLATE_MOVIE_GRID__",
                              return_value_from_storage[constant.PAYLOAD])
                          )


def generate_new_html_file(html_result):
    """
    Generates or updates an HTML file with movie data.

    Parameter:
        html_result (dict): Dictionary containing movie data.

    Returns:
        dict: A result message indicating success or failure.
    """
    result = replace_html_from_storage_items(html_result)

    if result[constant.RESULT]:

        return write_data(
            result[constant.PAYLOAD],
            constant.INDEX_HTML_FILE_PATH)
    else:

        write_data(result[constant.PAYLOAD],
                   constant.INDEX_HTML_FILE_PATH)

        return result_message(result[constant.RESULT],
                              result[constant.MESSAGE],
                              "")
