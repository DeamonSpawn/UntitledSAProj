#!/usr/bin/python
import re,nltk
import matplotlib.pyplot as plt
_end = '_end_'
negation=dict()
postrie=dict()
negtrie=dict()
rejectlist=[]

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
    pcount=0
    ncount=0
    unknwn=0
    lcount=0
    postrie = make_trie(load_wordbank(pos_source))
    negtrie = make_trie(load_wordbank(neg_source))
    f = open(source,'r')
    for line in f:
        lcount=lcount+1  
        negation = re.compile(r'(?<= no)\s\w+|(?<=sn\'t)\s\w+|(?<= not)\s\w+|\s(?<= less)\s\w+|(?<= without)\s\w+|(?<=barely)\s\w+|(?<= hardly)\s\w+|(?<= rarely)\s\w+|(?<= no longer)\s\w+|(?<= no more)\s\w+|(?<= no way)\s\w+|(?<= no where)\s\w+|(?<= by no means)\s\w+|(?<= at no time)\s\w+', re.IGNORECASE)
        opp_sent = [x.strip(" ") for x in re.findall(negation,line)]
        tokenized = nltk.word_tokenize(line)
        sans_neg = [word for word in tokenized if word not in opp_sent]
        for token in sans_neg:
            if (in_trie(postrie , token.lower())):
                    pscore=pscore+1
            elif (in_trie(negtrie , token.lower())):
                    nscore=nscore+1
            else:
                rejectlist.append(token.lower())
                continue
        for token in opp_sent:
            if (in_trie(postrie , token.lower())):
                    nscore=nscore+1
            elif (in_trie(negtrie , token.lower())):
                    pscore=pscore+1
            else:
                rejectlist.append(token.lower())
                continue
        if(pscore>nscore):
            pcount=pcount+1
        elif(nscore>pscore):
            ncount=ncount+1
        else:
            unknwn=unknwn+1
        pscore=0
        nscore=0
        print(sans_neg)
    return(pcount,ncount,unknwn,lcount)
def plotgraph(pcount,ncount,unknwn,lcount):
    fig, ax=plt.subplots()
    rect1=plt.bar([2],pcount,1,color='g')
    rect2=plt.bar([0],ncount,1,color='r')
    rect3=plt.bar([1],unknwn,1,color='c')
    ax.set_xlim(0,4)
    ax.set_ylim(0,lcount)
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.title('Sentiment Analysis')
    plt.legend((rect1,rect2,rect3),(str(pcount)+" positive tweets",str(ncount)+" negative tweets",str(unknwn)+" unknown tweets"))
    fig.canvas.draw()
    ax.set_xticklabels([' ','Negative',' ','Unknown',' ','Positive'])    
    plt.show()
    #print(rejectlist)
plotgraph(*evaluate('../test/tweetsansJSON.txt','../lib/positive-words.txt','../lib/negative-words.txt'))