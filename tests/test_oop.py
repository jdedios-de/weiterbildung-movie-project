from movie.storage.storage_csv import StorageCsv
from movie.storage.storage_json import StorageJson
from movie.utility import constant


def test_oop_json():
    json_storage = StorageJson(constant.JSON_PRODUCTION_FILE_PATH)
    print(json_storage.list_movies())
    assert True

def test_oop_csv():
    csv_storage = StorageCsv(constant.CSV_PRODUCTION_FILE_PATH)
    print(csv_storage.list_movies())
    assert True
