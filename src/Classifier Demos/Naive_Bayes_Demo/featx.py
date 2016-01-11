import collections
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.metrics import BigramAssocMeasures
def high_information_words(labelled_words, score_fn=BigramAssocMeasures.chi_sq, min_score=5):
    word_fd = FreqDist()
    label_word_fd = ConditionalFreqDist()
    for label, words in labelled_words:
        for word in words:
            word_fd[word] += 1
            label_word_fd[label][word] += 1
            
    n_xx = label_word_fd.N()
    high_info_words = set()
    
    for label in label_word_fd.conditions():
        n_xi = label_word_fd[label].N()
        word_scores = collections.defaultdict(int)
        
    for word, n_ii in label_word_fd[label].items():
        n_ix = word_fd[word]
        score = score_fn(n_ii, (n_ix, n_xi), n_xx)
        word_scores[word] = score
        
    bestwords = [word for word, score in word_scores.items() if score>= min_score]
    high_info_words |= set(bestwords)
    return high_info_words
    
def bag_of_words(words):# creates a list of tuples of format (word : True) if word exists in the word list
    return dict([(word,True) for word in words])
    
def bag_of_words_in_set(words, goodwords):# creates list of tuples of format (word : True) with words in goodwords list
    return bag_of_words(set(words) & set(goodwords))
    
def bag_of_words_not_in_set(words, badwords):# creates list of tuples of format (word : True) without words in badwords list
    return bag_of_words(set(words) - set(badwords))
    
def bag_of_non_stopwords(words,stopfile = 'english'):# creates a list of tuples of format (word : True) without stop words
    badwords = stopwords.words(stopfile)
    return bag_of_words_not_in_set(words,badwords)
    
def bag_of_bigram_words(words, score_fn = BigramAssocMeasures.chi_sq, n = 200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)
    
def label_feats_from_corpus(corp,feature_detector = bag_of_words):# gets features and assigns label associated for the reviews
    label_feats = collections.defaultdict(list)
    for label in corp.categories():
        for fileid in corp.fileids(categories=[label]):
            feats = feature_detector(corp.words(fileids=[fileid]))# gathers features in a list
            label_feats[label].append(feats)
    return label_feats # list of the form ( [features] : label )
    
def split_label_feats(lfeats,split = 0.75):# splits into training and test sets
    train_feats = []
    test_feats = []
    for label, feats in lfeats.items():
        cutoff = int(len(feats) * split)
        train_feats.extend([(feat,label) for feat in feats[:cutoff]])# tweets before the cuttoff are training set
        test_feats.extend([(feat,label) for feat in feats[cutoff:]])# tweets before the cuttoff are test set
    return train_feats, test_feats
