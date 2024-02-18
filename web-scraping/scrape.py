#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
#Allows us to use the html file and grab different data
from bs4 import BeautifulSoup
#pretty print module
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')

#Convert from html string (parsing) - Can also parse xml
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
links = soup.select('.titleline > a') #Grabs all the links
links2 = soup2.select('.titleline > a')

megas_links = links + links2
#votes = soup.select('.score') #Grabs the votes for each link, moved to func.

def sort_stories_by_votes(nwlist):
    return sorted(nwlist, key=lambda k:k['votes'], reverse=True)


def create_custom_news(links):
    news_list = []
    for link in links:
        title = link.getText()
        href = link.get('href', None)
        votes = link.find_next(class_="score")
        points = int(votes.getText().replace(" points", ""))
        if points > 99:
            news_list.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(news_list)

pprint.pprint(create_custom_news(megas_links))

#print(links)











""" 
#select allows us to use CSS selectors
#https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
print(soup.select('a'))   #Grab all <a> tags on page
print(soup.select('.score')) #Grab the score class
print(soup.select('#score_20514755')) #Grabs the span id """