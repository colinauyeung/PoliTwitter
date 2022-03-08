import json

with open('newnewnewhandles.json') as f:
    js = json.load(f)
total = 0;


for key in js:
    for riding in js[key]:
        demo = 0
        rep = 0
        other = 0

        incum = 0
        for i in range(0, len(js[key][riding])):
            if(js[key][riding][i]["Party"] == "D"):
                demo = demo + 1
            elif(js[key][riding][i]["Party"] == "R"):
                rep = rep + 1
            else:
                other = other + 1

            if(js[key][riding][i]["Incumbent"] == True):
                incum = incum + 1

        # if(len(js[key][riding])!=1 and (demo != 1 or rep !=1)):
        #     print(riding)

        if(incum>1):
            print(riding)