from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from text_sanitize import filter_tweet_addons
from nltk.corpus import movie_reviews
from feature_extractor import *
from classifiers import *
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import NaiveBayesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import NuSVC
from nltk.classify.util import accuracy
'''
    from nltk.corpus.reader import CategorizedPlaintextCorpusReader
    is for loading a file based corpus,
    with each tweet in a file tagged pos/neg and with a file id.
 
    from text_sanitize import filter_tweet_addons
    this loads the script to filter the additional text not usefull for classification
 
    from feature_extractor import *
    various functions to assist with feature extraction
    
    from nltk.classify.scikitlearn import SklearnClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.svm import NuSVC
    imports the ScikitLearn classifier which has various algorithms 
    LogisticRegression(Maximum Entropy),BernoulliNB(NaiveBayes),NuSVC(SupportVecctorMachine)
    
    from nltk.classify import NaiveBayesClassifier
    imports the fast simple NaiveBayesClassifier
    
    from nltk.classify.util import accuracy
    function to show the accuracy of the classifier
    
    from classifiers import *
    class created for a MaxVoteClassifier 
    i.e. a classifier which yields the combined analysis of more than one classifier
    and also 
    a function to check the precission and recall of the classifiers
    
'''
def trained_sk_classifier(classifier_algo,train_feats):
    return SklearnClassifier(classiffier_algo).train(train_feats)
def trained_simple_nb_classifier(train_feats):
    return NaiveBayesClassifier.train(train_feats)
def get_feats_from_tweet(tweet_message):
    tweet_feats = bag_of_non_stopwords(tweet_message)
    return tweet_feats
def get_tweet_sentiment(tweet_message,algo = 'fastnb'):
    tweet_feats = get_feats_from_tweet(tweet_message)
    train_feats = label_feats_from_corpus(movie_reviews)
    if(mode == 'fastnb'):
        pos_neg_classifier = trained_simple_nb_classifier(train_feats)
        
    else:
        pos_neg_classifier = trained_sk_classifier(algo,train_feats)
    return pos_neg_classifier.classify(tweet_feats)
