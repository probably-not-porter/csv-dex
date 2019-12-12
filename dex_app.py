from flask import Flask, render_template
import tablib
import os
 
app = Flask (__name__)

dataset1 = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'data/base_dex_890.csv')) as f:
    dataset1.csv = f.read()

dataset2 = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'data/combat_dex_890.csv')) as f:
    dataset2.csv = f.read()
 
@app.route("/")
def index():    
    return dataset1.html
 
if __name__ == "__main__":
    app.run()