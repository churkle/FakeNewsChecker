from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/checknews', methods=['GET'])
@cross_origin()
def fake_news_checker():
    # json_data = request.get_json()
    
    # if not json_data:
    #     return jsonify({'message': 'No input data provided'}), 400
    
    # print(json_data)

    response = jsonify({'status': 'success',
                    'message': 'FAKE!'})
    response.status_code = 200
    return response
