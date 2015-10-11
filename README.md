# Untitled Sentiment Analysis Project
This is a sentiment analysis project in python using twitter and it's API

Implementation of tweepy
========================

 __Libraries used so far:__
 
 For Python 3.4 and above

 __For Windows:__

Tweepy - The fastest way to install is using pip
 
    pip install tweepy

or alternatively use the GitHub repositry
    
    git clone https://github.com/tweepy/tweepy.git
    cd tweepy
    python setup.py install

Standard example to pull twitter feeds based on

   [Streaming tweets example](https://github.com/tweepy/tweepy/blob/master/examples/streaming.py)

Test code :
Extracting only the english language tweets using
    [twitter_streaming.py](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/Mods/tweepy/streaming.py)

__Modifications made:__

Modified tweepys existing [streaming.py](https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py) of which this is the [modified version](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/prototypes/tweet_extractor/twitter_streaming.py) based on the fix proposed 

   [Handle content-type header charset value for streaming API #635](https://github.com/tweepy/tweepy/issues/635)
   
Output of the tweet stream is in the JSON format from which the "text:" specifies the tweet which is extracted from the JSON text.

_Output:_

Output is stored to a [output text file](https://github.com/DeamonSpawn/UntitledSAProj/blob/debec75d722f92d299655e7949db6e8f53d9221f/Output%20Samples/tweetsansJSON.txt) using the command line
 
    python twitter_streaming.py >> output.txt 

The extraction process can be allowed to run until rate limitation by twitter occurs or alternatively the process can be interrupted using

    Ctrl+c

Implementation of a Wordbank based sentiment score using Patricia Tries
=======================================================================
__Libraries used so far:__
 
 For Python 3.4 and above

 __For Windows:__

NLTK - The fastest way to install is using pip
NLTK dependancies:

Numpy - Requires a GNU compiler like [MinGW](http://www.mingw.org/wiki/Getting_Started) or [Visual Studio 2013 or higher](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) installed

Using Visual Studio:
The Numpy installation looks for the Visual Studio file _vcvarsall.bat_ by default,
and installing Visual Studio is sufficient to meet this requirement and install Numpy
    
Using MinGW:

- [Install MinGW](http://www.mingw.org/wiki/Getting_Started) with C++ Compiler option checked
- Add C:\MinGW\bin to your PATH

- In PYTHONPATH\Lib\distutils, create a file distutils.cfg and add these lines:
    
        [build]
        compiler=mingw32
    
Then install using either

    pip install numpy
    pip install nltk
    

or alternatively using the Git Repositories
    
    git clone https://github.com/numpy/numpy.git
    cd tweepy
    python setup.py install
    git clone https://github.com/nltk/nltk.git
    cd tweepy
    python setup.py install

After NLTK is installed open the Python interpreter and type
    
    >>import nltk
    >>nltk.download
    
In the NLTK Downloader dialog box select _All packages_ and click the _Download_ button

Test Code: To evaluate our twitter tweets positive and negative sentiments we implement
[tweets_score.py](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/prototypes/tweet_score/tweets_score.py).It utilises a Patricia Trie constructed using a python dictionary data structure with wordbanks [negative-words.txt](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/Wordbanks/negative-words.txt) and [positive-words.txt](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/Wordbanks/positive-words.txt) as data. Using these tries we optimise the wordbank search for positive and negative word matches.

_Output_
 
    97
    29

 