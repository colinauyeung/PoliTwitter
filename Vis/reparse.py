import csv
import json
from fuzzywuzzy import fuzz

names_dict = {}
with open('allBallot.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: 
        name = row[0]
        party = row[1]
        state = row[2]
        district = row[3]
        campaign = row[5]
        personal = row[7]
        official = row[9]
        res = {}
        if(party == "Democratic"):
            res["party"] = "D"
        elif(party == "Republican"):
            res["party"] = "R"
        else:
            res["party"] = "O"
        res["state"] = state
        res["district"] = district
        arr = []
        if(campaign != "Missing" and state != "Special elections"):  
            if(campaign != "None"):
                arr.append(campaign)
            if(personal != "None"):
                arr.append(personal)
            if(official != "None"):
                arr.append(official)
            
            if(len(arr) != 0):
                res["twitters"] = arr
                names_dict[name] = res
                # print(res)

# print(names_dict)
data = None
with open("handlesnew.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

for state in data:
    for district in data[state]:
        for i in range(0, len(data[state][district])):
            if(data[state][district][i]['Winner']):
                rename = data[state][district][i]["Name"].split(",")
                if(len(rename)>=2):
                    rename = rename[1] + " " + rename[0]
                else:
                    rename = data[state][district][i]["Name"]
                # print(rename)

                highest_score = 0
                highest_name = ""
                for name in names_dict: 
                    if(names_dict[name]["state"].strip() == state.strip()):
                        score = fuzz.ratio(name.strip(), rename.strip())
                        if(score > highest_score):
                            highest_score = score
                            highest_name = name


                if(highest_score >60):
                    twt = data[state][district][i]["Twitter"].strip("@")
                    lowers = []
                    for twitter in names_dict[highest_name]["twitters"]:
                        lowers.append(twitter.lower())
                    if twt.lower() not in lowers:
                        # print(twt)
                        # print(names_dict[highest_name]["twitters"])
                        names_dict[highest_name]["twitters"].append(twt)
                    # print("High Score:{0} \t High name: {1} \t Json Name: {2}".format(highest_score, highest_name, rename))
                    data[state][district][i]["Twitter"] = names_dict[highest_name]["twitters"]

                else:
                    twt = data[state][district][i]["Twitter"].strip("@")
                    data[state][district][i]["Twitter"] = [twt]
                    pass
                    # print("High Score:{0} \t High name: {1} \t Json Name: {2}".format(highest_score, highest_name, rename))
            else:
                rename = data[state][district][i]["Name"]

                highest_score = 0
                highest_name = ""
                for name in names_dict: 
                    if(names_dict[name]["state"].strip() == state.strip()):
                        score = fuzz.ratio(name.strip(), rename.strip())
                        if(score > highest_score):
                            highest_score = score
                            highest_name = name
                if(highest_score > 80):
                    twt = data[state][district][i]["Twitter"].strip("@")
                    lowers = []
                    for twitter in names_dict[highest_name]["twitters"]:
                        lowers.append(twitter.lower())
                    if twt.lower() not in lowers:
                        print(twt)
                        print(names_dict[highest_name]["twitters"])
                        names_dict[highest_name]["twitters"].append(twt)
                    # print("High Score:{0} \t High name: {1} \t Json Name: {2}".format(highest_score, highest_name, rename))
                    data[state][district][i]["Twitter"] = names_dict[highest_name]["twitters"]
                else:
                    twt = data[state][district][i]["Twitter"].strip("@")
                    data[state][district][i]["Twitter"] = [twt]

with open("listedhandles.json", "w") as outfile:
    json.dump(data, outfile)


