import snscrape.modules.twitter as sntwitter
import json

with open('handles.json') as f:
    js = json.load(f)
total = 0;


for key in js:
    for i in js[key]:
        handle = i["Twitter"]
        handle = handle.strip("@")
        js[key][i]["Tweets"] = [];

        # Creating list to append tweet data to


        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{0} since:2020-10-3 until:2020-11-3'.format(handle)).get_items()):
            # if i>50:
            #     break
            js[key][i]["Tweets"].append([tweet.date, tweet.renderedContent, tweet.content, tweet.user.username])

        print(len(js[key][i]["Tweets"]))
        total = total + len(js[key][i]["Tweets"])

with open("out.json", "w") as outfile:
    json.dump(js, outfile)