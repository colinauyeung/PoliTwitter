import snscrape.modules.twitter as sntwitter
import json

with open('handles.json') as f:
    js = json.load(f)
total = 0;


for key in js:
    for i in range(0, len(js[key])):
        handle = js[key][i]["Twitter"]
        handle = handle.strip("@")
        js[key][i]["Tweets"] = [];
        print(js[key][i])
        # Creating list to append tweet data to


        # Using TwitterSearchScraper to scrape data and append tweets to list
        for j,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{0} since:2020-10-3 until:2020-11-3'.format(handle)).get_items()):
            # if i>50:
            #     break
            js[key][i]["Tweets"].append({"date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S"), "message":tweet.content, 
            "replies":tweet.replyCount, "retweets":tweet.retweetCount, "likes":tweet.likeCount, 
            "quotes": tweet.quoteCount})

        print(len(js[key][i]["Tweets"]))
        total = total + len(js[key][i]["Tweets"])

print(total)

with open("out2.json", "w") as outfile:
    json.dump(js, outfile)