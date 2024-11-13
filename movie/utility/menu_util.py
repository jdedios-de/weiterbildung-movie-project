from movie.controller import movies_controller
from movie.utility.print_util import print_menu
from movie.utility import constant

"""
This module manages the user interaction through a command-line menu for movie management.
It allows users to select various options to perform actions related to movies,
such as listing, adding, deleting, updating, and filtering movies.

Functions:
    select_options(user_choice: str) -> None:
        Takes a user's choice as input and executes the corresponding movie controller function.
        It uses a dictionary to map user choices to their respective functions.

    return_options() -> list:
        Returns a list of valid menu options for user input.
        This list is used to validate the user's choices.

    call_menu() -> str:
        Displays the menu and prompts the user to enter a choice.
        Validates the input and handles exceptions for invalid choices.
        Continues to prompt the user until a valid choice is made or the user chooses to exit.
        Returns the user's choice as a string.
"""


def select_options(user_choice: str) -> None:
    """
    Execute the appropriate controller function based on user choice.

    This function matches the user's input with a predefined set of options,
    calling the corresponding controller function if the input is valid.

    Parameter:
        user_choice (str): The option selected by the user, which should match
                           a key in the function dictionary.
    """
    func_dict = {
        f"{constant.EXIT}":
            movies_controller.exit_movies_controller,
        f"{constant.LIST_MOVIES}":
            movies_controller.list_movies_controller,
        f"{constant.ADD_MOVIE}":
            movies_controller.add_movie_controller,
        f"{constant.DELETE_MOVIE}":
            movies_controller.delete_movie_controller,
        f"{constant.UPDATE_MOVIE}":
            movies_controller.update_movie_controller,
        f"{constant.STATS}":
            movies_controller.stats_movies_controller,
        f"{constant.RANDOM_MOVIE}":
            movies_controller.generate_random_movie_controller,
        f"{constant.SEARCH_MOVIE}":
            movies_controller.search_movie_controller,
        f"{constant.MOVIES_SORTED_BY_RATING}":
            movies_controller.sort_movies_by_rating_controller,
        f"{constant.MOVIES_SORTED_BY_YEAR}":
            movies_controller.sort_movies_by_year_controller,
        f"{constant.FILTER_MOVIES}":
            movies_controller.service_filter_movies_controller,
    }

    option = return_options()

    if user_choice in option:
        func_dict[user_choice]()


def return_options() -> str:
    """
    Retrieve a list of available menu options.

    Returns:
        list: A list of constant values representing each menu option.
    """
    option = [
        constant.EXIT,
        constant.LIST_MOVIES,
        constant.ADD_MOVIE,
        constant.DELETE_MOVIE,
        constant.UPDATE_MOVIE,
        constant.STATS,
        constant.RANDOM_MOVIE,
        constant.SEARCH_MOVIE,
        constant.MOVIES_SORTED_BY_RATING,
        constant.MOVIES_SORTED_BY_YEAR,
        constant.FILTER_MOVIES
    ]
    return option


def call_menu() -> str:
    """
    Display the main menu and prompt the user to select an option.

    Prompts the user until a valid choice is entered, returning
    the selected option. Terminates if the exit (0) option is chosen.

    Returns:
        str: The user's chosen menu option.
    """
    while True:
        try:
            print_menu()

            input_available_commands = input("Enter choice (0-10): ")

            if input_available_commands == constant.EXIT:
                break

            option = return_options()

            if input_available_commands not in option:
                raise ValueError()

        except ValueError:
            print("Invalid choice\n")
        else:
            break

    return input_available_commands
