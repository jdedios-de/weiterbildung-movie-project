from movie.controller.movies_controller import list_movies_controller, \
    add_movie_controller, update_movie_controller, delete_movie_controller, \
    stats_movies_controller
from movie.utility.print_util import print_menu
from movie.utility import constant



def select_options(user_choice: str) -> None:
    func_dict = {
        f"{constant.LIST_MOVIES}": list_movies_controller,
        f"{constant.ADD_MOVIE}": add_movie_controller,
        f"{constant.DELETE_MOVIE}": delete_movie_controller,
        f"{constant.UPDATE_MOVIE}": update_movie_controller,
        f"{constant.STATS}": stats_movies_controller,
        f"{constant.RANDOM_MOVIE}": list_movies_controller,
        f"{constant.SEARCH_MOVIE}": list_movies_controller,
        f"{constant.MOVIES_SORTED_BY_RATING}": list_movies_controller,
        f"{constant.MOVIES_SORTED_BY_YEAR}": list_movies_controller,
        f"{constant.FILTER_MOVIES}": list_movies_controller,
    }

    option = return_options()

    if user_choice in option:
        func_dict[user_choice]()

def return_options():
    option = [
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
            print(
                f"\nInvalid input; please select an option from the menu.\n")
            input("Press any key to continue ...")
        else:
            break

    return input_available_commands

def main():
    select_options(call_menu())
if __name__ == '__main__':
    main()