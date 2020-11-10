# Frask-Graphql-MongoDB/scraping.py
import json
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

#crawl PopVortex to extract Top 100 rock songs and store them in Json file
url = 'http://www.popvortex.com/music/charts/top-rock-songs.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def _get_title_artist():
    ranking_list = [] 
    for i in range(1,101):
        div = soup.find('div',id= 'chart-position-'+ str(i))
        
        images = div.find('img', class_='cover-image b-lazy')
        title = div.find('cite', class_ = 'title')
        artist = div.find('em', class_ = 'artist')

        img = images['data-src']
        title = title.text
        artist = artist.text 

        ranking_list.append({"no":i,"title":title, "artist":artist, "img": img})
        

    return ranking_list

def get_table():
    yield{
        "songs": _get_title_artist()
    }


#Store data in ranking.json
def scraping():
    """ Main function """
    get_table()
    df = pd.DataFrame.from_dict(get_table())
    print(f"Found {len(df)} results")
    df.to_json("ranking.json", orient="records")

