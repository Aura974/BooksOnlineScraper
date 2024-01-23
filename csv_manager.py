from pathlib import Path
import csv


def create_csv(book):

    # Store upc code
    upc = book["universal_product_code"]

    # Create the data folder and file paths
    data_folder = Path.cwd() / "data"
    csv_file = data_folder / "books_data.csv"

    # Check if data folder exists
    data_folder.mkdir(exist_ok=True)

    # Open the file in a+ mode
    with open(csv_file, "a+", newline="", encoding="utf-8") as file:

        # Move to the beginning of the file
        file.seek(0)

        # Read the file
        reader = csv.DictReader(file)
        writer = csv.DictWriter(file, fieldnames=book.keys())

        # Check if file is empty
        if not reader.fieldnames:
            # and write header
            writer.writeheader()

        # Check if upc in file
        if upc not in [row["universal_product_code"] for row in reader]:
            # Move to the end of the file
            file.seek(0, 2)
            # and write data
            writer.writerow(book)
