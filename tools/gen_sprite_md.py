import os

f1 = open("../data/normal_sprites.md","w+")
f2 = open("../data/shiny_sprites.md","w+")
f3 = open("../data/type_badges.md","w+")

# CREATE FIRST FILE
f1.write("# Regular Sprites\n")

for file in os.listdir("../static/regular"):
    if file.endswith(".png"):
        f1.write("![](" + (os.path.join("../static/regular", file)) + ")\n" )
        print(os.path.join("../static/regular", file))

# CREATE SECOND FILE
f2.write("# Shiny Sprites\n")

for file in os.listdir("../static/shiny"):
    if file.endswith(".png"):
        f2.write("![](" + (os.path.join("../static/shiny", file)) + ")\n" )
        print(os.path.join("../static/shiny", file))

# CREATE THIRD FILE
f3.write("# Type Badges\n")

for file in os.listdir("../static/types"):
    if file.endswith(".gif"):
        f3.write("![](" + (os.path.join("../static/types", file)) + ")\n" )
        print(os.path.join("../static/types", file))