from movie.movie_services import movie_service
from movie.utility import constant, print_util, input_util
from movie.utility.input_util import input_filter_movie
from movie.utility.misc_util import validate_input_filter_movie
from movie.utility.print_util import print_movie_list, print_stats_movies, \
    print_movie_does_not_exist, clear_menu, print_filter_move

"""
This module provides controller functions for managing movies. It interacts
with the `movie_service` to perform various movie-related operations such as
listing, sorting, filtering, adding, updating, deleting, and searching movies.
The controllers handle user input and pass it to the services, then display
the results in a user-friendly manner.

Functions:
    exit_movies_controller():
        Prints a goodbye message and exits the movie menu.

    list_movies_controller():
        Retrieves and displays a list of all movies.

    sort_movies_by_rating_controller():
        Retrieves and displays a list of movies sorted by their rating.

    service_filter_movies_controller():
        Filters movies based on user-provided rating and year range, and displays the results.

    sort_movies_by_year_controller():
        Retrieves and displays a list of movies sorted by their release year.

    stats_movies_controller():
        Displays statistics related to the movies (e.g., average rating, total count).

    generate_random_movie_controller():
        Generates and displays a random movie from the list.

    add_movie_controller():
        Adds a new movie to the movie list based on user input (movie name, year, and rating).

    update_movie_controller():
        Updates the rating of an existing movie based on user input.

    delete_movie_controller():
        Deletes a movie from the list based on user input.

    search_movie_controller():
        Searches for a movie by a partial name match and displays the results.
"""


def exit_movies_controller() -> None:
    print("Bye!")


def list_movies_controller() -> None:
    result = movie_service.service_list_movies("",
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def sort_movies_by_rating_controller() -> None:
    result = movie_service.service_list_movies(constant.RATING_KEY,
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def service_filter_movies_controller() -> None:
    (input_minimum_rating,
     input_start_year, input_end_year) = input_filter_movie()

    minimum_rating, start_year, end_year = (validate_input_filter_movie
                                            (input_end_year,
                                             input_minimum_rating,
                                             input_start_year))

    result = (movie_service.service_filter_movies
              (minimum_rating,
               start_year,
               end_year,
               constant.PRODUCTION_FILE_PATH))

    print_filter_move(result[constant.PAYLOAD])

    clear_menu()


def sort_movies_by_year_controller() -> None:
    result = movie_service.service_list_movies(constant.YEAR_KEY,
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def stats_movies_controller():
    result = movie_service.service_stat_movies(constant.PRODUCTION_FILE_PATH)
    print_stats_movies(result[constant.PAYLOAD][0],
                       result[constant.PAYLOAD][1],
                       result[constant.PAYLOAD][2],
                       result[constant.PAYLOAD][3],
                       result[constant.PAYLOAD][4])

    clear_menu()


def generate_random_movie_controller():
    result = movie_service.service_random_movie(constant.PRODUCTION_FILE_PATH)

    print_util.print_random_generated_movie(result)

    clear_menu()


def add_movie_controller() -> None:
    try:
        movie_name, movie_year, movie_rating = input_util.input_add_movie()

        result = movie_service.service_add_movie(movie_name, movie_year,
                                                 movie_rating,
                                                 constant.PRODUCTION_FILE_PATH)
        if result["result"]:
            print(f"Movie {movie_name} successfully added")

    except Exception:
        print(f"Movie {movie_name} was not added")
    finally:
        clear_menu()


def update_movie_controller() -> None:
    while True:
        try:
            movie_name = input_util.input_update_movie()

            result = movie_service.service_find_movie(True, movie_name,
                                                      constant.PRODUCTION_FILE_PATH)
            if not result[constant.RESULT]:
                raise KeyError()

            movie_rating = input("Enter new movie rating: ")

            result_update = (movie_service.service_update_movie
                             (movie_name, movie_rating,
                              constant.PRODUCTION_FILE_PATH))

            if not result_update[constant.RESULT]:
                raise Exception()

            if result["result"]:
                print(f"Movie {movie_name} successfully updated")

        except KeyError:
            print_movie_does_not_exist(movie_name)
        except Exception:
            print(f"Movie {movie_name} was not updated")
        finally:
            break

    clear_menu()


def delete_movie_controller() -> None:
    while True:
        try:
            movie_name = input_util.input_delete_movie()

            result = (movie_service.service_delete_movie
                      (movie_name, constant.PRODUCTION_FILE_PATH))

            if not result[constant.RESULT]:
                raise KeyError()

            if result["result"]:
                print(f"Movie {movie_name} successfully deleted")

        except KeyError:
            print_movie_does_not_exist(movie_name)

        except Exception:
            print(f"Movie {movie_name} was not deleted")

        finally:
            break

    clear_menu()


def search_movie_controller() -> None:
    part_movie_name = input_util.input_search_movie()

    result = movie_service.service_find_movie(False, part_movie_name,
                                              constant.PRODUCTION_FILE_PATH)

    print_util.print_movie_search(result[constant.PAYLOAD])

    clear_menu()
