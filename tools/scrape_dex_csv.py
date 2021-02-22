from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import numpy as np
import csv
import string
import re

ascii = set(string.printable)  

"""
    This is step one of data collection.
    This will create files based on urls entered
    for data scraping from Serebii.
"""

### DEX CSV BUILDERS
def buildDex(url_ls, filename):
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
                        
                        if "♂" in stats[2].getText().replace("\n", ""): # specifically for the nidorans
                            name += "-m"
                        elif "♀" in stats[2].getText().replace("\n", ""):
                            name += "-f"
                        if "Flabébé" in stats[2].getText().replace("\n", ""): # for flabebe
                            name = "Flabebe"

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
    myFile = open(filename, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    print('Done!')

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
    type_dictionary = ['normal','fighting','flying','poison','ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic','ice','dragon','fairy','dark']
    output = {
        'defensive': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0
        },
        'offensive': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0
        }
    }
    matchup_dictionary = {
        'normal': {
            'normal': 1.0,
            'fighting': 2.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 0.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'fighting': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 2.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 0.5,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 2.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 2.0,
            'dark': 0.5,
        },
        'flying': {
            'normal': 1.0,
            'fighting': 0.5,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 0.0,
            'rock': 2.0,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 0.5,
            'electric': 2.0,
            'psychic': 1.0,
            'ice': 2.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'poison': {
            'normal': 1.0,
            'fighting': 0.5,
            'flying': 1.0,
            'poison': 0.5,
            'ground': 2.0,
            'rock': 1.0,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 0.5,
            'electric': 1.0,
            'psychic': 2.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 0.5,
            'dark': 1.0,
        },
        'ground': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 0.5,
            'ground': 1.0,
            'rock': 0.5,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 2.0,
            'grass': 2.0,
            'electric': 0.0,
            'psychic': 1.0,
            'ice': 2.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'rock': {
            'normal': 0.5,
            'fighting': 2.0,
            'flying': 0.5,
            'poison': 0.5,
            'ground': 2.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 2.0,
            'fire': 0.5,
            'water': 2.0,
            'grass': 2.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'bug': {
            'normal': 1.0,
            'fighting': 0.5,
            'flying': 2.0,
            'poison': 1.0,
            'ground': 0.5,
            'rock': 2.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 2.0,
            'water': 1.0,
            'grass': 0.5,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'ghost': {
            'normal': 0.0,
            'fighting': 0.0,
            'flying': 1.0,
            'poison': 0.5,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 0.5,
            'ghost': 2.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 2.0,
        },
        'steel': {
            'normal': 0.5,
            'fighting': 2.0,
            'flying': 0.5,
            'poison': 0.0,
            'ground': 2.0,
            'rock': 0.5,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 0.5,
            'fire': 2.0,
            'water': 1.0,
            'grass': 0.5,
            'electric': 1.0,
            'psychic': 0.5,
            'ice': 0.5,
            'dragon': 0.5,
            'fairy': 0.5,
            'dark': 1.0,
        },
        'fire': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 2.0,
            'rock': 2.0,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 0.5,
            'fire': 0.5,
            'water': 2.0,
            'grass': 0.5,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 0.5,
            'dragon': 1.0,
            'fairy': 0.5,
            'dark': 1.0,
        },
        'water': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 0.5,
            'fire': 0.5,
            'water': 0.5,
            'grass': 2.0,
            'electric': 2.0,
            'psychic': 1.0,
            'ice': 0.5,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'grass': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 2.0,
            'poison': 2.0,
            'ground': 0.5,
            'rock': 1.0,
            'bug': 2.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 2.0,
            'water': 0.5,
            'grass': 0.5,
            'electric': 0.5,
            'psychic': 1.0,
            'ice': 2.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'electric': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 0.5,
            'poison': 1.0,
            'ground': 2.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 0.5,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 0.5,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'psychic': {
            'normal': 1.0,
            'fighting': 0.5,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 2.0,
            'ghost': 2.0,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 0.5,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 2.0,
        },
        'ice': {
            'normal': 1.0,
            'fighting': 2.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 2.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 2.0,
            'fire': 2.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 0.5,
            'dragon': 1.0,
            'fairy': 1.0,
            'dark': 1.0,
        },
        'dragon': {
            'normal': 1.0,
            'fighting': 1.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 1.0,
            'ghost': 1.0,
            'steel': 1.0,
            'fire': 0.5,
            'water': 0.5,
            'grass': 0.5,
            'electric': 0.5,
            'psychic': 1.0,
            'ice': 2.0,
            'dragon': 2.0,
            'fairy': 2.0,
            'dark': 1.0,
        },
        'fairy': {
            'normal': 1.0,
            'fighting': 0.5,
            'flying': 1.0,
            'poison': 2.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 0.5,
            'ghost': 1.0,
            'steel': 2.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 1.0,
            'ice': 1.0,
            'dragon': 0.0,
            'fairy': 1.0,
            'dark': 0.5,
        },
        'dark': {
            'normal': 1.0,
            'fighting': 2.0,
            'flying': 1.0,
            'poison': 1.0,
            'ground': 1.0,
            'rock': 1.0,
            'bug': 2.0,
            'ghost': 0.5,
            'steel': 1.0,
            'fire': 1.0,
            'water': 1.0,
            'grass': 1.0,
            'electric': 1.0,
            'psychic': 0.0,
            'ice': 1.0,
            'dragon': 1.0,
            'fairy': 2.0,
            'dark': 0.5,
        }
    }
    for x in types:
        for y in type_dictionary:
            output['defensive'][y] *= matchup_dictionary[x][y]
            output['offensive'][y] *= matchup_dictionary[y][x]

    out_str = [
        [], # strong against
        [], # weak against
        [], # resistant to
        []  # vulnerable to
    ]
    for x in type_dictionary:
        if output['offensive'][x] > 1.0: #strong against
            out_str[0].append(x)
        elif output['offensive'][x] < 1.0: # weak against
            out_str[1].append(x)

        if output['defensive'][x] < 1.0: # resistant to
            out_str[2].append(x)
        elif output['defensive'][x] > 1.0: # vulnerable to
            out_str[3].append(x)
    return out_str
        

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
    print("Dex Data Scraping tool v0.3\n")
    print("--> Starting Web Scraper...")

    buildDex(["https://www.serebii.net/pokemon/nationalpokedex.shtml"], "../data/all.csv") 
    buildDex(["https://www.serebii.net/pokemon/gen1pokemon.shtml"], "../data/gen1.csv")
    buildDex(["https://www.serebii.net/pokemon/gen2pokemon.shtml"], "../data/gen2.csv")
    buildDex(["https://www.serebii.net/pokemon/gen3pokemon.shtml"], "../data/gen3.csv")
    buildDex(["https://www.serebii.net/pokemon/gen4pokemon.shtml"], "../data/gen4.csv")
    buildDex(["https://www.serebii.net/pokemon/gen5pokemon.shtml"], "../data/gen5.csv")
    buildDex(["https://www.serebii.net/pokemon/gen6pokemon.shtml"], "../data/gen6.csv")
    buildDex(["https://www.serebii.net/pokemon/gen7pokemon.shtml"], "../data/gen7.csv")
    buildDex(["https://www.serebii.net/pokemon/gen8pokemon.shtml"], "../data/gen8.csv")
    buildDex(["https://www.serebii.net/swordshield/galarpokedex.shtml"], "../data/sword_shield.csv")
    buildDex(["https://www.serebii.net/swordshield/isleofarmordex.shtml"], "../data/isle_of_armor.csv")
    buildDex(["https://www.serebii.net/swordshield/thecrowntundradex.shtml"], "../data/crown_tundra.csv")
    buildDex(["https://www.serebii.net/swordshield/pokemonnotindex.shtml"], "../data/sword_shield_non_indexed.csv")

main() #run when file is run


