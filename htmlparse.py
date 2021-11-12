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

        reppage = requests.get(replink)
        rep = BeautifulSoup(reppage.content, 'html.parser')
        ctwitter = ""
        ptwitter = ""
        for link in rep.find_all("a"):
            if "Campaign Twitter" in link.text:
                ctwitter = link["href"]
            if "Personal Twitter" in link.text:
                ptwitter = link["href"]
        twitter = ""
        if(len(ctwitter) > 0):
            twitter = self.parseTwitterUrl(ctwitter)
        elif (len(ptwitter) > 0):
            twitter = self.parseTwitterUrl(ptwitter)
        else:
            twitter = "None"
        return(twitter)

name = "Alison Hayden"
state = "California"
twitterHandler = BallotpediaGetter()
print(twitterHandler.getTwitter(name, state))
name2 = "TJ Cox"
print(twitterHandler.getTwitter(name2, state))
print(len(twitterHandler.getstates()))


# print(soup.prettify())