from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver

DRIVER_PATH = "C:/Users/Remi Mestdagh/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

films = []
genres = []
acteurs = []

teller = 0
for i in range(1, 500, 50):

    url = "https://www.imdb.com/search/title/?title_type=feature&year=1950-01-01,2017-12-31&sort=num_votes,desc&start={}&ref_=adv_nxt".format(
        i)
    driver.get(url)


    y = 1000
    for timer in range(0, 13):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 750
        time.sleep(1)
    time.sleep(2)
    page = driver.execute_script('return document.body.innerHTML')
    bs = BeautifulSoup(''.join(page), 'html.parser')

    for movie in bs.findAll('div', class_='lister-item mode-advanced'):
        title = movie.find('img', 'loadlate')['alt']
        titleImage = movie.find('img', 'loadlate')['src']
        genres = movie.find('span', 'genre').text.strip()
        runtime = movie.find('span', 'runtime').contents[0]
        rating = movie.find('span', 'value').contents[0]
        year = movie.find('span', 'lister-item-year text-muted unbold').contents[0]
        stars = ""
        description = movie.findAll('p', class_='text-muted')[1].text.strip()

        for actor in movie.find('p', '').findAll('a'):
            stars = stars + actor.text + ","
        teller = teller + 1
        print(teller, title, titleImage)
        films.append({'titel': title.strip(), 'titleImage': titleImage.strip(),
                      'genres': genres.strip(), 'runtime': runtime.strip(), 'score':
                          rating.strip(), 'stars': stars,
                      'year': year.strip().replace("(", "").replace(")", "").replace("I ", "").replace("I",""),

                      'description': description})

with open('films2000metId2020.json', 'w') as f:  # writing JSON object

    json.dump(films, f, indent=2)
