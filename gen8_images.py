import csv
import urllib.request
import requests
import time

results = []
with open("data/all.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row[1])


for x in range(808,890+1):
    name = results[x].lower()
    print(name)
    url = "https://www.serebii.net/pokedex-swsh/icon/"+ str(x) +".png"

    with open('static/regular/' + name + '.png', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    time.sleep(1)