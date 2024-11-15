from pathlib import WindowsPath

from movie.movie_services.istorage import IStorage
from movie.movie_services.movie_service import service_list_movies, \
    service_add_movie, service_delete_movie, service_update_movie, \
    service_find_movie, service_stat_movies, service_random_movie, \
    service_filter_movies


class StorageJson(IStorage):
    def __init__(self, file_path: WindowsPath):
        self.__file_path = file_path

    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file_path: int):
        if isinstance(file_path, WindowsPath) and file_path:
            self.__file_path = file_path
        else:
            raise ValueError("File path should be valid.")

    def list_movies(self):
        return service_list_movies("",
                                   self.get_file_path())

    def add_movie(self, title, year, rating, poster):
        return service_add_movie(title,
                                 year,
                                 rating,
                                 self.get_file_path())

    def delete_movie(self, title):
        return service_delete_movie(title,
                                    self.get_file_path())

    def update_movie(self, title, rating):
        return service_update_movie(title,
                                    rating,
                                    self.get_file_path())

    def find_movie(self, title):
        return service_find_movie(True, title,
                                  self.get_file_path())

    def stats_movie(self):
        return service_stat_movies(self.get_file_path())

    def random_movie(self):
        return service_random_movie(self.get_file_path())

    def search_movie(self, title):
        return service_find_movie(False, title,
                                  self.get_file_path())

    def search_movie_sorted_by_rating(self, option):
        return service_list_movies(option,
                                   self.get_file_path())

    def search_movie_sorted_by_year(self, option):
        return service_list_movies(option,
                                   self.get_file_path())

    def search_filter_movies(self, minimum_rating, start_year, end_year):
        return service_filter_movies(minimum_rating, start_year,
                                     end_year, self.get_file_path())
