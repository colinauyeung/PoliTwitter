import json
with open('outwithincumbent.json') as f:
    js = json.load(f)

with open('outwithD.json') as f:
    d = json.load(f)

checklist1 = [ 'biden', 'pelosi', 'kamala', 'harris', 'schumer']
checklist2 = ['libs', 'democrat', 'liberal', 'progressive']
checklist3 = checklist1 + checklist2

total = 0
total2 = 0
total3 = 0 
count = 0
top = []
missing = []
for state in js:
    for riding in js[state]:
        for candidate in js[state][riding]:
            if candidate["Party"] == "D":
                first = True
                total3 = 0 
                for tweet in candidate["Tweets"]:
                    print(total2)
                    found = False
                    for tweetd in d:
                        if tweetd["link"] == tweet["link"]:
                            found = True
                    if not found:
                        count = count + 1
                        print("Not found")
                        missing.append(tweet)
                    total3 = total3 + 1
                    dats = tweet["message"].lower()
                    found = False
                    for check in checklist1:
                        if check in dats:
                            found = True
                    if found:
                        total = total + 1
                        # print(tweet["message"])

                    total2 = total2 + 1
                    print(total2)
                if len(top) >= 100:
                    if total3 > top[-1]:
                        top.pop()
                        top.append(total3)
                        top.sort()
                        top.reverse()
                else:
                    top.append(total3)
                    top.sort()
                    top.reverse()

print(total)
print(total2)
print(top)
# sum = 0
# for i in top:
print(count)
print(missing)
print(len(js))