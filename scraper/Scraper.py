import requests
from bs4 import BeautifulSoup

from scraper.HashMap import HashMap

URL = 'https://drive.carrefour.eu/nl/search?store_ref=D0615&text=kaas'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchPageResults')
#print(results)
kaasMap = HashMap()


prijzenVanKazen = results.find_all_next('span', class_='bigprice')
namenVanKazen = results.find_all_next('a', class_='name')

for prijsKaas in prijzenVanKazen:
    kaasMap.add("", )
    print(prijsKaas, end='\n'*2)