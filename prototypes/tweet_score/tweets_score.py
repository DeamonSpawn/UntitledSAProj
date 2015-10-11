import re,nltk
_end = '_end_'
postrie=dict()
negtrie=dict()
#regex word search
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
#construct a patricia trie
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root
#search word in trie
def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
                return False
    else:
        if _end in current_dict:
            return True
        else:
            return False
#load wordbank
def load_wordbank(source):
    bankwords=[]          
    f = open(source,'r')
    for line in f:
        try:
            if word_in_text(r';(.||\n)',line):
                continue;
            bankwords.append(line.strip())     
        except Exception as e:
            print(e)
            break
    return bankwords
# word hit score
def evaluate(source,pos_source,neg_source):
    pscore=0
    nscore=0
    postrie = make_trie(load_wordbank(pos_source))
    negtrie = make_trie(load_wordbank(neg_source))
    f = open(source,'r')
    for line in f:    
        tokenized = nltk.word_tokenize(line)
        for token in tokenized:
            if (in_trie(postrie , token)):
                pscore=pscore+1
            elif (in_trie(negtrie , token)):
                nscore=nscore+1
            else:
                continue
    print(pscore)
    print(nscore)
evaluate('tweetsansJSON.txt','positive-words.txt','negative-words.txt')
 