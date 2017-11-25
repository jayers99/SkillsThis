# import the tools
import glob, os



# loop to concat a few files to create a file to do nlp on
for filepath in glob.glob("/Users/jayers/Temp/Jobpost[0-9][0-9][0-9].txt"):
    print(filepath)
    jobtext = open(filepath, 'r', encoding='utf-8', errors='ignore')
    #print(jobtext.read())
    with open("/Users/jayers/Temp/concatfile.txt", "a") as myfile:
        myfile.write(jobtext.read())
    

# read the concat file from disk

with open("/Users/jayers/Temp/concatfile.txt", "r", encoding='utf-8', errors='ignore') as myfile:
    concatstring = myfile.read()

type(concatstring)
print(concatstring)

# word tokenize the concat file
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

# needed to install some nltk stuff
nltk.download('punkt')
nltk.download('stopwords')
sents = sent_tokenize(concatstring)
words = word_tokenize(concatstring.lower())
_stopwords = set(stopwords.words('english') + list(punctuation))
words=[word for word in words if word not in _stopwords]
print("\n".join(words))

from nltk.probability import FreqDist
freq = FreqDist(words)
freq.pprint(200)
type(freq)
freqdict = dict(freq)

# could iterat this way but no
for word in freqdict:
    print(word, freqdict[word])

# another way to iterate over the whole freq
s = [(k, freqdict[k]) for k in sorted(freqdict, key=freqdict.get, reverse=True)]
for k, v in s[:1000]:
    k, v
    linestr = "{}, , , {}\n".format(k, v)
    with open("/Users/jayers/Temp/freqdistwords.csv", "a") as myfile:
        myfile.write(linestr)

from heapq import nlargest
nlargest(10, freq, key=freq.get)

# n-grams
from nltk.collocations import *
#bigram_measures = nltk.collocations.BigramAssocMeasures()
finderbi = BigramCollocationFinder.from_words(words)
#type(finderbi.ngram_fd.items())
bigrams = finderbi.ngram_fd.items()
sorted(bigrams, key=lambda bigram: bigram[1], reverse=True)[:40]
s = sorted(bigrams, key=lambda bigram: bigram[1], reverse=True)
for k, v in s[:500]:
    k, v
    linestr = "{}, , {}\n".format(k, v)
    with open("/Users/jayers/Temp/freqdistwords.csv", "a") as myfile:
        myfile.write(linestr)

findertri = TrigramCollocationFinder.from_words(words)
trigrams = findertri.ngram_fd.items()
s = sorted(trigrams, key=lambda trigram: trigram[1], reverse=True)[:40]
for k, v in s[:500]:
    k, v
    linestr = "{}, {}\n".format(k, v)
    with open("/Users/jayers/Temp/freqdistwords.csv", "a") as myfile:
        myfile.write(linestr)

