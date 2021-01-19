import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/"


def url_category(base_url):
    """Get all the categories' urls from the homepage."""
    page = requests.get(base_url)
    url_category = []

    soup = BeautifulSoup(page.text, "html.parser")
    category = soup.find("aside").find_all("a")

    for cat in category:
        link = cat.get("href")
        url_category.append(base_url + link)
    del url_category[0]
    return url_category


def nb_of_pages(url_category):
    """
    Gives the number of pages for each category.

    That function get the total number of books in one category.
    As there are only 20 books displayed per page, the function checks
    how many times you can have 20 in the total number of books,
    and return that result.
    """
    nb_of_pages = []
    page = requests.get(url_category)
    soup = BeautifulSoup(page.text, "html.parser")
    nb_of_books = int(soup.find_all("strong")[1].text)
    for i in range(0, nb_of_books, 20):
        nb_of_pages.append(i)
    nb_of_pages = len(nb_of_pages)
    return nb_of_pages


def get_category_url(url_category):
    """Gets every books' urls in one given category."""
    category = []
    pattern = url_category.replace("index.html", "")
    for i in range(nb_of_pages(url_category)):
        page = requests.get(url_category)
        if page.ok:
            soup = BeautifulSoup(page.text, "html.parser")
            lists = soup.find_all("article", "product_pod")

            for li in lists:
                a = li.find("a")
                link = a["href"]
                link = link.replace("../../..", "catalogue")
                category.append(base_url + link)

            try:
                soup = BeautifulSoup(page.text, "html.parser")
                next_page = soup.find("li", "next").a["href"]
                url_category = pattern + next_page
                # Here we check if the next page exists.

            except Exception:
                break
    return category
