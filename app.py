import os
from flask import Flask, render_template
import csv
import codecs


app = Flask(__name__)


results = []
with open("data/all.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    print(reader)
    for row in reader: # each row is a list
        results.append(row)

chart_data = {
    "normal": {
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "fighting": {
        "normal": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "flying": {
        "normal": 0,
        "fighting": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "poison": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "ground": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "rock": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "bug": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "ghost": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "steel": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "fire": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "water": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "grass": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "electric": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "psychic": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "ice": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "dragon": 0,
        "dark": 0,
        "fairy": 0
    },
    "dragon": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dark": 0,
        "fairy": 0
    },
    "dark": {
        "normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "fairy": 0
    },
    "fairy": {"normal": 0,
        "fighting": 0,
        "flying": 0,
        "poison": 0,
        "ground": 0,
        "rock": 0,
        "bug": 0,
        "ghost": 0,
        "steel": 0,
        "fire": 0,
        "water": 0,
        "grass": 0,
        "electric": 0,
        "psychic": 0,
        "ice": 0,
        "dragon": 0,
        "dark": 0
    }
}
colors = {
    "normal": "#A8A77A",
    "fighting": "#C22E28",
    "flying": "#A98FF3",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "rock": "#B6A136",
    "bug": "#A6B91A",
    "ghost": "#735797",
    "steel": "#B7B7CE",
    "fire": "#EE8130",
    "water": "#6390F0",
    "grass": "#7AC74C",
    "electric": "#F7D02C",
    "psychic": "#F95587",
    "ice": "#96D9D6",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "fairy": "#D685AD"
}
type_totals = {
    "normal": 0,
    "fighting": 0,
    "flying": 0,
    "poison": 0,
    "ground": 0,
    "rock": 0,
    "bug": 0,
    "ghost": 0,
    "steel": 0,
    "fire": 0,
    "water": 0,
    "grass": 0,
    "electric": 0,
    "psychic": 0,
    "ice": 0,
    "dragon": 0,
    "dark": 0,
    "fairy": 0
}

for x in results:
    types = x[2].replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")
    types.sort()
    if "Type" not in types:
        for y in range(len(types)):
            type_totals[types[y]] += 1

        if len(types) == 2:
            chart_data[types[0]][types[1]] += 1


@app.route("/")
def index():
    return render_template("index.html", message="Home", data=results);   

@app.route("/vis1")
def vis1():
    return render_template("vis1.html", message="Vis 1", data=[chart_data, colors]); 

@app.route("/vis2")
def vis2():
    return render_template("vis2.html", message="Vis 2", data=[type_totals, colors]); 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)