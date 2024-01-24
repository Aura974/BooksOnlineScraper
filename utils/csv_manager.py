from pathlib import Path
import csv


def get_upcs(csv_file):

    # Check if file is empty
    if not csv_file.exists() or csv_file.stat().st_size == 0:
        return set()

    # Get a set of all existing upcs
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return {row["universal_product_code"] for row in reader}


def create_csv(book):

    # Get category name
    category = book["category"]

    # Create the data folder and file paths
    data_folder = Path.cwd() / "data"
    csv_file = data_folder / f"{category}.csv"

    # Check if data folder exists
    data_folder.mkdir(exist_ok=True)

    # Load existing UPCs
    existing_upcs = get_upcs(csv_file)

    # Open the file in append mode only
    with open(csv_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=book.keys())

        # Write header if file is empty
        if not existing_upcs:
            writer.writeheader()

        # Write data only if upc not in file
        if book["universal_product_code"] not in existing_upcs:
            writer.writerow(book)
