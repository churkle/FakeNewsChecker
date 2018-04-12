from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def run_model(text):
    f1 = open("./tfidf_vectorizer.pckl","rb")
    tfidf_vectorizer = pickle.load(f1)
    v = tfidf_vectorizer.transform([text]) #vectorized string
    print(v)

    f2 = open("./PAC_model.pckl","rb")
    model = pickle.load(f2)
    pred = model.predict(v)
    f1.close()
    f2.close()

    return pred

@app.route('/checknews/', methods=['GET'])
@cross_origin()
def fake_news_checker():
    url = request.args.get('article')
    
    if not url:
        return jsonify({'message': 'No input data provided'}), 400

    rawtext = requests.get(url).text
    soup = BeautifulSoup(rawtext, 'lxml')
    body = soup.find_all('p')
    
    article = ''
    for paragraph in body:
        stripped_text = paragraph.get_text(' ', strip = True)
        article = article + '\n' + stripped_text

    pred = run_model(article)

    response = jsonify({'status': 'success',
                    'message': pred.tolist()})
    response.status_code = 200
    return response

@app.route('/checktext', methods=['POST'])
@cross_origin()
def text_checker():

    text = request.json['text']
    
    if not text:
        return jsonify({'message': 'No input data provided'}), 400

    pred = run_model(text)

    response = jsonify({'status': 'success',
                    'message': pred.tolist()})
    response.status_code = 200
    return response