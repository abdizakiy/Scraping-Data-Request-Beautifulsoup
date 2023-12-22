import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd
from fake_useragent import UserAgent

list_nama     = []
list_lokasi   = []
list_jam      = []
list_prov     = []
list_kontak   = []
list_parkir   = []
list_kategori = []
list_url      = []

headers = {'user-agent': UserAgent().random}
link = 'https://lippomallpuri.com/tenant'

while True:
    idx = 1
    print("scanning page...")
    print(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    stores = soup.select(".tenantBoxLogo a")
    print(len(stores))
    for store in stores:
        url_store = 'https://lippomallpuri.com/' + store['href']
        print(idx, url_store)

        req1 = requests.get(url_store, headers=headers)
        soup1 = BeautifulSoup(req1.text, "html.parser")
        nama = " ".join(soup1.select_one('h2').text.split())
        lokasi = " ".join(soup1.select_one('div.detailMenu:nth-of-type(1) font').text.split())
        kategori = " ".join(soup1.select_one('.detailMenu > a.btnNew3').text.split())

        try: kontak = " ".join(soup1.select_one('div:nth-of-type(3) font').text.split())
        except: kontak = ''
        try: parking = " ".join(
            soup1.select_one('div.detailMenu:nth-of-type(6)').text
            .split()).lstrip('Nearest Parking Area :').strip()
        except: parking = " ".join(
            soup1.select_one('div.detailMenu:nth-of-type(5)').text
            .split()).lstrip('Nearest Parking Area :').strip()

        print([nama, lokasi, kontak, parking, kategori])
        idx += 1

        list_nama.append(nama)
        list_lokasi.append(lokasi)
        list_kontak.append(kontak)
        list_parkir.append(parking)
        list_kategori.append(kategori)
        list_url.append(url_store)

        
    data = pd.DataFrame(list(zip(
        list_nama, 
        list_lokasi,
        list_kontak, 
        list_parkir,
        list_kategori,
        list_url)), 
        
        columns=[
            'Nama', 
            "Lokasi",
            "Kontak", 
            "Parkir",
            "Kategori",
            "URL Tenant"])

    data.to_csv(link.lstrip('https://www.').split('/')[0].replace('.', '_').strip()+'.csv', 
        index=False)
    
    break