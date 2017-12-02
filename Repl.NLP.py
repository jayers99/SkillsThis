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

# sentence tokenization does not work with this data because of lots of list items
# i added a \n to as a seperator when i convert from html
paragraphs = [p.strip() for p in jobdescs.split('\n') if p.strip()]
# and here, sent_tokenize each one of the paragraphs
sents[]
for paragraph in paragraphs:
    sents += sent_tokenize(paragraph)

# extract all the words
words[]
for sent in sents:
    words += word_tokenize(sent.lower())

# take out the stopwords
_stopwords = set(stopwords.words('english') + list(punctuation))
words=[word for word in words if word not in _stopwords]
print("\n".join(words))

# let's add stemming
from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in words]
words = stemmedWords
# try the porter stemmer
from nltk.stem import PorterStemmer
st = PorterStemmer()
stemmedWords=[st.stem(word) for word in words]
words = stemmedWords

# add parts of speech
# tag list https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
poswords = nltk.pos_tag(words)
posfreq = FreqDist(poswords)
freqdict = dict(freq)
posfreq.pprint(200)
# this looks good

# add some word sense disambiguation
# this will give all the definitions of words
from nltk.corpus import wordnet as wn
for ss in wn.synsets('bass'):
    print(ss, ss.definition())

#this will look as the use in sentence and return word sense
from nltk.wsd import lesk
sense1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"),'bass')
print(sense1, sense1.definition())

# calc the frequencies
freq = FreqDist(words)
freqdict = dict(freq)

# take a quick look at the dist
freq.pprint(200)
type(freq)
for word in freqdict:
    print(word, freqdict[word])
from heapq import nlargest
nlargest(10, freq, key=freq.get)

# Output to a csv file
#####################################
# intialize the csv file with a heading
outputfile = "/Users/jayers/Temp/freqdistwordsLinkedinStemmedPorter.csv"
with open(outputfile, "w") as myfile:
    linestr = "Word1, Word2, Word3, Frequency, Class, Notes\n".format(k, v)
    myfile.write(linestr)

# generate single word frequencies
s = [(k, freqdict[k]) for k in sorted(freqdict, key=freqdict.get, reverse=True)]
for k, v in s[:2000]:
    k, v
    linestr = "{}, , , {}\n".format(k, v)
    with open(outputfile, "a") as myfile:
        myfile.write(linestr)

# Add bigram frequencies
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
    with open(outputfile, "a") as myfile:
        myfile.write(linestr)

findertri = TrigramCollocationFinder.from_words(words)
trigrams = findertri.ngram_fd.items()
s = sorted(trigrams, key=lambda trigram: trigram[1], reverse=True)[:40]
for k, v in s[:1000]:
    k, v
    linestr = "{}, {}, {}, {}\n".format(k[0], k[1], k[2], v)
    with open(outputfile, "a") as myfile:
        myfile.write(linestr)

