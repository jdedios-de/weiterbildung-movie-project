import pytest

from movie.movie_services import movie_service
from movie.utility import constant

movie = {
    "Titanic": {
        "rating": 7.9,
        "year": 1997
    }
}


@pytest.fixture()
def resource():
    print("\nsetUp..................................")
    yield "resource"
    print("\ntearDown...............................")


class TestMovie:

    @pytest.mark.parametrize("title, year, rating, expected_output",
                             [
                                 ("Movie Jerome", 2024, 9.9, True),
                                 ("Movie Savanna", 2017, 9.9, True)
                             ]
                             )
    def test_add_movie(self, title, year, rating, expected_output, resource):
        result = movie_service.service_add_movie(title, year, rating,
                                                 constant.TEST_FILE_PATH)
        assert result["result"] == expected_output

    @pytest.mark.parametrize("title, expected_output",
                             [
                                 ("Movie Jerome", True),
                                 ("Movie Savanna", True)
                             ]
                             )
    def test_delete_movie(self, title, expected_output, resource):
        result = movie_service.service_delete_movie(title,
                                                    constant.TEST_FILE_PATH)
        assert result["result"] == expected_output

    def test_list_movies(self, resource):
        result = movie_service.service_list_movies(constant.TEST_FILE_PATH)
        assert result == movie
