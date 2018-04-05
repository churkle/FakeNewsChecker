i = input() # expecting single string of news article text
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

tfidf_vectorizer = pickle.load("tfidf_vectorizer.pckl")
v = tfidf_vectorizer.transform(i) #vectorized string
model = pickle.load("PAC_model.pckl")
pred = model.predict(v)
print(pred)