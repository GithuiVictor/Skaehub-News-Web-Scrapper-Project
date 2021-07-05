from app import NewsScraperApp
import unittest
import os
from unittest.mock import patch


"""Create test class"""
class TestApp(unittest.TestCase):
    def setUp(self):
        self.path = './app.py'
        self.app = NewsScraperApp('https://news.search.yahoo.com/', 'iphone 12')
    

    """Check if the app file exists"""
    def test_filrExists(self):
        assert os.path.isfile(self.path)


    """Test if input is a url"""
    def test_inputUrl(self):
        user_input = 'https://search.yahoo.com/search?p=iphone+12+leaked&fr=yfp-t&ei=UTF-8&fp=1'

        with patch('builtins.input', side_effect=user_input):
            articles = NewsScraperApp.get_general_news()

        self.assertTrue(articles)


    """Test if the url input is an number instead of a string"""
    def test_inputNumber(self):
        self.user_input = 2

        with patch('builtins.input', side_effect=self.user_input):

            articles = NewsScraperApp.get_general_news()
        
        self.assertFalse(articles)

    
    """Test if input is a topic is a number instead of a string"""
    def test_topic(self):
        user_input = 12

        with patch('builtins.input', side_effect=user_input):

            articles = NewsScraperApp.get_specific_news(self)

        self.assertFalse(articles)


    """Test if the card details are generated """



if __name__ == '__main__':
    unittest.main()
