import requests
import os
import json
from bs4 import BeautifulSoup


def make_json(description_items):
    json = []
    for item in description_items:
        attr = item.find('th').text
        val = item.find('td').text
        json.append({'nazwa_atrybutu': attr, 'atrybut': val})
    return json

def download_image(url):
    dir_name = 'images'
    response = requests.get(url, stream=True)
    filename = os.path.join(dir_name, url.split("/")[-1])
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename


base_url = 'lampy.pl'

categories = [
    'lampy-wiszace', 
    'lampy-stojace', 
    #'lampy-sufitowe', 
    #'kinkiety', 
    #'lampy-sufitowe'
]

styles = ['designerskie']#, 'industrialne', 'nowoczesne', 'szklane']

response_data = []
to_save = []

for category in categories:
    for style in styles:
        response = requests.get('https://www.lampy.pl/{0}-{1}/'.format(category, style), timeout=100)
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all(class_="item"):
            info = item.find(class_="product-info")
            href = info.find('a', href=True)['href']
            details = requests.get(href)
            details_soup = BeautifulSoup(details.content, 'html.parser')
            price = item.find(class_="regular-price") or item.find(class_="special-price")
            old_price = item.find(class_="old-price")
            image = item.find(class_='product-image').find('img')
            image_url = image.attrs.get('data-src') or image['src']
            response_data.append({
                'nazwa': item.find(class_="product-name").text,
                'kategoria': category,
                'styl': style,
                'cena': price.text.replace('\xa0', ' '),
                'stara cena': old_price.text.replace('\xa0', ' ') if old_price else None,
                'atrybuty': make_json(details_soup.find_all('tr')),
                'zdjecie': download_image(image_url)
            })
            print(response_data)
with open('data.json', 'w',encoding="utf-8") as f:
    json.dump(response_data, f)
            



