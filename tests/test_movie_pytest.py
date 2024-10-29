import pytest

from movie.movie_services import movie_service
from movie.utility import constant

"""
Test Module for Movie Services

This module contains unit tests for the movie management functionality
implemented in the `movie_service` module. It uses the pytest framework
to verify that various operations related to movie data are performed
correctly.

The following functionalities are tested:
- Adding a movie to the database
- Updating an existing movie's rating
- Deleting a movie from the database
- Listing all movies
- Sorting movies by rating and year
- Filtering movies based on specified criteria
- Searching for movies by title
- Generating random movie selections
- Calculating statistics such as average and median ratings

Usage:

Run the tests using the pytest command in the terminal:
    $ pytest
"""

movie = {
    "Titanic": {
        "rating": 7.9,
        "year": 1997
    },
    "Spider Man": {
        "rating": 9.0,
        "year": 2009
    },
    "Finding Forrester": {
        "rating": 8.1,
        "year": 2025
    }
}

movie_sort_rating = {
    "Spider Man": {
        "rating": 9.0,
        "year": 2009
    },
    "Finding Forrester": {
        "rating": 8.1,
        "year": 2025
    },
    "Titanic": {
        "rating": 7.9,
        "year": 1997
    }
}

movie_sort_year = {
    "Finding Forrester": {
        "rating": 8.1,
        "year": 2025
    },
    "Spider Man": {
        "rating": 9.0,
        "year": 2009
    },
    "Titanic": {
        "rating": 7.9,
        "year": 1997
    }
}

filter_movie = [{'Titanic': {'rating': 7.9, 'year': 1997}},
                {'Spider Man': {'rating': 9.1, 'year': 2009}}]


@pytest.fixture()
def resource():
    print("\nsetUp..................................")
    yield "resource"
    print("\ntearDown...............................")


class TestMovie:

    # 2. Add movie      *********************************

    @pytest.mark.parametrize("title, year, rating, expected_output",
                             [
                                 ("Movie Jerome", 2025, 9.9, True),
                                 ("Movie Savanna", 2017, 9.9, True),
                                 ("Finding Jerome", 2017, 9.9, True)
                             ]
                             )
    def test_add_movie(self, title, year, rating, expected_output, resource):
        result = movie_service.service_add_movie(title, year, rating,
                                                 constant.TEST_FILE_PATH)
        assert result["result"] == expected_output

    # 4. Update movie   *********************************

    @pytest.mark.parametrize("title, rating, expected_output",
                             [
                                 ("Movie Jerome", 9.1, True),
                                 ("Movie Savanna", 9.1, True)
                             ]
                             )
    def test_update_movie(self, title, rating, expected_output, resource):
        result = movie_service.service_update_movie(title, rating,
                                                    constant.TEST_FILE_PATH)

        assert result["rating"] == rating
        assert result["result"] == expected_output

    # 5. Stats          *********************************

    def test_stats_movies(self, resource):
        result = movie_service.service_stat_movies(constant.TEST_FILE_PATH)
        assert result[constant.PAYLOAD][0] == 8.85
        assert result[constant.PAYLOAD][1] == 9.05

    # 6. Random movie   *********************************

    def test_random_movie(self, resource):
        result = movie_service.service_random_movie(constant.TEST_FILE_PATH)

        result_list = movie_service.service_list_movies("",
                                                        constant.TEST_FILE_PATH)

        assert any(
            [True
             if list(result[constant.PAYLOAD])[0] == key
             else False
             for key, value in result_list[constant.PAYLOAD].items()])

    # 7. Search movie   *********************************

    @pytest.mark.parametrize("to_search",
                             [
                                 "mov",
                                 "JER"
                             ]
                             )
    def test_search_movies(self, to_search, resource):
        result = movie_service.service_find_movie(False, to_search,
                                                  constant.TEST_FILE_PATH)
        assert len(result[constant.PAYLOAD]) == 2

    # 3. Delete movie   *********************************

    @pytest.mark.parametrize("title, expected_output",
                             [
                                 ("Movie Jerome", True),
                                 ("Movie Savanna", True),
                                 ("Finding Jerome", True)
                             ]
                             )
    def test_delete_movie(self, title, expected_output, resource):
        result = movie_service.service_delete_movie(title,
                                                    constant.TEST_FILE_PATH)
        assert result["result"] == expected_output

    # 1. List movies    *********************************

    def test_list_movies(self, resource):
        result = movie_service.service_list_movies("",
                                                   constant.TEST_FILE_PATH)

        assert result[constant.PAYLOAD] == movie

    # 8. Movies sorted by rating    *********************************

    def test_sorted_movies_rating(self, resource):
        result = movie_service.service_list_movies(constant.RATING_KEY,
                                                   constant.TEST_FILE_PATH)

        assert result[constant.PAYLOAD] == movie_sort_rating

    # 9. Movies sorted by year    *********************************

    def test_sorted_movies_year(self, resource):
        result = movie_service.service_list_movies(constant.YEAR_KEY,
                                                   constant.TEST_FILE_PATH)

        assert result[constant.PAYLOAD] == movie_sort_year

    # 10. Filter movies    *********************************

    def test_filter_movies(self, resource):
        minimum_rating = 0
        start_year = 1990
        end_year = 2024

        result = movie_service.service_filter_movies(minimum_rating,
                                                     start_year,
                                                     end_year,
                                                     constant.TEST_FILE_PATH)

        assert result[constant.PAYLOAD] == filter_movie
