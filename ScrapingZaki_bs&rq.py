import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd

link = 'https://www.malkelapagading.com/directory?page='


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


list_nama    = []
list_produk  = []
list_kontak  = []
list_wa      = []
list_lokasi  = []
list_lantai  = []
list_gambar  = []
list_profil  = []
list_parkir  = []


for page in range(0, 25):
    print("scanning page", page, "...")
    req = requests.get(link + str(page).replace(" ", ""), headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    container =soup.find_all("div", class_="col-md-4 col-sm-6 col-xs-6 text-center work-process-sub position-relative overflow-hidden wow fadeIn")
    
    for x in container:
        name = x.find("h5", class_="margin-two text-center").text
        list_nama.append(name)
        
        try : location = x.find("p", class_="text-uppercase no-margin-bottom").text
        except : location = ""
        list_lokasi.append(location)
        
        try : floor = x.find("h6", class_="no-margin-top margin-two-bottom").text
        except : floor = ""
        list_lantai.append(floor)

        try : profile = x.find_all("a", class_="highlight-button-dark btn btn-very-small margin-three no-margin")
        except : profile = ""
        for y in profile:
            linktoko = y.get('href')
            list_profil.append(y.get('href'))


        toko_req        = requests.get(linktoko)
        toko_soup       = BeautifulSoup(toko_req.text, "html.parser")
        toko_container  = toko_soup.find_all("div", class_="col-md-5 col-sm-12 col-md-offset-1 padding-two-bottom")

        for y in toko_container:
            product = y.find(text='product').find_next('p').text
            list_produk.append(product)

            try : park = y.find(text='where to park').find_next('p').text
            except : park = ""
            list_parkir.append(park)

            try : contact = y.find("a", class_="btn-phone")
            except : contact = ""
            if contact is None:
                list_kontak.append("")
            else :
                list_kontak.append(contact.get('href')[4:])

            whatsapp = y.find("a", class_="btn-wa")
            if whatsapp is None:
                list_wa.append("")
            else :
                list_wa.append(whatsapp.get('href'))
            

        try : image = x.find_all("img")
        except : image = ""
        for x in image:
            # print(x.get('src'))
#             # print(x.get('src'))
            list_gambar.append(x.get('src'))


data = pd.DataFrame(list(zip(list_nama, list_produk, list_kontak, list_wa, list_lokasi, list_lantai, list_parkir, list_profil, list_gambar)), 
                    columns=['Nama', "Produk", "Kontak", "WhatsApp", "Lokasi", 'Lantai', "Lokasi Parkir", "Link Toko", "Link Gambar"])

data.to_csv('Assignment1_bs&rq.csv', index=False)