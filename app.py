import requests
import json
from bs4 import BeautifulSoup
import pyfiglet


class NewsScraperApp:
    def __init__(self, url):
        self.url = url
    

    def data_parse(self, soup):
        news = []
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
        

        return news, single_news


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



if __name__ == "__main__":
    print('--------------------------------------------------------------------\n')
    result = pyfiglet.figlet_format("NEWS WEB SCRAPER", font = "slant"  )
    print(result)
    print('\n------------------------------------------------------------------\n')
    scraper = NewsScraperApp(input("Please input or paste your news URL: "))
    print(scraper.get_general_news())
    print('--------------------------------------------------------------------\n')
    print('\n \n You now can run the command $ cat general-news.txt on your shell\n \n')
