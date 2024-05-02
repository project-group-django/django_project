import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def parse_news():
    url = "https://www.pravda.com.ua/articles/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        container_title = soup.find('div', class_='container_title', text='Усі публікації')

        if container_title:
            news_container = container_title.find_parent()

            news_elements = news_container.find_all('div', class_='article_list')

            news_list = []
            
            months = {'січня': 1, 'лютого': 2, 'березня': 3, 'квітня': 4, 'травня': 5, 'червня': 6, 'липня': 7, 'серпня': 8, 'вересня': 9, 'жовтня': 10, 'листопада': 11, 'грудня': 12}
            
            today = datetime.now().strftime("%d %B %Y").lower()
            
            for news_element in news_elements:
                date_time_str = news_element.find('div', class_='article_author').text.strip()
                match = re.search(r'(\d+) (\w+) (\d+),', date_time_str)
                day, month_str, year = match.groups()
                month = months[month_str.lower()]
                
                date_str = f"{day} {month} {year}"
                news_date = datetime.strptime(date_str, '%d %m %Y')
                
                if (news_date.date() == (datetime.now() - timedelta(days=1)).date()) or (news_date.date() == datetime.now().date()):
                    image = news_element.find('img')['src']
                    title = news_element.find('h3').text.strip()
                    content = news_element.find('div', class_='article_subheader').text.strip()
                    author = re.search(r'— ([^—]+) —', date_time_str).group(1).strip()
                    link = news_element.find('a')['href']
                    news_list.append({'image': image, 'title': title, 'content': content, 'author': author, 'link': link})

            return news_list
        else:
            print("Container title not found.")
            return None
    else:
        print("Failed to retrieve news.")
        return None
