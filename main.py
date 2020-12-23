import book_info
import categories

url_category = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'

if __name__ == '__main__':
		
	url_category = categories.get_category_url(url_category)

	for url in url_category:
		book = book_info.get_book_info(url)
		book_info.create_csv(book)




	


