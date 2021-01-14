import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path

base_url = 'http://books.toscrape.com/'
path = Path.cwd()
home = Path.home()

def get_book_info(url):
	page = requests.get(url)
	book = dict()

	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find('table', class_='table table-striped')
	rows = table.select('tr')

	book['product_url'] = url
	book['universal_product_code'] = rows[0].td.text
	book['title'] = soup.ul.find_all('li')[-1].text
	book['price_including_tax'] = rows[3].td.text
	book['price_excluding_tax'] = rows[2].td.text
	book['number_available'] = rows[5].td.text	
	
	
	
	try:
		description = soup.find('article', 'product_page').find_all('p', recursive=False)[0].text 
		book['description'] = description
	except:
		book['description'] = "None"
	
	
	book['category'] = soup.ul.find_all('a')[-1].text

	review_rating = soup.find('p', {'class': 'star-rating'})['class']
	ratings_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
	book['review_rating'] = str(ratings_dict[review_rating[1]])

	image_url = soup.find('article', 'product_page').img['src']
	book['image_url'] = image_url.replace('../../', base_url)

	return book

def create_csv(book):
	category = book['category']
	Path(path, 'data').mkdir(exist_ok=True)
	Path(path, 'data', category).mkdir(exist_ok=True)
	file = f'{category}.csv' 
	csv_file = Path(path, 'data', category, file)
	with csv_file.open('a+', newline = '', encoding='utf-8') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=book.keys())

		if csv_file.stat().st_size == 0:
			writer.writeheader()

		writer.writerow(book)