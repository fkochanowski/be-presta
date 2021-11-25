import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

base_url = 'lampy.pl'

categories = [
    'lampy-wiszace', 
    'lampy-stojace', 
    'lampy-sufitowe', 
    'kinkiety', 
]

styles = {'designerskie': [34, 35, 36, 37], 'industrialne': [38, 39, 40, 41], 'nowoczesne': [42, 43, 44, 45], 'szklane': [46, 47, 48, 49]}

response_data = []
to_save = {'Nazwa': [], 'Kategoria': [], 'zdjecie':[], 'Cena zawiera podatek. (brutto)': [], 'Opis':[], 'Ilosc': [], 'Stan':[]}
limit = 700 // len(categories) // len(styles)
print(limit)
attributes = {'Produkt': [], 'Arybut': [], 'Wartość': []}
counter = 0

for i, category in enumerate(categories):
    for style, indexes in styles.items():
        response = requests.get(f'https://www.lampy.pl/{category}-{style}/')
        soup = BeautifulSoup(response.content, 'html.parser')
        for index, item in enumerate(soup.find_all(class_="item")):
            info = item.find(class_="product-info")
            href = info.find('a', href=True)['href']
            details = requests.get(href)
            details_soup = BeautifulSoup(details.content, 'html.parser')
            description = details_soup.find(class_='std')
            price = (item.find(class_="regular-price") or item.find(class_="special-price")).find(class_="price")
            old_price = item.find(class_="old-price")
            image = item.find(class_='product-image').find('img')
            image_url = image.attrs.get('data-src') or image['src']
            to_save['zdjecie'].append(image_url),
            to_save['Opis'].append(description.text if description else "")
            to_save['Nazwa'].append(item.find(class_="product-name").text)
            to_save['Kategoria'].append(indexes[i])
            to_save['Ilosc'].append(50)
            to_save['Cena zawiera podatek. (brutto)'].append(price.text.replace('\xa0', ''))
            counter += 1
            if counter >= limit:
                counter = 0
                break
    df = pd.DataFrame(to_save)
    df.to_csv('products.csv', sep=";")
            



