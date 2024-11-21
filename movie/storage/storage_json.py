from pathlib import WindowsPath

from movie.storage.istorage import IStorage
from movie.movie_services.movie_service import service_list_movies, \
    service_add_movie, service_delete_movie, service_update_movie, \
    service_find_movie, service_stat_movies, service_random_movie, \
    service_filter_movies


class StorageJson(IStorage):
    """
    A class to handle movie data stored in a JSON file.
    Implements the IStorage interface for standardized storage operations.
    """

    def __init__(self, file_path: WindowsPath):
        """
        Initializes the StorageJson class with a file path.

        Parameter:
            file_path (WindowsPath): Path to the JSON file.
        """
        self.__file_path = file_path

    def get_file_path(self):
        """
        Retrieves the current file path.

        Returns:
            WindowsPath: The current file path.
        """
        return self.__file_path

    def set_file_path(self, file_path: int):
        """
        Updates the file path if valid.

        Parameters:
            file_path (int): The new file path.

        Raises:
            ValueError: If the input is not a valid `WindowsPath`.
        """
        if isinstance(file_path, WindowsPath) and file_path:
            self.__file_path = file_path
        else:
            raise ValueError("File path should be valid.")

    def list_movies(self):
        """
        Lists all movies in the storage.

        Parameter : A result message containing all stored movies.
        """
        return service_list_movies("",
                                   self.get_file_path())

    def add_movie(self, title, year, rating, poster, notes, imdbid):
        """
        Adds a new movie to the storage.

        Parameters:
        title: The title of the movie.
        year: The release year of the movie.
        rating: The rating of the movie.
        poster: The URL of the movie's poster.
        notes: Additional notes about the movie.
        imdbid: The IMDb ID of the movie.

        Return: A result message indicating success or failure.
        """
        return service_add_movie(title,
                                 year,
                                 rating,
                                 poster,
                                 notes,
                                 imdbid,
                                 self.get_file_path())

    def delete_movie(self, title):
        """
        Deletes a movie from the storage by title.

        Parameter:
            title: The title of the movie to delete.

        Returns: A result message indicating success or failure.
        """
        return service_delete_movie(title,
                                    self.get_file_path())

    def update_movie(self, title, rating):
        """
        Updates the rating of a specific movie in the storage.

        Parameter:
            title: The title of the movie to update.
            rating: The new rating for the movie.

        Return: A result message indicating success or failure.
        """
        return service_update_movie(title,
                                    rating,
                                    self.get_file_path())

    def find_movie(self, title):
        """
        Searches for a specific movie by its title.

        Parameter:
            title: The title of the movie to find.

        Return: A result message containing the movie details or an error.
        """
        return service_find_movie(True, title,
                                  self.get_file_path())

    def stats_movie(self):
        """
        Retrieves statistical information about movies in storage.

        Return: A result message containing movie statistics.
        """
        return service_stat_movies(self.get_file_path())

    def random_movie(self):
        """
        Retrieves a random movie from the storage.

        Return: A result message containing a randomly selected movie.
        """
        return service_random_movie(self.get_file_path())

    def search_movie(self, title):
        """
        Searches for movies containing a specific keyword in their title.

        Parameter:
            title: The keyword to search for in movie titles.

        Return: A result message containing matching movies.
        """
        return service_find_movie(False, title,
                                  self.get_file_path())

    def search_movie_sorted_by_rating(self, option):
        """
        Retrieves movies sorted by their rating.

        Parameter:
            option: The key for sorting movies by rating.

        Return: A result message containing sorted movies.
        """
        return service_list_movies(option,
                                   self.get_file_path())

    def search_movie_sorted_by_year(self, option):
        """
        Retrieves movies sorted by their release year.

        Parameter:
            option: The key for sorting movies by year.

        Return: A result message containing sorted movies.
        """
        return service_list_movies(option,
                                   self.get_file_path())

    def search_filter_movies(self, minimum_rating, start_year, end_year):
        """
        Filters movies based on rating and release year range.

        Parameter:
            minimum_rating: The minimum rating to filter by.
            start_year: The start year of the range.
            end_year: The end year of the range.

        Return: A result message containing filtered movies.
        """
        return service_filter_movies(minimum_rating, start_year,
                                     end_year, self.get_file_path())
