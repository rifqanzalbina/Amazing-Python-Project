import sys
import requests
from bs4 import BeautifulSoup
import re
import time

def details(soup):
    try:
        info = soup.find('div', {'class': 'pure-1 md-3-5'})
        
        print("\nAbout the Anime : \n", "\t\t", info.find('p').getText(), "\n")

        total_episodes = soup.find('div', {'class': 'pure-1 md-1-5'})
        print("\nTotal number of episodes :\t", re.sub("[^0-9]", "", total_episodes.find('span').getText()))

        Active_years = soup.find('span', {'class': 'iconYear'})
        print("\n Years Active (From-To)\t:\t", Active_years.getText(), "-\n")

        rating = soup.find('div', {'class': 'avgRating'})
        print("Rating : ", rating.find('span').getText())

        tags = soup.find('div', {'class': 'tags'})
        tag_list = tags.find('ul').getText().replace("\n", "  ")
        print("\nTags : \n", tag_list)

    except AttributeError:
        print("Anime info not found")

def entry():
    print("\nType complete name>>\n")
    anime_name = input("Enter the name of the anime : ")
    
    anime_name = anime_name.lower().replace(" ", "-")

    print("\nSearching for:", anime_name)

    search_url = f"https://www.anime-planet.com/anime/{anime_name}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        source_code = requests.get(search_url, headers=headers)
        source_code.raise_for_status() 
        content = source_code.content
        global soup
        soup = BeautifulSoup(content, features="html.parser")

        details(soup)
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")

if __name__ == "__main__":
    entry()
