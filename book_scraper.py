import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://books.toscrape.com"


def get_book_data(url):

    with requests.Session() as session:
        # Create an empty dict to store data
        book = {}

        # Parse the html to retrieve data
        page = session.get(url)
        soup = bs(page.content, "html.parser")

        # table where are most of a book data
        table = soup.select("tr")

        # Retrieve and add data to the dict
        book["universal_product_code"] = table[0].td.text
        book["title"] = soup.find("h1").text
        book["price_excluding_tax"] = table[2].td.text
        book["price_including_tax"] = table[3].td.text
        book["number_available"] = table[5].td.text
        book["product_description"] = soup.find("article", "product_page").find("p", recursive=False).text
        book["category"] = soup.select("ul.breadcrumb li")[-2].text.strip()

        star_rating = soup.select_one("p.star-rating")["class"][1]
        ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        book["review_rating"] = ratings[star_rating]

        image_partial_url = soup.select_one(".carousel-inner").img["src"]
        book["image_url"] = BASE_URL + image_partial_url[5:]

    return book
