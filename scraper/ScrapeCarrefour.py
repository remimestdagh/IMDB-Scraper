import requests
from bs4 import BeautifulSoup
from scraper.HashMap import HashMap
from scraper.Kaas import Kaas


for i in range(4):
    URL1='https://drive.carrefour.eu/nl/search?q=kaas%3Arelevance&page={}'.format(i)
    resultsMany = requests.get(URL1)
    soup = BeautifulSoup(resultsMany.content,'html.parser')
    results = soup.find(id='SearchPageResults')
    # print(results)
    kaasNamen = []
    kaasPrijzen = []
    kaasCenten = []
    kazen = []

    prijzenVanKazen = results.find_all_next('span', class_='bigprice')
    prijzenNaKommaVanKazen = results.find_all_next('span', class_='cents')
    namenVanKazenHTML = results.find_all_next('a', class_='name')
    namenVanKazen = namenVanKazenHTML
    naKommaKazen = results.find_all_next('span', class_='cents')
    for prijsKaas in prijzenVanKazen:
        # print(prijsKaas.text, end='\n'*2)
        kaasPrijzen.append(int(prijsKaas.text.strip()))
    for naamKaas in namenVanKazen:
        # print(naamKaas.text, end='\n'*2)
        kaasNamen.append(naamKaas.text.strip())
    for centKaas in naKommaKazen:
        kaasCenten.append(int(centKaas.text.replace('€','').strip()))

    for i in range(len(prijzenVanKazen)):
        kaasPrijzen[i]=kaasPrijzen.__getitem__(i)+(kaasCenten.__getitem__(i)/100)
        kazen.append(Kaas(kaasNamen.__getitem__(i), kaasPrijzen.__getitem__(i)))
        print(kazen.__getitem__(i).name +" " +str(kazen.__getitem__(i).price) +" "+"euro")