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
    else:
        return name

def getMoves(poke_name):
    poke_name = exceptions(poke_name)
    url = "https://marriland.com/pokedex/"+poke_name.lower()+"/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    moves = []

    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e)
    except URLError:
        print("ERR: " + poke_name + " didn't work right")
    else:
        print("--> Server connected!")
        print("--> Copying HTML from " + url)
        res = BeautifulSoup(html.read(),"html5lib")
        for node in res.findAll("div", attrs={"data-move-name":True}):
            moves.append(node.findAll(text=True)[0])

    return moves


def main(input_csv):
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

main("all.csv")