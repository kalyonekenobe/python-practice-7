def write_to_console(text):
    """
    Prints the given text to the console.

    This function takes a string as input and prints it to the standard output (console).
    It supports multi-line text and special characters.

    Args:
        text (str): The text to be displayed in the console.

    Returns:
        None

    Example:
        >>> write_to_console("Hello, world!")
        Hello, world!

        >>> write_to_console("Line 1\\nLine 2")
        Line 1
        Line 2

    Notes:
        - This function does not return any value; it only prints the output.
        - To redirect output to a file instead of the console, use `write_to_file()`.
    """
    print(text)

def write_to_file(filepath, text):
    """
    Writes the given text to a file using built-in Python methods.

    This function opens the specified file in write mode (`'w'`), writes the provided text,
    and closes the file. If the file does not exist, it will be created.
    If the file already exists, its contents will be overwritten.

    Args:
        filepath (str): The path to the file where the text will be written.
        text (str): The text content to be written to the file.

    Returns:
        None

    Raises:
        IOError: If an I/O error occurs while writing to the file, such as permission issues.

    Example:
        >>> write_to_file("output.txt", "Some text")
        (Creates a file named "output.txt" with the specified content)

    Notes:
        - If the file is large, consider writing data in chunks instead of a single operation.
        - If you need to append to an existing file instead of overwriting, use mode `'a'` instead of `'w'`.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
    except IOError as e:
        print(f"Error writing to file '{filepath}': {e}")