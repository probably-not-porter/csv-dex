from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv


data = []
# add header
data.append(['Dex Num', 'Name', 'Abilities', 'HP', 'ATTACK', 'DEFENSE', 'S. ATTACK', 'S. DEFENSE', 'SPEED'])
 
try:
    html = urlopen("https://www.serebii.net/pokemon/all.shtml")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    tags = res.findAll("table", {"class": "dextable"})
    for tag in tags:
        inf = tag.findAll("tr")
        
        for i in range(2, len(inf)):
            stats = inf[i].findAll("td", {"class": "fooinfo"})
            if stats != []:
                dexnum = stats[0].getText().replace("\n", "").replace("\t", "")
                name = stats[2].getText().replace("\n", "").replace("\t", "")
                ability = stats[4].getText().replace("\n", "").replace("\t", "")
                health = stats[5].getText().replace("\n", "")
                attack = stats[6].getText().replace("\n", "")
                defense = stats[7].getText().replace("\n", "")
                sattack = stats[8].getText().replace("\n", "")
                sdefense = stats[9].getText().replace("\n", "")
                speed = stats[10].getText().replace("\n", "")

                # create row
                data_item = []
                data_item.append(dexnum)
                data_item.append(name)
                data_item.append(ability)
                data_item.append(health)
                data_item.append(attack)
                data_item.append(defense)
                data_item.append(sattack)
                data_item.append(sdefense)
                data_item.append(speed)
                data.append(data_item)
 
# create datafile
myFile = open('all.csv', 'w')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(data)