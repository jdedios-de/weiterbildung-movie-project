import os
import sys
from movie.storage.storage_csv import StorageCsv
from movie.utility import constant
from movie_app import MovieApp


def main():
    """
    Main script to initialize and run the Movie application with a specified JSON data file.

    Modules:
        - os: Provides functionality to interact with the operating system, including file path checks.
        - sys: Accesses command-line arguments.
        - movie.storage.storage_csv: Contains the `StorageCsv` class for handling CSV-based storage.
        - movie.utility.constant: Supplies constants, such as the production file path.
        - movie_app: Contains the `MovieApp` class, which drives the application's core functionality.

    Example:
        python main.py data.json

    Error Handling:
        - Raises `FileNotFoundError` if the specified JSON file does not exist.
        - Prints a usage guide if incorrect arguments are provided.

    """
    try:
        arguments = len(sys.argv)
        file_path = constant.PRODUCTION_FILE_PATH / sys.argv[1]
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"The file at {file_path} does not exist.")
        if arguments == 2:
            storage = StorageCsv(constant.PRODUCTION_FILE_PATH / sys.argv[1])
            movie_app = MovieApp(storage)
            movie_app.run()
        else:
            print(
                "Run the application: python3 main.py <data.json> e.g. python3 main.py data.json")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception:
        print(
            "Run the application: python3 main.py <data.json> e.g. python3 main.py data.json")


if __name__ == '__main__':
    main()
