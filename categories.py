import requests
from bs4 import BeautifulSoup

URL_category = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
base_url = "http://books.toscrape.com/"

def get_category_url(URL_category):
    category = []
    page = requests.get(URL_category)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all("article", "product_pod")
    
    for li in lists:
        a = li.find("a")
        link = a["href"]
        link = link.replace("../../..", "catalogue")
        category.append(base_url + link)
    
    print(len(category))
    
    print(category)
   
