try:
         import json
except ImportError:
        import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError,TwitterStream

    # Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '235228993-UMgntnuS8UKyGU7pitxvMNxQO4Eqte2tgAGk9ijK'
ACCESS_SECRET = '9I8YOVtb6zIZaPpQEnAdVOZaq6vNBZJZVaRiU2OZir8os'
CONSUMER_KEY = 'pPa5GLuxOLzK57woQ1pdYQIAf'
CONSUMER_SECRET = 'IAsBqLL6lOQdcZ4VRu1ZIPvTOMIDw2Pa4bMbPtXbxP8Xwkjjd6'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)



twitter = Twitter(auth=oauth)
recent_posts = twitter.search.tweets(q='from:@hm_morgan #GoogleAlerts ', result_type='recent', lang='en', count=2)

print json.dumps(recent_posts)
