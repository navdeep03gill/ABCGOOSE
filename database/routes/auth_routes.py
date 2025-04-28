from flask import Blueprint, Flask, jsonify, current_app
from services.token_service import TokenService

auth_blueprint = Blueprint('auth', __name__)
tokenService = TokenService()

@auth_blueprint.route('/get-auth-token', methods=['GET'])
def get_auth_token():
    return tokenService.generate_token()
