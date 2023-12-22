import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd
from fake_useragent import UserAgent

list_nama    = []
list_lokasi  = []
list_jam     = []
list_prov    = []
list_url     = []
list_maps    = []

headers = {'user-agent': UserAgent().random}
link = 'https://www.ikea.co.id/in/lokasi-kami'

while True:
    idx = 0
    print("scanning page...")
    print("URL: ", link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    stores = soup.select("strong a")
    print(len(stores))
    for store in stores:
        url_store = store['href']
        print(url_store)

        req1 = requests.get(url_store, headers=headers)
        soup1 = BeautifulSoup(req1.text, "html.parser")
        nama = " ".join(soup1.select_one('h1.plp-heading.heading-alignment.mb-5').text.split())
        info = " ".join(soup1.select_one('div:nth-of-type(4) div.text-wrap').text.split())

        if 'Alamat' not in info: 
            info_jam = info
            info = " ".join(soup1.select_one('div:nth-of-type(5) div.text-wrap').text.split())
        else: info_jam = " ".join(soup1.select_one('div.col-12:nth-of-type(3) div').text.split())

        alamat = info.split('Alamat')[1].split('Hubungi kami')[0].lstrip(':').strip()
        jam = (
            info_jam.lstrip('Jam operasional').
            split('Restoran')[0].
            split('Food court')[0].
            split('Swedish Deli')[0]).lstrip(":").strip()
        
        if "Phone" in info: kontak = info.split('Phone:')[1].split('Fax')[0].split('cs')[0].strip()
        else: kontak = ''

        idx += 1
        print(idx, [jam])
        
        list_nama.append(nama)
        list_url.append(url_store)
        list_lokasi.append(alamat)
        list_jam.append(jam)
        list_maps.append('')

    print('Saving Data...')
    data = pd.DataFrame(list(zip(
        list_nama,
        list_lokasi, 
        list_jam,
        list_url)), 
        
        columns=[
            'Nama', 
            "Alamat", 
            "Jam",
            "URL Store"])
    
    file_name = link.lstrip('https://www.').split('/')[0].replace('.', '_')+'.csv'
    data.to_csv(file_name, index=False)

    print('Data Saved: ', file_name)
    break