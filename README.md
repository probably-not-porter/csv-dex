# Dex 

## Data
Here is a table of contents for the data I compiled:

![img](static/shiny/lugia.png)[International Dex [main] (csv)](data/base_dex_890.csv)

![img](static/shiny/blaziken.png)[Internaltional Dex [combat] (csv)](data/combat_dex_890.csv)

![img](static/shiny/ho-oh.png)[ GEN8 Galar Dex [main] (csv)](data/base_dex_galar.csv)

![img](static/shiny/meganium.png)[ GEN8 Galar Dex [combat] (csv)](data/combat_dex_galar.csv)

![img](static/shiny/bulbasaur.png)[ GEN1 Kanto Dex [main] (csv)](data/base_dex_kanto.csv)

![img](static/shiny/wartortle.png)[GEN1 Kanto Dex [combat] (csv)](data/combat_dex_kanto.csv)

![img](static/shiny/typhlosion.png)[GEN2 Johto Dex [main] (csv)](data/base_dex_johto.csv)

![img](static/shiny/umbreon.png)[GEN2 Johto Dex [combat] (csv)](data/combat_dex_johto.csv)

![img](static/regular/charizard.png)[Regular Sprites](dex_images.md#regular-sprites)

![img](static/shiny/charizard.png)[Shiny Sprites](dex_images.md#shiny-sprites)

![img](static/shiny/empoleon.png)[Type Badges](dex_images.md#type-badges)


Using the information from serebii to create a generalized CSV of pokemon data. I wanted a better way to see combat related stats quickly while playing Pokemon so I made this set of tools, including an automated data collector with a web scraper to fetch states of pokemon, and generate additional reference data.

# Usage
## Installation 
1. Use `pip` to install the project dependencies. Make sure you are using the `python3` environment.
2. Clone this project to your local machine

## Creating Data
`python3 dex_gen.py` will create a set of data CSV files, which are based on web scraped info from Serebii.

## Using Data
`python3 dex_app.py` will start a Flask server running a web app version of the CSV data generated.


## Dependencies
- BeautifulSoup4
- urllib
- tablib
- csv
- flask
- numpy


## Information

## References/Sources
- https://github.com/msikma/pokesprite
- https://www.serebii.net/

## Liscenses
The source icons are © Nintendo/Creatures Inc./GAME FREAK Inc.

Everything else, and usage of the programming code, is governed by the MIT license.