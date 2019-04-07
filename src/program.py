import requests
from bs4 import BeautifulSoup

site_url = 'http://explosm.net/comics/5212/'
image_id = 'main-comic'

def get_content():
    response = requests.get(site_url)
    if response.status_code == 200:
        return response.text

    return ""

def get_image_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find('img', {'id' : image_id})
    return tag['src']

html  = get_content()
print(get_image_url(html))