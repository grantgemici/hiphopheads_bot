import re
import requests

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




