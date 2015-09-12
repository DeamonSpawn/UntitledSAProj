# UntitledSAProj
This is a sentiment analysis project in python using twitter and it's API

Implementation of tweepy
========================

 __Libraries used so far:__
 
 For Python 3.4 and above
 
 Tweepy - The fastest way to install is using pip
 
    pip install tweepy

or alternatively use the GitHub repositry
    
    git clone https://github.com/tweepy/tweepy.git
    cd tweepy
    python setup.py install

Standard example to pull twitter feeds based on

   [Streaming tweets example] (https://github.com/tweepy/tweepy/blob/master/examples/streaming.py)

Test code :
Extracting only the english language tweets
    [twitter_streaming.py] (https://github.com/DeamonSpawn/UntitledSAProj/blob/master/Mods/tweepy/streaming.py)

__Modifications made:__

Modified tweepys existing [streaming.py] (https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py) 

   of which this is the [modified version] (https://github.com/DeamonSpawn/UntitledSAProj/blob/master/prototypes/tweet_extractor/twitter_streaming.py)

based on the fix proposed 

   [Handle content-type header charset value for streaming API #635] (https://github.com/tweepy/tweepy/issues/635)
   

 