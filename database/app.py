import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
from db import WordDatabase 
from auth_middleware import token_required

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)

# @app.before_request
# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = secrets.token_hex(16)
#     g.csrf_token = session['_csrf_token']

@app.route('/get-csrf-token', methods=['GET'])
def get_csrf_token():
    response = jsonify({'csrf_token': SECRET_KEY})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/thesaurus/get_words')
@token_required
def index():
    word_db = WordDatabase()
    words = word_db.get_some_words_with_synonyms(limit=50)
    return jsonify(words)


@app.route('/create', methods=['POST'])
@token_required
def create():
    data = request.json
    new_words = data['words']
    print(new_words)
    for word in new_words:
        print(word)
        print()

    word_db = WordDatabase()
    word_db.populate_table(new_words)
    return redirect(url_for('index')) 


if __name__ == '__main__': 
    app.run(debug=True) 
