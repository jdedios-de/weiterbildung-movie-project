from movie.repository.movie_storage import list_movies
from movie.repository.movie_storage import add_movie
from movie.repository.movie_storage import delete_movie
from movie.utility import constant

def service_list_movies(file_path):
    return list_movies(file_path)


def service_add_movie(title, year, rating, file_path):
    return add_movie(title, year, rating, file_path)


def service_delete_movie(title, file_path):
    return delete_movie(title, file_path)


def main():
    title = "Movie Jerome"

    result = delete_movie(title, constant.TEST_FILE_PATH)

    print(result)

if __name__ == '__main__':
    main()