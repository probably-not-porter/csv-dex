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
from tqdm import tqdm

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
    else:
        return name

def getMoves(poke_name):
    poke_name = exceptions(poke_name)
    url = "https://pokemondb.net/pokedex/"+poke_name.lower().replace(" ", "-")
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

    length = 0
    with open(input_csv) as f:
        length = sum(1 for line in f)
    
    pbar = tqdm(total=length, desc=input_csv)
    with open(input_csv) as csvfile, tempfile:
        reader = csv.reader(csvfile) # change contents to floats
        writer = csv.writer(tempfile)
        title_flag = False
        loop_check = False

        for row in reader: # each row is a list
            pbar.update(1)
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
def scrape_dex_moves(location):
    print("=== Add moves to dex CSVs ===")

    amend_file(location +"/all.csv")
    amend_file(location +"/gen1.csv")
    amend_file(location +"/gen2.csv")
    amend_file(location +"/gen3.csv")
    amend_file(location +"/gen4.csv")
    amend_file(location +"/gen5.csv")
    amend_file(location +"/gen6.csv")
    amend_file(location +"/gen7.csv")
    amend_file(location +"/gen8.csv")
    amend_file(location +"/gen9.csv")
    print("Done!\n")