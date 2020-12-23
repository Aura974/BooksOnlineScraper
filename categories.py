import requests
from bs4 import BeautifulSoup

url_category = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'
base_url = 'http://books.toscrape.com/'

def nb_of_pages(url_category):
    nb_of_pages = []
    page = requests.get(url_category)
    soup = BeautifulSoup(page.text, 'html.parser')
    nb_of_books = int(soup.find_all('strong')[1].text)
    for i in range(0, nb_of_books, 20):
        nb_of_pages.append(i)
    nb_of_pages = (len(nb_of_pages))
    return nb_of_pages
    
    

def get_category_url(url_category):
    category = []
    pattern = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/'
    url_category = url_category.replace('index', 'page-1')
    for i in range(nb_of_pages(url_category)):
        page = requests.get(url_category)
        if page.ok:
            soup = BeautifulSoup(page.text, 'html.parser')
            lists = soup.find_all('article', 'product_pod')
            
            for li in lists:
                a = li.find('a')
                link = a['href']
                link = link.replace('../../..', 'catalogue')
                category.append(base_url + link)

            try:
                soup = BeautifulSoup(page.text, 'html.parser')
                next_page = soup.find('li', 'next').a['href']
                url_category = pattern + next_page
                
            except:
                break
    print(len(category))
   
