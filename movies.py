from movie.utility import menu_util


def main():
    """
    Main Module for Movie Database Application

    This module serves as the entry point for the Movie Database application.

    The application utilizes a menu-driven approach, where users can
    select options to perform specific actions on the movie database.

    Usage:
    Run this module to start the Movie Database application:
        $ python movies.py
    """
    menu_util.select_options(menu_util.call_menu())


if __name__ == '__main__':
    main()
