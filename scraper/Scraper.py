import requests
from bs4 import BeautifulSoup

from scraper.HashMap import HashMap
from scraper.Kaas import Kaas

URL = 'https://drive.carrefour.eu/nl/search?store_ref=D0615&text=kaas'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchPageResults')
#print(results)
kaasNamen = []
kaasPrijzen = []
kazen=[]


prijzenVanKazen = results.find_all_next('span', class_='bigprice')
prijzenNaKommaVanKazen = results.find_all_next('span', class_='cents')
namenVanKazenHTML = results.find_all_next('a', class_='name')
namenVanKazen = namenVanKazenHTML
for prijsKaas in prijzenVanKazen:
    #print(prijsKaas.text, end='\n'*2)
    kaasPrijzen.append(prijsKaas.text)
for naamKaas in namenVanKazen:
    #print(naamKaas.text, end='\n'*2)
    kaasNamen.append(naamKaas.text)
for i in range(len(namenVanKazen)):
    kazen=Kaas(kaasNamen[i],kaasPrijzen[i])
    print(kazen[i].name)