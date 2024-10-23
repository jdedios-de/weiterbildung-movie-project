from movie.movie_services import movie_service
from movie.utility import constant, print_util, input_util
from movie.utility.print_util import print_movie_list, print_stats_movies


def list_movies_controller():
    result = movie_service.service_list_movies("",constant.PRODUCTION_FILE_PATH)
    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])


def stats_movies_controller():
    result = movie_service.service_stat_movies(constant.PRODUCTION_FILE_PATH)
    print_stats_movies(result[constant.PAYLOAD][0],
                       result[constant.PAYLOAD][1],
                       result[constant.PAYLOAD][2],
                       result[constant.PAYLOAD][3],
                       result[constant.PAYLOAD][4])


def generate_random_movie_controller():
    result = movie_service.service_random_movie(constant.PRODUCTION_FILE_PATH)

    print_util.print_random_generated_movie(result)


def add_movie_controller():
    movie_name, movie_year, movie_rating = input_util.input_add_movie()

    result = movie_service.service_add_movie(movie_name, movie_year, movie_rating,
                                     constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully added")


def update_movie_controller():
    movie_name, movie_rating = input_util.input_update_movie()

    result = movie_service.service_update_movie(movie_name, movie_rating,
                                        constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully updated")


def delete_movie_controller():
    movie_name = input_util.input_delete_movie()

    result = movie_service.service_delete_movie(movie_name,
                                        constant.PRODUCTION_FILE_PATH)
    if result["result"]:
        print(f"Movie {movie_name} successfully deleted")

def search_movie_controller():
    part_movie_name = input_util.input_search_movie()

    result = movie_service.service_find_movie(part_movie_name,
                                        constant.PRODUCTION_FILE_PATH)

    print_util.print_movie_search(result[constant.PAYLOAD])


