import json

with open('outwithlink.json') as f:
    js = json.load(f)

noincum = ['Wisconsin 5th District',
'Texas 24th District',
'Texas 23rd District',
'Texas 22nd District',
'Texas 17th District',
'Texas 13th District',
'Texas 11th District',
'Tennessee 1st District',
'Oregon 2nd District',
'North Carolina 6th District',
'North Carolina 2nd District',
'New York 2nd District',
'New York 17th District',
'New York 15th District',
'Michigan 3rd District',
'Michigan 10th District',
'Louisiana 5th District',
'Iowa 2nd District',
'Indiana 5th District',
'Indiana 1st District',
'Illinois 15th District',
'Georgia 7th District',
'Florida 3rd District',
'Florida 19th District',
'California 53rd District',
'Alabama 2nd District',
'Hawaii 2nd District',
'Alabama 1st District',
'New Mexico 3rd District',
'Kansas 1st District',
'Massachusetts 4th District',
'Georgia 9th District',
'Montana At-Large',
'California 8th District',
'Washington 10th District',
'Utah 1st District']

flipped = ['California 21st District',
'California 39th District',
'California 48th District',
'Florida 26th District',
'Florida 27th District',
'Iowa 1st District',
'Minnesota 7th District']

for state in js:
    for riding in js[state]:
        if riding in noincum:
            for i in range(0, len(js[state][riding])):
                js[state][riding][i]["Incumbent"] = False
        elif riding in flipped:
            for i in range(0, len(js[state][riding])):
                if not js[state][riding][i]["Winner"]:
                    if js[state][riding][i]["Party"] == "D" or js[state][riding][i]["Party"] == "R":
                        js[state][riding][i]["Incumbent"] = True
                    else:
                        js[state][riding][i]["Incumbent"] = False
                else:
                    js[state][riding][i]["Incumbent"] = False
        else:
            for i in range(0, len(js[state][riding])):
                js[state][riding][i]["Incumbent"] = js[state][riding][i]["Winner"]


with open("outwithincumbent.json", "w") as outfile:
    json.dump(js, outfile)