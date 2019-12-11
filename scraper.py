from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
 
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
                dexnum = stats[0].getText()
                name = stats[2].getText()
                ability = stats[4].getText()