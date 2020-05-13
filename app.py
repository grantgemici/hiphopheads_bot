import time
import praw
import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Import utilities
from lib.utils import *

# these keys can be set in a file named .env in your local directory
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     username=USERNAME,
                     password=PASSWORD,
                     user_agent="testscript by u/pawsibility"
                     )
 
# create subreddit instance
subreddit = reddit.subreddit("hiphopheads")
 
# troll subreddit
i = 0
for submission in subreddit.new():
    user = submission.author
    title = submission.title

    if ' - ' not in title:
        continue

    title_clean = clean_title(title, remove_features=False)
    t_items = title_clean.split(' - ')
    artist_name = (t_items[0])
    song_name = (t_items[1]) 
    # if ' - ' in title:
    #     msg = ('Use [this link](https://www.reddit.com/r/hiphopheads/search?q=' + artist_name + '+' + song_title + '&restrict_sr=on&include_over_18=on&sort=new&t=year&feature=legacy_search to check whether your post is a repost and use this link to check if the song you posted is on the [Overposted list](https://docs.google.com/spreadsheets/d/1Qpbd-fHbMyfWXlWPRA_XfgzYayc8cIjn8J9CuL-aNpE/edit).' + \n + \n + 'If your post is a repost or on the Overposted list and you fail to remove it within 2 hours of posting, you will receive a temporary ban of 1 or 2 days. Repeated offenses will carry larger penalties.')
    #     reddit.send_message(user, 'Please make sure your post is not a repost', msg)
    #     print('A submission was made and I messaged the author')
    # else:
    #     print('A submisison was made, but I did not message the author.')
    print(i,'|',title,'|',title_clean,'|',artist_name,'|',song_name)
    check_repost(artist_name,song_name)
    time.sleep(1)
    i += 1