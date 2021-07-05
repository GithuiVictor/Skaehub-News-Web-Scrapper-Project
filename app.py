# import csv
# # from typing import KeysView, Pattern
# from bs4 import BeautifulSoup
# from time import sleep
# import re
# import requests



# class NewsScraperApp:
#     def __init__(self, url, topic):
#         self.url = url
#         self.topic = topic
#         self.headers = {
#             'accept': '*/*',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language' : 'en-US,en;q=0.5',
#             'referer' : 'https://www.google.com',
#             'user-agent' : 'Mozilla/5.0Gecko/20100101Firefox/89.0'
#         }


#     """Get specific article method"""
#     def get_article(self, card):
#         try:
#             headline = card.find('h4', 's-title').text
#             source = card.find('span', 's-source').text
#             posted = card.find('span', 's-time').text.replace('.',' ').strip()
#             description = card.find('p', 's-desc').text.strip()

#             # raw_link = card.find('a').get('href')
#             # unquoted_link = requests.utils.unquote(raw_link)
#             # pattern = re.compiler(r'RU=(.+)\?RK')
#             # clean_link = re.search(pattern, unquoted_link).group(1)

#             article = (headline, source, posted, description)

#             print(article)

#             return article
#         except TypeError:
#             return


#     """Main method to get all the articles"""
#     def get_general_news(self):
#         template = self.url
#         article = []
#         # links = set()

#         while True:
#             response = requests.get(template)
#             # print(response)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # print(soup)

#             try:
#                 cards = soup.find_all('div', 'NewsArticle')
#                 # print(cards)
#             except TypeError:
#                 cards = soup.find_all('div', 'NewsArticle')
#                 # print(cards)

#             #Extract Article from page 
#             for card in cards:
#                 article = self.get_article(card)
#                 print(article)
#                 # link = article[-1]
#                 # if link in links:
#                 #     links.add(link)
#                 #     article.append(article)
#                 #     print(article)

            
#             # Save article data
#             # with open('general-news.csv', 'w', newline='n1') as output_file:
#             #     dict_writer = csv.DictWriter(output_file, KeysView)
#             #     dict_writer.writeheader()
#             #     dict_writer.writerows('all_products')

#             # print(article)

#             return article

#     """Main method to get all the articles"""
#     def get_specific_news(self):
#         template = self.url
#         article = []
#         # links = set()

#         while True:
#             response = requests.get(template)
#             # print(response)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # print(soup)

#             try:
#                 cards = soup.find_all('div', 'NewsArticle')
#                 print(cards)
#             except TypeError:
#                 cards = soup.find_all('div', 'NewsArticle')
#                 # print(cards)

#             #Extract Article from page 
#             for card in cards:
#                 article = self.get_article(card)
#                 print(article)
#                 # link = article[-1]
#                 # if link in links:
#                 #     links.add(link)
#                 #     article.append(article)
#                 #     print(article)

            
#             # Save article data
#             # with open('general-news.csv', 'w', newline='n1') as output_file:
#             #     dict_writer = csv.DictWriter(output_file, KeysView)
#             #     dict_writer.writeheader()
#             #     dict_writer.writerows('all_products')

#             # print(article)

#             return article


#     """Run main program to get specific news list according to the topic he/ she wants"""
#     def get_specific_news(self):
#         template = self.url
#         url = "{}/search?channel={}".format(template, self.topic)
#         articles = []
#         links = set()

#         while True:
#             response = requests.get(url, headers=self.headers)
#             soup = BeautifulSoup(response.text, 'html.parser')

#             try:
#                 cards = soup.find_all('div', 'NewsArticle')
#             except TypeError:
#                 cards = soup.find_all('div', 'NewsArticle')

#             #extract articles from page
#             for card in cards:
#                 article = self.get_article(card)
#                 # link = article[-1]
#                 # if link in links:
#                 #     links.add(link)
#                 #     articles.append(article)

#             # Save article data
#             # with open('general-news.csv', 'w', newline='n1') as output_file:
#             #     dict_writer = csv.DictWriter(output_file, KeysView)
#             #     dict_writer.writeheader()
#             #     dict_writer.writerows('all_products')

#             # print(article)
#             return articles


# # url = input("Please input or paste your news url: ")
# # topic = input("Please input a specific topic you'd like to get from the url: ")
# url = NewsScraperApp('https://news.search.yahoo.com/search?p=iphone+12+leaked&fr=yfp-t&ei=UTF-8&fp=1', 'iphone')
# print(NewsScraperApp.get_general_news(url))
# print(NewsScraperApp.get_specific_news(url))

import requests
import json
from bs4 import BeautifulSoup


class NewsScraperApp:
    def __init__(self, url):
        self.url = url
        return


    # """Scrap all urls of a website"""
    # def scrap_all_urls(self):
    #     #Creating an empty list 
    #     urls = []
    #     site = self.url

    #     #Creating requests for urls
    #     response = requests.get(site)
    #     soup = BeautifulSoup(response.text, 'html5lib')

    #     for link in soup.find_all('a'):
    #         href = link.attrs['href']
    #         if href.startswith("/"):
    #             site = site + href
    #             if site not in urls:
    #                 urls.append(site)
    #                 print(site)
    #                 #calling the scrape function itself
    #                 #generally called recursion
    #                 self.scrap_all_urls(site)



    def data_parse(self, soup):
        news = []
        urls = []
        site = self.url
        for data in soup.find_all(['h2', 'h3']):
            single_news = {
                "headline": data.getText(),
                "article_link": '',
                "description": ''
            }
            
            try:
                for link in data.find_all('a'):
                    href = link.attrs['href']
                    full_url = "{}{}".format(site, href)
                    single_news["article_link"] = full_url
                    print(full_url)
                single_news["description"] = data.find_next_sibling('p').text
            except TypeError:
                single_news["article_link"] = data.find_parent('a').text
                single_news["description"] = data.find('p')
            except AttributeError:
                single_news["description"] = data.find_next_sibling('a')
                single_news["description"] = data.find_previous_sibling('p')
            
            news.append(single_news)
        
        return news


    def get_general_news(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html5lib')

        data = self.data_parse(soup)
        with open('general-news.txt', 'w') as output_file:
                # output_file.write(str(data))
                output_file.write(json.dumps(data, indent=4))
                
        return self.data_parse(soup)


    # def get_specific_news(self,topi):
    #     url = f"https://www.nytimes.com/search?query={topic}"



if __name__ == "__main__":
    scraper = NewsScraperApp(input("Please input or paste your news URL: "))
    print(scraper.get_general_news())
    # print(scraper.scrap_all_urls())