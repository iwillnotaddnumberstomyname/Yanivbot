import tweepy

auth = tweepy.OAuthHandler("Q8ay5ZNICw95Y5HfGmLJcGRDg", "x04pKVGbkkgc0FFdS6cNteCo04SVXILqmTrWvCaIWgTuJEyrVj")
auth.set_access_token("1248396218088198144-skkYmsE49E1PtgCnUfBG8oezRDPzZq", "CJ6xTHVQCnNOURQiyqTnELaT6HWRUWADwTI6ZDeMWSbRL")
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
