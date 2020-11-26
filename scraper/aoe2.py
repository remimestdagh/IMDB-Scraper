import requests
import json

matches = []
timestampLastIteration = ""

for i in range(1, 50):
    # append and change to date of last one of previous iteration &since=1596775000
    url = "https://aoe2.net/api/matches?game=aoe2de&count=1000"
    if matches:
        url += "&since="
        url += str(timestampLastIteration)

    r = requests.get(url).json()
    matches.append(r)

    for j in r:
        print(j["finished"])
        timestampLastIteration = j["finished"]

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(matches)

with open('matches50k.json', 'w') as f:  # writing JSON object

    json.dump(matches, f, indent=4)


