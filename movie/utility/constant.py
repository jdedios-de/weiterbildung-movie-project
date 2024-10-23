from pathlib import Path

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


#RETURN CONSTANT
RESULT = "result"
MESSAGE = "message"
PAYLOAD = "payload"
AVERAGE_RATING = "average_rating"
MEDIAN_RATING = "median_rating"
BEST_MOVIE = "best_movie"
WORST_MOVIE = "worst_movie"
