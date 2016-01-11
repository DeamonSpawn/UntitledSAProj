""" This is a demo of the Scikit-learn Classifier from the NLTK
    package using the movie reviews corpus  """
from nltk.corpus import movie_reviews
from featx import *
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression
from nltk.classify.util import accuracy
from nltk import word_tokenize
lfeats = label_feats_from_corpus(movie_reviews)# extracts the features and its labels (neg/pos) associated with each tweets
train_feats,test_feats = split_label_feats(lfeats, split = 0.75) # splits labeled feature sets into training and test feats see featx.py
sk_classifier = SklearnClassifier(LogisticRegression())# trains classifier
sk_classifier.train(train_feats)
print("The associated accuracy for this classfier on the data is :" )
print(accuracy(sk_classifier,test_feats))
while True:
    text = input("Enter your fake tweet use only words: \n")
    test = bag_of_words(word_tokenize(text)) # converts text into a bag of words see featx.py
    print("Sentiment:")
    print(sk_classifier.classify(test))
    control = input("press aney key to continue 'q' to quit:")
    if(control == "q" ):
        break
