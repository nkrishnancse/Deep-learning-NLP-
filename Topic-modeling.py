import nltk
import numpy as np
from nltk import sent_tokenize, word_tokenize, pos_tag
import matplotlib.pyplot as plt
from pylab import *
from bs4 import BeautifulSoup
from nltk import sent_tokenize, word_tokenize, pos_tag
import nltk
import numpy as np
import matplotlib.pyplot as plt

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import re

consumer_key = 'bHl88nynHzz1s4eoZNydePLOr'
consumer_secret = '93CtvfiuBSJrHfTE5Gm2rf6YtKLpRfZoRYFcAz81RPU6ahQf5f'
access_token = '2846625020-w39HadQOaVXki6JdpzdYbETZb51IjCOvjAQk5j6'
access_secret = 'tpzWaOVg4uqFWTy500YrY5BZHull6i3iFuIZRNGHdkHhS'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

number_tweets = 200
data = []
for status in tweepy.Cursor(api.user_timeline, id="cnn").items(number_tweets):
    try:
        URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', status.text)
        print(URLless_string, '\n')
        data.append(URLless_string)
    except:
        pass

number_tweets = 250
data = []
for status in tweepy.Cursor(api.search, q="overthinking").items(number_tweets):
    try:
        URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', status.text)
        print(URLless_string, '\n')
        data.append(URLless_string)
    except:
        pass

### print(tweet.entities.get('hashtags'))

text = data

sentences = sent_tokenize(str(text))
sentences2 = sentences
sentences2

tokens = word_tokenize(str(text))
tokens
len(tokens)

tagged_tokens = pos_tag(tokens)
tagged_tokens

## NOUNS
text2 = word_tokenize(str(text))
is_noun = lambda pos: pos[:2] == 'NN'
b = nltk.pos_tag(text2)
b
nouns = [word for (word, pos) in nltk.pos_tag(text2) if is_noun(pos)]
nouns
V = set(nouns)
long_words1 = [w for w in tokens if 4 < len(w) < 10]
sorted(long_words1)
fdist01 = nltk.FreqDist(long_words1)
fdist01
a1 = fdist01.most_common(40)
a1

names0 = []
value0 = []
for i in range(0, len(a1)):
    names0.append(a1[i][0])
    value0.append(a1[i][1])
names0.reverse()
value0.reverse()
val = value0  # the bar lengths
pos = arange(len(a1)) + .5  # the bar centers on the y axis
pos
val
plt.figure(figsize=(9, 9))
barh(pos, val, align='center', alpha=0.7, color='blue')
yticks(pos, names0)
xlabel('Mentions')
title(['Nouns'])
grid(True)


def lexical_diversity(text):
    return len(set(text)) / len(text)


lexical_diversity(text)

vocab = set(text)
vocab_size = len(vocab)
vocab_size

' '.join(['Monty', 'Python'])
'Monty Python'.split()
a = "This is a text.'"
chars_to_remove = ['.', '!', '?', "'"]
sc = set(chars_to_remove)
''.join([c for c in a if c not in sc])

V = set(text)
long_words = [w for w in tokens if 4 < len(w) < 13]
sorted(long_words)

text2 = nltk.Text(word.lower() for word in long_words)
print(text2.similar('wound'))

fdist1 = nltk.FreqDist(long_words)
fdist1
a = fdist1.most_common(15)
a

names = []
value = []
for i in range(0, len(a)):
    names.append(a[i][0])
    value.append(a[i][1])
names.reverse()
value.reverse()
val = value  # the bar lengths
pos = arange(15) + .5  # the bar centers on the y axis
pos

plt.figure(figsize=(9, 9))
barh(pos, val, align='center', alpha=0.7, color='rgbcmyk')
yticks(pos, names)
xlabel('Mentions')
grid(True)

list(nltk.bigrams(tokens))

list(nltk.trigrams(tokens))

sorted(w for w in set(tokens) if w.endswith('ing'))

[w.upper() for w in tokens]

for token in tokens:
    if token.islower():
        print(token, 'is a lowercase word')
    elif token.istitle():
        print(token, 'is a titlecase word')
    else:
        print(token, 'is punctuation')

########################################################

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import matplotlib.pyplot as plt
from gensim import corpora
from string import punctuation


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


documents = [strip_punctuation(re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', sentences2[i])) for i in
             range(0, len(sentences2))]

stoplist = set('for a of the and to in is the he she on i will it its us as that at who be '.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in long_words]
texts

from collections import defaultdict

frequency = defaultdict(int)

for text in texts:
    for token in text:
        frequency[token] += 1
frequency

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
from pprint import pprint

pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester4.dict')

print(dictionary.token2id)

## VETOR DAS FRASES
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester4.mm', corpus)
print(corpus)

from gensim import corpora, models, similarities

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]
lsi.print_topics(2)

todas = []
for doc in corpus_lsi:
    todas.append(doc)
todas

from gensim import corpora, models, similarities

dictionary = corpora.Dictionary.load('/tmp/deerwester4.dict')
corpus = corpora.MmCorpus('/tmp/deerwester4.mm')  # comes from the first tutorial, "From strings to vectors"
print(corpus)

np.array(corpus).shape

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

p = []
for i in range(0, len(documents)):
    doc1 = documents[i]
    vec_bow2 = dictionary.doc2bow(doc1.lower().split())
    vec_lsi2 = lsi[vec_bow2]  # convert the query to LSI space
    p.append(vec_lsi2)

p

index = similarities.MatrixSimilarity(lsi[corpus])

index.save('/tmp/deerwester4.index')
index = similarities.MatrixSimilarity.load('/tmp/deerwester4.index')

#################

import gensim
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl

matrix1 = gensim.matutils.corpus2dense(p, num_terms=4)
matrix3 = matrix1.T
matrix3

from sklearn import manifold, datasets, decomposition, ensemble, discriminant_analysis, random_projection


def norm(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))


X = norm(matrix3)

tsne = manifold.TSNE(n_components=2, init='pca', random_state=0, perplexity=50, verbose=1, n_iter=1500, method='exact')
X_tsne = tsne.fit_transform(X)

plt.hist(X_tsne)

from sklearn.cluster import KMeans

model3 = KMeans(n_clusters=4, random_state=0)
model3.fit(X_tsne)
cc = model3.predict(X_tsne)

tokens2 = word_tokenize(str(sentences2))
tokens2

long_words12 = [w for w in tokens2 if len(w) > 6]
sorted(long_words12)
fdist012 = nltk.FreqDist(long_words12)
a12 = fdist012.most_common(5)

from matplotlib.colors import LinearSegmentedColormap

print('TOPIC 1\n')

print(a12, '\n')

for i in np.where(cc == 2)[0][2:10]:
    print(i, sentences2[i])

n_classes = 4
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
cm = LinearSegmentedColormap.from_list(
    cc, colors, N=4)
cor = [colors[cc[i]] for i in range(0, len(cc))]

h = []
label = []
fig = plt.figure(figsize=(8, 4))
plt.title('NATURAL LANGUAGE PROCESSING\n\n' + 'TOPIC MODELING at TWITTER page: ' + 'CNN', fontweight="bold")
for i in range(0, 4):
    label.append('Topic {}'.format([0, 1, 2, 3][i]))
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=cc, cmap=cm, marker='o', s=100)
    h1, = plt.plot(1, 1, color=colors[i], linewidth=3)
    h.append(h1)
plt.legend(h, label, loc="upper left")
plt.show()

model = models.LdaModel(corpus, id2word=dictionary, num_topics=4)
model.print_topics(4)