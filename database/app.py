from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
import sqlite3
from db import WordDatabase
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()
CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)
USER_DATA = {"admin": "SuperSecretPwd"}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        resp = make_response(self.get_words())
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    def connect_to_db(self):
        conn = sqlite3.connect("database.db")
        return conn

    def get_words(self):
        wordDb = WordDatabase()
        allWords = wordDb.get_some_words_with_synonyms(100)
        print("num all words", len(allWords))
        return allWords

    def get_random_key_value_pairs(self, my_dict):
        wordDb = WordDatabase()
        allWords = wordDb.get_all_words_with_synonyms()
        print(wordDb.wordCount())

        if len(allWords) < 5:
            raise ValueError("Dictionary should have at least 5 items")

        random_keys = random.sample(allWords.keys(), 5)
        random_pairs = {key: allWords[key] for key in random_keys}
        return random_pairs


api.add_resource(PrivateResource, "/words")

# @app.route("/api/words", methods=["GET"])
# def api_get_words():
#     response = jsonify(get_words())
#     return response


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run(debug=True)  # run app
