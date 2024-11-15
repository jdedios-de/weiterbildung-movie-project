from movie.movie_services.storage_json import StorageJson
from movie.utility import constant


def test_oop():
    storage = StorageJson(constant.PRODUCTION_FILE_PATH)
    print(storage.list_movies())
    assert True
