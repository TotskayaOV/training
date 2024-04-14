import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
from time import sleep


URL = "https://books.toscrape.com/"
BASE_URL = "https://books.toscrape.com/catalogue/"
url = URL
book_info = {}
book_info_list = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    next_page_link = soup.find('li', ('class', 'next'))

    #получаем все ссылки на страницы с книгами с текущей страницы
    parse_links = []
    for link in soup.find_all("article", {"class",  "product_pod"}):
        link_a = link.find("h3").find("a")
        if link_a:
            parse_links.append(link_a.get("href"))
    for link in parse_links:
        if 'catalogue' in link:
            url = urllib.parse.urljoin(URL, link)
        else:
            url = urllib.parse.urljoin(BASE_URL, link)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        #Парсим название книги
        book_name = soup.find('div', ('class', 'col-sm-6 product_main')).find("h1").text
        # Парсим цену
        price = soup.find('p', ('class', 'price_color')).text.strip()[1::]
        try:
            price = float(price)
        except:
            print(f'Error: {price}')
        # Парсим остаток
        count_book = soup.find('p', ('class', 'instock availability')).text.strip()
        try:
            count_book = count_book.replace("In stock (", "").replace(" available)", "").strip()
            count_book = int(count_book)
        except:
            print(f'Errore {book_name}: {count_book}')
        # Парсим описание
        description = soup.find("meta", attrs={"name": "description"})["content"].strip()
        book_info = {"book_name": book_name, "price": price, "stock": count_book, "description": description,
                     "book_url": url}
        book_info_list.append(book_info)

    # проверка перехода на следующую страницу
    if not next_page_link:
        break
    next_page_link = next_page_link.find("a").get("href")
    if 'catalogue' in next_page_link:
        url = urllib.parse.urljoin(URL,  next_page_link)
    else:
        url = urllib.parse.urljoin(BASE_URL, next_page_link)
    sleep(10)

with open('box_info.json', 'w', encoding='utf-8') as f:
    json.dump(book_info_list, f, indent=4)

print('Done')
