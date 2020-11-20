from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import numpy as np
import csv
import string
import re

import wr_chart as wr_chart


ascii = set(string.printable)  

### DEX CSV BUILDERS
def buildDex(url_ls):
    data = []
    # add header
    data.append(['Dex', 'Name','Type', 'Abilities', 'HP', 'A', 'D', 'SA', 'SD', 'SP', 'Strong Against', 'Weak Against', 'Resistant To', 'Vulnerable To', 'base stat total', 'base stat avg'])
    count = 0

    for url in url_ls:
        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError:
            print("ERR: Server down or incorrect domain")
        else:
            print("--> Server connected!")
            print("--> Copying HTML from " + url)

            res = BeautifulSoup(html.read(),"html5lib")
            tags = res.findAll("table", {"class": "dextable"})
            if (tags == []):
                tags = res.findAll("table", {"class": "tab"})
                
            print("--> Done!")
            print("--> Filtering...")
            for tag in tags:
                inf = tag.findAll("tr")
                for i in range(2, len(inf)): # This step is iterating over the length of the pokedex, basically. (call this pokemon N)
                    duplicate = False
                    stats = inf[i].findAll("td", {"class": "fooinfo"})

                    if stats != [] and len(url_ls) > 1: # check to make sure there arent any duplicates for multiple URLS
                        for item in data:
                            for attr in item:
                                if attr == stats[2].getText().replace("\n", "").replace("\t", ""):
                                    duplicate = True


                    if stats != [] and duplicate == False:
                        count = count + 1 # the element is a pokedex entry
                        # pokedex N dex number (string)
                        dexnum = stats[0].getText().replace("\n", "").replace("\t", "")

                        # pokemon N name (string)
                        name = (re.sub("([^\x00-\x7F])+"," ", stats[2].getText().replace("\n", "").replace("\t", "")).strip())

                        # pokemon N types (array of types)
                        imgs = stats[3].findAll("img")
                        types = genTypeArray(imgs)

                        # pokemon N ability (array of abilities)
                        ability = []
                        ability_ = stats[4]
                        abil = ability_.findAll("a")
                        for ab in abil:
                            new_ability = ab.getText().replace("\n", "").replace("\t", "")
                            ability.append(new_ability)

                        # pokemon N HP base stat (int)
                        health = stats[5].getText().replace("\n", "")
                        attack = stats[6].getText().replace("\n", "")
                        defense = stats[7].getText().replace("\n", "")
                        sattack = stats[8].getText().replace("\n", "")
                        sdefense = stats[9].getText().replace("\n", "")
                        speed = stats[10].getText().replace("\n", "")

                        # pokemon N attacking modifiers
                        attk_matchups = genWeaknessResistance(types)
                        

                        # pokemon N stat total and avg
                        total = int(health) + int(attack) + int(defense) + int(sattack) + int(sdefense) + int(speed)
                        avg = total // 6
                        

                        # create row
                        data_item = []
                        data_item.append(dexnum)
                        data_item.append(name)
                        data_item.append(str(types))
                        data_item.append(str(ability))
                        data_item.append(health)
                        data_item.append(attack)
                        data_item.append(defense)
                        data_item.append(sattack)
                        data_item.append(sdefense)
                        data_item.append(speed)
                        data_item.append(attk_matchups[0])
                        data_item.append(attk_matchups[1])
                        data_item.append(attk_matchups[2])
                        data_item.append(attk_matchups[3])
                        data_item.append(total)
                        data_item.append(avg)

                        # append row
                        data.append(data_item)
    print("--> Done!")
    print("--> creating CSV...")
    # create datafile
    myFile = open('raw_dex_output'+ str(count) +'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    print('Done!')
    return data

### UTIL
def genTypeArray(imgs): # create an array of types out of the type data from dex info
    types = []
    for image in imgs:
        img = str(image)
        if "normal" in img:
            types.append("normal")
        elif "fighting" in img:
            types.append("fighting")
        elif "flying" in img:
            types.append("flying")
        elif "poison" in img:
            types.append("poison")
        elif "ground" in img:
            types.append("ground")
        elif "rock" in img:
            types.append("rock")
        elif "bug" in img:
            types.append("bug")
        elif "ghost" in img:
            types.append("ghost")
        elif "steel" in img:
            types.append("steel")
        elif "fire" in img:
            types.append("fire")
        elif "water" in img:
            types.append("water")
        elif "grass" in img:
            types.append("grass")
        elif "electric" in img:
            types.append("electric")
        elif "psychic" in img:
            types.append("psychic")
        elif "ice" in img:
            types.append("ice")
        elif "dragon" in img:
            types.append("dragon")
        elif "dark" in img:
            types.append("dark")
        elif "fairy" in img:
            types.append("fairy")
        else:
            print("error")
    return types

def genWeaknessResistance(types):
    matchup_dictionary = {
        'normal': [
            [],
            ['rock','ghost','steel'],
            ['ghost'],
            ['fighting']
        ],
        'fighting': [
            ['normal', 'rock', 'steel', 'ice', 'dark'],
            ['flying', 'poison', 'psychic', 'bug', 'ghost', 'fairy'],
            ['rock', 'bug', 'ghost'],
            ['flying', 'psychic', 'fairy']
        ],
        'flying': [
            ['fighting', 'bug', 'grass'],
            ['rock', 'steel', 'electric'],
            ['fighting', 'ground','bug','grass'],
            ['rock', 'electric', 'ice']
        ],
        'poison': [
            ['grass', 'fairy'],
            ['poison', 'ground', 'rock', 'steel', 'ghost'],
            ['fighting', 'poison', 'grass', 'fairy', 'bug'],
            ['ground', 'psychic']
        ],
        'ground': [
            ['poison', 'rock', 'steel', 'fire', 'electric'],
            ['flying', 'bug', 'grass'],
            ['poison', 'rock', 'electric'],
            ['water', 'ice', 'grass']
        ],
        'rock': [
            ['flying', 'bug', 'fire', 'ice'],
            ['fighting', 'ground', 'steel'],
            ['normal', 'flying', 'poison', 'fire'],
            ['fighting', 'ground', 'steel', 'water', 'grass']
        ],
        'bug': [
            ['grass', 'psychic', 'dark'],
            ['fighting', 'flying', 'poison', 'ghost', 'steel', 'fire', 'fairy'],
            ['fighting', 'ground', 'grass'],
            ['flying', 'rock', 'fire']
        ],
        'ghost': [
            ['ghost', 'psychic'],
            ['normal', 'dark'],
            ['normal', 'fighting', 'poison', 'bug'],
            ['ghost', 'dark']
        ],
        'steel': [
            ['rock', 'ice', 'fairy'],
            ['steel', 'fire', 'water', 'electric'],
            ['normal', 'flying', 'poison', 'rock', 'bug', 'steel', 'grass', 'psychic', 'ice', 'dragon', 'fairy'],
            ['fighting', 'ground', 'fire']
        ],
        'fire': [
            ['bug', 'steel', 'grass', 'ice'],
            ['rock', 'fire', 'water', 'dragon'],
            ['bug', 'steel', 'fire', 'grass', 'ice'],
            ['ground', 'rock', 'water']
        ],
        'water': [
            ['ground', 'rock', 'fire'],
            ['water', 'grass', 'dragon'],
            ['steel', 'fire', 'water', 'ice'],
            ['grass', 'electric']
        ],
        'grass': [
            ['ground', 'rock', 'water'],
            ['flying', 'poison', 'bug', 'steel', 'fire', 'grass', 'dragon'],
            ['ground', 'water', 'grass', 'electric'],
            ['flying', 'poison', 'bug', 'fire', 'ice']
        ],
        'electric': [
            ['flying', 'water'],
            ['ground', 'grass', 'electric', 'dragon'],
            ['flying', 'steel', 'electric'],
            ['ground']
        ],
        'psychic': [
            ['fighting', 'poison'],
            ['steel', 'dark', 'psychic'],
            ['fighting', 'psychic'],
            ['bug', 'ghost', 'dark']
        ],
        'ice': [
            ['flying', 'ground', 'grass', 'dragon'],
            ['steel', 'fire', 'water', 'ice'],
            ['ice'],
            ['fighting', 'rock', 'steel', 'fire']
        ],
        'dragon': [
            ['dragon'],
            ['steel', 'fairy'],
            ['fire', 'water', 'grass', 'electric'],
            ['ice', 'dragon', 'fairy']
        ],
        'fairy': [
            ['fighting', 'dragon', 'dark'],
            ['poison', 'steel', 'fire'],
            ['fighting', 'bug', 'dragon', 'dark'],
            ['poison', 'steel']
        ],
        'dark': [
            ['ghost', 'psychic'],
            ['fighting', 'dark', 'fairy'],
            ['ghost', 'psychic', 'dark'],
            ['fighting', 'bug', 'fairy']
        ]
    }
    if len(types) == 1:
        return matchup_dictionary[types[0]] # simple as dat
    elif len(types) == 2:
        new_matchup = [
            list(dict.fromkeys(matchup_dictionary[types[0]][0] + matchup_dictionary[types[1]][0])),
            list(dict.fromkeys(matchup_dictionary[types[0]][1] + matchup_dictionary[types[1]][1])),
            list(dict.fromkeys(matchup_dictionary[types[0]][2] + matchup_dictionary[types[1]][2])),
            list(dict.fromkeys(matchup_dictionary[types[0]][3] + matchup_dictionary[types[1]][3])),
        ]

        for t in new_matchup[0]:
            if t in new_matchup[1]:
                new_matchup[0].remove(t)
                new_matchup[1].remove(t)

        for t in new_matchup[2]:
            if t in new_matchup[3]:
                new_matchup[2].remove(t)
                new_matchup[3].remove(t)

        return new_matchup
    else:
        print("ERR: invalid type array")

def remove_non_ascii(s):
    return str(filter(lambda x: x in ascii, s))

def getComposite(arr_1, arr_2):
    if len(arr_1) == len(arr_2):
        new_arr = []
        for x in range(len(arr_1)):
            if arr_1[x] == arr_2[x]:
                new_arr.append(arr_1[x])
            else:
                new_arr.append(arr_1[x] * arr_2[x])
        return new_arr

    else:
        print("ERR: Types are not same length")

def typeToNum(typestring):
    typestring = typestring.replace(" ", "")
    if typestring == "normal":
        return 0
    elif typestring == "fire":
        return 1
    elif typestring == "water":
        return 2
    elif typestring == "electric":
        return 3
    elif typestring == "grass":
        return 4
    elif typestring == "ice":
        return 5
    elif typestring == "fighting":
        return 6
    elif typestring == "poison":
        return 7
    elif typestring == "ground":
        return 8
    elif typestring == "flying":
        return 9
    elif typestring == "psychic":
        return 10
    elif typestring == "bug":
        return 11
    elif typestring == "rock":
        return 12
    elif typestring == "ghost":
        return 13
    elif typestring == "dragon":
        return 14
    elif typestring == "dark":
        return 15
    elif typestring == "steel":
        return 16
    elif typestring == "fairy":
        return 17
    else:
        print('ERR: invalid type in typeToNum conversion')

def numToType (num):
    types = ["normal", "fire", "water", "electric",
    "grass", "ice", "fighting", "poison", "ground",
    "flying", "psychic", "bug", "rock", "ghost",
    "dragon", "dark", "steel", "fairy"]
    return types[num]
 
### MAIN PROGRAM 
def main(): # do all the things in the order
    url_ls = [
        "https://www.serebii.net/pokemon/nationalpokedex.shtml"
    ]
    print("Dex Data Scraping tool v0.3\n")
    print("--> Starting Web Scraper...")
    base_data = buildDex(url_ls) # generate base dex and return data

main() #run when file is run