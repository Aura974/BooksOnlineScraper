import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://books.toscrape.com"


def get_category_urls(url):

    # Use Session() to reuse the same connection
    with requests.Session() as session:
        # set the category_url to current url
        category_url, categories = url, []

        while category_url:
            # Parse the html to retrieve data
            page = session.get(category_url)
            soup = bs(page.content, "html.parser")

            # Retrieve the urls, reconstruct them and add to list
            base_url = BASE_URL + "/catalogue"
            categories.extend([base_url + part.get("href")[8:] for part in soup.select("h3 a")])

            # Find the next page link
            next_page = soup.select_one("li.next a")

            # Update category_url accordingly
            if next_page:
                category_url = f"{url.rsplit("/", 1)[0]}/{next_page["href"]}"
            else:
                category_url = None

    return categories
