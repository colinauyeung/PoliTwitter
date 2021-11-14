import json
import csv

file = "sampleO"

with open(file + '.json') as f:
    js = json.load(f)

# with open('outwithlink.json') as f:
#     links = json.load(f)

simple = []
for tweet in js:
    blob = []
    link = ""
    for candidate in links[tweet["State"]][tweet["Riding"]]:
        if candidate["Name"] == tweet["name"]:
            for tw in candidate["Tweets"]:
                if tw["date"] == tweet["date"] and tw["message"] == tweet["message"]:
                    link = tw["link"]
    blob.append(tweet["name"])
    blob.append(tweet["date"])
    blob.append(tweet["message"])
    blob.append(tweet["link"])
    simple.append(blob)

with open(file + '.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(simple)