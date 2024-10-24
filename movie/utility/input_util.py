
def input_add_movie() -> tuple:
    movie_name = input("Enter new movie name: ")
    movie_year = input("Enter new movie year: ")
    movie_rating = input("Enter new movie rating: ")

    return movie_name, movie_year, movie_rating


def input_update_movie() -> str:
    movie_name = input("Enter movie name: ")
    return movie_name


def input_delete_movie() -> str:
    return input("Enter movie name to delete: ")


def input_search_movie() -> str:
    return input("Enter part of movie name: ")


def please_enter_to_continue() -> str:
    input("\nPress enter to continue ")


def input_filter_movie() -> tuple:
    minimum_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
    start_year = input("Enter start year (leave blank for no start year): ")
    end_year = input("Enter end year (leave blank for no end year): ")

    return minimum_rating, start_year, end_year
