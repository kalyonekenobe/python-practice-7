import os

import pandas

from app.io.input import read_from_file, read_from_file_with_pandas


def test_read_from_file_success():
    test_file = "data/test_file.txt"
    content = "This is a test file."

    with open(test_file, 'w', encoding='utf-8') as file:
        file.write(content)

    result = read_from_file(test_file)
    assert result == content

    os.remove(test_file)

def test_read_from_file_file_not_found():
    result = read_from_file("data/non_existing_file.txt")
    assert result == "Error: File 'data/non_existing_file.txt' not found."


def test_read_from_file_empty_file():
    test_file = "data/empty_file.txt"
    with open(test_file, 'w', encoding='utf-8'):
        pass

    result = read_from_file(test_file)
    assert result == ""

    os.remove(test_file)


def test_read_from_file_with_pandas_success():
    test_file = "data/test_file.csv"
    content = "Name,Age\nAlice,30\nBob,25"

    with open(test_file, 'w', encoding='utf-8') as file:
        file.write(content)

    result = read_from_file_with_pandas(test_file)
    assert isinstance(result, pandas.DataFrame)
    assert result.shape[0] == 2

    os.remove(test_file)
