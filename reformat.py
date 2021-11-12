import json

with open('handles.json') as f:
    js = json.load(f)

new = {}

for state in js:
    new[state] = {}
    for riding in js[state]:
        print(riding)
        new[state][riding["Riding"]] = [{"Name": riding["Name"], "Twitter": riding["Twitter"], "Party": riding["Party"], "Winner": True}];


with open("newhandles.json", "w") as outfile:
    json.dump(new, outfile)