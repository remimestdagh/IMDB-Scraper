from bs4 import BeautifulSoup
import requests
import json

from scraper.domein.Film import Film

films=[]
genres=[]
acteurs=[]
teller = 0
for i in range(1, 2000, 50):
    url = "https://www.imdb.com/search/title/?title_type=feature&year=1950-01-01,2017-12-31&sort=num_votes,desc&start={}&ref_=adv_nxt".format(i)
    r = requests.get(url) # where url is the above url
    bs = BeautifulSoup(r.content, 'html.parser')

    for movie in bs.findAll('div',class_='lister-item mode-advanced'):
        title = movie.find('img','loadlate')['alt']
        titleImage = movie.find('img', 'loadlate')['src']
        genres = movie.find('span','genre').text.strip()
        runtime = movie.find('span','runtime').contents[0]
        rating = movie.find('span','value').contents[0]
        year = movie.find('span','lister-item-year text-muted unbold').contents[0]
        imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
        stars=""

        for actor in movie.find('p','').findAll('a'):
            stars=stars+actor.text+","
        teller=teller+1
        print(teller,title, genres,runtime, rating, year, imdbID,stars)
        films.append({'titel':title.strip(),'titleImage':titleImage.strip(),
                         'genres':genres.strip(),'runtime':runtime.strip(),'score':
                      rating.strip(),'stars':stars,'year': year.strip().replace("(","").replace(")","").replace("I ",""),'imdbID':imdbID.strip()})



with open('films2000metId.json', 'w') as f:  # writing JSON object


    json.dump(films, f,indent=2)