import requests
from bs4 import BeautifulSoup

def parse_news():
    url = "https://www.pravda.com.ua/articles/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Знаходимо елемент з текстом "Усі публікації"
        container_title = soup.find('div', class_='container_title', text='Усі публікації')

        # Знаходимо батьківський контейнер для цього елемента
        if container_title:
            news_container = container_title.find_parent()

            # Знаходимо всі елементи з класом 'article_list' всередині батьківського контейнера
            news_elements = news_container.find_all('div', class_='article_list')

            news_list = []

            # Перебираємо кожен елемент новини і додаємо його в список новин
            for news_element in news_elements:
                image = news_element.find('img')['src']
                title = news_element.find('h3').text.strip()
                content = news_element.find('div', class_='article_subheader').text.strip()
                author = news_element.find('div', class_='article_author').text.strip()
                link = news_element.find('a')['href']
                news_list.append({'image': image, 'title': title, 'content': content, 'author': author, 'link': link})

            return news_list
        else:
            print("Container title not found.")
            return None
    else:
        print("Failed to retrieve news.")
        return None
