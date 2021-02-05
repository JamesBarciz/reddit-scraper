# Standard packages
import pandas as pd
import pprint
from decouple import config
import time

# External packages
import praw


# Bring in the environment variables
CLIENT_ID = config('CLIENT_ID')
SECRET_TOKEN = config('SECRET_TOKEN')
USER_APP_NAME = config('USER_APP_NAME')
AUTH_USERNAME = config('AUTH_USERNAME')
AUTH_PASSWORD = config('AUTH_PASSWORD')

# Instance of Reddit
REDDIT = praw.Reddit(
  client_id=CLIENT_ID,
  client_secret=SECRET_TOKEN,
  password=AUTH_PASSWORD,
  user_agent=USER_APP_NAME,
  username=AUTH_USERNAME
)

# Will cause the script to fail if OAuthError
assert REDDIT.user.me() == AUTH_USERNAME

# List of subrettits to gather from REDDIT API
TEMP_SUBREDDITS = [
  'golang', 'java', 'javahelp', 'javascript', 'LearnJavaScript', 'lua',
  'python', 'learnpython', 'rust', 'shell', 'sql'
]

def get_top_subreddits(subreddits, output, time_filter='day', limit=5):
  """
  get_top_subreddits(subreddits: [str, List], time_filter='day': str, limit=25: int)

  Returns a list of JSON for subreddits passed into function.
  
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Parameters:
    
    subreddits - A list of subreddits to obtain.  If a string, it will be converted into an iterable.

    time_filter - ['all', 'day', 'hour', month', 'week', year'] - (default: 'day')

    limit - Limits the amount of subreddits obtained

  """

  if isinstance(subreddits, str):
    subreddits = [subreddits]

  for r in subreddits:

    subreddit = REDDIT.subreddit(r)
    top_subreddit = subreddit.top(time_filter=time_filter, limit=limit)

    for submission in top_subreddit:  # https://praw.readthedocs.io/en/latest/code_overview/models/submission.html

      field_dict = {
        'subreddit': None,
        'title': None,
        'id': None,
        'score': None,
        'link_url': None,
        'post_url': None,
        'body': None
      }

      field_dict['subreddit'] = r
      field_dict['title'] = submission.title
      field_dict['id'] = submission.id
      field_dict['score'] = submission.score
      field_dict['link_url'] = submission.url
      field_dict['post_url'] = 'https://www.reddit.com' + submission.permalink
      if submission.is_self:
        field_dict['body'] = submission.selftext
      else:
        field_dict['body'] = 'https://www.reddit.com' + submission.permalink
    
      output.append(field_dict)
    
    time.sleep(0.5)
  
  return output


# print(get_top_subreddits(TEMP_SUBREDDITS))