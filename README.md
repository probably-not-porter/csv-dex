# ![img](static/master.png) Dex 0.5.3
Porter Libby, 2020

I have collected this data in CSV format so that it can be used for small projects and useful tools. This information is not to be used for profit, but it is available to anyone and everyone who wishes to make something neat under the MIT license. 

It should also be understood that this is NOT my data. It is data created by Nintendo and Game Freak, and collected/harvested by Serebii and PokemonDB.

Please send me links to anything cool to make with this data; I'd love to see it.

# ![img](static/master.png) CSV Data

## Full International Dex
![img](static/regular/darkrai.png) [Full International Dex (898) (CSV)](data/all.csv)

## Dex by Generation
![img](static/regular/charizard.png) [Generation 1 Dex (151) (CSV)](data/gen1.csv)
![img](static/regular/typhlosion.png) [Generation 2 Dex (100) (CSV)](data/gen2.csv)

![img](static/regular/blaziken.png) [Generation 3 Dex (136) (CSV)](data/gen3.csv)
![img](static/regular/infernape.png) [Generation 4 Dex (107) (CSV)](data/gen4.csv)

![img](static/regular/emboar.png) [Generation 5 Dex (156) (CSV)](data/gen5.csv)
![img](static/regular/delphox.png) [Generation 6 Dex (72) (CSV)](data/gen6.csv)

![img](static/regular/incineroar.png) [Generation 7 Dex (88) (CSV)](data/gen7.csv)
![img](static/shiny/cinderace.png) [Generation 8 Dex (89) (CSV)](data/gen8.csv)

## Dex by Game
![img](static/regular/eternatus.png) [Sword / Shield (400) (CSV)](data/sword_shield.csv)
![img](static/regular/urshifu.png) [Isle of Armor (211) (CSV)](data/isle_of_armor.csv)

![img](static/regular/calyrex.png) [Crown Tundra (210) (CSV)](data/crown_tundra.csv)
![img](static/regular/arceus.png) [Sw / Sh Non-Indexed (68) (CSV)](data/sword_shield_non_indexed.csv)

## Full Move List
![img](static/regular/cresselia.png) [Full Move List (CSV)](data/all_moves.csv)

## Moves by Generation
![img](static/regular/blastoise.png) [Generation 1 Moves (CSV)](data/gen1-moves.csv)
![img](static/regular/feraligatr.png) [Generation 2 Moves (CSV)](data/gen2-moves.csv)

![img](static/regular/swampert.png) [Generation 3 Moves (CSV)](data/gen3-moves.csv)
![img](static/regular/empoleon.png) [Generation 4 Moves (CSV)](data/gen4-moves.csv)

![img](static/regular/samurott.png) [Generation 5 Moves (CSV)](data/gen5-moves.csv)
![img](static/regular/greninja.png) [Generation 6 Moves (CSV)](data/gen6-moves.csv)

![img](static/regular/primarina.png) [Generation 7 Moves (CSV)](data/gen7-moves.csv)
![img](static/shiny/inteleon.png) [Generation 8 Moves (CSV)](data/gen8-moves.csv)

## Sprite Catalogues
![img](static/regular/rayquaza.png)[Regular Sprites](data/normal_sprites.md) 
![img](static/shiny/rayquaza.png)[Shiny Sprites](data/shiny_sprites.md) 
![img](static/regular/kyogre.png)[Type Badges](data/type_badges.md) 


# ![img](static/master.png) Tools
![img](static/regular/lugia.png) [CSV Dex Scraping Tool (py)](tools/scrape_dex_csv.py)
![img](static/regular/mewtwo.png) [CSV Dex Move Ammender (py)](tools/scrape_dex_moves.py)

![img](static/regular/suicune.png) [CSV Move Scraping Tool (py)](tools/scrape_move_list.py)

![img](static/regular/ho-oh.png) [Dex Data Visualizer (py) (WIP)](tools/vis_dex_data.py)
![img](static/regular/mew.png) [Stat Anylsis Tool (py) (WIP)](tools/analysis.py)

![img](static/regular/moltres.png) [Weakness/Resistance Chart (py)](tools/wr_chart.py)
![img](static/regular/zapdos.png) [Image Markdown Dex Tool (py)](tools/gen_sprite_md.py)

# ![img](static/master.png) Dex

- http://combat-dex.herokuapp.com/

Dex is my personal project using this data. Written in Flask with Python, I used this data to create a different kind of pokedex which could be used quickly and efficiently while in combat in a game. This is the main time that I use a pokedex, and typically it takes me a lot of time to find the exact information I'm looking for. With online play and battle timers, I needed something to fit my needs, so I made it.

I will also be hosting several small tools I create here; diagrams and charts and different interactive bits that I like. I will attempt to keep track of them here:

- http://combat-dex.herokuapp.com/vis

# ![img](static/master.png) Usage
## Installation 
1. Use `pip` to install the project dependencies. Make sure you are using the `python3` environment.
2. Clone this project to your local machine


## Dependencies
- BeautifulSoup4 (4.8.1)
- Flask (1.0.3)
  
(full dependencies can be found in `requirements.txt`)


# ![img](static/master.png) References/Sources
- https://github.com/msikma/pokesprite
- https://www.serebii.net/
- https://pokemondb.net/

# ![img](static/master.png) Licenses
The source icons are © Nintendo/Creatures Inc./GAME FREAK Inc.

Everything else, and usage of the programming code, is governed by the MIT license.