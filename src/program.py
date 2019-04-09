import requests
import datetime
from bs4 import BeautifulSoup

site_url = 'http://explosm.net/'
image_id = 'main-comic'
dest_path = 'E:\\comic'

def get_content():
    response = requests.get(site_url)
    if response.status_code == 200:
        return response.text

    return ""

def get_image_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find('img', {'id' : image_id})
    return tag['src'][2::]

def download_image(url):
    response = requests.get(f'http://{url}')
    if response.status_code != 200:
        return
        
    save_to_file(response.content)

def save_to_file(content):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{dest_path}\\{now}.png', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    html  = get_content()
    url = get_image_url(html)
    download_image(url)