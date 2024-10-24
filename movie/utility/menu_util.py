from movie.controller import movies_controller
from movie.utility.print_util import print_menu
from movie.utility import constant


def select_options(user_choice: str) -> None:
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
            print(f"Invalid choice\n")
        else:
            break

    return input_available_commands
