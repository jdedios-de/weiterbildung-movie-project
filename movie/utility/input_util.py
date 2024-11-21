def input_add_movie() -> tuple[str, str]:
    return input("Enter new movie name: "), input("Enter movie notes: ")


def input_update_movie() -> str:
    movie_name = input("Enter movie name: ")
    return movie_name


def input_delete_movie() -> str:
    return input("Enter movie name to delete: ")


def input_search_movie() -> str:
    return input("Enter part of movie name: ")


def please_enter_to_continue() -> None:
    input("\nPress enter to continue ")


def input_filter_movie() -> tuple:
    minimum_rating = input(
        "Enter minimum rating (leave blank for no minimum rating): ")
    start_year = input("Enter start year (leave blank for no start year): ")
    end_year = input("Enter end year (leave blank for no end year): ")

    return minimum_rating, start_year, end_year
