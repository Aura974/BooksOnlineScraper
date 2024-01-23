import book_scraper as bk
import csv_manager as csvmng


url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"

if __name__ == "__main__":

    book = bk.get_book_data(url)
    csvmng.create_csv(book)
