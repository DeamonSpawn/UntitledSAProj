import re
from nltk.tokenize import RegexpTokenizer
def filter_url(line):
    text_sans_url = re.sub(r'https?:\\\/.*[\r\n]*', ' ', line)# removes website urls
    return text_sans_url
def filter_emoji(line):
    text_sans_emo=re.sub(r'\\u\w\w\w\w','',line)#removes emoticons
    return text_sans_emo
def filter_timestamp(line):
    text_sans_timestamp=re.sub(r'\d+.\d+::','',line)#removes time-stamp of the tweet
    return text_sans_timestamp
def filter_RTtags(line):
    text_sans_RTtags=re.sub(r'RT @\w+:','',line)#remove RT tagged people in text
    return text_sans_RTtags
def filter_usertags(line):
    text_sans_usertags = re.sub(r'@','',line)#removes usertags present in the text
    return text_sans_usertags
def filter_tweet_addons(line):
    return filter_usertags(filter_RTtags(filter_timestamp(filter_emoji(filter_url(line)))))
