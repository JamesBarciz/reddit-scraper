# Standard Packages
import requests
import pandas as pd
import datetime as dt
from decouple import config

# External packages
import praw


# Bring in the environment variables
CLIENT_ID = config('CLIENT_ID')
SECRET_TOKEN = config('SECRET_TOKEN')
USER_APP_NAME = config('USER_APP_NAME')
AUTH_USERNAME = config('AUTH_USERNAME')
AUTH_PASSWORD = config('AUTH_PASSWORD')

REDDIT = praw.Reddit(
  client_id=CLIENT_ID,
  client_secret=SECRET_TOKEN,
  password=AUTH_PASSWORD,
  user_agent=USER_APP_NAME,
  username=AUTH_USERNAME
)

assert REDDIT.user.me() == AUTH_USERNAME

subreddit = REDDIT.subreddit('programming')
top_subreddit = subreddit.top(limit=20)

programming = {
  'title': [],
  'id': [],
  'score': [],
  'body': [],
  'url': []
}

for submission in top_subreddit:
  programming['title'].append(submission.title)
  programming['id'].append(submission.id)
  programming['score'].append(submission.score)
  programming['body'].append(submission.selftext)
  programming['url'].append(submission.url)

print(programming.items())

# auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# data = {
#     'grant_type': 'password',
#     'username': AUTH_USERNAME,
#     'password': AUTH_PASSWORD
# }

# headers = {
#     'User-Agent': 'LeScraper/0.0.1'
# }

# res = requests.post('https://www.reddit.com/api/v1/access_token',
#                     auth=auth, data=data, headers=headers
# )

# TOKEN = res.json()['access_token']

# headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

# requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


# res = requests.get("https://oauth.reddit.com/r/programming/hot",
#                    headers=headers
# )

# print(res.json())
