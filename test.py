import snscrape.modules.twitter as sntwitter
from fuzzywuzzy import process
i = 0
n = []
nv = []
ndict = {}
name = "Shahid Buttar"
for j,tweet in enumerate(sntwitter.TwitterSearchScraper(name).get_items()):
    if i>200:
        break
    i = i + 1
    ndict[tweet.user.displayname] = tweet.user.username
    n.append(tweet.user.displayname)
    if(tweet.user.verified):
        nv.append(tweet.user.displayname)


i = 0
nc = []
ncv = []
ncdict = {}
for j,tweet in enumerate(sntwitter.TwitterSearchScraper(name + 'Congress').get_items()):
    if i>200:
        break
    i = i + 1
    ncdict[tweet.user.displayname] = tweet.user.username
    if(tweet.user.verified):
        ncv.append(tweet.user.displayname)
        

highestn = process.extractOne(name,n)
highestnv = process.extract(name,nv, limit=5)
highestnc = process.extractOne(name,ncv)
res = []

maxver = "None"
number = 0
if(highestnv != None):
    if(highestnc != None):
        if highestnv[0][1] > highestnc[1]:
            maxver = ndict[highestnv[0][0]]
            number = highestnv[0][1]
        else:
            maxver = ncdict[highestnc[0]]
            number = highestnc[1]
    else:
        maxver = ndict[highestnv[0][0]]
        number = highestnv[0][1]
else:
    if(highestnc != None):
        maxver = ncdict[highestnc[0]]
        number = highestnc[1]

if number < 80:
    if(highestn != None):
        if highestn[1] > 80:
            maxver = ndict[highestn[0]]
            number = highestn[1]
            
res.append(maxver)

if highestn == None:
    res.append("None")
    res.append(0)
else:
    res.append(ndict[highestn[0]])
    res.append(highestn[1])
if highestnv == None:
    res.append("None")
    res.append(0)
else:
    for i in range(0, len(highestnv)):
        res.append(ndict[highestnv[i][0]])
        res.append(highestnv[i][1])  
if highestnc == None:
    res.append("None")
    res.append(0)
else:
    res.append(ncdict[highestnc[0]])
    res.append(highestnc[1])
print(res)