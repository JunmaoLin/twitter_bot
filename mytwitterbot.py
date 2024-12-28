# mytwitterbot.py
# Name: Junmao Lin

import sys
import time, random
import simple_twit

API_KEY = NULL

# API Key Secret, also known as Consumer Secret
API_KEY_SECRET = NULL
    
# Exercise 1 - Get and print 3 tweets from your home timeline
# For each tweet, print:
#   the tweet ID,
#   the author ID, 
#   the tweet creation date, and
#   the tweet text
def exercise1(client):
    tweets = simple_twit.get_home_timeline(client, 10).data
    for i in range (3):
        tweet = tweets[i]
        print("Tweet #" + str(i+1))
        print("Tweet ID: " + str(tweet.id))
        print("Author ID: " + str(tweet.author_id))
        print("Tweet Creation Date: " + str(tweet.created_at))
        print("Tweet Text: " + str(tweet.text))
        print()
        
# Retrieve and print out the 10 most recent tweets from your bot's home timeline.
#    for i in range (10): 
#        tweet = tweets[i]
#        print("Tweet #" + str(i+1))
#        print("Tweet ID: " + str(tweet.id))
#        print("Author ID: " + str(tweet.author_id))
#        print("Tweet Creation Date: " + str(tweet.created_at))
#        print("Tweet Text: " + str(tweet.text))
#        print()


# Exercise 2 - Get and print 3 tweets from another user
# For each tweet, print:
#   the tweet ID,
#   the author ID,
#   the tweet creation date, and
#   the tweet text
def exercise2(client):
    tweets = simple_twit.get_users_tweets(client, "IAE101_ckane", 10).data
    for i in range (3):
        tweet = tweets[i]
        print("Tweet #" + str(i+1))
        print("Tweet ID: " + str(tweet.id))
        print("Author ID: " + str(tweet.author_id))
        print("Tweet Creation Date: " + str(tweet.created_at))
        print("Tweet Text: " + str(tweet.text))
        print()

# Retrieve and print out the 10 most recent tweets from another user.
#    for i in range (10):
#        tweet = tweets[i]
#        print("Tweet #" + str(i+1))
#        print("Tweet ID: " + str(tweet.id))
#        print("Author ID: " + str(tweet.author_id))
#        print("Tweet Creation Date: " + str(tweet.created_at))
#        print("Tweet Text: " + str(tweet.text))
#        print()


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(client):

    # Post a single tweet to your bot's timeline.
    msg = "Hello World! This is a testing tweet!"
    simple_twit.send_tweet(client, msg)


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(client):

    #Post a single media tweet to your bot's timeline.
    msg = "This is a media tweet!"
    filename = "742b42b4-dc19-4b71-b797-0197992806a7.jpg"
    simple_twit.send_media_tweet(client, msg, filename)

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(client):
    sixHoursInSeconds = (60*60*6)
    while(True):
        #Computing a value in your program (e.g., the current time of day)
        #request for information
        currentTime = time.localtime()
        formattedTime = time.strftime("%Y-%m-%d %H:%M:%S %Z (UTC%z)", currentTime)

        #A simple post with text.
        #post to Twitter
        tweetMsg = "The current time is " + str(formattedTime) + "."
        simple_twit.send_tweet(client, tweetMsg)

        #Action unit should at most be executed once every 6 hours.
        time.sleep(sixHoursInSeconds)
        
    


if __name__ == "__main__":
    # This call to simple_twit.create_client will create the Tweepy Client 
    # object that Tweepy needs in order to make authenticated requests to 
    # Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "client" holding this Tweepy Client object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    print()
    
    try:
        client = simple_twit.create_client(API_KEY, API_KEY_SECRET)
    except Exception as e:
        print("ERROR:", e)
    
    print(client)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
#    exercise1(client)
#    exercise2(client)
#    exercise3(client)
#    exercise4(client)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(client)
