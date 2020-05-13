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
                     user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
                     )
 
# create subreddit instance
subreddit = reddit.subreddit("hiphopheads")
 
# troll subreddit
i = 0
for submission in subreddit.new():
    user = submission.author.name
    title = submission.title

    if ' - ' not in title or user == None:
        continue
    title_clean = clean_title(title, remove_features=False)

    t_items = title_clean.split(' - ')
    if len(t_items)<2:
        continue
    artist_name = (t_items[0])
    song_name = (t_items[1]) 
    
    req_url = generate_url(artist_name,song_name)

    
    msg = ('Use [this link]({}) to check whether your post is a repost (has previously gotten >= 60 upvotes in past year) and use this link to check if the song you posted is on the [Overposted list](https://docs.google.com/spreadsheets/d/1Qpbd-fHbMyfWXlWPRA_XfgzYayc8cIjn8J9CuL-aNpE/edit).'.format(req_url) + '\n' + '\n' + 'If your post is a repost or on the Overposted list and you fail to remove it within 2 hours of posting, you will receive a temporary ban of 1 or 2 days. Repeated offenses will carry larger penalties.')

    reddit.redditor(user).message('Please make sure your post is not a repost', msg)
    print('-='*50)
    print('Title:',title)
    print('Clean Title:',title_clean)
    print('Artist:',artist_name)
    print('Song:',song_name)
    print('Message:')
    print(msg)

    time.sleep(1)
