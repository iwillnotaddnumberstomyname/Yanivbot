import tweepy

auth = tweepy.OAuthHandler("","")
auth.set_access_token("", "")
api = tweepy.API(auth)
yaniv = "@trustednerd"
lastid = None
page = 1 
firstid = None
timeline = api.user_timeline("@trustednerd")
ids = None
i = open("ids.txt")
while True:
  for tweet in timeline:
      if tweet.id in 
      timeline = api.user_timeline("@trustednerd", max_id = firstid)
      print(tweet.text)
      ids = []
      print(ids)
      i.write(tweet.id)
      page += page
      lastid = max(ids)
      firstid = min(ids)
