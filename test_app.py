from app import NewsScraperApp
import unittest
import os
from unittest.mock import patch
import requests
from bs4 import BeautifulSoup


# https://news.yahoo.com/


"""Create test class"""
class TestApp(unittest.TestCase):
    def setUp(self):
        self.path = './app.py'
        self.app = NewsScraperApp('https://news.yahoo.com/')
    

    #Check if the app file exists
    def test_file_exists(self):
        assert os.path.isfile(self.path)


    #Test if input is a url
    def test_input_url(self):
        articles = self.app.get_general_news()

        self.assertTrue(articles)

    
    #Test if single news is a dictionary
    def test_single_news(self):
        response = requests.get('https://news.yahoo.com/')
        soup = BeautifulSoup(response.text, 'html.parser')
        news = self.app.data_parse(soup)
        result_instance = {}

        
        self.assertIs(type(result_instance), type(news[1]))


    #Test if news list is a list
    def test_news_list(self):
        response = requests.get('https://news.yahoo.com/')
        soup = BeautifulSoup(response.text, 'html.parser')
        news_list = self.app.data_parse(soup)
        results = []

        
        self.assertIs(type(results), type(news_list[0]))


if __name__ == '__main__':
    unittest.main()
