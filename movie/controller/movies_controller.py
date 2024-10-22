from movie.movie_services.movie_service import service_stat_movies
from movie.utility.input_util import input_add_movie, input_update_movie, \
    input_delete_movie
from movie.utility.misc_util import get_best_movie, get_worst_movie, \
    get_average_rating, get_median_rating
from movie.utility.print_util import print_movie_list, print_stats_movies
from movie.movie_services import movie_service
from movie.utility import constant


def list_movies_controller():
    result = movie_service.service_list_movies(constant.PRODUCTION_FILE_PATH)
    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])


def stats_movies_controller():
    (average_rating, median_rating, best_movie,
     worst_movie, result) = service_stat_movies(constant.PRODUCTION_FILE_PATH)

    print_stats_movies(average_rating, median_rating, best_movie, worst_movie,
                       result)


def add_movie_controller():
    movie_name, movie_year, movie_rating = input_add_movie()

    result = movie_service.add_movie(movie_name, movie_year, movie_rating,
                                     constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully added")


def update_movie_controller():
    movie_name, movie_rating = input_update_movie()

    result = movie_service.update_movie(movie_name, movie_rating,
                                        constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully updated")


def delete_movie_controller():
    movie_name = input_delete_movie()

    result = movie_service.delete_movie(movie_name,
                                        constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully deleted")


def main():
    stats_movies_controller()


if __name__ == '__main__':
    main()
