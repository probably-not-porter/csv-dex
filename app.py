import os
from flask import Flask, render_template
import csv

app = Flask(__name__)


results = []
with open("data/all.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)


@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", data=results);   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)