from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
"""
    Scrapes move from PokemonDB
"""

def scrape_list(url, filename):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    data = [
        ["name", "type", "catagory", "power", "accuracy", "pp", "effect"]
    ]

    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e)
    except URLError:
        print("ERR")
    else:
        #print("--> Copying HTML from " + url)
        res = BeautifulSoup(html.read(),"html5lib")
        tags = res.findAll("table", {"id": "moves"})
        pbar = tqdm(total=len(tags), desc=filename)
        for tag in tags:
            pbar.update(1)
            inf = tag.findAll("tr")
            for i in range(1, len(inf)): 
                stats = inf[i].findAll("td")
                move_info = []
                if len(list(stats)) > 7:
                    m_name = (stats[0].getText()) # name
                    m_type = (stats[1].getText().lower()) # type
                    m_cat = (stats[2]['data-sort-value']) # catagory
                    m_power = (stats[3].getText()) # power
                    m_acc = (stats[4].getText()) # accuracy
                    m_pp = (stats[5].getText()) # PP
                    m_effect = (stats[7].getText()) # effect
                    move_info = [
                        m_name, m_type, m_cat, m_power, m_acc, m_pp, m_effect
                    ]
                else:
                    m_name = (stats[0].getText()) # name
                    m_type = (stats[1].getText().lower()) # type
                    m_cat = (stats[2]['data-sort-value']) # catagory
                    m_power = (stats[3].getText()) # power
                    m_acc = (stats[4].getText()) # accuracy
                    m_pp = (stats[5].getText()) # PP
                    m_effect = (stats[6].getText()) # effect
                    move_info = [
                        m_name, m_type, m_cat, m_power, m_acc, m_pp, m_effect
                    ]

                for j in range(len(move_info)):
                    if move_info[j] == "" or move_info[j] == "—":
                        move_info[j] = "none"

                data.append(move_info)
                #print(m_name)

    # create datafile
    myFile = open(filename, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    #print('Done!')

### MAIN PROGRAM 
def scrape_move_list(location):
    print("=== Scraping Pokemon move CSVs ===")

    scrape_list("https://pokemondb.net/move/all", location + "/all_moves.csv")
    scrape_list("https://pokemondb.net/move/generation/1", location + "/gen1-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/2", location + "/gen2-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/3", location + "/gen3-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/4", location + "/gen4-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/5", location + "/gen5-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/6", location + "/gen6-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/7", location + "/gen7-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/8", location + "/gen8-moves.csv")
    scrape_list("https://pokemondb.net/move/generation/9", location + "/gen9-moves.csv")
    
    print("Done!\n")