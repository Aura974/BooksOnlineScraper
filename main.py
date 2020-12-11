import TestAurore
import category

URL = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"

if __name__ == '__main__':
	book = TestAurore.get_book_info(URL)
	