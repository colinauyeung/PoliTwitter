import snscrape.modules.twitter as sntwitter
import json

with open('newnewhandles.json') as f:
    js = json.load(f)
total = 0;


for key in js:
    for riding in js[key]:
        for i in range(0, len(js[key][riding])):
            handle = js[key][riding][i]["Twitter"]
            handle = handle.strip("@")
            js[key][riding][i]["Tweets"] = [];
            print(js[key][riding][i])
            # Creating list to append tweet data to


            # Using TwitterSearchScraper to scrape data and append tweets to list
            for j,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{0} since:2020-10-3 until:2020-11-3'.format(handle)).get_items()):
                # if i>50:
                #     break
                js[key][riding][i]["Tweets"].append({"date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S"), "message":tweet.content, 
                "replies":tweet.replyCount, "retweets":tweet.retweetCount, "likes":tweet.likeCount, 
                "quotes": tweet.quoteCount, "link": tweet.url})

            print(len(js[key][riding][i]["Tweets"]))
            total = total + len(js[key][riding][i]["Tweets"])

print(total)

with open("outwithlink.json", "w") as outfile:
    json.dump(js, outfile)