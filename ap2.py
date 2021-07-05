import requests
from bs4 import BeautifulSoup
import pandas


url = input('Enter A News Link: ')
res = requests.get(url).text
soup = BeautifulSoup(res, 'html5lib')
for data in soup.find_all(['h2','h3']):
     article_link = ''
     description = ''
     try:
        article_link = data.findChild("a")['href']
        description = data.find_next_sibling("p").text
     except TypeError:
         article_link = data.find_parent('a')
         description = data.find("p")
     except AttributeError:
         description = data.find_next_sibling("a")
         description = data.find_previous_sibling("p")
     print('Headline: ', data.getText())
     print('Story: ', description)
     print('Read More: ', article_link, '\n')