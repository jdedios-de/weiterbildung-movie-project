def input_add_movie() -> tuple[str, str]:
    """
    Prompts the user to input a new movie's name and optional notes.

    Returns:
        tuple[str, str]: A tuple containing the movie name and notes.
    """
    return input("Enter new movie name: "), input("Enter movie notes: ")


def input_update_movie() -> str:
    """
    Prompts the user to input the name of the movie they want to update.

    Returns:
        str: The name of the movie to update.
    """
    return input("Enter movie name: ")


def input_delete_movie() -> str:
    """
    Prompts the user to input the name of the movie they want to delete.

    Returns:
        str: The name of the movie to delete.
    """
    return input("Enter movie name to delete: ")


def input_search_movie() -> str:
    """
    Prompts the user to input part of a movie name for a search.

    Returns:
        str: A partial or full movie name for searching.
    """
    return input("Enter part of movie name: ")


def please_enter_to_continue() -> None:
    """
    Pauses the application until the user presses enter.

    Returns:
        None
    """
    input("\nPress enter to continue ")


def input_filter_movie() -> tuple:
    """
    Prompts the user to input filtering criteria for movies, including
    minimum rating, start year, and end year.

    Returns:
        tuple: A tuple containing:
            - minimum_rating (str): Minimum rating input by the user.
            - start_year (str): Start year input by the user.
            - end_year (str): End year input by the user.
    """
    minimum_rating = input(
        "Enter minimum rating (leave blank for no minimum rating): ")
    start_year = input("Enter start year (leave blank for no start year): ")
    end_year = input("Enter end year (leave blank for no end year): ")

    return minimum_rating, start_year, end_year
