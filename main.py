import book_scraper as bk
import csv_manager as csvmng
import category_scraper as cat


url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

if __name__ == "__main__":

    # book = bk.get_book_data(url)
    # csvmng.create_csv(book)

    print(cat.get_category_urls(url))
