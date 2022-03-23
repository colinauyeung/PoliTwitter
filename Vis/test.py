import json

with open('listedhandles.json', encoding="utf-8") as f:
    js = json.load(f)
total = 0;

print(len(js))
total = 0
for key in js:
    for riding in js[key]:
        total = total + len(js[key][riding])
print(total)