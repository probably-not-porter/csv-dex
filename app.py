import os
from flask import Flask, render_template
import csv

app = Flask(__name__)


results = []
with open("data/base_dex_890.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

results2 = []
with open("data/combat_dex_890.csv") as csvfile:
    reader2 = csv.reader(csvfile) # change contents to floats
    for row in reader2: # each row is a list
        results2.append(row)


@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", data=results, data2=results2);   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)