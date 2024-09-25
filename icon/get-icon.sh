#!/bin/bash
# Icons for README

# Ditto
curl https://img.pokemondb.net/sprites/scarlet-violet/icon/porygon.png --output porygon.png

# Birds
for x in articuno zapdos moltres; do
    curl https://img.pokemondb.net/sprites/scarlet-violet/icon/$x.png --output $x.png
done;

# Fire Starters
for x in charizard typhlosion blaziken infernape emboar delphox incineroar cinderace skeledirge; do
    curl https://img.pokemondb.net/sprites/scarlet-violet/icon/$x.png --output $x.png
done;

# Water Starters
for x in blastoise feraligatr swampert empoleon samurott greninja primarina inteleon quaquaval; do
    curl https://img.pokemondb.net/sprites/scarlet-violet/icon/$x.png --output $x.png
done;

# Grass Starters
for x in venusaur meganium sceptile torterra serperior chesnaught decidueye rillaboom meowscarada; do
    curl https://img.pokemondb.net/sprites/scarlet-violet/icon/$x.png --output $x.png
done;