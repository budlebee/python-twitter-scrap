# %%
import datetime
from decouple import config
import twitter
import pandas as pd
# %%

consumer_key = config('consumer_key')
consumer_secret = config('consumer_secret')

access_token = config('access_token')
secret_token = config('secret_token')

#directory_of_python_script = os.path.dirname(os.path.abspath(__file__))
directory_of_python_script = "/Users/zowan/Documents/python/twitter-scrap"

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=secret_token)

qr = '#BTC'
stats = api.GetSearch(term=qr, count=50000)

timestamp = []
likes = []
user_info = []
hashtags = []
text = []

for i in range(len(stats)):
    # Sat Jan 15 01:55:09 +0000 2022
    # %a %b %d %H:%M:%S %z %Y
    timestamp.append(int(datetime.datetime.strptime(
        stats[i].created_at, "%a %b %d %H:%M:%S %z %Y").timestamp()*1000))
    likes.append(stats[i].favorite_count)
    user_info.append(stats[i].user)
    hashtags.append(stats[i].hashtags)
    text.append(stats[i].text)
    if i % 50 == 0:
        print(f"scrap {i}...")

df = pd.DataFrame()
df['timestamp'] = timestamp
df['likes'] = likes
df['user_info'] = user_info
df['hashtags'] = hashtags
df['text'] = text

df.to_csv(directory_of_python_script + '/data/twitter_data.csv', index=False)
