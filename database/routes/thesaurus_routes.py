from flask import Blueprint, jsonify, request, redirect, url_for
from middleware.auth import token_required
from services.synonym_service import SynonymService

thesaurus_blueprint = Blueprint('thesaurus', __name__)
synonym_service = SynonymService()

@thesaurus_blueprint.route('/get_words', methods=['GET'])
@token_required
def get_words():
    words = synonym_service.get_words(limit=50)
    return jsonify(words)


@thesaurus_blueprint.route('/create', methods=['POST'])
@token_required
def create_words():
    data = request.get_json()
    synonym_service.create_words(data['words'])
    return redirect(url_for('thesaurus.get_words'))

