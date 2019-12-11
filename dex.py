from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import numpy as np
import csv

import wr_chart


### DEX CSV BUILDERS
def baseDex():
    data = []
    # add header
    data.append(['Dex Num', 'Name','Types', 'Abilities', 'HP', 'ATTACK', 'DEFENSE', 'S. ATTACK', 'S. DEFENSE', 'SPEED'])
    count = 0
    try:
        html = urlopen("https://www.serebii.net/pokemon/all.shtml")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        print("Server connected!")
        print("Copying HTML...")

        res = BeautifulSoup(html.read(),"html5lib")
        tags = res.findAll("table", {"class": "dextable"})
        print("Done!")
        print("Filtering...")

        for tag in tags:
            inf = tag.findAll("tr")
            for i in range(2, len(inf)): # This step is iterating over the length of the pokedex, basically. (call this pokemon N)
                stats = inf[i].findAll("td", {"class": "fooinfo"})
                if stats != []:
                    count = count + 1 # the element is a pokedex entry
                    # pokedex N dex number (string)
                    dexnum = stats[0].getText().replace("\n", "").replace("\t", "")

                    # pokemon N name (string)
                    name = stats[2].getText().replace("\n", "").replace("\t", "")

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
                    data.append(data_item)
    print("Done!")
    print("creating CSV...")
    # create datafile
    myFile = open('base_dex_'+ str(count) +'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    print('Done!')
    return data

def combatDex(data):
    new_data = []
     # add header
    new_data.append(['Dex Num', 'Super Effective (attacking)', 'Not Very Effective (attacking)'])
    count = 0
    for item in range(1, len(data)):
        new_data_line = []
        count = count + 1

        # Pokemon N dex number for reference
        dexnum = data[item][0]
        new_data_line.append(dexnum)

        # Pokemon N name for reference
        name = data[item][1]
        new_data_line.append(name)

        # pokemon N attacking modifiers
        types = data[item][2]
        attk_matchups = genWeaknessResistance(types)
        new_data_line.append(attk_matchups[0])
        new_data_line.append(attk_matchups[1])


        new_data.append(new_data_line)
        
    # create datafile
    myFile = open('combat_dex_'+ str(count) +'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(new_data)

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
            types.append("ice ")
        elif "dragon" in img:
            types.append("dragon")
        elif "dark" in img:
            types.append("dark")
        elif "fairy" in img:
            types.append("fairy")
        else:
            print("error")
    return types

def genWeaknessResistance(types_string):
    types = types_string.strip("][").replace("'","").split(', ') 
    if len(types) == 0:
        print("ERR: found 0 types")
    elif len(types) == 1:
        typenum = typeToNum(types[0])
        se_chart = wr_chart.matrix[typenum] # pokemon N is super effective against these things
        se_against = []
        nve_against = []
        for matchup_ind in range(len(se_chart)):
            if se_chart[matchup_ind] < 1:
                nve_against.append(numToType(matchup_ind))
            elif se_chart[matchup_ind] > 1:
                se_against.append(numToType(matchup_ind))
        return [se_against, nve_against]
    elif len(types) == 2:
        typenum_1 = typeToNum(types[0])
        typenum_2 = typeToNum(types[1])
        se_chart = getComposite(wr_chart.matrix[typenum_1], wr_chart.matrix[typenum_2])
        se_against = []
        nve_against = []
        for matchup_ind in range(len(se_chart)):
            if se_chart[matchup_ind] < 1:
                nve_against.append(numToType(matchup_ind))
            elif se_chart[matchup_ind] > 1:
                se_against.append(numToType(matchup_ind))
        return [se_against, nve_against]
    else:
        print("ERR: invalid type array")

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
    print("Dex Data tool v0.1\n")
    print("------- CREATE BASE DEX -------")
    base_data = baseDex() # generate base dex and return data

    print("------- CREATE ADDITIONAL INFO DEX --------")
    combatDex(base_data)


main() #run when file is run