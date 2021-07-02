import csv
from typing import KeysView, Pattern
from bs4 import BeautifulSoup
from time import sleep
import re
import requests



class NewsScraperApp:
    def __init__(self, url, topic):
        self.url = url
        self.topic = topic
        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language' : 'en-US,en;q=0.5',
            'referer' : 'https://www.google.com',
            'user-agent' : 'Mozilla/5.0Gecko/20100101Firefox/89.0'
        }


    """Get specific article method"""
    def get_article(self, card):
        try:
            headline = card.find('h4', 's-title').text
            source = card.find('span', 's-source').text
            posted = card.find('span', 's-time').text.replace('.',' ').strip()
            description = card.find('p', 's-desc').text.strip()

            # raw_link = card.find('a').get('href')
            # unquoted_link = requests.utils.unquote(raw_link)
            # pattern = re.compiler(r'RU=(.+)\?RK')
            # clean_link = re.search(pattern, unquoted_link).group(1)

            article = (headline, source, posted, description)

            print(article)

            return article
        except TypeError:
            return


    """Main method to get all the articles"""
    def get_general_news(self):
        template = self.url
        article = []
        links = set()

        while True:
            response = requests.get(template)
            # print(response)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)

            try:
                cards = soup.find_all('div', 'NewsArticle')
                # print(cards)
            except TypeError:
                cards = soup.find_all('div', 'NewsArticle')
                # print(cards)

            #Extract Article from page 
            for card in cards:
                article = self.get_article(card)
                print(article)
                # link = article[-1]
                # if link in links:
                #     links.add(link)
                #     article.append(article)
                #     print(article)

            
            # Save article data
            # with open('general-news.csv', 'w', newline='n1') as output_file:
            #     dict_writer = csv.DictWriter(output_file, KeysView)
            #     dict_writer.writeheader()
            #     dict_writer.writerows('all_products')

            # print(article)

            return article

    """Main method to get all the articles"""
    def get_specific_news(self):
        template = self.url
        article = []
        links = set()

        while True:
            response = requests.get(template)
            # print(response)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)

            try:
                cards = soup.find_all('div', 'NewsArticle')
                # print(cards)
            except TypeError:
                cards = soup.find_all('div', 'NewsArticle')
                # print(cards)

            #Extract Article from page 
            for card in cards:
                article = self.get_article(card)
                print(article)
                # link = article[-1]
                # if link in links:
                #     links.add(link)
                #     article.append(article)
                #     print(article)

            
            # Save article data
            # with open('general-news.csv', 'w', newline='n1') as output_file:
            #     dict_writer = csv.DictWriter(output_file, KeysView)
            #     dict_writer.writeheader()
            #     dict_writer.writerows('all_products')

            # print(article)

            return article

url = NewsScraperApp('https://news.search.yahoo.com/search?p=iphone+12+leaked&fr=yfp-t&ei=UTF-8&fp=1', 'iphone')
print(NewsScraperApp.get_general_news(url))


# url = input("Please input or paste your news url: ")
# topic = input("Please input a specific topic you'd like to get from the url: ")