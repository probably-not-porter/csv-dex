# Dex 
![img](static/shiny/raichu.png)![img](static/shiny/swampert.png)![img](static/shiny/crobat.png)![img](static/shiny/shiftry.png)![img](static/shiny/banette.png)![img](static/shiny/swellow.png)</br>
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


## Information

## References
https://github.com/msikma/pokesprite