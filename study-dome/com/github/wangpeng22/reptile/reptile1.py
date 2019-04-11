import requests
from bs4 import BeautifulSoup

base_url = 'https://book.douban.com/j/home/ebooks?user_id='

articles = []
data_list = []

r = requests.get(base_url)

html = r.text

print(html)