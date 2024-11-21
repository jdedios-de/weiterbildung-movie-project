from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, notes, imdbid):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass

    @abstractmethod
    def find_movie(self, title):
        pass

    @abstractmethod
    def stats_movie(self):
        pass

    @abstractmethod
    def random_movie(self):
        pass

    @abstractmethod
    def search_movie(self, title):
        pass

    @abstractmethod
    def search_movie_sorted_by_rating(self, option):
        pass

    @abstractmethod
    def search_movie_sorted_by_year(self, option):
        pass

    @abstractmethod
    def search_filter_movies(self, minimum_rating, start_year, end_year):
        pass
