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

