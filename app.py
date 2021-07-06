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
            #Save individual article in a dictionary
            single_news = {
                "headline": data.getText(),
                "article_link": '',
                "description": ''
            }
            
            #Get the article URL link
            for link in data.find_all('a'):
                href = link.attrs['href']
                full_url = "{}{}".format(site, href)
                single_news["article_link"] = full_url
                print(full_url)

            #Get description from the article
            try:
                single_news["description"] = data.find_next_sibling('p').text
            except TypeError:
                single_news["description"] = data.find('p').text
            except AttributeError:
                single_news["description"] = data.find_next_sibling('a')
                single_news["description"] = data.find_previous_sibling('p')
            
            #Add article to news list
            news.append(single_news)
        
        return news


    def get_general_news(self):
        # Request response from the url from user 
        response = requests.get(self.url)


        #initialize beautifulSoup as soup
        soup = BeautifulSoup(response.text, 'html.parser')


        # Call the data_parse method to parse and get news list
        data = self.data_parse(soup)


        #store the output in a txt file
        with open('general-news.txt', 'w') as output_file:
                # output_file.write(str(data))
                output_file.write(json.dumps(data, indent=4))

                
        return self.data_parse(soup)


    # def get_specific_news(self, topic):
    #     url = "{}/{}"



if __name__ == "__main__":
    scraper = NewsScraperApp(input("Please input or paste your news URL: "))
    print(scraper.get_general_news())
    # print(scraper.scrap_all_urls())