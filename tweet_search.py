from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'aRQFyWoJfLp0tQ7H1XxuPZ6yf',
        consumer_secret = 'ROrOrif6nMVLGhdiAMsTbxvtJTPYHdR8xeY3BOsVLqSDt9h9DM',
        access_token = '194929190-oJ9PnQ25hj0scOtZE0QdqYwLMr2SjQNsVpzIjLop',
        access_token_secret = 'R9nhtdha7UMBgs2lBeTiGPhHuAh2moMdJBBJajUKS6LkU'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)