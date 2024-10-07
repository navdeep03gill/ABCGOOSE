import jwt
import os
from functools import wraps
from flask import request, jsonify, current_app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {
                "message": "Token is missing!",
                "error": "Unauthorized"
            }, 401

        try:
            jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return {
                "message": "Token has expired!",
                "error": "Unauthorized"
            }, 401
        except jwt.InvalidTokenError:
            return {
                "message": "Token is invalid!",
                "error": "Unauthorized"
            }, 401

        return f(*args, **kwargs)
    return decorated
