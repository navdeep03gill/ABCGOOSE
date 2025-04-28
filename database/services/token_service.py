from flask import jsonify, current_app
from jwt import encode
import datetime

class TokenService:
    def __init__(self):
        return
    def generate_token(self):
        try:
            # Generate a token with expiration time (e.g., 30 minutes)
            token = encode({
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, current_app.config['SECRET_KEY'], algorithm="HS256")
            response = jsonify({'auth_token': token})
            response.headers.add('Access-Control-Allow-Origin', '*')  # Adjust this based on your CORS policy
            return response
        # Catch any other unforeseen exceptions
        except Exception as e:
            current_app.logger.error(f"Unexpected error: {str(e)}")  # Log the actual error for debugging
            return jsonify({
                'error': 'Internal server error',
                'message': str(e)
            }), 500
