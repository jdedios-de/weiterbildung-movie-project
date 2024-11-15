from movie.movie_services.storage_csv import StorageCsv
from movie.utility import constant
from movie_app import MovieApp


def main():
    storage = StorageCsv(constant.JSON_PRODUCTION_FILE_PATH)
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == '__main__':
    main()
