#!/usr/bin/env python3
import pickle

from extractor import articleExtractor
from sklearn.externals import joblib
from vectorize import sentenceVectorizer, model

classifier = joblib.load('classifier.joblib') #Load the classifier outputted by classifierTrain.py

def bias(url, model):
    """Take an article URL and the word embedding model,
    Output a dictionary of political ideologies by percentage
    
    """
    article_sentences = articleExtractor(url)
    total_sentences, lib, con, neutral = 0, 0, 0, 0
    for sentence in article_sentences:
        total_sentences += 1
        polBias = classifier.predict([sentenceVectorizer(sentence, model)])
        if polBias == ['Liberal']:
            lib += 1
        elif polBias == ['Conservative']:
            con += 1
        elif polBias == ['Neutral']:
            neutral += 1
    result = {"Neutral" : format((neutral/total_sentences)*100, '.2f') + '%', \
             "Liberal" :  format((lib/total_sentences)*100, '.2f') + '%', \
             "Conservative" : format((con/total_sentences)*100, '.2f') + '%'}
    return result


if __name__ == '__main__':
    url = input("Enter article url: ")
    bias(url, model)
    