import re
import requests
import urllib
from bs4 import BeautifulSoup

URL='https://www.reddit.com/r/hiphopheads/search?'

# use regular expressions to remove any noise in the title
def clean_title(title, remove_features=True):

    # remove any instances of [ ] and ( ) text
    title = re.sub(r'[\(\[].*?[\)\]]', '', title)

    try:
        # remove feature text
        feature_tags = ['feat','feat.','ft','ft.']
        for tag in feature_tags:
            if tag in title:
                # find index of feature tag
                tag_index = title.index(tag)
                # slice string to get rid of text afterwards to help clean it up
                title = title[:tag_index]
            else:
                continue
    except:
        print('Replace feature tag didnt work... Skipping')

    return title

def check_repost(artist_name,song_name):

    # set paramters dict
    params = {'q':artist_name + ' ' + song_name,
            'restrict_sr': 'on',
            'include_over_18': 'on',
            'sort': 'new',
            't': 'year',
            'feature': 'legacy_search'
            }
    
    # generate the request URL and headers
    req_url = URL + urllib.parse.urlencode(params)
    headers = requests.utils.default_headers()
    # submit request
    res = requests.get(req_url, headers=headers)
    print(res.text)

    # generate a soup and search for noresults id
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.findAll(id='noresults')

    print(soup.prettify())
    print(req_url)
    print(data)

    if data:
        # found nothing
        print('Not posted!')
    else:
        # stuff has been found
        print('Posted')






