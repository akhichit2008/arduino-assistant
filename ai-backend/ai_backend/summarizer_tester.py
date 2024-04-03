import bs4 as bs
import urllib.request
import re
import nltk
import heapq

nltk.download('punkt')
nltk.download('stopwords')

url = "https://en.wikipedia.org/wiki/Spider-Man"


data = urllib.request.urlopen(url)
data = data.read()

parsed_data = bs.BeautifulSoup(data,'lxml')
paragraphs = parsed_data.find_all('p')

data = ""

for para in paragraphs:
    data += para.text
    data= re.sub(r'\[[0-9]*\]', ' ', data)
    data = re.sub(r'\s+', ' ', data)
    formatted_data = re.sub('[^a-zA-Z]', ' ', data )
    formatted_data = re.sub(r'\s+', ' ', formatted_data)

sentence_tensor = nltk.sent_tokenize(data)
stopwords = nltk.corpus.stopwords.words('english')


word_freq = {}

def build_word_freq_distrib(formatted_data):
    for w in nltk.word_tokenize(formatted_data):
        if w not in stopwords:
            if w not in word_freq.keys():
                word_freq[w] = 1
            else:
                word_freq[w] += 1

build_word_freq_distrib(formatted_data)

max_freq = max(word_freq.values())

for w in word_freq.keys():
    word_freq[w] = (word_freq[w]/max_freq)


sentence_scores = {}

for s in sentence_tensor:
    for w in nltk.word_tokenize(s.lower()):
        if w in word_freq.keys():
            if len(s.split(" ")) < 30:
                if s not in sentence_scores.keys():
                    sentence_scores[s] = word_freq[w]
                else:
                    sentence_scores[s] += word_freq[w]



summary = heapq.nlargest(5,sentence_scores,key=sentence_scores.get)

summary = ' '.join(summary)


with open("summary.txt","w") as f:
    for w in summary:
        f.write(w)