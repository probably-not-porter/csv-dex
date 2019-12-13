import os

f= open("../data/dex_images.md","w+")

f.write("# Sprites\n")

f.write("## Regular Sprites\n")

for file in os.listdir("../static/regular"):
    if file.endswith(".png"):
        f.write("![](" + (os.path.join("../static/regular", file)) + ")\n" )
        print(os.path.join("../static/regular", file))

f.write("## Shiny Sprites\n")

for file in os.listdir("../static/shiny"):
    if file.endswith(".png"):
        f.write("![](" + (os.path.join("../static/shiny", file)) + ")\n" )
        print(os.path.join("../static/shiny", file))

f.write("## Type Badges\n")

for file in os.listdir("../static/types"):
    if file.endswith(".gif"):
        f.write("![](" + (os.path.join("../static/types", file)) + ")\n" )
        print(os.path.join("../static/types", file))