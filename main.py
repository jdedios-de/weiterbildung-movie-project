import os
import sys
from movie.storage.storage_csv import StorageCsv
from movie.utility import constant
from movie_app import MovieApp


def main():
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
                "Run the application: python main.py <data.json> e.g. python main.py data.json")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception:
        print(
            "Run the application: python main.py <data.json> e.g. python main.py data.json")

    """

    storage = StorageCsv(constant.JSON_PRODUCTION_FILE_PATH)
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == '__main__':
    main()
