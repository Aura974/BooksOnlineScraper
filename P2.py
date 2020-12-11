import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
base_url = "http://books.toscrape.com/"

def get_book_info(url):
	page = requests.get(URL)
	book = dict()
	review = []

	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find("table", class_="table table-striped")
	rows = table.select("tr")

	book["product_url"] = url
	book["universal_product_code"] = rows[0].td.text
	book["title"] = soup.ul.find_all("li")[-1].text
	book["price_including_tax"] = rows[3].td.text
	book["price_excluding_tax"] = rows[2].td.text
	book["number_available"] = rows[5].td.text	
	book["description"] = soup.find("article", "product_page").find_all("p", recursive=False)[0].text
	book["category"] = soup.ul.find_all("a")[-1].text

	review_rating = soup.find("article", "product_page").find("div", "row").find_all("p")
	for p in review_rating:
		p.get("class")
		review_rating = p.get("class")
	print(review_rating[1])

	image_url = soup.find("article", "product_page").img["src"]
	book["image_url"] = image_url.replace("../../", base_url)
	
	
	
	# print(universal_product_code)
	# print(description)
	# print(price_excluding_tax)
	# print(price_including_tax)
	# print(number_available)
	# print(price_excluding_tax)
	# print(price_including_tax)
	# print(number_available)
	return book


	