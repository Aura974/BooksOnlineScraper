import book_scraper as bk
import csv_manager as csvmng
import category_scraper as cat


url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

if __name__ == "__main__":

    category_urls = cat.get_category_urls(url)

    books = [bk.get_book_data(url) for url in category_urls]
    csvmng.create_csv(books)
