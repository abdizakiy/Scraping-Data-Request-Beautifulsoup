import requests
from bs4 import BeautifulSoup
# import csv
import pandas as pd
from fake_useragent import UserAgent
import random
import time

list_price     = []
list_address   = []
list_idplace   = []
list_state     = []
list_bed       = []
list_parking   = []
list_bath      = []
list_type      = []


headers = {
    'authority': 'www.realestate.com.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': cookie,
    'referer': 'https://www.realestate.com.au/rent/in-qld/list-1',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
params = {
    'activeSort': 'list-date',
}
            
cookie_list = []
states = ["qld", "nsw", "vic", "sa", "wa", "act", "nt", "tas"]
idx = 1

for state in states:
    page = 1
    time.sleep(5)

    # IF YOU WANT TO GET ALL PAGE USE WHILE TRUE
    # while True:

    # IF YOU WANT TO GET FEW PAGES USE FOR, 
    # CHANGE THE RANGE WITH THE NUMBER OF PAGES YOU WANT
    for _ in range(10):
        link = "https://www.realestate.com.au/rent/in-" + state + "/list-" + str(page)
        print("scanning page " + str(page) + " state " + state)
        for _ in range(10):
            cookie_list = [
                {
                #     'reauid': '15b411609fc9210099819565eb010000e3360200',
                    'KP_UIDz-ssn': '010kKHemSp9fXoKbjsnljVprfbMacv0QaxUjrf7vEs9hguj1w2Aqm3Aw9UCxRdFE0eM82CwXuLPjczsKE9pnW7AaqLvWN2pNxXJ7fnTMde6HZYuMhBnkDAQNCEjeQjfHOqrDA1xMxdxvuMOQXxuaToF0yJiVDYs64UzaNg4i56Rnhm3yu',
                    'KP_UIDz': '010kKHemSp9fXoKbjsnljVprfbMacv0QaxUjrf7vEs9hguj1w2Aqm3Aw9UCxRdFE0eM82CwXuLPjczsKE9pnW7AaqLvWN2pNxXJ7fnTMde6HZYuMhBnkDAQNCEjeQjfHOqrDA1xMxdxvuMOQXxuaToF0yJiVDYs64UzaNg4i56Rnhm3yu',
                #     '_sp_id.2fe7': '746a6b96-76fd-4b42-b42e-4a79e6064d00.1704297873.1.1704297889.1704297873.da9b9de4-0999-413a-97c5-ec0ede4771de',
                },
                {
                #     'reauid': '9432dd17f7630100ba1b95653d000000a26e0000',
                    'KP_UIDz-ssn': '0Rn7P2TdsQMNRXFNQpVU3dL8BaLYIlcDOUABpDOzyTW3rOoJGzaCrxnTGtJLmFyHKeJiCLupKM0OzO5nAueM3k7BRgD5bWF0LZx5CVFCaSgG0daHMpMf5SKQHfQFAqYTqU9r4fz06lHZOAwq4PrO1FaRAM1VcU21lL9JIVrYFcJUN43i',
                    'KP_UIDz': '0Rn7P2TdsQMNRXFNQpVU3dL8BaLYIlcDOUABpDOzyTW3rOoJGzaCrxnTGtJLmFyHKeJiCLupKM0OzO5nAueM3k7BRgD5bWF0LZx5CVFCaSgG0daHMpMf5SKQHfQFAqYTqU9r4fz06lHZOAwq4PrO1FaRAM1VcU21lL9JIVrYFcJUN43i',
                #     '_sp_id.2fe7': '7987d967-c8f9-4edf-a665-24bb2702a6e7.1704296949.1.1704298914.1704296949.cd157d77-fd49-4b15-9cc5-920eb746ba14',
                },
                {
                #     'reauid': '8e32dd17f0500200198a95658201000087b80000',
                    'KP_UIDz-ssn': '0fa3zwmSp1msGDmbQug6WnfqcoMPuMjBxn7lte9TN9eLhZR5uK2in4X8R9LcxZPF9yw7q13JnRseV5MUragZBM7nLEKfXTEfQxS9aJbHsXnvx5ebAhmK5wiJCd8RDuxYB4rFOaQeWKZFsDmjI1z4JiZJwXKS9sEssWggaLLCg3hCfX5',
                    'KP_UIDz': '0fa3zwmSp1msGDmbQug6WnfqcoMPuMjBxn7lte9TN9eLhZR5uK2in4X8R9LcxZPF9yw7q13JnRseV5MUragZBM7nLEKfXTEfQxS9aJbHsXnvx5ebAhmK5wiJCd8RDuxYB4rFOaQeWKZFsDmjI1z4JiZJwXKS9sEssWggaLLCg3hCfX5',
                #     '_sp_id.2fe7': '7c0a8b2a-3dc5-4536-872f-e05fbb7510ca.1704334203.1.1704334257.1704334203.c6f05e21-6ebf-4dbb-916b-336940fa49c4',
                }
            ]
            # req1 = requests.get(link, params=params, headers=headers)
            # # time.sleep(3)
            # # print(cookie_list)
            # cookie = requests.utils.dict_from_cookiejar(req1.cookies)
            # # cookie['_sp_id.2fe7'] = '7c0a8b2a-3dc5-4536-872f-e05fbb7510ca.1704334203.1.1704334257.1704334203.c6f05e21-6ebf-4dbb-916b-336940fa49c4'
            # print(cookie)
            # cookie_list.append(cookie)
            # print(cookie_list)
 
            cookies = random.choice(cookie_list)
            req = requests.get(link, params=params, cookies=cookies, headers=headers)
            soup = BeautifulSoup(req.text, "html.parser")
            
            stores = soup.select(".Card__Box-sc-g1378g-0.iyqwWq.results-card.residential-card")
            print(len(stores))
            if len(stores) != 0: break
        
        print(req.url)
        if len(stores) == 0: break
        page += 1

        for store in stores:
            price = store.select_one(".property-price ").text
            address = store.select_one(".residential-card__address-heading").text
            info = store.select(".Inline__InlineContainer-sc-lf7x8d-0.iuOPWU div div")
            try: parking = info[2]['aria-label']
            except: parking = ''
            try: bath = info[1]['aria-label']
            except: bath = ''
            bed = info[0]['aria-label']
            id_place = store.select_one(".ButtonBase-sc-18zziu4-0.iqtDgx.MoreButton__StyledButton-sc-hk6ggq-0.elVrsd")["id"].lstrip("action-menu-button-")
            type = store.select_one(".residential-card__property-type").text
            print(idx, [id_place, state.upper(), type, address, price, bed, bath, parking])
            idx += 1

            list_idplace.append(id_place)
            list_state.append(state.upper())
            list_address.append(address)
            list_price.append(price)
            list_bed.append(bed)
            list_bath.append(bath)
            list_parking.append(parking)
            list_type.append(type)
            


print('Saving Data...')
data = pd.DataFrame(list(zip(
    list_idplace,
    list_state,
    list_type,
    list_address,
    list_price, 
    list_bed, 
    list_bath,
    list_parking)), 
    
    columns=[
        'ID', 
        "State",
        "Type",
        "Address", 
        "Price",
        "Bedroom",
        "Bathroom",
        "Parking"])

file_name = link.lstrip('https://www.').split('/')[0].replace('.', '_')+'.csv'
data.to_csv(file_name, index=False)

print('Data Saved.')