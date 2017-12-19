"""

The file is full of a bunch of commands i was experimenting with analyzing text
i pulled off linkedin.  It will NOT run as a complete program.

"""
# pylint: skip-file

# setup NLP env
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
# you might have to install somestuff
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# working with linkedin 1000 job data

# read the file
with open('/Users/jayers/Temp/Linkedin1000JobDesctions.txt', 'r', encoding='utf-8', errors='ignore') as file:
    jobdescs = file.read()

jobdescs

# sentence tokenization does not work with this data because of lots of list items
# i added a \n to as a seperator when i convert from html
paragraphs = [p.strip() for p in jobdescs.split('\n') if p.strip()]
# and here, sent_tokenize each one of the paragraphs
sents = []
for paragraph in paragraphs:
    sents += sent_tokenize(paragraph)

# extract all the words
mycustomstopwords = ["'s", "'re", "'ll", "n't", "'ve", "'d", "us"]
_stopwords = set(stopwords.words('english') + list(punctuation) + mycustomstopwords)

lmtzr = WordNetLemmatizer()
st = PorterStemmer()

# create a tuple of all the words with 4 word attributes
# wait for this one to complete for linedin 1000 it will take 10 seconds
words = list()
for sent in sents:
    #print(sent)
    sentwords = word_tokenize(sent)
    sentwordsPOS = nltk.pos_tag(sentwords)
    for sentword in sentwordsPOS:
        if sentword[0].lower() not in _stopwords:
            if sentword[1][0].lower().replace("j", "a") in ("n", "v", "a", "r"):
                sentwordsense = lesk(sentwords, sentword[0], sentword[1][0].lower().replace("j", "a"))
            else:
                sentwordsense = lesk(sentwords, sentword[0])
            if sentwordsense is not None:
                sentwordsense = str(sentwordsense).replace("Synset('", "").replace("')", "").lower()
            sentwordlm = lmtzr.lemmatize(sentword[0])
            sentwordst = st.stem(sentword[0])
            #print(sentword[0], sentword[1], sentwordsense, sentwordlm, sentwordst)
            wordrow = (sentword[0].lower(), sentword[1], sentwordsense, sentwordlm.lower(), sentwordst.lower())
            words.append(wordrow)
        else:
            #print(sentword[0], sentword[1], "stopword", "stopword", "stopword")
            wordrow = (sentword[0].lower(), sentword[1], "stopword", "stopword", "stopword")
            words.append(wordrow)


words = [word for word in words if word[2] != "stopword"]
freq = FreqDist(words)
freqdict = dict(freq)

# take out the stopwords
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
# also a thing called Lemmatization?
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
lmtzr.lemmatize('cars')

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
outputfile = "/Users/jayers/Temp/freqdistwordsLinkedinTuple.csv"
with open(outputfile, "w") as myfile:
    #linestr = "Word1, Word2, Word3, Frequency, Class, Notes\n".format(k, v)
    linestr = '"Word","POS","Sense","Lem","Stem","Frequency"\n'
    myfile.write(linestr)

# generate single word frequencies
s = [(k, freqdict[k]) for k in sorted(freqdict, key=freqdict.get, reverse=True)]
for k, v in s:
    if v < 5:
        break
    k, v
    linestr = '"{}","{}","{}","{}","{}", {}\n'.format(k[0], k[1], k[2], k[3], k[4], v)
    with open(outputfile, "a") as myfile:
        myfile.write(linestr)


# new bigram stuff taking into account complete sentences
ngrams = list()
for sent in sents:
    sentwords = word_tokenize(sent)
    sentwords = [word.lower() for word in sentwords if word.lower() not in _stopwords]
    ngrams += nltk.bigrams(sentwords)
    ngrams += nltk.trigrams(sentwords)

print(ngrams)
freq = FreqDist(ngrams)
freqdict = dict(freq)
print(freqdict)

# output to a file
outputfile = "/Users/jayers/Temp/FreqDistNgrams.csv"
with open(outputfile, "w") as myfile:
    linestr = '"Words","Frequency"\n'
    myfile.write(linestr)

# generate single word frequencies
s = [(k, freqdict[k]) for k in sorted(freqdict, key=freqdict.get, reverse=True)]
for k, v in s:
    if v < 20:
        break
    k, v
    linestr = '"{}",{}\n'.format(k, v)
    with open(outputfile, "a") as myfile:
        myfile.write(linestr)

import sys
sys.getsizeof(jobdescs)




# OLD --- Add bigram frequencies
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


# convert my word class ground truth set from json to csv
import csv
import json

# to create json from dictionary
json_string = json.dumps(wordclassdict)
# from json to dictionary
wordclassdict = json.loads(json_string)
# load json from file
wordclassdict = {}
with open('/Users/jayers/Dropbox/Code/SkillsThis/data/WordClassDict.json', 'r') as f:
    wordclassdict = json.load(f)
# write my dictionary back to json file
with open('/Users/jayers/Dropbox/Code/SkillsThis/data/WordClassDict2.json', 'w') as f:
    json.dump(wordclassdict, f)
# convert my diction into csv file
with open('/Users/jayers/Dropbox/Code/SkillsThis/data/WordClassDict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in wordclassdict.items():
       writer.writerow([key, value])
