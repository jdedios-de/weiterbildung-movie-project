from movie.storage.istorage import IStorage
from movie.utility import constant, input_util, api_util
from movie.utility.generate_html import generate_new_html_file
from movie.utility.input_util import input_filter_movie
from movie.utility.misc_util import validate_input_filter_movie, \
    result_message

"""
MovieApp: A CLI-based application to manage a collection of movies.

This script defines a `MovieApp` class and associated utility functions to manage movies,
including operations such as listing, adding, deleting, updating, filtering, and generating
a website for the movies.


Modules and Utilities:
    - `IStorage`: Interface for storage backends to manage movie data.
    - `constant`: Defines application constants (e.g., keys and command options).
    - `input_util`: Handles user inputs for various commands.
    - `api_util`: Interacts with external movie APIs to fetch movie data.
    - `generate_html`: Generates an HTML file to represent the movies.
    - `misc_util`: Contains helper utilities such as data validation and messaging.
"""


def print_filter_move(movies: dict) -> None:
    """
    Print filtered movies by delegating to the movie search print function.

    Parameter:
        movies (dict): A dictionary containing filtered movie data.

    Returns:
        None
    """
    print_movie_search(movies)


def print_movie_search(movies: dict) -> None:
    """
    Display a formatted list of movies with their release year and rating.

    Parameters: movies (dict): A dictionary containing movie data.

    Returns:
        None
    """
    print("\n".join(
        [
            f"{mov} ({details[constant.YEAR_KEY]}): "
            f"{details[constant.RATING_KEY]}"
            for movie in movies
            for mov, details in movie.items()]
    ))


def print_random_generated_movie(result: dict) -> None:
    print(f"Your movie for tonight: {result[constant.PAYLOAD][0]}, "
          f"it's rated {result[constant.PAYLOAD][1][constant.RATING_KEY]}")


