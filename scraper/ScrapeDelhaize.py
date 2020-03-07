import requests
from bs4 import BeautifulSoup
from scraper.domein.Kaas import Kaas


for i in range(4):
    URL1='https://www.delhaize.be/nl-be/shop/Zuivel-en-kaas/Kazen/c/v2DAICHE?pageNumber={}'.format(i)
    resultsMany = requests.get(URL1)
    soup = BeautifulSoup(resultsMany.content,'html.parser')
    results = soup.find(class_='DataView ProductList padded-items js-data-view')
    # print(results)
    kaasNamen = []
    kaasPrijzen = []
    kazen = []
    kaasPrijsPerKilo = []

    prijzenVanKazen = results.find_all_next('span', class_='quantity-price super-bold')
    prijzenNaKommaVanKazen = results.find_all_next('span', class_='cents')
    prijsPerKilo = results.find_all_next('div', class_='property')
    namenVanKazenHTML = results.find_all_next('p', class_='text-bold title ellipsis')
    namenVanKazen = namenVanKazenHTML
    categorieKazen = results.find_all_next('p',class_='ellipsis')
    for prijsKaas in prijzenVanKazen:
        # print(prijsKaas.text, end='\n'*2)
        kaasPrijzen.append(prijsKaas.text.strip())
    for naamKaas in namenVanKazen:
        # print(naamKaas.text, end='\n'*2)
        kaasNamen.append(naamKaas.text.strip())
    for prijsPerK in prijsPerKilo:
        kaasPrijsPerKilo.append(prijsPerK.text.strip())
    for i in range(len(prijzenVanKazen)):
        kazen.append(Kaas(kaasNamen.__getitem__(i), kaasPrijzen.__getitem__(i), kaasPrijsPerKilo.__getitem__(i)))
        print(kazen.__getitem__(i).name +" " +kazen.__getitem__(i).price +" "+"euro",kazen.__getitem__(i).pricePerKilo)