import json
import pandas as pd
import matplotlib.pyplot as plt

def display():

    tweets_data_path = 'E:/Code/CommentClassifier/DataSet/Tweets.json'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    #print len(tweets_data)

    tweets = pd.DataFrame()

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

    '''
    pd.set_option('display.max_colwidth', -1)
    print(tweets)
    print('\n')
    '''

    myTweetsList = []

    # Convert Pandas DataFrame into Python List
    myTweetsList = tweets['text'].values.T.tolist()


    # Print list element without 'u'
    #print(myTweetsList[0])
    
    # This will also go through list and print all list items without 'u'
    '''
    for str in myTweetsList:
        print str
        #print(''.join(str))
        #print('\n')
    '''

    # tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    # tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    return myTweetsList
