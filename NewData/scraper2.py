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
            for j,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{0} since:2020-9-3 until:2020-11-3'.format(handle)).get_items()):
                # if i>50:
                #     break
                video = False
                photo = False
                photourl = []
                gif = False
                replyuser = "null"
                mentionedusers = []
                if(type(tweet.media) != type(None)):
                    for media in tweet.media:
                        if(type(media) == sntwitter.Photo):
                            photo = True
                            photourl.append(media.fullUrl)
                        if(type(media) == sntwitter.Video):
                            video = True
                        if(type(media) == sntwitter.Gif):
                            gif = True

                if(type(tweet.inReplyToUser) != type(None)):
                    replyuser = tweet.inReplyToUser.username
                
                if(type(tweet.mentionedUsers) != type(None)):
                    for user in tweet.mentionedUsers:
                        mentionedusers.append(user.username)

                js[key][riding][i]["Tweets"].append({"date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S"), "message":tweet.content, 
                "replies":tweet.replyCount, "retweets":tweet.retweetCount, "likes":tweet.likeCount, 
                "quotes": tweet.quoteCount, "link": tweet.url, "id":tweet.id, "outlinks": tweet.outlinks,
                "tcooutlinks":tweet.tcooutlinks, 
                "inReplyToTweetId":tweet.inReplyToTweetId, "inReplyToUser": replyuser, "mentionedUsers": mentionedusers,
                "hashtags":tweet.hashtags, "photo":photo, "photoruls":photourl, "video":video, "gif":gif}
                )

                # "retweetedtweet":tweet.retweetedTweet, "quotedTweet":tweet.quotedTweet,
                





                
            print(len(js[key][riding][i]["Tweets"]))
            total = total + len(js[key][riding][i]["Tweets"])
            
    #     break
    # break
print(total)

with open("outwithlonger.json", "w") as outfile:
    json.dump(js, outfile)