def print_stats_movies(average_rating: float,
                       median_rating: float,
                       best_movie: list,
                       worst_movie: list,
                       payload) -> None:
    print(f"\nAverage rating: {average_rating:.1f}")
    print(f"Median rating: {median_rating:.1f}")

    # Display best movies
    print("\n".join(
        [
            f"Best movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in best_movie]
    ))

    print("\n".join(
        [
            f"Worst movie: {movie}, "
            f"{payload[movie][constant.RATING_KEY]}"
            for movie in worst_movie]
    ))


def print_movie_does_not_exist(movie: str) -> None:
    """
    Notify that a specific movie does not exist.

    Parameter:
        movie (str): The title of the movie that doesn't exist.
    """
    print(f"Movie {movie} doesn't exist!\n")


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
    print("10. Filter movies")
    print("11. Generate website\n")


def select_options(self, user_choice: str) -> None:
    func_dict = {
        f"{constant.EXIT}":
            _command_exit_app,
        f"{constant.LIST_MOVIES}":
            self._command_list_movies,
        f"{constant.ADD_MOVIE}":
            self._command_add_movie,
        f"{constant.DELETE_MOVIE}":
            self._command_delete_movie,
        f"{constant.UPDATE_MOVIE}":
            self._command_update_movie,
        f"{constant.STATS}":
            self._command_movie_stats,
        f"{constant.RANDOM_MOVIE}":
            self._command_random_movie,
        f"{constant.SEARCH_MOVIE}":
            self._command_search_movie,
        f"{constant.MOVIES_SORTED_BY_RATING}":
            self._command_movie_sorted_by_rating,
        f"{constant.MOVIES_SORTED_BY_YEAR}":
            self._command_movie_sorted_by_year,
        f"{constant.FILTER_MOVIES}":
            self._command_filter_movie,
        f"{constant.GENERATE_MOVIES}":
            self._generate_website,
    }

    option = return_options()

    if user_choice in option:
        func_dict[user_choice]()


def please_enter_to_continue() -> None:
    input("\nPress enter to continue ")


def return_options() -> list:
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
        constant.FILTER_MOVIES,
        constant.GENERATE_MOVIES
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
            print("Invalid choice\n")
        else:
            break

    return input_available_commands


def _command_exit_app():
    print("Bye!")


class MovieApp:

    def __init__(self, storage: IStorage):
        """
        Initializes the MovieApp with a specified storage instance.
        """
        self.__storage = storage

    def get_storage(self):
        """
        Retrieves the current storage instance used by the application.

        Returns:
            IStorage: The storage instance handling movie data operations.
        """
        return self.__storage

    def set_storage(self, storage: IStorage):
        """
        Updates the storage instance used by the application.

        Parameters:
            storage (IStorage): A valid storage instance implementing the
                                IStorage interface.

        Raises:
            ValueError: If the provided storage is not an instance of IStorage
                        or is invalid.
        """
        if isinstance(storage, IStorage) and storage:
            self.__storage = storage
        else:
            raise ValueError("storage should be valid IStorage class.")

    def _command_list_movies(self):
        """
        Retrieves the list of movies from the storage, then prints the movie
        details including the total count and relevant information such as
        movie title, year, and rating.
        """
        result = self.get_storage().list_movies()
        print_movie_list(len(result[constant.PAYLOAD]),
                         result[constant.PAYLOAD])

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_add_movie(self):
        """
        Adds a new movie to the storage system. Prompts the user to input a
        movie name and optional notes. It then fetches movie data from an
        external API. If the movie data is successfully retrieved, it adds
        the movie to the storage with the provided information.

        If the movie is added successfully, a confirmation message is displayed.
        If the movie is not found in the API, an error message is shown.

        Raises:
            Exception: If the movie data cannot be fetched from the API or
                       if the movie cannot be added to storage.
        """
        movie_name, movie_notes = input_util.input_add_movie()

        try:
            movie_return = api_util.get_movie_data_from_api(movie_name)

            if not movie_return[constant.RESULT]:
                raise Exception(movie_return[constant.PAYLOAD])

            for key, value in movie_return[constant.PAYLOAD].items():
                result = self.get_storage().add_movie(key,
                                                      value[
                                                          constant.YEAR_KEY],
                                                      value[
                                                          constant.RATING_KEY],
                                                      value[
                                                          constant.POSTER_KEY],
                                                      movie_notes,
                                                      value[
                                                          constant.IMDBID_KEY])
                if result["result"]:
                    print(f"Movie {movie_name} successfully added")

        except Exception as e:
            print(f"Didn't find movie {movie_name} in the API: {e}")
        finally:
            please_enter_to_continue()
            select_options(self, call_menu())

    def _command_delete_movie(self):
        """
        Deletes a movie from the storage system. Prompts the user to input
        the name of the movie they wish to delete. It then attempts to
        delete the movie from the storage.

        If the movie is not found in the storage, an error message is shown.
        If the deletion is successful, a confirmation message is displayed.

        Raises:
            KeyError: If the movie is not found in the storage.
            Exception: If there is any other error during the deletion process.
        """
        while True:
            movie_name = input_util.input_delete_movie()
            try:
                result = self.get_storage().delete_movie(movie_name)

                if not result[constant.RESULT]:
                    raise KeyError()

                if result["result"]:
                    print(f"Movie {movie_name} successfully deleted")

            except KeyError:
                print_movie_does_not_exist(movie_name)

            except Exception as e:
                print(f"Movie was not deleted: {e}")
            finally:
                break

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_update_movie(self):
        """
        Updates the rating of an existing movie in the storage system.
        Prompts the user to input the name of the movie they wish to update.
        The method checks if the movie exists in the storage.
        If the movie is found, it allows the user to enter a new rating for
        the movie. The movie's rating is then updated in the storage.

        If the movie is not found in the storage, an error message is shown.
        If the update is unsuccessful, an exception is raised, and the error
        is reported.

        Raises:
            KeyError: If the movie is not found in the storage.
            Exception: If there is an issue updating the movie's rating.
        """
        while True:
            movie_name = input_util.input_update_movie()
            try:
                result = self.get_storage().find_movie(movie_name)

                if not result[constant.RESULT]:
                    raise KeyError()

                movie_rating = input("Enter new movie rating: ")

                result_update = self.get_storage().update_movie(movie_name,
                                                                movie_rating)

                if not result_update[constant.RESULT]:
                    raise Exception()

                if result["result"]:
                    print(f"Movie {movie_name} successfully updated")

            except KeyError:
                print_movie_does_not_exist(movie_name)
            except Exception as e:
                print(f"Movie was not updated {e}")

            finally:
                break

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_movie_stats(self):
        """
        Displays statistics about movies stored in the system.

        Raises:
            Exception: If there is an issue retrieving or processing the
                       movie statistics from the storage.
        """
        result = self.get_storage().stats_movie()
        print_stats_movies(result[constant.PAYLOAD][0],
                           result[constant.PAYLOAD][1],
                           result[constant.PAYLOAD][2],
                           result[constant.PAYLOAD][3],
                           result[constant.PAYLOAD][4])
        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_random_movie(self):
        """
        Displays a randomly selected movie from the stored collection.

        Raises:
            Exception: If there is an issue retrieving or
                       processing the random movie from the storage.
        """
        result = self.get_storage().random_movie()

        print_random_generated_movie(result)

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_search_movie(self):
        """
        Searches for movies based on a partial name input by the user.

        Raises:
            Exception: If there is an issue retrieving or processing the
                       movie search results.
        """
        part_movie_name = input_util.input_search_movie()

        result = self.get_storage().search_movie(part_movie_name)

        print_movie_search(result[constant.PAYLOAD])

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_movie_sorted_by_rating(self):
        """
        Displays a list of movies sorted by their rating.

        Raises:
            Exception: If there is an issue retrieving or processing
                       the sorted movie list.
        """

        result = (self.get_storage().search_movie_sorted_by_rating
                  (constant.RATING_KEY))

        print_movie_list(len(result[constant.PAYLOAD]),
                         result[constant.PAYLOAD])

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_movie_sorted_by_year(self):
        """
        Displays a list of movies sorted by their release year.

        Raises:
            Exception: If there is an issue retrieving or processing
                       the sorted movie list.
        """

        result = (self.get_storage().search_movie_sorted_by_year
                  (constant.YEAR_KEY))

        print_movie_list(len(result[constant.PAYLOAD]),
                         result[constant.PAYLOAD])

        please_enter_to_continue()
        select_options(self, call_menu())

    def _command_filter_movie(self):
        """
        Filters movies based on a minimum rating and a range of release years.

        Raises:
            ValueError: If the provided filter values are invalid or
                        do not match expected formats.
        """

        (input_minimum_rating,
         input_start_year, input_end_year) = input_filter_movie()

        minimum_rating, start_year, end_year = (validate_input_filter_movie
                                                (input_end_year,
                                                 input_minimum_rating,
                                                 input_start_year))

        result = self.get_storage().search_filter_movies(minimum_rating,
                                                         start_year,
                                                         end_year
                                                         )

        print_filter_move(result[constant.PAYLOAD])

        please_enter_to_continue()
        select_options(self, call_menu())

    def _generate_website(self):
        """
        Generates a static HTML website displaying the list of movies.

        This method retrieves the list of movies from storage and generates a
        static HTML file displaying the movie details using the
        `generate_new_html_file` function. The user is notified whether
        the website was successfully generated.

        Raises:
            Exception: If there is an issue generating the website.
        """
        result: result_message = self.get_storage().list_movies()

        result = generate_new_html_file(result)

        if result[constant.RESULT]:
            print("Website was generated successfully.")
        else:
            print("Website was generated unsuccessfully.")

        please_enter_to_continue()
        select_options(self, call_menu())

    def run(self):
        """
        Runs the main menu of the MovieApp.

        The method continuously prompts the user to select an option
        until the app is terminated.
        """
        select_options(self, call_menu())
