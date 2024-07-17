import os
from flask import Flask, request, jsonify
from functools import wraps
from flask import current_app



API_TOKEN = os.environ.get('SECRET_KEY') 

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Authorization" in request.headers:
            token = request.headers.get('Authorization')
            print(token, current_app.config["SECRET_KEY"])
        if not token or token != current_app.config["SECRET_KEY"]:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        return f(*args, **kwargs)
    return decorated

