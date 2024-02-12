import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

list_nama     = []
list_harga    = []

idx = 1
page = 1
headers = {'user-agent': UserAgent().random}
print("scanning page...")

while True:
    link = 'https://www.tokopedia.com/search?page='+ str(page) +'&q=label%20thermal'
    print(page, link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    cards = soup.select('.pcv3__info-content.css-gwkf0u')
    print(len(cards))
    if len(cards) == 0: break

    page += 1
    for card in cards:
        nama = card.select_one('.prd_link-product-name.css-3um8ox').text
        harga = card.select_one('.prd_link-product-price.css-h66vau').text
        print(idx, [nama, harga])
        idx += 1

        list_nama.append(nama)
        list_harga.append(harga)

print('Saving Data...')
data = pd.DataFrame(list(zip(
    list_nama, 
    list_harga)), 
    
    columns=[
        'Nama', 
        "Harga"])

file_name = link.lstrip('https://www.').split('/')[0].replace('.', '_')+'.csv'
data.to_csv(file_name, index=False)

print('Data Saved.')