from app.io.input import read_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import write_to_console, write_to_file


def main():
    console_text = read_from_console()

    file_text = read_from_file("data/input.txt")

    try:
        pandas_text = read_from_file_with_pandas("data/data.csv").to_string()
    except Exception as e:
        pandas_text = f"Error reading CSV file: {e}"

    write_to_console("Console Input:\n" + console_text)
    write_to_console("\nFile Content:\n" + file_text)
    write_to_console("\nPandas File Content:\n" + pandas_text)

    output_data = f"Console Input:\n{console_text}\n\nFile Content:\n{file_text}\n\nPandas File Content:\n{pandas_text}"
    write_to_file("data/output.txt", output_data)


if __name__ == '__main__':
    main()
