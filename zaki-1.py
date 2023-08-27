import pandas as pd
import requests as rq 
from bs4 import BeautifulSoup as bs

url = 'https://www.malkelapagading.com/directory'

page = rq.get(url)

soup = bs(page.content, "html.parser")
category_arr = []

# soup.find('a')

category_container = soup.find(id="accordion-one-link0")
category = category_container.find_all("a", class_="list-group-item")

for a in category_container.find_all("a", class_="list-group-item"):
    category_arr.append(a.get('href')[52:])
    # print(a.get('href'))


data = pd.DataFrame(list(zip(category_arr)),columns=['Category'])

data.to_excel('output.xlsx')


# zak = soup.find_all('a', class_="list-group-item")