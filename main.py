import book_info as bkinfo
import categories as cat
from tqdm import tqdm  # the tqdm module displays a progress bar.

base_url = "http://books.toscrape.com/"

if __name__ == "__main__":

    url_category = cat.url_category(base_url)
    for url in tqdm(url_category):
        book_category = cat.get_category_url(url)

        for book in book_category:
            book = bkinfo.get_book_info(book)
            bkinfo.create_csv(book)
            bkinfo.images(book)
