from pathlib import Path

# Constants used throughout the program
PRODUCTION_FILE = "data.json"
TEST_FILE = "temp_data.json"
PACKAGE_REPOSITORY = "repository"

PRODUCTION_FILE_PATH = Path(__file__).parent.parent / PACKAGE_REPOSITORY / PRODUCTION_FILE

TEST_FILE_PATH = Path(__file__).parent.parent / PACKAGE_REPOSITORY / TEST_FILE
