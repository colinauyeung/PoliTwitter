import snscrape.modules.twitter as sntwitter
from progress.bar import ChargingBar
import json
import time
import csv


with open('listedhandles.json', encoding="utf-8") as f:
    js = json.load(f)
total = 0;




    
    # count = 0
    # for key in js:
    #     for riding in js[key]:
    #         count = count + len(js[key][riding])
    # bar = ChargingBar("Processing", max =count)
ignore =['Mississippi', 'Oklahoma', 'Minnesota', 'Alaska At-Large', 'Arkansas', 'New Mexico', 'Virgin Islands At-Large', 'Indiana', 'Maryland', 'Louisiana', 'Idaho', 'American Samoa At-Large', 'Arizona', 'Iowa', 'Montana At-Large', 'Michigan', 'Kansas', 'Utah', 'Virginia', 'Oregon', 'District of Columbia At-Large', 'Connecticut', 'Tennessee', 'California', 'Massachusetts', 'Vermont At-Large', 'West Virginia', 'South Carolina', 'New Hampshire', 'North Dakota At-Large', 'Wisconsin', 'Wyoming At-Large', 'Georgia', 'Pennsylvania', 'Florida', 'Hawaii', 'Kentucky', 'Northern Mariana Islands At-Large', 'Guam At-Large', 'Nebraska', 'Missouri', 'Ohio', 'Alabama', 'Illinois', 'Colorado', 'New Jersey', 'Washington', 'Puerto Rico At-Large', 'North Carolina', 'South Dakota At-Large', 'New York', 'Texas', 'Delaware At-Large', 'Nevada', 'Maine', 'Rhode Island']
for key in js:
    if(key in ignore):
        continue
    with open('output'+key+'.csv', mode="w", encoding="utf-8") as csv_file:
        fieldnames = ['id', 'name', 'winner', 'Incumbent', 'party','District','username', 'date', 'messagetext', 
                        'lengthofmessage',
                        'retweets', 'replies', 'quotes',
                        'likes', 'photo', 'numofphoto',
                        'gif', 'video', 'ReplyingTo','ReplyToID',
                        'mentionedusers', 'numofmentions',
                        'hashtags',"numofhashtags"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'id':'id', 
                        'name':'name', 
                        'winner':'winner', 
                        'Incumbent':'incumbent', 
                        'party': 'party',
                        'District':'district',
                        'username': 'username', 
                        'date': 'date', 
                        'messagetext': 'message',
                        'lengthofmessage':'lengthofmessage', 
                        'retweets':'retweets', 
                        'replies':'replies', 
                        'quotes':'quotes',
                        'likes':'likes', 
                        'photo':'hasphoto', 
                        'numofphoto':'numofphoto',
                        'gif':'hasgif', 
                        'video':'hasvideo', 
                        'ReplyingTo':'ReplyingTo',
                        'ReplyToID':'ReplyToID',
                        'mentionedusers':'mentionedusers', 
                        'numofmentions':'numofmentions',
                        'hashtags':'hashtags', 
                        "numofhashtags": "numofhashtags"})
        count = 0
        for riding in js[key]:
            for i in range(0, len(js[key][riding])):
                count = count + len(js[key][riding][i]["Twitter"])
        bar = ChargingBar(key, max =count)

        for riding in js[key]:
            for i in range(0, len(js[key][riding])):
                for handle in js[key][riding][i]["Twitter"]:
                    # print(js[key][riding][i])
                    # Creating list to append tweet data to

                    # print(handle)
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

                        mytweet = {"date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S"), "message":tweet.content, 
                        "replies":tweet.replyCount, "retweets":tweet.retweetCount, "likes":tweet.likeCount, 
                        "quotes": tweet.quoteCount, "link": tweet.url, "id":tweet.id, "outlinks": tweet.outlinks,
                        "tcooutlinks":tweet.tcooutlinks, 
                        "inReplyToTweetId":tweet.inReplyToTweetId, "inReplyToUser": replyuser, "mentionedUsers": mentionedusers,
                        "hashtags":tweet.hashtags, "photo":photo, "photoruls":photourl, "video":video, "gif":gif}
                        

                        name = js[key][riding][i]["Name"]
                        winner = js[key][riding][i]["Winner"]
                        incumbent = js[key][riding][i]["Incumbent"]
                        party = js[key][riding][i]["Party"]
                        district = riding
                        district = district.replace("st District", "")
                        district = district.replace("nd District", "")
                        district = district.replace("rd District", "")
                        district = district.replace("th District", "")
                        district = district.replace("At-Large", "0")
                        district = district.upper()


            
                        hash = ""
                        hashnum = 0
                        if(type(mytweet["hashtags"]) != type(None)):
                            first = True
                            for tag in mytweet["hashtags"]:
                                if(not first):
                                    hash = hash + ','
                                first = False
                                hash = hash + tag
                            hashnum = len(mytweet["hashtags"])
                        else:
                            hash = 'null'

                        users = ""
                        usersnum = 0
                        if(len(mytweet["mentionedUsers"]) != 0):
                            first = True
                            for user in mytweet["mentionedUsers"]:
                                if(not first):
                                    users = users + ','
                                first = False
                                users = users + user
                            usersnum = len(mytweet["mentionedUsers"])
                        else:
                            users = 'null'

                        writer.writerow(
                            {'id':mytweet['id'],
                            'name':name, 
                            'winner':winner, 
                            'Incumbent':incumbent, 
                            'party':party,
                            'District':district,
                            'username': handle, 
                            'date':  mytweet["date"].replace(",",""), 
                            'messagetext': mytweet["message"], 
                            'lengthofmessage':len(mytweet["message"]), 
                            'retweets': mytweet["retweets"], 
                            'replies': mytweet['replies'], 
                            'quotes': mytweet['quotes'],
                            'likes': mytweet['likes'], 
                            'photo': mytweet['photo'], 
                            'numofphoto':len(mytweet['photoruls']),
                            'gif': mytweet['gif'], 
                            'video': mytweet['video'], 
                            'ReplyingTo':mytweet['inReplyToUser'],
                            'ReplyToID':mytweet['inReplyToTweetId'],
                            'mentionedusers':users, 
                            'numofmentions':usersnum,
                            'hashtags': hash, 
                            "numofhashtags": hashnum}
                        )
                    bar.next()
                    time.sleep(5);

                    # "retweetedtweet":tweet.retweetedTweet, "quotedTweet":tweet.quotedTweet,
                
        bar.finish()
        ignore.append(key)
        print(ignore)
                





                
            # print(len(js[key][riding][i]["Tweets"]))
            # total = total + len(js[key][riding][i]["Tweets"])
            
    #     if(total > 500):
    #         break
    # if(total > 500):
    #     break
# print(total)

# with open("outmini.json", "w") as outfile:
#     json.dump(js, outfile)