from flask import Flask, render_template, request
from MLAlgorithm import classify
from twitter_streaming import mining
from DisplayTweets import display

MinedTweets = []

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('LandingPage.html')


@app.route('/about')
def about():
    return render_template('AboutPage.html')


@app.route('/login')
def login():
    return render_template('LoginPage.html')


@app.route('/testPage', methods=['POST', 'GET'])
def displayTestPage():
    if request.method == 'POST':
        return render_template('TestPage.html')


@app.route('/test', methods=['POST', 'GET'])
def showTestPage():
    if request.method == 'POST':
        if request.form['backToTest'] == 'searchAgain':

            f = open('E:/Code/CommentClassifier/DataSet/Tweets.json', 'r+')
            f.truncate()
            return render_template('TestPage.html')

        elif request.form['backToTest'] == 'activate':

            Tweets = display()
            results = []
            for tweet in Tweets:
                classifierResult = classify(tweet)
                results.append(classifierResult)

        print("Activating Prospect")
        print(Tweets)
        print(results)
        return render_template('ProspectActivated.html',results=results, Tweets=Tweets)


# @app.route('/predict/<comment>')
# def abusiveCommentsClassificationService(comment):
#     classfierResult=classify(comment)
#     return classfierResult


@app.route('/deleteTweets')
def deleteTweets():
    print("Delete Tweets route hit")
    Tweets = display()
    ProperTweets = []
    results = []
    count = 0
    for tweet in Tweets:
        classifierResult = classify(tweet)
        results.append(classifierResult)

    for tweet in Tweets:
        if results[count] == 'Not abusive':
            ProperTweets.append(tweet)
        count = count + 1

    return render_template('ResultPage.html', ProperTweets=ProperTweets)


@app.route('/predict', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':

        keyword1 = request.form['word1']
        keyword2 = request.form['word2']
        keyword3 = request.form['word3']

        mining(keyword1, keyword2, keyword3)

        MinedTweets = display()

        print(MinedTweets)

        return render_template('ResultPage.html', MinedTweets=MinedTweets, keyword1=keyword1, keyword2=keyword2, keyword3=keyword3)

        # Return multiple values
        # return '{} {} {} {}'.format(classfierResult, keyword1, keyword2, keyword3)


@app.route('/inspect', methods=['POST', 'GET'])
def inspect():
    if request.method == 'POST':

        inspectTweet = request.form.get('tweetID')
        return render_template('InspectPage.html', inspectTweet=inspectTweet)


@app.route('/prospect', methods=['POST', 'GET'])
def prospect():
    if request.method == 'POST':

        delTweet = request.form.get('delete')

        Tweets = display()
        userVerifiedTweets = []

        for tweet in Tweets:
            if tweet != delTweet:
                userVerifiedTweets.append(tweet)

        return render_template('ResultPage.html', userVerifiedTweets=userVerifiedTweets)


@app.route('/runProspect', methods=['POST', 'GET'])
def runProspect():
    if request.method ==  'POST':

        tweet = request.form.get('run')
        classifierResult = classify(tweet)

        return render_template('RunProspectPage.html', classifierResult=classifierResult)


@app.route('/testTweet', methods= ['POST', 'GET'])
def testTweet():
    if request.method == 'POST':

        tweet = request.form['comment']
        classifierResult = classify(tweet)

        return render_template('RunProspectPage.html', classifierResult=classifierResult)


app.run()
