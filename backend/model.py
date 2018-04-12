import pickle

i = [input()] # expecting single string of news article text
# from sklearn.linear_model import PassiveAggressiveClassifier
# from sklearn.feature_extraction.text import TfidfVectorizer

f1 = open("tfidf_vectorizer.pckl","rb")
tfidf_vectorizer = pickle.load(f1)
v = tfidf_vectorizer.transform(i) #vectorized string
f2 = open("PAC_model.pckl","rb")
model = pickle.load(f2)
pred = model.predict(v)
print(pred)
f1.close()
f2.close()