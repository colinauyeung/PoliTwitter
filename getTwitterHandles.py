import re
import json

file = open("data.txt")
data = file.read()
file.close()

data = data.split("<td class=\"ninja_column_0 ninja_clmn_nm_state footable-first-visible\" style=\"display: table-cell;\">")
data = data[1:]
ndata = []
for i in data:
    dats = re.split(r"(<[^<>]*>)", i)
    ndats = []
    for j in dats:
        if(len(j) == 0):
            continue
        if(j[0] == '<'):
            continue
        if(j[0] == '\n'):
            continue
        if(j[0] == 'x'):
            continue
        ndats.append(j)
    ndata.append(ndats)

filtered = {}
for i in ndata:
    if(i[1] == "U.S. Senator"):
        continue
    state = re.split(r"[0-9]+" , i[0])[0].strip()
    # print(len(i))
    if(len(i) < 6):
        continue
    d = {}
    d["Riding"] = i[0]
    d["Name"] = i[2]
    if(i[3][0] != "h"):
        d["Twitter"] = i[4]
        d["Party"] = i[3]
    else:
        d["Twitter"] = i[5]
        d["Party"] = i[4]
    if state in filtered:
        filtered[state].append(d)
    else:
        filtered[state] = [d]
    
print(filtered)

with open("handles.json", "w") as outfile:
    json.dump(filtered, outfile)
# for i in filtered:
#     print("\n")
#     print(i)

# print(len(filtered))