import pickle
import pandas as pd
import numpy as np

from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Tokenization, Stemming, Vectorization
tokenizer = RegexpTokenizer(r"[A-Za-z]+")
stemmer = SnowballStemmer("english")
cv = CountVectorizer()

with open("vectorizer.pkl", "rb") as file:
    cvectorizer = pickle.load(file)


def prepare_data(text):
    tokens = tokenizer.tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    stemmed_text = " ".join(stemmed_tokens)
    vectorized_text = cvectorizer.transform([text])
    return vectorized_text
