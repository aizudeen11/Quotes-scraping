from bs4 import BeautifulSoup
import requests as r
import pandas as pd

info = []

def Quotes(page_num):
    url = f'https://quotes.toscrape.com/page/{page_num}/'
    page = r.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    parents = soup.find_all('div', class_='quote')
    for parent in parents:
        tags_list = []
        quotes = parent.find('span', class_='text').text
        authors = parent.find('small', class_='author').text
        URL = 'https://quotes.toscrape.com' + parent.find('a')['href']
        pages = r.get(URL)
        soups = BeautifulSoup(pages.text, 'html.parser')
        parents_born_date = soups.find('span', class_='author-born-date').text
        parents_born_location = soups.find('span', class_='author-born-location').text
        parents_born_location1 = parents_born_location.replace('in', '')
        tags = parent.find_all('a', class_='tag')
        for x in tags:
            tags_list.append(x.text)
        Quotes_info = {
        'quotes' : quotes,
        'authors' : authors,
        'URL' : URL,
        'tag(s)' : tags,  
        'author born date' : parents_born_date,
        'author born location' :  parents_born_location1
        }
        info.append(Quotes_info)
    
    return

for x in range(1,2):
    Quotes(x)

df = pd.DataFrame(info)
print(df.head())
df.to_csv('Quotes.csv')
            