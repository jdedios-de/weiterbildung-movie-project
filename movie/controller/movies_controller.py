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
    """
    Exit the movie application.

    This function prints a goodbye message to the console
    and exits the application.
    """
    print("Bye!")


def list_movies_controller() -> None:
    """
    List all movies from the service.

    This function retrieves a list of movies using the movie_service,
    and then prints the list to the console.

    Returns:
        None
    """
    result = movie_service.service_list_movies("",
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def sort_movies_by_rating_controller() -> None:
    """
    Sort and list movies by their ratings.

    This function retrieves a list of movies sorted by rating
    from the movie_service, then prints the sorted list to the console.

    Returns:
        None
    """
    result = movie_service.service_list_movies(constant.RATING_KEY,
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def service_filter_movies_controller() -> None:
    """
    Filter and display movies based on rating and year range.

    This function prompts the user to input a minimum rating and a range of years
    to filter movies. The input is then validated, and the filtered movies are
    retrieved from the movie_service. Finally, the filtered movie list is printed
    to the console.

    Returns:
        None
    """
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
    """
    Sort and display movies by their release year.

    This function retrieves a list of movies sorted by release year
    from the movie_service, then prints the sorted list to the console.

    Returns:
        None
    """
    result = movie_service.service_list_movies(constant.YEAR_KEY,
                                               constant.PRODUCTION_FILE_PATH)

    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    clear_menu()


def stats_movies_controller():
    """
    Retrieve and display movie statistics.

    This function fetches statistical data about movies from the movie_service
    and prints it to the console.

    Returns:
        None
    """
    result = movie_service.service_stat_movies(constant.PRODUCTION_FILE_PATH)
    print_stats_movies(result[constant.PAYLOAD][0],
                       result[constant.PAYLOAD][1],
                       result[constant.PAYLOAD][2],
                       result[constant.PAYLOAD][3],
                       result[constant.PAYLOAD][4])

    clear_menu()


def generate_random_movie_controller():
    """
    Generate and display a random movie.

    This function retrieves a randomly selected movie from the movie_service
    and displays it using the print_util module.

    Returns:
        None
    """
    result = movie_service.service_random_movie(constant.PRODUCTION_FILE_PATH)

    print_util.print_random_generated_movie(result)

    clear_menu()


def add_movie_controller() -> None:
    """
    Add a new movie to the collection.

    This function prompts the user to input details for a new movie
    (name, year, and rating) and attempts to add it to the collection
    through the movie_service. If the addition is successful, a confirmation
    message is printed. In case of an error, a failure message is displayed.

    Returns:
        None
    """
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
    """
    Update the rating of an existing movie.

    This function prompts the user to input the name of a movie
    to update. It checks if the movie exists in the collection
    using the movie_service. If found, the user is prompted
    to enter a new rating, and the movie's rating is updated.
    Success and failure messages are printed based on the result
    of the update operation.

    Returns:
        None
    """
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
    """
    Delete a movie from the collection.

    This function prompts the user to input the name of a movie to delete.
    It attempts to remove the specified movie using the movie_service.
    If the movie is successfully deleted, a confirmation message is printed.
    If the movie does not exist or the deletion fails, appropriate
    error messages are displayed.

    Returns:
        None
    """
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
    """
    Search for movies by a partial name match.

    This function prompts the user to input a partial movie
    name to search for. It retrieves a list of movies matching
    the input string using the movie_service and displays the results.

    Returns:
        None
    """
    part_movie_name = input_util.input_search_movie()

    result = movie_service.service_find_movie(False, part_movie_name,
                                              constant.PRODUCTION_FILE_PATH)

    print_util.print_movie_search(result[constant.PAYLOAD])

    clear_menu()
