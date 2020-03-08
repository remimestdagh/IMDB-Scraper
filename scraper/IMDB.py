from bs4 import BeautifulSoup
import requests
import json

from scraper.domein.Film import Film

films=[]
genres=[]
acteurs=[]
teller = 0
for i in range(40):
    url = "https://www.imdb.com/search/title/?sort=num_votes,desc&start={}&title_type=feature&year=1950,2017".format(i)
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
                      rating.strip(),'stars':stars,'year': year.strip().replace("(","").replace(")","")})



with open('films2000.json', 'w') as f:  # writing JSON object


    json.dump(films, f,indent=2)