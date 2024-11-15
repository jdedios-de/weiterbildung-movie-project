"""
This module provides utility functions for handling user input related to movie management.
It includes functions for adding, updating, deleting, searching, and filtering movies.
Each function prompts the user for specific information and returns the relevant data.

Functions:
    input_add_movie() -> tuple:
        Prompts the user to enter details for a new movie, including the name, year, and rating.
        Returns a tuple containing the movie name, year, and rating.

    input_update_movie() -> str:
        Prompts the user to enter the name of the movie they wish to update.
        Returns the movie name as a string.

    input_delete_movie() -> str:
        Prompts the user to enter the name of the movie they wish to delete.
        Returns the movie name as a string.

    input_search_movie() -> str:
        Prompts the user to enter a part of the movie name for searching.
        Returns the input string.

    please_enter_to_continue() -> str:
        Prompts the user to press enter to continue. This can be used to pause the program for user acknowledgment.

    input_filter_movie() -> tuple:
        Prompts the user for filtering criteria, including minimum rating, start year, and end year.
        Returns a tuple containing the minimum rating, start year, and end year as strings.
"""


def input_add_movie() -> str:
    return input("Enter new movie name: ")


def input_update_movie() -> str:
    """
    Prompt user to input the name of a movie to update.

    Returns:
        str: The name of the movie to update.
    """
    movie_name = input("Enter movie name: ")
    return movie_name


def input_delete_movie() -> str:
    """
    Prompt user to input the name of a movie to delete.

    Returns:
        str: The name of the movie to delete.
    """
    return input("Enter movie name to delete: ")


def input_search_movie() -> str:
    """
    Prompt user to input part of a movie name for search purposes.

    Returns:
        str: A partial or full name of the movie to search.
    """
    return input("Enter part of movie name: ")


def please_enter_to_continue() -> None:
    """
    Pause execution and prompt user to press enter to continue.

    Returns:
        str: Empty string, as this function waits for user input to proceed.
    """
    input("\nPress enter to continue ")


def input_filter_movie() -> tuple:
    """
    Prompt user to input filtering criteria for movies.

    This function collects user input for minimum rating, start year,
    and end year to filter movies based on these criteria.

    Returns:
        tuple: A tuple containing the minimum rating (str), start year (str),
               and end year (str).
    """
    minimum_rating = input(
        "Enter minimum rating (leave blank for no minimum rating): ")
    start_year = input("Enter start year (leave blank for no start year): ")
    end_year = input("Enter end year (leave blank for no end year): ")

    return minimum_rating, start_year, end_year
