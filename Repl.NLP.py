# setup NLP env
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
# you might have to install somestuff
nltk.download('punkt')
nltk.download('stopwords')


# working with linkedin 1000 job data

# read the file
with open('/Users/jayers/Temp/Linkedin1000JobDesctions.txt', 'r', encoding='utf-8', errors='ignore') as file:
    jobdescs = file.read()

jobdescs

sents = sent_tokenize(jobdescs)
words = word_tokenize(jobdescs.lower())
_stopwords = set(stopwords.words('english') + list(punctuation))
words=[word for word in words if word not in _stopwords]
print("\n".join(words))

#let's add stemming

freq = FreqDist(words)
freq.pprint(200)
type(freq)
freqdict = dict(freq)

# could iterat this way but no
for word in freqdict:
    print(word, freqdict[word])
#from heapq import nlargest
#nlargest(10, freq, key=freq.get)

# another way to iterate over the whole freq
s = [(k, freqdict[k]) for k in sorted(freqdict, key=freqdict.get, reverse=True)]
for k, v in s[:2000]:
    k, v
    linestr = "{}, , , {}\n".format(k, v)
    with open("/Users/jayers/Temp/freqdistwordsLinkedin.csv", "a") as myfile:
        myfile.write(linestr)

# n-grams
from nltk.collocations import *
#bigram_measures = nltk.collocations.BigramAssocMeasures()
finderbi = BigramCollocationFinder.from_words(words)
#type(finderbi.ngram_fd.items())
bigrams = finderbi.ngram_fd.items()
sorted(bigrams, key=lambda bigram: bigram[1], reverse=True)[:40]
s = sorted(bigrams, key=lambda bigram: bigram[1], reverse=True)
for k, v in s[:1000]:
    k, v
    linestr = "{}, {}, , {}\n".format(k[0], k[1], v)
    with open("/Users/jayers/Temp/freqdistwordsLinkedin.csv", "a") as myfile:
        myfile.write(linestr)

findertri = TrigramCollocationFinder.from_words(words)
trigrams = findertri.ngram_fd.items()
s = sorted(trigrams, key=lambda trigram: trigram[1], reverse=True)[:40]
for k, v in s[:1000]:
    k, v
    linestr = "{}, {}, {}, {}\n".format(k[0], k[1], k[2], v)
    with open("/Users/jayers/Temp/freqdistwordsLinkedin.csv", "a") as myfile:
        myfile.write(linestr)

