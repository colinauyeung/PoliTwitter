import json
import csv

with open('outwithlonger.json') as f:
    js = json.load(f)
total = 0;

with open('output.csv', mode="w") as csv_file:

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
                
    for key in js:
        for riding in js[key]:
            for i in range(0, len(js[key][riding])):
                handle = js[key][riding][i]["Twitter"]
                handle = handle.strip("@")
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
                # print(district)
                # print(handle)
                js[key][riding][i]["Tweets"]
                
                print(len(js[key][riding][i]["Tweets"]))


                for tweet in js[key][riding][i]["Tweets"]:
                    hash = ""
                    hashnum = 0
                    if(type(tweet["hashtags"]) != type(None)):
                        first = True
                        for tag in tweet["hashtags"]:
                            if(not first):
                                hash = hash + ','
                            first = False
                            hash = hash + tag
                        hashnum = len(tweet["hashtags"])
                    else:
                        hash = 'null'

                    users = ""
                    usersnum = 0
                    if(len(tweet["mentionedUsers"]) != 0):
                        first = True
                        for user in tweet["mentionedUsers"]:
                            if(not first):
                                users = users + ','
                            first = False
                            users = users + user
                        usersnum = len(tweet["mentionedUsers"])
                    else:
                        users = 'null'

                    writer.writerow(
                        {'id':tweet['id'],
                        'name':name, 
                        'winner':winner, 
                        'Incumbent':incumbent, 
                        'party':party,
                        'District':district,
                        'username': handle, 
                        'date':  tweet["date"].replace(",",""), 
                        'messagetext': tweet["message"], 
                        'lengthofmessage':len(tweet["message"]), 
                        'retweets': tweet["retweets"], 
                        'replies': tweet['replies'], 
                        'quotes': tweet['quotes'],
                        'likes': tweet['likes'], 
                        'photo': tweet['photo'], 
                        'numofphoto':len(tweet['photoruls']),
                        'gif': tweet['gif'], 
                        'video': tweet['video'], 
                        'ReplyingTo':tweet['inReplyToUser'],
                        'ReplyToID':tweet['inReplyToTweetId'],
                        'mentionedusers':users, 
                        'numofmentions':usersnum,
                        'hashtags': hash, 
                        "numofhashtags": hashnum}
                    )
                        
                    


                    total = total + 1;

print(total)
                

# with open("outtest.json", "w", encoding='utf-8') as outfile:
#     json.dump(js, outfile, ensure_ascii=False)