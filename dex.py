from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv

def mainDex():
    data = []
    # add header
    data.append(['Dex Num', 'Name','Types', 'Abilities', 'HP', 'ATTACK', 'DEFENSE', 'S. ATTACK', 'S. DEFENSE', 'SPEED'])

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
    myFile = open('all.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)

    print('Done!')
    return 0


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


def main():
    print("Dex Scraping tool v0.1\n")

    print("------- CREATE MAIN DEX -------")
    mainDex()

main()