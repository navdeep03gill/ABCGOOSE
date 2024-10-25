import os
from flask import Flask, jsonify, request, redirect, url_for, current_app
from flask_cors import CORS
import jwt
from jwt.exceptions import PyJWTError
import datetime
from middleware import token_required
from db import WordDatabase 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'this is a secret'

#CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)
CORS(app, resources={r"/*": {
    "origins": [
        "http://localhost:3000",
        "http://abcgoose-word-game.s3-website-us-east-1.amazonaws.com", 
        "https://d3crrl3dlac4zm.cloudfront.net",
        "http://d3crrl3dlac4zm.cloudfront.net",
        "https://d3crrl3dlac4zm.cloudfront.net/singleWord",
        "https://d3crrl3dlac4zm.cloudfront.net/multiWord",
    ],
    "methods": ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
    "allow_headers": "*"
    }}, support_credentials=True)


@app.route('/get-auth-token', methods=['GET'])
def get_auth_token():
    try:
        # Generate a token with expiration time (e.g., 30 minutes)
        token = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")

        # Return the token as a JSON response
        response = jsonify({'auth_token': token})
        response.headers.add('Access-Control-Allow-Origin', '*')  # Adjust this based on your CORS policy
        return response
    # Catch JWT-specific errors
    except PyJWTError as jwt_err:
        return jsonify({
            'error': 'Token generation error',
            'message': str(jwt_err)
        }), 500

    # Catch any other unforeseen exceptions
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")  # Log the actual error for debugging
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500


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
    app.run(host='0.0.0.0', port=8000) #app.run(host='0.0.0.0', port=8080, debug=True)
