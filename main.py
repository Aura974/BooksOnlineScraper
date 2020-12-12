import P2


URL = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"

if __name__ == '__main__':
	book = P2.get_book_info(URL)
	P2.create_csv(book)



