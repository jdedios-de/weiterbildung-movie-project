from movie.utility import constant, menu_util
from movie.utility.input_util import please_enter_to_continue

"""
This module contains utility functions for printing
and displaying information related to the movie database.

Functions:
    print_header() -> None:
        Prints the header for the movies database.

    print_menu() -> None:
        Displays the main menu options for the user.

    print_stats_movies(average_rating: float,
                       median_rating: float,
                       best_movie: list,
                       worst_movie: list,
                       payload) -> None:
        Prints the average and median ratings, along with the best
        and worst movies from the provided statistics.

    print_movie_list(total_movies: int, movies: dict) -> None:
        Displays the total number of movies and lists each movie's
        title, year, and rating.

    print_filter_move(movies: dict) -> None:
        Prints the filtered movies; delegates to print_movie_search.

    print_movie_search(movies: dict) -> None:
        Displays a list of movies that match a search query, showing
        each movie's title, year, and rating.

    print_random_generated_movie(result: dict) -> None:
        Prints a randomly selected movie for the user, displaying
        its title and rating.

    print_movie_does_not_exist(movie: str) -> None:
        Notifies the user that a specified movie does not exist
        in the database.

    clear_menu() -> None:
        Pauses the menu display and prompts the user to continue
        before showing the menu again.
"""


def print_header() -> None:
    """Print the header for the movies database."""
    print("********** My Movies Database **********")


def print_menu() -> None:
    """Display the menu options for the user."""
    print("Menu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Movies sorted by year")
    print("10. Filter movies\n")


def print_stats_movies(average_rating: float,
                       median_rating: float,
                       best_movie: list,
                       worst_movie: list,
                       payload) -> None:
    """
    Display statistics about the movies.

    Parameters:
        average_rating (float): The average rating of the movies.
        median_rating (float): The median rating of the movies.
        best_movie (list): A list of the best movie(s).
        worst_movie (list): A list of the worst movie(s).
        payload (dict): The dictionary containing movie details.
    """
    print(f"\nAverage rating: {average_rating:.1f}")
    print(f"Median rating: {median_rating:.1f}")

    # Display best movies
    print("\n".join(
        [
            f"Best movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in best_movie]
    ))

    # Display worst movies
    print("\n".join(
        [
            f"Worst movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in worst_movie]
    ))


def print_movie_list(total_movies: int, movies: dict) -> None:
    """
    Display a list of movies with their details.

    Parameters:
        total_movies (int): The total number of movies.
        movies (dict): The dictionary containing movie details.
    """
    print(f"{total_movies} movies in total")
    print("\n".join(
        [
            f"{movie} ({movies[movie][constant.YEAR_KEY]}): "
            f"{movies[movie][constant.RATING_KEY]}"
            for movie in movies]
    ))


def print_filter_move(movies: dict) -> None:
    """
    Display filtered movie search results.

    Parameter:
        movies (dict): The filtered movie details.
    """
    print_movie_search(movies)


def print_movie_search(movies: dict) -> None:
    """
    Display the search results for movies.

    Parameter:
        movies (dict): The dictionary containing the search results.
    """
    print("\n".join(
        [
            f"{mov} ({details[constant.YEAR_KEY]}): "
            f"{details[constant.RATING_KEY]}"
            for movie in movies
            for mov, details in movie.items()]
    ))


def print_random_generated_movie(result: dict) -> None:
    """
    Display a randomly generated movie.

    Parameter:
        result (dict): The result containing the randomly chosen movie.
    """
    print(f"Your movie for tonight: {result[constant.PAYLOAD].key}, "
          f"it's rated {result[constant.PAYLOAD][1][constant.RATING_KEY]}")


def print_movie_does_not_exist(movie: str) -> None:
    """
    Notify that a specific movie does not exist.

    Parameter:
        movie (str): The title of the movie that doesn't exist.
    """
    print(f"Movie {movie} doesn't exist!\n")


def clear_menu() -> None:
    """Pause the program and display the menu."""
    please_enter_to_continue()
    menu_util.select_options(menu_util.call_menu())
