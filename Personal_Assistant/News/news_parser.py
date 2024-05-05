# news_parser.py
from bs4 import BeautifulSoup
import requests

def parse_news():
    url = 'https://www.unian.net'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_list = []
    for news_item in soup.find_all('div', class_='news-item'):
        title = news_item.find('h2').text.strip()
        content = news_item.find('p').text.strip()
        news_list.append({'title': title, 'content': content})
    
    return news_list
