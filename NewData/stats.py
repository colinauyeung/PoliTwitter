import json
with open('outwithR.json') as f:
    js = json.load(f)

checklist1 = [ 'biden', 'pelosi', 'kamala', 'harris', 'schumer']
checklist2 = ['libs', 'democrat', 'liberal', 'progressive']
checklist3 = checklist1 + checklist2

total = 0
total2 = 0
for tweet in js:
    dats = tweet["message"].lower()
    found = False
    for check in checklist1:
        if check in dats:
            found = True
    if found:
        total = total + 1
        # print(tweet["message"])

    if not (len(dats.split(" ")) == 1 and "http" in dats):
        total2 = total2 + 1

print(total)
print(total2)
print(len(js))