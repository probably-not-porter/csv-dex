# Dex: CSV Pokemon Data
Using webscraping and algorithmic content generation, I have created the following datasets. If they are of use to you, please feel free to use them (under the terms of the MIT open source license)

![img](static/shiny/lugia.png) All Gens: [International Dex [main] (csv)](data/base_dex_890.csv) && [Internaltional Dex [combat] (csv)](data/combat_dex_890.csv)

![img](static/shiny/ditto.png) Gen 8: [ Galar Dex [main] (csv)](data/base_dex_galar.csv) && [ Galar Dex [combat] (csv)](data/combat_dex_galar.csv)

![img](static/shiny/empoleon.png) Gen 4: [Sinnoh Dex [main] (csv)](data/base_dex_sinnoh.csv) && [Sinnoh Dex [combat] (csv)](data/combat_dex_sinnoh.csv)

![img](static/shiny/sceptile.png) Gen 3: [Hoenn Dex [main] (csv)](data/base_dex_hoenn.csv) && [Hoenn Dex [combat] (csv)](data/combat_dex_hoenn.csv)

![img](static/shiny/typhlosion.png) Gen 2: [Johto Dex [main] (csv)](data/base_dex_johto.csv) && [Johto Dex [combat] (csv)](data/combat_dex_johto.csv)

![img](static/shiny/blastoise.png) Gen 1: [ Kanto Dex [main] (csv)](data/base_dex_kanto.csv) && [Kanto Dex [combat] (csv)](data/combat_dex_kanto.csv)

![img](static/regular/rayquaza.png)[Regular Sprites](dex_images.md#regular-sprites) (no Galar sprites)

![img](static/shiny/rayquaza.png)[Shiny Sprites](dex_images.md#shiny-sprites) (no Galar sprites)

![img](static/shiny/regigigas.png)[Type Badges](dex_images.md#type-badges) 


Using the information from serebii to create a generalized CSV of pokemon data. I wanted a better way to see combat related stats quickly while playing Pokemon so I made this set of tools, including an automated data collector with a web scraper to fetch states of pokemon, and generate additional reference data.

# Usage
## Installation 
1. Use `pip` to install the project dependencies. Make sure you are using the `python3` environment.
2. Clone this project to your local machine

## Creating Data
`python3 dex_gen.py` will create a set of data CSV files, which are based on web scraped info from Serebii.

`python3 util/create_dex_md.py` will create a readme of a directory full of sprites, effectively creating a markdown version of a sprite sheet. Used this to create the `dex_images.md` resource.

`util/wr_chart.py` contains a python version of nintendos weakness and resistance matrix, which is used to comput combat values in `dex_gen.py`.

`util/vis.py` (coming soon) 

## Using Data
`python3 dex_app.py` will start a Flask server running a web app version of the CSV data generated.


## Dependencies
- BeautifulSoup4 (4.8.1)
- Flask (1.0.3)
  
(full dependencies can be found in `requirements.txt`)

## Information

## References/Sources
- https://github.com/msikma/pokesprite
- https://www.serebii.net/

## Liscenses
The source icons are © Nintendo/Creatures Inc./GAME FREAK Inc.

Everything else, and usage of the programming code, is governed by the MIT license.