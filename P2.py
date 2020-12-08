import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find("table", class_="table table-striped")
rows = table.select("tr")

for row in rows:
    universal_product_code = rows[0].td.text
    price_excluding_tax = rows[2].td.text
    price_including_tax = rows[3].td.text
    number_available = rows[5].td.text
    print(universal_product_code)
    print(price_excluding_tax)
    print(price_including_tax)
    print(number_available)


