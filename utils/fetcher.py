from bs4 import BeautifulSoup as bs


def fetch_and_parse(url, session):
    page = session.get(url)
    return bs(page.content, "html.parser")
