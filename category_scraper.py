import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://books.toscrape.com"


def get_category_urls(url):

    # set the category_url to current url
    category_url, categories = url, []

    while category_url:
        # Parse the html to retrieve data
        page = requests.get(category_url)
        soup = bs(page.content, "html.parser")

        # Retrieve the truncated urls
        partial_urls = [a["href"] for a in soup.select("h3 a")]

        # Reconstruct the urls and add to list
        categories.extend([BASE_URL + "/catalogue" + part[8:] for part in partial_urls])

        # Find the next page link
        next_page = soup.select_one("li.next a")

        # Update category_url accordingly
        if next_page:
            category_url = url.replace("index", next_page["href"][:-5])
        else:
            category_url = None

    return categories
