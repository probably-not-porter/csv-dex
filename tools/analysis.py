import csv

# Perform Viability analysis

def main():
    results = []
    data = []
    with open("../data/SWSH.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)

    print("--> Create Stat Order")
    stat_order = Sort(results[1:], 14)

    for pokemon in stat_order:
        name = pokemon[1]
        total = pokemon[14]
        def_score = 0
        att_score = 0

        print("--> Stat Calc: " + name)

        for x in range(len(stat_order)):
            opponent = stat_order[x]
            if opponent[1] != name:
                for t in opponent[2]:
                    if t in pokemon[13]: # Vulnerable To
                        def_score -= 1 / (x + 1)
                    if t in pokemon[12]: # Resistant To
                        def_score += 1 / (x + 1)
                    if t in pokemon[11]: # Weak Against
                        att_score -= 1 / (x + 1)
                    if t in pokemon[10]: # Strong Against
                        att_score += 1 / (x + 1)

        _score = int(total) + att_score*20 + def_score*20

        data_item = []
        data_item.append(name)
        data_item.append(_score)
        data.append(data_item)

    data = Sort(data,1)
    print("\n\n\n")
    show_data(data[:20])







def Sort(sub_li, n): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][n] < sub_li[j + 1][n]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

def show_data(data):
    print("--> Show top 20")
    for line in data:
        
        print(line[0] + " - " + str(line[1]))

main()