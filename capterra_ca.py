import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd
from fake_useragent import UserAgent
import time

list_name     = []
list_rev   = []
list_jam      = []
list_prov     = []
list_kontak   = []
list_parkir   = []
list_kategori = []
list_url      = []
list_web      = []

headers = {'user-agent': UserAgent().random}
link = 'https://www.capterra.ca/directory'

while True:
    idx = 1
    print("scanning page...")
    print(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    catgrs = soup.select('a.list-group-item')
    print(len(catgrs))

    for catgr in catgrs:
        page = 1
        while True:
            catgr_url = catgr["href"]+"?page="+str(page)
            print(catgr_url)

            for _ in range(10):
                req1 = requests.get(catgr_url, headers=headers)
                soup1 = BeautifulSoup(req1.text, "html.parser")

                cards = soup1.select('article.card')
                print(len(cards))
                if len(cards) != 0: break
            if len(cards) == 0: break
            page += 1
            for card in cards:
                name = card.select_one('.h5 a').text
                try: 
                    review = " ".join(card.select_one('a.mos-star-rating').text.split())
                    prod_url = "https://www.capterra.ca" + card.select_one('a.mos-star-rating')["href"]
                except: 
                    review = 'No Review'
                    prod_url = "https://www.capterra.ca" + card.select_one('.h5 a')['href']
                print(idx, [name, review], prod_url)
                idx += 1

                list_name.append(name)
                list_rev.append(review)
                list_url.append(prod_url)

    print('Saving Data...')
    data = pd.DataFrame(list(zip(
        list_name, 
        list_rev,
        list_url)), 
        
        columns=[
            'Name', 
            "Review",
            "Product URL"])

    file_name = link.lstrip('https://www.').split('/')[0].replace('.', '_')+'.csv'
    data.to_csv(file_name, index=False)
    
    print('Data Saved.')
    break