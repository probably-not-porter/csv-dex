import os

f= open("../data/dex_images.md","w+")

for file in os.listdir("../static/regular"):
    if file.endswith(".png"):
        f.write("![]('" + (os.path.join("../static/regular", file)) + "')\n" )
        print(os.path.join("../static/regular", file))