[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GithuiVictor_Skaehub-News-Web-Scrapper-Project&metric=alert_status)](https://sonarcloud.io/dashboard?id=GithuiVictor_Skaehub-News-Web-Scrapper-Project)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GithuiVictor_Skaehub-News-Web-Scrapper-Project&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GithuiVictor_Skaehub-News-Web-Scrapper-Project)


# A News Web Scraper App  (Skaehub Boot Camp Project)
### A project completed as part of the Cycle #1 Skaehub Boot Camp program's first checkpoint. 

#### Problem Definition
The main goal of this project is to accept a user's news url as input, scrape all of the news data from the url, display the data in the CLI app, and save it to a.txt file. 

#### How are we supposed to achieve this?
* Explore news sites and understand how different sites are structured so that you can have some knowledge on how to extract the information that is relevant to you
* Now that you have an idea of what you're working with, install and import the necessary dependencies for your project. That include:
  * Requests module
  ```python
    pip3 install requests
  ```
  * BeautifulSoup from bs4 package manager
  ```python
    sudo apt-get install python-bs4
  ```
* Prompt or Request input from the user. It should be a news url.
* Make a HTTP request from the url
```python
  import requests
  
  #Lets assume the user url is https://news.yahoo.com/
  user_url = "https://news.yahoo.com/"
  response = requests.get(user_url)
```
* Parse the HTML code from **response** using BeautifulSoup
```python
  from bs4 import BeautifulSoup
  
  soup = BeautifulSoup(response.content, "html.parser")
```




