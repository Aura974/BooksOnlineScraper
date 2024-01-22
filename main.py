import requests
from bs4 import BeautifulSoup as bs

url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"
BASE_URL = "https://books.toscrape.com"

page = requests.get(url)

soup = bs(page.content, "html.parser")
rows = soup.select("tr")

universal_product_code = rows[0].td.text
title = soup.find("h1").text
price_excluding_tax = rows[2].td.text
price_including_tax = rows[3].td.text
number_available = rows[5].td.text
product_description = soup.find("article", "product_page").find("p", recursive=False).text
category = soup.select("ul.breadcrumb li")[-2].text.strip()

star_rating = soup.select_one("p.star-rating")["class"][1]
ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
review_rating = ratings[star_rating]

image_partial_url = soup.select_one(".carousel-inner").img["src"]
image_url = BASE_URL + image_partial_url[5:]

print(universal_product_code)
print(title)
print(price_excluding_tax)
print(price_including_tax)
print(number_available)
print(product_description)
print(category)
print(review_rating)
print(image_url)
