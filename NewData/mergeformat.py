import json
import csv

with open('newhandles.json') as f:
    js = json.load(f)

for state in js:
    for state2 in js:
        if(state in state2 and state != state2):
            print(state + " in " + state2)

with open('losershandles.csv') as cv:
    csv_reader = csv.reader(cv, delimiter=',')
    for row in csv_reader:
        if row[5] != "None":
            party = row[1]
            if party == "Democratic":
                party = "D"
            elif party == "Republican":
                party = "R"
            else:
                party = "O"
            for state in js:
                if row[2] in state:
                    if "West" in state and "West" not in row[2]:
                        continue
                    if "At-Large" in state:
                        for riding in js[state]:
                            js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                    else:
                        for riding in js[state]:
                            if row[3] == '1':
                                if " 1st " in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '2':
                                if " 2nd " in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '3':
                                if " 3rd " in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '21':
                                if "21st" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '22':
                                if "22nd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '23':
                                if "23rd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '31':
                                if "31st" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '32':
                                if "32nd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '33':
                                if "33rd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '41':
                                if "41st" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '42':
                                if "42nd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '43':
                                if "43rd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '51':
                                if "51st" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '52':
                                if "52nd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            elif row[3] == '53':
                                if "53rd" in riding:
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                            else:
                                if " " + row[3] + "th " in riding:
                                    print(row[3] + " is " + riding)
                                    js[state][riding].append({"Name": row[0], "Twitter": row[4], "Party": party, "Winner": False});
                                
                           


with open("newnewhandles.json", "w") as outfile:
    json.dump(js, outfile)