# Built-in Python modules
import os

# Standard Packages
import pandas as pd
import datetime as dt

# Other Packages
import praw


# Bring in the environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
USER_APP_NAME = os.getenv('USER_APP_NAME')
AUTH_USERNAME = os.getenv('AUTH_USERNAME')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')

# Create an instance of Reddit
REDDIT = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_TOKEN,
                     user_agent=USER_APP_NAME,
                     username=AUTH_USERNAME,
                     password=AUTH_PASSWORD
)

print(REDDIT.user.me())
# subreddit = REDDIT.subreddit('programming')

# top_subreddit = subreddit.top(limit=1)

# topics_dict = {
#     'title': [],
#     'score': [],
#     'id': [],
#     'url': [],
#     'created': [],
#     'body': []
# }

# for submission in top_subreddit:
#     topics_dict['title'].append(submission.title)
#     topics_dict['score'].append(submission.score)
#     topics_dict['id'].append(submission.id)
#     topics_dict['url'].append(submission.url)
#     topics_dict['created'].append(submission.created)
#     topics_dict['body'].append(submission.selftext)

# print(topics_dict)

# auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# data = {
#     'grant_type': 'password',
#     'username': AUTH_USERNAME,
#     'password': AUTH_PASSWORD
# }

# headers = {
#     'User-Agent': 'LeScraper/0.0.1'
# }

# res = requests.post('https://www.twitter.com/api/v1/access_token',
#                     auth=auth, data=data, headers=headers)

# TOKEN = res.json()['access_token']

# headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

# requests.get('https://oauth.reddit.com/api/v1/me', header=headers)


# #--------------------------------------