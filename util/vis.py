import csv
from matplotlib import pyplot as plt

filename = 'data/base_dex_890.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    hp = []
    attack = []
    for row in reader:
        a = int(row[5],10)
        h = int(row[4],10)
        hp.append(h)  
        attack.append(a)
    
    #Plot Data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(hp, c = 'green') #Line 1
    plt.plot(attack, c = 'red') #Line 2
    #Format Plot
    plt.title("Daily High Temperatures, 2018", fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 16)
    plt.show()