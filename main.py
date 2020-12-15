import P2
import categories

URL = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
URL_category = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"

if __name__ == '__main__':
	book = P2.get_book_info(URL)
	P2.create_csv(book)
	categories.get_category_url(URL_category)



