import re
import json
import numpy
import csv
import snscrape.modules.twitter as sntwitter
from thefuzz import process
import requests
from bs4 import BeautifulSoup

class BallotpediaGetter:
    def __init__(self) -> None:
        self.states = {}

    def getstates(self):
        return self.states

    def parseTwitterUrl(self, url):
        parts = url.split("/")
        return parts[3]

    def getTwitter(self, name, state):
        soup = None
        if(state in self.states):
            soup = self.states[state]
        else:
            fstate = state.replace(" ", "_")
            URL = f"https://ballotpedia.org/United_States_House_of_Representatives_elections_in_{fstate},_2020"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            self.states[state] = soup

        replink = ""
        for link in soup.find_all("a"):
            if name in link.text:
                replink = link["href"]
        rep = None
        if(len(replink) == 0 or ".org" not in replink):
            fname = name.replace(" ", "_")
            URL2 = f"https://ballotpedia.org/{fname}"
            page2 = requests.get(URL2)
            rep = BeautifulSoup(page2.content, 'html.parser')
            if("Oops! The page you’re looking for does not exist." in rep.prettify()):
                return ("Missing", "Missing", "Missing","Missing","Missing","Missing")
        else:
            reppage = requests.get(replink)
            rep = BeautifulSoup(reppage.content, 'html.parser')
        ctwitter = ""
        ptwitter = ""
        otwitter = ""
        for link in rep.find_all("a"):
            if "Campaign Twitter" in link.text:
                ctwitter = link["href"]
            if "Personal Twitter" in link.text:
                ptwitter = link["href"]
            if "Official Twitter" in link.text:
                otwitter = link["href"]
        cctwitter = "None"
        cres = "Campaign"
        if(len(ctwitter) > 0):
            cctwitter = self.parseTwitterUrl(ctwitter)
        pptwitter = "None"
        pres = "Personal"
        if (len(ptwitter) > 0):
            pptwitter = self.parseTwitterUrl(ptwitter)
        ootwitter = "None"
        ores = "Official"
        if (len(otwitter) > 0):
            ootwitter = self.parseTwitterUrl(otwitter)
        # else:
        #     twitter = "None"
        #     res = "None"
        return((cres, cctwitter, pres, pptwitter, ores, ootwitter))

def gethandles(name):
    i = 0
    n = []
    nv = []
    ndict = {}
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
    for j,tweet in enumerate(sntwitter.TwitterSearchScraper(name + ' Congress').get_items()):
        if i>200:
            break
        i = i + 1
        ncdict[tweet.user.displayname] = tweet.user.username
        if(tweet.user.verified):
            ncv.append(tweet.user.displayname)
            

    highestn = process.extractOne(name,n)
    highestnv = process.extractOne(name,nv)
    highestnc = process.extractOne(name,ncv)
    res = []

    maxver = "None"
    number = 0
    if(highestnv != None):
        if(highestnc != None):
            if highestnv[1] > highestnc[1]:
                maxver = ndict[highestnv[0]]
                number = highestnv[1]
            else:
                maxver = ncdict[highestnc[0]]
                number = highestnc[1]
        else:
            maxver = ndict[highestnv[0]]
            number = highestnv[1]
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
        res.append(ndict[highestnv[0]])
        res.append(highestnv[1])  
    if highestnc == None:
        res.append("None")
        res.append(0)
    else:
        res.append(ncdict[highestnc[0]])
        res.append(highestnc[1])
    return(res)

file = open("wiki.txt")
data = file.read()
file.close()

data = data.split("\n")
ndata = []
state = ""
district = 0


twitterHandler = BallotpediaGetter()
for i in data:
 

    if(len(i) > 0):
        if(i[0] == "*") :    
            j = re.split(r"(\(|\))", i)
            if(len(j) > 2):
                name = ""
                party = ""
                if("{{Aye}}" not in i):
                    # f = i.split()
                    
                    name = j[0].strip("* []")
                    name = name.split("|")[-1]
                    party = j[-3].strip("()[]")
                    party = party.split("|")[-1]
                    party = party.split("/")[-1]
                    # print(name)
                    # handle = twitterHandler.getTwitter(name, state)
                    # res = [name, party, state, district, handle[0], handle[1]]
                    # print(name + " " + party)
                    # ndata.append(res)
                    # print(res)
                    # print(len(twitterHandler.getstates()))
                
                else:
                    i = i.split("ref")[0]
                    namesearch = re.search("{{(.*)}}", i[10:])
                    if namesearch != None:
                        namebits = namesearch.group()
                        namebits = namebits.strip("{}")
                        namebits = namebits.split("|")
                        first = namebits[1].strip()
                        last = namebits[2].strip()
                        name = first + " " + last
                        partysearch = re.search(" \((.*)\) ", i[10:])
                        if(partysearch != None):
                            party = partysearch.group().strip()
                            
                            party = party.split()
                            
                            party = party[-1].strip().strip("\(\)")
                            party = party.split("/")[-1]
                            # print(party)
                        else:
                            partysearch = re.search(" \((.*)\)", i[10:])
                            party = partysearch.group().strip()
                            
                            party = party.split()
                            
                            party = party[-1].strip().strip("\(\)")
                            party = party.split("/")[-1]

                      
                    else:
                        namesearch = re.search("\[\[(.*)\]\]", i[10:])
                        name = namesearch.group().strip()
                        name = name.split("|")
                        name = name[-1].strip("\[\]")
                        partysearch = re.search(" \((.*)\) ", i[10:])
                        if(partysearch != None):
                            party = partysearch.group().strip()
                            
                            party = party.split()
                            
                            party = party[-1].strip().strip("\(\)")
                            party = party.split("/")[-1]
                        else:
                            partysearch = re.search(" \((.*)\)", i[10:])
                            party = partysearch.group().strip()
                            
                            party = party.split()
                            party = party[-1].strip().strip("\(\)")
                            party = party.split("/")[-1]

                    # if len(name) > 50:
                    #     print("name: " +name)
                    # if len(party) > 50:
                    #     print("party: " +party)
                print(name + " " + party)
                handle = twitterHandler.getTwitter(name, state)
                res = [name, party, state, district, handle[0], handle[1], handle[2], handle[3], handle[4], handle[5]]
                # print(name + " " + party)
                ndata.append(res)
                print(res)
                print(len(twitterHandler.getstates()))


        if("ushr" in i):
            district = district + 1
        if(i[0] == "="):
            j = i.strip("= ")
            state = j
            district = 0

# for i in ndata:
#     print()
#     print(i)

# print(len(ndata))


with open('allBallot.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(ndata)