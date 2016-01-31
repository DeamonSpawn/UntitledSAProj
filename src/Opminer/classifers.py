import collections
from nltk.metrics import precision,recall
from nltk.classify import util, ClassifierI, MultiClassifierI
from nltk.probability import FreqDist
def precision_recall(classifier, testfeats):
    #gives precision and recall of classifiers
    #precision = lack of false positives
    #recall = lack of false negatives
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    
    for i, (feats, label) in enumerate(testfeats):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)

    precisions = {}
    recalls = {}
    for label in classifier.labels():
        precisions[label] = precision(refsets[label], testsets[label])
        recalls[label] = recall(refsets[label], testsets[label])
    return precisions, recalls
class MaxVoteClassifier(ClassifierI):
    #classifier with the combined power of more than one classifiers
	def __init__(self, *classifiers):
		self._classifiers = classifiers
		self._labels = sorted(set(itertools.chain(*[c.labels() for c in classifiers])))
	
	def labels(self):
		return self._labels
	
	def classify(self, feats):
		counts = FreqDist()
		
		for classifier in self._classifiers:
			counts[classifier.classify(feats)] += 1
		
		return counts.max()