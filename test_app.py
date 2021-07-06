# from app import NewsScraperApp
# import unittest
# import os
# from unittest.mock import patch


# """Create test class"""
# class TestApp(unittest.TestCase):
#     def setUp(self):
#         self.path = './app.py'
#         self.app = NewsScraperApp('https://news.search.yahoo.com/', 'iphone 12')
    

#     """Check if the app file exists"""
#     def test_filrExists(self):
#         assert os.path.isfile(self.path)


#     """Test if input is a url"""
#     def test_inputUrl(self):
#         user_input = 'https://search.yahoo.com/search?p=iphone+12+leaked&fr=yfp-t&ei=UTF-8&fp=1'

#         with patch('builtins.input', side_effect=user_input):
#             articles = NewsScraperApp.get_general_news()

#         self.assertTrue(articles)


#     """Test if the url input is an number instead of a string"""
#     def test_inputNumber(self):
#         self.user_input = 2

#         with patch('builtins.input', side_effect=self.user_input):

#             articles = NewsScraperApp.get_general_news()
        
#         self.assertFalse(articles)

    
#     """Test if input is a topic is a number instead of a string"""
#     def test_topic(self):
#         user_input = 12

#         with patch('builtins.input', side_effect=user_input):

#             articles = NewsScraperApp.get_specific_news(self)

#         self.assertFalse(articles)


#     """Test if the card details are generated """



# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.case import TestCase
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests.api import get
from app import *

url = 'https://news.yahoo.com/science/'
res = requests.get(url).text
soup = BeautifulSoup(res, 'html5lib')

class test_scaper(TestCase):

    #testing when the user enters an empty string as a url
    # def test_blank_url(self):
    #     def is_url(url):
    #         try:
    #             result = urlparse(url)
    #             return all([result.scheme, result.netloc])
    #         except ValueError:
    #              return False
    #     self.assertFalse(is_url(''))


    #testing when the user enters an invalid string as a url
    def test_invalid_url(self):
        def is_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except ValueError:
                 return False
        self.assertFalse(is_url('hello'))
    
    
    #testing when a valid url is entered
    def test_valid_url(self):
        def is_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except ValueError:
                 return False
        self.assertTrue(is_url(url))


    #test if the page content exists
    def test_content_exist(self):
        self.assertIsNotNone(soup)

    #test whether the headlines(h2, h3) are fetched/exists
    def test_headline_exists(self):
        headline = soup.find(['h2', 'h3'])
        self.assertIsNotNone(headline)

    #test whether the story(p tags) are fetched/exists  
    def test_story(self):
        headline = soup.find_all(['h2', 'h3'])

        for data in headline:
            try:
                story = data.find_next_sibling("p").text
            except TypeError:
                story = data.find_next_sibling("p").text
            except:
                story = data.find_previous_sibling("p").text
            self.assertIsNotNone(story)

    #test whether the links to the story are fetched/exists 
    def test_link(self):
        headline = soup.find_all(['h2', 'h3'])
        for data in headline:
            try:
                link = data.findChild("a")['href']
            except TypeError:
                link = data.find_parent('a')['href']

            self.assertIsNotNone(link)
        

if __name__ == '__main__':
    unittest.main()