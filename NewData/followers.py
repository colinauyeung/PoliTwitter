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
            
           
            # Creating list to append tweet data to

            print(js[key][riding][i])
            # Using TwitterSearchScraper to scrape data and append tweets to list
            for j,user in enumerate(sntwitter.TwitterUserScraper(handle, False).get_items()):
                js[key][riding][i]["Followers"] = user.user.followersCount;
                js[key][riding][i]["Verified"] = user.user.verified;
                print(js[key][riding][i])
                break;
                # if i>50:
                #     break
                # js[key][riding][i]["Tweets"].append({"date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S"), "message":tweet.content, 
                # "replies":tweet.replyCount, "retweets":tweet.retweetCount, "likes":tweet.likeCount, 
                # "quotes": tweet.quoteCount, "link": tweet.url})

            # print(len(js[key][riding][i]["Tweets"]))
            # total = total + len(js[key][riding][i]["Tweets"])

print(total)

with open("followers.json", "w") as outfile:
    json.dump(js, outfile)