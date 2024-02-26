from re import L
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin

import sqlite3
from db import WordDatabase
import random

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
        resp = make_response({"meaning of life": 42})
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp


api.add_resource(PrivateResource, "/private")

if __name__ == "__main__":
    app.run(debug=True)
