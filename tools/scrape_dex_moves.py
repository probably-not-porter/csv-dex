from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import numpy as np
import csv
import shutil
import string
import re
from tempfile import NamedTemporaryFile

"""
    Run this as step 2 after creating a CSV. 
    This step will pull move information from bulbapedia
    and attempt to create a new column in each CSV entry.
"""

def exceptions(name):
    if name.lower() == "mr. mime":
        return "mr-mime"
    elif name.lower() == "mr. rime":
        return "mr-rime"
    elif name.lower() == "mime jr.":
        return "mime-jr"
    elif name.lower() == "farfetch'd":
        return "farfetchd"
    elif name.lower() == "sirfetch'd":
        return "sirfetchd"
    elif name.lower() == "type: null":
        return "type-null"
    elif name.lower() == "flabébé":
        return "flabebe"
    elif name.lower() == "tapu koko":
        return "tapu-koko"
    elif name.lower() == "tapu lele":
        return "tapu-lele"
    elif name.lower() == "tapu bulu":
        return "tapu-bulu"
    elif name.lower() == "tapu fini":
        return "tapu-fini"
    else:
        return name

def getMoves(poke_name):
    poke_name = exceptions(poke_name)
    url = "https://pokemondb.net/pokedex/"+poke_name.lower()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    moves = []

    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e)
        print(poke_name)
    except URLError:
        print("ERR: " + poke_name + " didn't work right")
    else:
        print("--> Copying HTML from " + url)
        res = BeautifulSoup(html.read(),"html5lib")
        for node in res.findAll("a", attrs={'href': re.compile("/move/")}):
            move = node.findAll(text=True)[0]
            if move in moves:
                pass
            else:
                moves.append(move)

    return moves


def amend_file(input_csv):
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
    with open(input_csv) as csvfile, tempfile:

        reader = csv.reader(csvfile) # change contents to floats
        writer = csv.writer(tempfile)
        title_flag = False
        loop_check = False

        for row in reader: # each row is a list
            if title_flag == False: # title row
                title_flag = True
                if "moves" in row:
                    loop_check = True
                row.append("moves")
                writer.writerow(row)

            else:                   # regular row
                moves = getMoves(row[1])
                row.append(moves)
                writer.writerow(row)

    if loop_check == False:
        shutil.move(tempfile.name, input_csv)
    else:
        print("File has already been run!")

### MAIN PROGRAM 
def main():
    print("Dex Moves Scraping tool v0.1\n")
    print("--> Starting Web Scraper...")

    amend_file("../data/all.csv")
    amend_file("../data/gen1.csv")
    amend_file("../data/gen2.csv")
    amend_file("../data/gen3.csv")
    amend_file("../data/gen4.csv")
    amend_file("../data/gen5.csv")
    amend_file("../data/gen6.csv")
    amend_file("../data/gen7.csv")
    amend_file("../data/gen8.csv")
    amend_file("../data/crown_tundra.csv")
    amend_file("../data/isle_of_armor.csv")
    amend_file("../data/sword_shield_non_indexed.csv")
    amend_file("../data/sword_shield.csv")

main() #run when file is run
