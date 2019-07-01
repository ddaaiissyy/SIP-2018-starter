'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!py
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

def Average(lst): 
    return sum(lst) / len(lst)

tweettext = []
tweetstring = ''
for tweet in tweetData:
    tweetstring += tweet['text']
print(tweetstring)



    # blob = TextBlob(tweet["text"])
    # tweettext.append(blob)
   
blob_polarity = []
for blob in tweetData:
    b = TextBlob(blob['text'])
    blob_polarity.append(b.polarity)
# print(blob_polarity)

blob_subjectivity = []
for blob in tweetData:
    b = TextBlob(blob['text'])
    blob_subjectivity.append(b.subjectivity)

print(Average(blob_polarity))
print(Average(blob_subjectivity))

tb = TextBlob(tweetstring)
word_dict = {}
for word in tb.words:
    word_dict[word.lower()] = tb.word_counts[word.lower()]
print(word_dict)


#HISTOGRAM
import matplotlib.pyplot as plt

someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
plt.hist(someList, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('POLARITY')
plt.axis([-1.1, 1.1, 0, 6])
plt.grid(True)
plt.show()
0.1403954771379014

import matplotlib.pyplot as plt

someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
plt.hist(someList, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('SUBJECTIVITY') 
plt.axis([-1.1, 1.1, 0, 6])
plt.grid(True)
plt.show()