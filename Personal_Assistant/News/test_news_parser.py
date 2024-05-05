from news_parser import parse_news
import unittest

class TestNewsParser(unittest.TestCase):
    
    def test_parse_news(self):
        # Переконайтеся, що парсер новин повертає список новин, а не None
        news_list = parse_news()
        self.assertIsNotNone(news_list, "Парсер повернув пустий список")

        # Перевірте, що список новин не є пустим
        self.assertTrue(len(news_list) > 0, "Парсер повернув пустий список")

        # Перевірте, що кожна новина в списку має непорожні заголовок і посилання
        for news in news_list:
            self.assertIsNotNone(news['title'], "Новина має пустий заголовок")
            self.assertIsNotNone(news['link'], "Новина має пусте посилання")

if __name__ == '__main__':
    unittest.main()

