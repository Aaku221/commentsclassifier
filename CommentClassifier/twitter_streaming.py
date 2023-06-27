# Import the necessary methods from the Tweepy library
import tweepy
from tweepy.streaming import Stream
from tweepy import OAuthHandler
import time

# Issues with the previous code - did not stream tweets for a second search. That is because time_limit was
# initialized and set the first time stream started. By putting the listener class code inside mining(),
# each time mining() is called, listener object is initialized every time and thus time_limit is set again,
# allowing for multiple searches.

def mining(word1, word2, word3):
    # Variables that contains the user credentials to access Twitter API
    access_token = "790079938766319616-PUeDcl36kT1ZTc5xFiQonuSIdTdENZb"
    access_token_secret = "lohFw9alwspffo5miwWy9gcqCqbrrmTVBXRdNbsj2RooL"
    consumer_key = "w53Z5IgxNpsRjDSBahddw5ZdB"
    consumer_secret = "YQJ8rVyzs6daXIR5g3VzzqUlw5gdZSLYoJgKRyZtUYOTNXAtdw"
    start_time = time.time()

    # This is a basic listener that just prints received tweets to stdout.
    class listener(tweepy.Stream):
        def __init__(self, start_time,time_limit=60):
            self.time = start_time
            self.limit = time_limit

            # Open Tweets.json file to store the streamed tweets
            self.saveFile = open('E:/Code/CommentClassifier/DataSet/Tweets.json', 'a')

            # self.tweet_data = []

        def on_data(self, data):

            if (time.time() - self.time) < self.limit:
                try:
                    print(data)
                    # self.tweet_data.append(data)
                    # Store/Write all streamed tweets to Tweets.json
                    self.saveFile.write(data)
                    self.saveFile.write('\n')
                    return True
                except BaseException as e:
                    print('failed ondata,', str(e))
                    time.sleep(5)
                    pass
            else:
                print("Mining has stopped")
                self.saveFile.close()
                return False

        def on_error(self, status):
            print(status)

    # if __name__ == '__main__':

    # Twitter authentication and the connection to the Twitter Streaming API
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    stream = Stream(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(track=['kill', 'word2', 'word3'], languages=["en"])

    # Sample tweet streaming
    # This line filters Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['python', 'javascript', 'ruby'])
