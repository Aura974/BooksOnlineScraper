import requests
import scrapers.book_scraper as bk
import scrapers.category_scraper as cat
import utils.csv_manager as csvmng
import utils.image_handler as img
from tqdm import tqdm


if __name__ == "__main__":

    try:
        with requests.Session() as session:

            # Get the categories
            categories = cat.get_categories(session)

            # Loop over each category
            for cat_url in categories:

                # extract category name
                category_name = cat_url.split("/")[-2].split("_")[0].title()
                print(f"\n\nProcessing category: {category_name}")

                # and get all the books' urls
                category_urls = cat.get_category_urls(cat_url, session)

                total_books = len(category_urls)
                print(f"Total books in {category_name}: {total_books}\n")

                # Write all the books of one category in the csv file and download images
                for url in tqdm(
                        category_urls,
                        desc=f"Downloading {category_name}",
                        unit="book",
                        colour="#005b5b",
                        total=total_books
                        ):
                    book = bk.get_book_data(url, session)
                    csvmng.create_csv(book)
                    img.download_image(book)

    except KeyboardInterrupt:
        print("\nScraping interrupted by user. Exiting...")
