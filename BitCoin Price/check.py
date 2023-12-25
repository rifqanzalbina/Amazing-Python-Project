import requests
from bs4 import BeautifulSoup
import time

def get_latest_crypto_price(coin):
    url = 'https://www.google.com/search?q=' + (coin) + 'price'
    
    HTML = requests.get(url)
    
    soup = BeautifulSoup(HTML.text, 'html.parser')
    
    texti = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).find({
        'div': 'BNeawe iBp4i AP7Wnd'
    }).text
    return texti

price = get_latest_crypto_price('bitcoin')
print('BITCOIIN PRICE : ' + price)