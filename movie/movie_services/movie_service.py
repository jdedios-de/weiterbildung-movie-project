from movie.repository.movie_storage import list_movies, find_movie, \
    stats_movies
from movie.utility.misc_util import get_average_rating, get_median_rating, \
    get_best_movie, get_worst_movie
from movie.repository.movie_storage import add_movie
from movie.repository.movie_storage import delete_movie
from movie.repository.movie_storage import update_movie
from movie.utility import constant


def service_list_movies(file_path):
    return list_movies(file_path)


def service_stat_movies(file_path):
    rating_for_all_movies = []

    result = stats_movies(file_path)

    for movie in result[constant.PAYLOAD]:
        rating_for_all_movies.append(
            float(result[constant.PAYLOAD][movie][constant.RATING_KEY]))

    average_rating = get_average_rating(rating_for_all_movies)
    median_rating = get_median_rating(rating_for_all_movies)
    best_movie = get_best_movie(result[constant.PAYLOAD])
    worst_movie = get_worst_movie(result[constant.PAYLOAD])

    return average_rating, median_rating, best_movie, worst_movie, result[constant.PAYLOAD]


def service_add_movie(title, year, rating, file_path):
    return add_movie(title, year, rating, file_path)


def service_delete_movie(title, file_path):
    return delete_movie(title, file_path)


def service_update_movie(title, rating, file_path):
    return update_movie(title, rating, file_path)


def service_find_movie(title, file_path):
    return find_movie(title, file_path)


def main():
    title = "Titanic"

    result = service_find_movie(title, constant.TEST_FILE_PATH)

    print(result)


if __name__ == '__main__':
    main()
