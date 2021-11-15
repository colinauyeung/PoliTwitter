import json

with open('outwithincumbent.json') as f:
    js = json.load(f)

partytweets = []

comp = ['Indiana 5th District',
'New Jersey 2nd District',
'Virginia 5th District',
'Oklahoma 5th District',
'Pennsylvania 10th District',
'Texas 24th District',
'New Mexico 2nd District',
'California 25th District',
'Utah 4th District',
'Michigan 3rd District',
'Arizona 6th District',
'Georgia 7th District',
'Ohio 1st District',
'New York 2nd District',
'New York 11th District',
'Nebraska 2nd District',
'California 21st District',
'Minnesota 1st District',
'Colorado 3rd District',
'Illinois 13th District',
'New York 24th District',
'South Carolina 1st District',
'Arkansas 2nd District',
'North Carolina 8th District',
'Texas 22nd District',
'Missouri 2nd District',
'Texas 21st District',
'California 48th District',
'Michigan 6th District',
'New York 22nd  District',
'California 39th District',
'Georgia 6th District',
'Texas 23rd District',
'North Carolina 11th District',
'Montana at-large District',
'Texas 7th District',
'Nevada 4th District',
'New Jersey 7th District',
'Florida 15th District',
'Alaska At-Large',
'Minnesota 7th District',
'Virginia 7th District',
'Oregon 4th District',
'Washington 3rd District',
'Pennsylvania 1st District',
'Iowa 3rd District',
'Florida 27th District',
'New Hampshire 1st District',
'New York 1st District',
'Virginia 2nd District']

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

for state in js:
    for riding in js[state]:
        if riding in comp or True:
            for candidate in range(0, len(js[state][riding])):
                if js[state][riding][candidate]["Party"] == "O" :
                # and js[state][riding][candidate]["Incumbent"] == False:
                    for tweet in range(0, len(js[state][riding][candidate]["Tweets"])):
                        copy = js[state][riding][candidate]["Tweets"][tweet]
                        copy["name"] = js[state][riding][candidate]["Name"]
                        copy["Winner"] = js[state][riding][candidate]["Winner"]
                        copy["Incumbent"] = js[state][riding][candidate]["Incumbent"]
                        copy["State"] = state
                        copy["Riding"] = riding
                        partytweets.append(copy)

with open("outwithO.json", "w") as outfile:
    json.dump(partytweets, outfile)