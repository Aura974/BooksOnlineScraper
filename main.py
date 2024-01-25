import requests
import scrapers.book_scraper as bk
import scrapers.category_scraper as cat
import utils.csv_manager as csvmng
import utils.image_handler as img


if __name__ == "__main__":

    with requests.Session() as session:

        # Get the categories
        categories = cat.get_categories(session)

        # Loop over each category
        for cat_url in categories:
            # and get all the books' urls
            category_urls = cat.get_category_urls(cat_url, session)

            # Write all the books of one category in the csv file and download images
            for url in category_urls:
                book = bk.get_book_data(url, session)
                csvmng.create_csv(book)
                img.download_image(book)
