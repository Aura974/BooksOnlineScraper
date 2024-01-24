from utils.fetcher import fetch_and_parse as fp

BASE_URL = "https://books.toscrape.com/"


def get_category_urls(url, session):

    # set the category_url to current url
    category_url, categories = url, []

    while category_url:
        # Parse the html to retrieve data
        soup = fp(category_url, session)

        # Retrieve the urls, reconstruct them and add to list
        base_url = BASE_URL + "catalogue"
        categories.extend([base_url + part.get("href")[8:] for part in soup.select("h3 a")])

        # Find the next page link
        next_page = soup.select_one("li.next a")

        # Update category_url accordingly
        if next_page:
            category_url = f"{url.rsplit("/", 1)[0]}/{next_page.get("href")}"
        else:
            category_url = None

    return categories


def get_categories(session):

    # fetch and parse html
    soup = fp(BASE_URL, session)

    return [BASE_URL + cat_url.get("href") for cat_url in soup.select("ul.nav ul li a")]
