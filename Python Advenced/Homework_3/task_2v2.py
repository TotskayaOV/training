# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


import requests
from bs4 import BeautifulSoup
from collections import Counter

def parse_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # пример класса элемента, содержащего текст статьи
    article = soup.find('div', {'xmlns': 'http://www.w3.org/1999/xhtml'})
    if article:
        text = article.get_text()
        return text
    return ''


def remove_punctuation(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    without_punct = ""
    for char in text:
        if char not in punctuation:
            without_punct += char
    return without_punct


NUM_WORDS = 10

article_url = 'https://habr.com/p/558228/'
article_text = parse_article(article_url)
lower_text = article_text.lower()
pure_text = remove_punctuation(lower_text)
words_list = pure_text.split()
word_counts = Counter(word for word in words_list)
top_10 = word_counts.most_common(NUM_WORDS)

for elem in top_10:
    print(f'{elem[0]} - {elem[1]}')