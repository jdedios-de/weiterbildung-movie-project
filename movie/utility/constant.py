from pathlib import Path

"""
This module defines constants used across the application for handling movie data.
It includes file paths, keys for movie attributes, user input options, and return types.

Constants:
    PRODUCTION_FILE (str): The name of the production JSON file containing movie data.
    TEST_FILE (str): The name of the test JSON file used for testing purposes.
    PACKAGE_REPOSITORY (str): Directory name where the movie data files are stored.

    PRODUCTION_FILE_PATH (Path): Path object pointing to the production movie database.
    TEST_FILE_PATH (Path): Path object pointing to the test movie database.

    RATING_KEY (str): Key for accessing the movie rating in the data structure.
    YEAR_KEY (str): Key for accessing the movie release year in the data structure.

    User Input Constants:
        EXIT (str): Option for exiting the program.
        LIST_MOVIES (str): Option for listing all movies.
        ADD_MOVIE (str): Option for adding a movie.
        DELETE_MOVIE (str): Option for deleting a movie.
        UPDATE_MOVIE (str): Option for updating a movie's rating.
        STATS (str): Option for displaying movie statistics.
        RANDOM_MOVIE (str): Option for generating a random movie.
        SEARCH_MOVIE (str): Option for searching for a movie by name.
        MOVIES_SORTED_BY_RATING (str): Option for sorting movies by rating.
        MOVIES_SORTED_BY_YEAR (str): Option for sorting movies by release year.
        FILTER_MOVIES (str): Option for filtering movies by rating and year.

    Return Constants:
        RESULT (str): Key indicating the result of a service operation.
        MESSAGE (str): Key for the message associated with the result.
        PAYLOAD (str): Key for the actual movie data payload.
        AVERAGE_RATING (str): Key for the average movie rating.
        MEDIAN_RATING (str): Key for the median movie rating.
        BEST_MOVIE (str): Key for the highest-rated movie.
        WORST_MOVIE (str): Key for the lowest-rated movie.
"""


# OTHERS CONSTANTS

PRODUCTION_FILE = "data.json"
TEST_FILE = "temp_data.json"
PACKAGE_REPOSITORY = "repository"

RATING_KEY = "rating"
YEAR_KEY = "year"

# DEPENDENCY INJECTION

PRODUCTION_FILE_PATH = Path(__file__).parent.parent / PACKAGE_REPOSITORY / PRODUCTION_FILE

TEST_FILE_PATH = Path(__file__).parent.parent / PACKAGE_REPOSITORY / TEST_FILE

# USER INPUT CONSTANTS

EXIT = "0"
LIST_MOVIES = "1"
ADD_MOVIE = "2"
DELETE_MOVIE = "3"
UPDATE_MOVIE = "4"
STATS = "5"
RANDOM_MOVIE = "6"
SEARCH_MOVIE = "7"
MOVIES_SORTED_BY_RATING = "8"
MOVIES_SORTED_BY_YEAR = "9"
FILTER_MOVIES = "10"


# RETURN CONSTANT

RESULT = "result"
MESSAGE = "message"
PAYLOAD = "payload"
AVERAGE_RATING = "average_rating"
MEDIAN_RATING = "median_rating"
BEST_MOVIE = "best_movie"
WORST_MOVIE = "worst_movie"
