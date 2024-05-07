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
                author_publication_split = date_time_str.split('—')
                if len(author_publication_split) > 1:
                    author = author_publication_split[-1].strip()
                    publication = author_publication_split[-2].strip()
                else:
                    author = None
                    publication = None

                if author:
                    if ',' in author:
                        author_parts = [part.strip() for part in author.split(',')]
                        author_name_parts = []
                        for index, part in enumerate(author_parts):
                            if len(part) <= 7:
                                author_name_parts.append(part)
                            else:
                                if len(part) <= 2 and part[:-1].isdigit() and index < len(author_parts) - 1:
                                    author_name_parts.append(part)
                                else:
                                    author_name_parts.append(' '.join(word.capitalize() for word in part.split()))
                        author_name = ', '.join(author_name_parts)
                    else:
                        author_name = ' '.join(word.capitalize() for word in author.split())
                else:
                    author_name = None

                match = re.search(r'(\d+) (\w+) (\d+),', date_time_str)
                day, month_str, year = match.groups()
                month = months[month_str.lower()]
                
                date_str = f"{day} {month} {year}"
                news_date = datetime.strptime(date_str, '%d %m %Y')
                
                if (news_date.date() == (datetime.now() - timedelta(days=1)).date()) or (news_date.date() == datetime.now().date()):
                    image = news_element.find('img')['src']
                    title = news_element.find('h3').text.strip()
                    content = news_element.find('div', class_='article_subheader').text.strip()
                    link = news_element.find('a')['href']
                    news_list.append({'image': image, 'title': title, 'content': content, 'author': author_name, 'publication': publication, 'link': link})
                
            return news_list
        else:
            print("Назва контейнера не знайдена.")
            return None
    else:
        print("Не вдалося отримати новини.")
        return None

parse_news()
