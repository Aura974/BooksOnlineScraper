import requests
from pathlib import Path


def download_image(book):

    # Get category, upc and url from book
    category, upc, image_url = book["category"], book["universal_product_code"], book["image_url"]

    # Use the existing category folder
    image_folder = Path.cwd() / "data" / category

    # Get filename from upc and extension
    image_ext = image_url.split(".")[-1]
    image_file = image_folder / f"{upc}.{image_ext}"

    # Download and save the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_file, "wb") as file:
            file.write(response.content)
