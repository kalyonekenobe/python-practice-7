import pandas


def read_from_console():
    """
    Reads a line of text input from the console.

    This function prompts the user to enter a line of text and captures the input.
    The input is returned as a string, including spaces and special characters.
    If the user provides an empty input, an empty string is returned.

    Returns:
        str: The text entered by the user.

    Example:
        >>> text = read_from_console()
        (User enters: "Hello, world!")
        >>> print(text)
        'Hello, world!'
    """
    return input("Enter text: ")

def read_from_file(filepath):
    """
    Reads the content of a text file using built-in Python methods.

    This function opens the specified file in read mode (`'r'`), reads its entire content,
    and returns it as a string. The file should be encoded in UTF-8 to avoid decoding issues.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If an I/O error occurs while reading the file, such as permission issues.

    Example:
        >>> content = read_from_file("example.txt")
        >>> print(content)
        'This is an example file.\\nIt has multiple lines.'

    Notes:
        - This function assumes that the file is a plain text file.
        - If the file is too large, reading it all at once may cause high memory usage.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except IOError as e:
        return f"Error reading file '{filepath}': {e}"

def read_from_file_with_pandas(filepath):
    """
    Reads the content of a text file using the pandas library.

    This function uses `pandas.read_csv()` to read the file into a DataFrame.
    It assumes that the file is a structured text file (e.g., CSV or TSV).
    If the file contains a delimiter-separated structure, it will be parsed accordingly.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: The contents of the file as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pandas.errors.EmptyDataError: If the file is empty.
        pandas.errors.ParserError: If the file contains parsing errors (e.g., malformed CSV structure).
        IOError: If an I/O error occurs while accessing the file.

    Example:
        >>> df = read_from_file_with_pandas("data.csv")
        >>> print(df)
           Name    Age
        0  Alice   25
        1  Bob     30

    Notes:
        - This function is best suited for structured text files like CSV or TSV.
        - For plain text files without a structured format, use `read_from_file()`.
    """
    try:
        df = pandas.read_csv(filepath)
        return df
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except pandas.errors.EmptyDataError:
        return f"Error: File '{filepath}' is empty."
    except pandas.errors.ParserError:
        return f"Error: Could not parse file '{filepath}'."