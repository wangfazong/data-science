#!/usr/bin/env python
#coding=utf-8

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


vec = CountVectorizer(min_df=1)

corpus =['this is the first document',
        'this is the second document',
         'And the third one',
         'what the hell is that']

x = vec.fit_transform(corpus).toarray()

print(x)

bigram_vectorizer=CountVectorizer(ngram_range=(2,3),
                                  token_pattern=r'\b\w+\b',min_df=1)
x2=bigram_vectorizer.fit_transform(corpus).toarray()

print(x2)

analyze=bigram_vectorizer.build_analyzer()

print(analyze("this is the first document"))