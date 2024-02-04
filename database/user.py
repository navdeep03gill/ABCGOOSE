from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import sqlite3
from db import WordDatabase
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)


CORS(app, support_credentials=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def connect_to_db():
    conn = sqlite3.connect("database.db")
    return conn


def get_words():
    wordDb = WordDatabase()
    allWords = wordDb.get_all_words_with_synonyms()
    print(allWords)
    return allWords


def get_random_key_value_pairs(my_dict):
    wordDb = WordDatabase()
    allWords = wordDb.get_all_words_with_synonyms()

    if len(allWords) < 5:
        raise ValueError("Dictionary should have at least 5 items")

    random_keys = random.sample(allWords.keys(), 5)
    random_pairs = {key: allWords[key] for key in random_keys}
    return random_pairs


@app.route("/api/words", methods=["GET"])
@cross_origin(origin="*")
def api_get_words():
    return jsonify(get_words())


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run(debug=True)  # run app
