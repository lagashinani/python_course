import requests
from bs4 import BeautifulSoup
import re
import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'гравитация', 'Lenovo', 'Java']
URL = 'https://habr.com/ru/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' + \
                         'Chrome/86.0.4240.111 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;' + \
                     'q=0.8,application/signed-exchange;v=b3;q=0.9'}

search_list = '(' + '|'.join(KEYWORDS) + ')'


def find_embedded_text(tag):
    """Возвращает Boolean gj условию нахождкения нужного тега"""
    if tag.name == 'li' and 'content-list__item_post' in tag['class']:
        return True if re.search(search_list, tag.text) else False
    return False


html = False
try:
    html = requests.get(URL, headers=HEADERS, timeout=10)
except Exception as e:
    print('Ошибка requests: \n', e)
    exit(0)

if not html or html.status_code != 200:
    print('При загрузке страницы возникла ошибка')
    exit(0)

soup = BeautifulSoup(html.text, 'html.parser')

posts_li = soup.find_all(find_embedded_text)

for post in posts_li:
    post_date = post.find('span', class_='post__time').text
    post_title = post.article.h2.a.text
    post_link = post.article.h2.a['href']
    print(f'{post_date} - {post_title} - {post_link}')
