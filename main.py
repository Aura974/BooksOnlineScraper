import requests
import scrapers.book_scraper as bk
import scrapers.category_scraper as cat
import utils.csv_manager as csvmng


if __name__ == "__main__":

    with requests.Session() as session:

        # Get the categories
        categories = cat.get_categories(session)

        # Loop over each category
        for cat_url in categories:
            # and get all the books' urls
            category_urls = cat.get_category_urls(cat_url, session)

            # Write all the books of one category in the csv file
            for url in category_urls:
                book = bk.get_book_data(url, session)
                csvmng.create_csv(book)
