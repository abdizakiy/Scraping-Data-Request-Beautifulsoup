import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd
from fake_useragent import UserAgent

list_nama    = []
list_lokasi  = []
list_jam     = []
list_prov    = []

headers = {'user-agent': UserAgent().random}
link = 'https://www.gramedia.com/best-seller/daftar-alamat-toko-buku-gramedia-di-seluruh-wilayah-indonesia'

while True:
    idx = 1
    print("scanning page...")
    print(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    provs = soup.select("h3 strong")
    for prov in provs:
        provinsi = prov.text
        stores = prov.find_all_next("p")

        for store in stores:
            if store.find_previous("h3").text == provinsi:
                print(idx, provinsi)

                if store.text.startswith('Gramedia'): 
                    nama = store.text
                    print(idx, 'Nama: ', nama)
                    list_nama.append(nama)
                    list_prov.append(provinsi)
                    idx += 1  

                elif 'Lokasi' in store.text: 
                    lokasi = store.text.lstrip("Lokasi:").strip()
                    print(idx, 'Alamat: ', lokasi)
                    list_lokasi.append(lokasi)

                elif 'Operasional' in store.text: 
                    jam = store.text.lstrip("Operasional:").strip()
                    print(idx, 'Jam: ', jam)
                    list_jam.append(jam)

 


    data = pd.DataFrame(list(zip(
        list_nama, 
        list_prov,
        list_lokasi, 
        list_jam)), 
        
        columns=[
            'Nama', 
            "Provinsi",
            "Lokasi", 
            "Jam"])

    data.to_csv(link.lstrip('https://www.').split('/')[0].replace('.', '_').strip()+'.csv', 
        index=False)
    
    break